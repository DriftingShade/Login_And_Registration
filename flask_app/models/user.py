from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
PASSWORD_REGEX = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$")


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

    @staticmethod
    def validate_register(user):
        is_valid = True
        if len(user["first_name"]) == 0:
            flash("First Name is required")
            is_valid = False
        elif len(user["first_name"]) < 2:
            flash("First Name must be more than 2 characters")
            is_valid = False
        if len(user["last_name"]) == 0:
            flash("Last Name is required")
            is_valid = False
        elif len(user["last_name"]) < 2:
            flash("Last Name must be more than 2 characters")
            is_valid = False
        if len(user["email"]) == 0:
            flash("Email Address is required")
            is_valid = False
        elif not EMAIL_REGEX.match(user["email"]):
            flash("Invalid Email Address")
            is_valid = False
        if not PASSWORD_REGEX.match(user["password"]):
            flash("Password must be at least 8 characters", "Length")
            flash("Password must contain one capital letter", "Capital")
            flash("Password must contain one special character (!@#$)", "Special")
            flash("Password must contain one number", "Number")
            is_valid = False
        if user["password"] != user["password_confirm"]:
            flash("Passwords must match")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        if len(user["email"]) == 0:
            flash("Email Address is required")
            is_valid = False
        if len(user["password"]) == 0:
            flash("Password is required")
            is_valid = False
        lookup_email = User.find_by_email(user["email"])
        if lookup_email:
            lookup_pw = User.find_by_password(user["password"])
        elif not lookup_email:
            flash("Email Not Found")
        if lookup_pw:
            return is_valid
        else:
            flash("Password is Incorrect")
            is_valid = False
        return is_valid

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

    @classmethod
    def find_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return results

    @classmethod
    def find_by_password(cls, data):
        query = "SELECT * FROM users WHERE password = %(password)s"
        connectToMySQL(cls.DB).query_db(query, data)
        return
