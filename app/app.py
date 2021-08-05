from flask import Flask, request
from flask.templating import render_template
from model.utilisateurModel import UtilisateurModel
from werkzeug.utils import redirect

app=Flask(__name__)
app.config['MYSQL_HOST']='127.0.0.1:3306'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='mabdd'

utilisateur=UtilisateurModel()

@app.route("/")
def hello():
    result=utilisateur.fetch_all_utilisateur()
    return render_template("./Hello.html", data=result)

@app.route("/bye/")
def bye():
    return render_template("bye.html")

@app.route("/add_user/")
def add_user():
    return render_template("add_user.html")

@app.route("/insert_user/", methods=["POST", "GET"])
def user_continent():
    data=request.form
    utilisateur.addUser(data)
    return redirect("http://localhost:5000")

@app.route("/delete_user/<id>")
def delete_user(id):
    utilisateur.deleteById(id)
    return redirect("http://localhost:5000")

@app.route("/update_user/")
def update_user():
    data1=request.args
    return render_template(f"update_user.html",data=data1)

@app.route("/update_user_t/", methods=["POST", "GET"])
def update_user_t():
    data=request.form
    utilisateur.update(data)
    return redirect("http://localhost:5000")
