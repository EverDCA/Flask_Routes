from flask import Flask


#Ejercicio 1
app = Flask(__name__)

@app.route('/')
def home():
    return "¡Bienvenido a Flask!"

#Ejercicio 2

#2.1
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"Hola, {nombre}"

#2.2
@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    return f"la suma de {num1} + {num2} es {num1 + num2}"

#2.3
@app.route('/consulta/<string:palabra>')
def consulta(palabra):
    return palabra.upper()


if __name__ == '__main__':
    app.run(debug=True, port=5050, host='127.0.0.1')
    
    
    

