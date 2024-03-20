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
    session["user"] = user_id
    return redirect(f"/success/{user_id}")


@app.route("/success/<int:user_id>")
def success(user_id):
    if user_id not in session:
        return "Invalid URL entered.  Please return to localhost:5000"
    user = User.find_by_id({"id": user_id})
    return render_template("success.html", user=user)

@app.post("/login")
def login():
    

@app.route("/logout")
def logout():
    session.clear()
    return render_template("/")