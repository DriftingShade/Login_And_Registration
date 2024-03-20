from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class User:
    DB = "users_db"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, password, 
        created_at, updated_at) VALUES ( %(first_name)s, %(last_name)s, %(email)s, 
        %(password)s, NOW(), NOW());"""

        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return results

    @classmethod
    def find_by_id(cls, data):

        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return results[0]

    @staticmethod
    def validate_register(user):
        is_valid = True
        if len(user["first_name"]) < 2:
            flash("First Name must be more than 2 characters")
            is_valid = False
        if len(user["last_name"]) < 2:
            flash("Last Name must be more than 2 characters")
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid Email Address")
            is_valid = False
        if user["password"] != user["password_confirm"]:
            flash("Passwords must match")
            is_valid = False
        if not re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", user["password"]):
            flash("Password must be 8 characters long")
            is_valid = False
        return is_valid
