from flask import Flask, request, render_template
from operaciones import sumar, restar, multiplicar, dividir, dividir_entero
from livereload import Server
import random






app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/")
def suma():
    return render_template("suma.html")


@app.route("/suma")
def ruta_suma():
    num1=request.args.get("num1",type=float)
    num2=request.args.get("num2",type=float)
    
    if num1 is None or num2 is None:
        num1=random.randint(1,100)
        num2=random.randint(1,100)
        return f"la suma de num1 y num2 generados aleatoriamente es {sumar(num1,num2)}"
    
    else:

        return f"la suma de num1 y num2 es {sumar(num1,num2)}"


@app.route("/resta")
def ruta_resta():
    num1=request.args.get("num1",type=float)
    num2=request.args.get("num2",type=float)
    if num1 is None or num2 is None:
        return "faltan datos"
    return f"la resta de num1 y num2 es {restar(num1,num2)}"


@app.route("/multiplicacion")
def ruta_multiplicacion():
    num1=request.args.get("num1",type=float)
    num2=request.args.get("num2",type=float)
    if num1 is None or num2 is None:
        return "faltan datos"
    return f"la multiplicacion de num1 y num2 es {multiplicar(num1,num2)}"


@app.route("/division")
def ruta_division():
    num1=request.args.get("num1",type=float)
    num2=request.args.get("num2",type=float)
    if num1 is None or num2 is None:
        return "faltan datos"
    return f"la division de num1 y num2 es {dividir(num1,num2)}"


@app.route("/divisionpiso")
def ruta_divisionpiso():
    num1=request.args.get("num1",type=float)
    num2=request.args.get("num2",type=float)
    if num1 is None or num2 is None:
        return "faltan datos"
    return f"la division de num1 y num2 es {dividir_entero(num1,num2)}"


