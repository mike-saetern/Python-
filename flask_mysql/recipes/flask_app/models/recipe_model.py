from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user_model
from flask_app.models.user_model import User


class Recipe:
    db ="recipes"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30min = data['under_30min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user']

    @classmethod
    def save(cls,data):
        query = """INSERT INTO recipe (name,description,instructions,
        date_cooked,under_30min,user_id) VALUES (%(name)s,%(description)s,
        %(instructions)s,%(date_cooked)s,%(under_30min)s,%(user_id)s);"""
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def delete(cls,id):
        query = "DELETE from recipe WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,{"id":id})
    
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * From recipe LEFT JOIN users ON recipe.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)#have to left join to get recipes and user table together
        all_recipes =[]
        for one in results:
            user_recipe = User({
                "id": one['user_id'],
                "first_name": one['first_name'],
                "last_name": one['last_name'],
                "email": one['email'],
                "password": one['password'],
                "created_at": one['users.created_at'],
                "updated_at": one['users.updated_at']
            })
            new_recipe = Recipe({
                "id" : one['id'],
                "name" : one['name'],
                "description" : one['description'],
                "instructions" : one['instructions'],
                "date_cooked" : one['date_cooked'],
                "under_30min" : one['under_30min'],
                "created_at" : one['created_at'],
                "updated_at" : one['updated_at'],
                "user" : user_recipe
            })
            all_recipes.append(new_recipe)
        return all_recipes
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM recipe LEFT JOIN users ON recipe.user_id = users.id WHERE recipe.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE recipe SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_cooked= %(date_cooked)s, under_30min = %(under_30min)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if recipe['name'] == 0 or recipe['description'] == 0 or recipe['instructions'] == 0:
            flash("Fields must not be blank", "recipe")
            is_valid = False
        if len(recipe['name']) < 3 or len(recipe['description']) < 3 or len(recipe['instructions']) < 3:
            flash("Fields must have 3 characters", "recipe")
            is_valid = False
        if recipe['date_cooked'] == "": #check to make sure date is selected
            flash("Please select a date", "recipe")
            is_valid = False
        if 'under_30min' not in recipe: #check to make sure radio is selected
            flash("Must select yes or no for under 30 mins", "recipe")
            is_valid = False  
        return is_valid
        
