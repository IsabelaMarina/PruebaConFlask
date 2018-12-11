from flask import Flask
app = Flask(__name__)

@app.route('/acerca')
def acerca_de():
    saludo = """Programa de Phyton creado en terminal<br>
	Creado por: Isabela Mercado<br>
	Fecha: 10-dic-2018"""
    return saludo

@app.route('/emoticon')
def emoticon():
    emoticono = "Prueba de emoticono 😉"
    return emoticono

@app.route('/suma/<a>/<b>')
def sumas(a,b):
    a = int(a)
    b = int(b)
    res = a + b
    muestra = "El resultado es " + str(res)
    return muestra

@app.route('/divide/<a>/<b>')
def divides(a,b):
    a = int(a)
    b = int(b)
    res = a / b
    muestra = "El resultado es " + str(res)
    return muestra
