import math

def calcularProporcion(datos, grupo):
    try:
        return len(grupo) / len(datos) 
    except ZeroDivisionError:
        return 0.0

def calcularEntropia(prop1, prop2):

    if prop1 == 0 or prop2 == 0:
        return 0.0
    else:
        return - (prop1 * math.log2(prop1) + prop2 * math.log2(prop2))
