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
    saludo = acerca_de()
    return jsonify(resultado = saludo)

@app.route('/suma/<a>/<b>')
def sumas(a, b):
    try:
        if a == '' or b == '':
            res = "-> Error"
        else:
            a = float(a)
            b = float(b)
            res = a + b
    except:
        res = "-> Error"
    muestra = "El resultado es " + str(res)
    return muestra

@app.route('/suma/<a>/<b>/json')
def sumas_json(a,b):
    muestra = sumas(a,b)
    return jsonify(resultado = muestra)

@app.route('/divide/<a>/<b>')
def divides(a,b):
    try:
        a = float(a)
        b = float(b)
        res = a / b
    except:
        res = "-> Error"
    muestra = "El resultado es " + str(res)
    return muestra

@app.route('/divide/<a>/<b>/json')
def divides_json(a,b):
    muestra = divides(a,b)
    return jsonify(resultado = muestra)

if __name__ == '__main__':
    app.run()
