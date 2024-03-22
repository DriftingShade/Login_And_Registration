from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "That's my;u8 secret: %I'm AL|WAYS angy829ckc823//*9dc2a8[dkl"
