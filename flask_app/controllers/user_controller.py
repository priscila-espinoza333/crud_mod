#Importamos Flask y lo que utilizamos de flask 
from flask import Flask, render_template, request, redirect

# Importamos la app
from flask_app import app

# Importamos los modelos que usaremos --- el ultimo User va con mayuscula porque es la clase
from flask_app.models.users import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create():
    # recibimos  el formulario a través de  una variable llamada  request.form
    User.guardar(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    formulario = {"id": id} #diccionario que lo ponemos como nombre de variable 
    User.borra(formulario)
    return rendirect('/ ')

@app.route('/edit/<int:id>')
def edit(id):
    formulario = {"id:": id}
    user = User.mostrar(formulario) #instancia de usuario 
    return render_template('edit.html', usuario = user)

@app.route('/update', methods=['POST'])
def update():
    #request.form = diccionario con el formulario de edit.html
    User.actualizar(request.form)
    return redirect('/')