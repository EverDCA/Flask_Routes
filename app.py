from flask import Flask,request,make_response


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

@app.route('/info')
def info():
    navegador = request.headers.get('User-Agent', 'Desconocido')
    es_seguro = "Sí" if request.is_secure else "No"
    return {
        "Navegador": navegador,
        "Conexión segura": es_seguro
    }

@app.route('/personalizado')
def personalizado():
    response = make_response("<h1>Bienvenido</h1>", 201)
    response.set_cookie("mi_cookie", "valor_demo")
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5050, host='127.0.0.1')
    
    
    

