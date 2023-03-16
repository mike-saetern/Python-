from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Cookie:
    db = "cookie_orders"
    def __init__(self, data):
        self.id = data['id']
        self.cust_name = data['cust_name']
        self.cookie_type = data['cookie_type']
        self.num_boxes = data['num_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie_orders"
        results = connectToMySQL(cls.db).query_db(query)
        orders = []
        for order in results:
            orders.append( cls(order) )
        return orders
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO cookie_orders (cust_name,cookie_type,num_boxes) VALUES (%(cust_name)s,%(cookie_type)s,%(num_boxes)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def update(cls, data):

        query = """
                UPDATE cookie_orders
                SET cust_name = %(cust_name)s, cookie_type = %(cookie_type)s, num_boxes = %(num_boxes)s
                WHERE id = %(id)s;"""

        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def delete(cls,id):
        query = "DELETE FROM cookie_orders WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query,{"id": id})
    
    @classmethod
    def get_by_id(cls,id):
        query = "SELECT * from cookie_orders WHERE id = %(id)s;"
        data = {
            "id": id
        }
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            order = result[0]
            return order
        return False
    
    @staticmethod
    def is_valid(data):
        valid = True

        if len(data["cust_name"]) <= 0 or len(data["cookie_type"]) <= 0 or len(data["num_boxes"]) <= 0:
            valid = False
            flash("All fields required")
        elif len(data["cust_name"]) < 2:
            valid = False
            flash("Name must be at least 2 characters")
        elif len(data["cookie_type"]) < 2:
            valid = False
            flash("Cookie type must be at least 2 characters")
        elif int(data["num_boxes"]) <= 0:
            valid = False
            flash("Please enter a valid number of boxes.")
        return valid