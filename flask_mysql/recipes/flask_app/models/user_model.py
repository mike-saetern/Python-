from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "recipes"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = [] #empty list to put recipes in

    @classmethod
    def save(cls,data):
        query = """INSERT INTO users (first_name,last_name,email,password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    
    @staticmethod
    def register_is_valid(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if len(user['email']) == 0 or len(user['first_name']) == 0 or len(user['last_name']) == 0:
            flash("All fields must be filled out", "register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!","register")
            is_valid=False
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters","register")
            is_valid= False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters","register")
            is_valid= False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        if not re.search('[A-Z]', user['password']):
            flash("Password must contain at least one capital letter","register")
            is_valid=False
        if not re.search('[0-9]', user['password']):
            flash("Password must contain at least one number", "register")
            is_valid=False
        if user['password'] != user['confirm']:
            flash("Passwords don't match","register")
        return is_valid
    