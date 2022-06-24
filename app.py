#Importamos os para poder utilizar os.environ
import os
from flask import Flask, render_template, request
app = Flask(__name__)
import json
with open("static/MSX.json") as fichero:
    datos=json.load(fichero)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/juegos')
def juegos():
    return render_template("juegos.html")


@app.route('/lista_juegos',methods=["POST"])
def lista_juegos():
    juego=[]
    texto=request.form.get("texto")
    print(texto)
    error=True
    for dato in datos:
        nombre=str(dato.get("nombre"))
        if nombre.startswith(texto):
            diccionario={"nombre":dato.get("nombre"),"id":dato.get("id"),"desarrollador":dato.get("desarrollador")}
            juego.append(diccionario)
            error=False
    if error == False:    
        return render_template("lista_juegos.html",juego=juego)
    else:
        return render_template("lista_juegos_error.html",juego=juego)



@app.route('/juego/<id>')
def juego(id):
    for dato in datos:
        if dato.get("id") == int(id):
            return render_template("juego.html",dato=dato)


port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=False)
#app.run("0.0.0.0",5000,debug=True)