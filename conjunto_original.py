import pandas as pd
import funciones as fn

datos = pd.read_csv('TablaPrediccionAbandono-Entrenamiento.csv')

#Grupos
continua = datos[datos['EstadoFinal'] == 'Continúa']
abandona = datos[datos['EstadoFinal'] == 'Abandonó']

#Proporciones
prop_continua = fn.calcularProporcion(datos, continua)
prop_abandona = fn.calcularProporcion(datos, abandona)

#Entropia
entropia_conjunto_original = fn.calcularEntropia(prop_continua, prop_abandona)

def main():
    print(f'''
    Cantidad de alumnos: {len(datos)} 

    De los cuales:
        Continuan: {len(continua)}, Abandonan: {len(abandona)}.

    La proporcion de cada grupo:
        Continuan: {prop_continua}, Abandonan: {prop_abandona}.

    Entropía del conjunto: {entropia_conjunto_original}
    ''')

if __name__ == '__main__':
    main()