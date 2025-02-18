'''
Programa principal del juego del ahorcado
'''
import os
import string
import unicodedata
import argparse
from random import choice
import funciones as fn

def main(archivo_texto:str,nombre_plantilla='plantilla'):
    '''
    El main 

    '''
    #cargar plantillas
    plantillas = fn.carga_plantillas(nombre_plantilla)

    #cargamos las oraciones
    oraciones = fn.carga_archivo(archivo_texto)

    #obtenemos palabras
    palabras = fn.obten_palabras(oraciones)

    o= 5 #oportunidades

    #elegir la palabra al azar
    p = choice(palabras)

    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    print(p)

    while o > 0:
        fn.despliega_plantilla(plantillas,o)
        o= fn.adivina_letra(abcdario,p,adivinadas,o)
        if p=="".join([letra if letra in adivinadas else '_' for letra in p]):
            print("Felicidades! adivinaste la palabra oculta... Maestro!")
            break

    fn.despliega_plantilla(plantillas,o)
    print(f"la palabra era: {p}, pa la próxima, campeón")    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Juego del Ahorcado')
    parser.add_argument('-a','--archivo',help='Archivo de texto con palabras a adivinar', default='./datos/pg15532.txt')
    args = parser.parse_args()
    archivo = args.archivo
    if os.stat(archivo) is False:
        print(f'el archivo {archivo} no exite !')

    #archivo = './datos/pg15532.txt'
    else:
        main(archivo)






