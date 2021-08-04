from flask import Flask, request
from flask.templating import render_template
from model.utilisateurModel import utilisateurModel
from werkzeug.utils import redirect

app=Flask(__name__)
utilisateur=UtilisateurModel()

@app.route("/app/")
def hello():
    result=utilisateur.fetch_all_utilisateur()
    return render_template("./app/Hello.html", data=result)

@app.route("/app/bye/")
def bye():
    return render_template("./app/bye.html")

@app.route("/app/add_user/")
def add_user():
    return render_template("./app/add_user.html")

@app.route("/app/insert_user/", methods=["POST", "GET"])
def user_continent():
    data=request.form
    utilisateur.addUser(data)
    return redirect("http://localhost/app/")

@app.route("/app/delete_user/<id>")
def delete_user(id):
    utilisateur.deleteById(id)
    return redirect("http://localhost/app/")

@app.route("/app/update_user/")
def update_user():
    data1=request.args
    return render_template(f"./app/update_user.html",data=data1)

@app.route("/app/update_user_t/", methods=["POST", "GET"])
def update_user_t():
    data=request.form
    utilisateur.update(data)
    return redirect("http://localhost/app/")