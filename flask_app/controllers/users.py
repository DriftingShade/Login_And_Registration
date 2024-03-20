from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.post("/register")
def register():
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    print(pw_hash)
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash,
    }
    if not User.validate_register(request.form):
        return redirect("/")
    user_id = User.create(data)
    session["user_id"] = user_id
    return redirect("/success")


@app.route("/success/<user_id>")
def success(user_id):
    if user_id not in session:
        return "Not so fast there, partner!  You haven't signed up yet!"
    return render_template("success.html")
