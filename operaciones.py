def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b==0:
        return "error: division por cero" 
    return a/b

def dividir_entero(a,b):
    if b==0:
        return "error: division por cero"
    return a//b
