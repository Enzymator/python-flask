from flask import Flask
from flask.templating import render_template
from model.utilisateurModel import ContinentModel
from werkzeug.utils import redirect

app=Flask(__name__)
utilisateur=utilisateurModel()
@app.route("/hello")
def hello():
    return "Hello World"