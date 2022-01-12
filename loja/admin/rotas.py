from flask import render_template, session, request, url_for

from loja import app, db

@app.route('/')

def home():
    return "Seja bem vindo a Flask"

@app.route('/registrar')

def registrar():
    return render_template('admin/registrar.html', title="Registrar_user")