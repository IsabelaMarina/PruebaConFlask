from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/acerca')
def acerca_de():
    saludo = """Programa de Phyton creado en terminal<br>
	Creado por: Isabela Mercado<br>
	Fecha: 10-dic-2018"""
    return saludo

@app.route('/acerca/json')
def acerca_de_json():
    saludo = """Programa de Phyton creado en terminal<br>
    Creado por: Isabela Mercado<br>
    Fecha: 10-dic-2018"""
    return jsonify(resultado = saludo)

@app.route('/emoticon')
def emoticon():
    emoticono = "Prueba de emoticono 😉"
    return emoticono

@app.route('/emoticon/json')
def emoticon_json():
    emoticono = "Prueba de emoticono 😉"
    return jsonify(mostrar = emoticono)

@app.route('/suma/<a>/<b>')
def sumas(a,b):
    a = int(a)
    b = int(b)
    res = a + b
    muestra = "El resultado es " + str(res)
    return muestra

@app.route('/suma/<a>/<b>/json')
def sumas_json(a,b):
    a = int(a)
    b = int(b)
    res = a + b
    muestra = "El resultado es " + str(res)
    return jsonify(resultado = muestra)

@app.route('/divide/<a>/<b>')
def divides(a,b):
    a = int(a)
    b = int(b)
    try:
        res = a / b
    except:
        res = "-> Error de división por cero"
    muestra = "El resultado es " + str(res)
    return muestra

@app.route('/divide/<a>/<b>/json')
def divides_json(a,b):
    a = int(a)
    b = int(b)
    try:
        res = a / b
    except:
        res = "-> Error de división por cero"
    muestra = "El resultado es " + str(res)
    return jsonify(resultado = muestra)

if __name__ == '__main__':
    app.run()
