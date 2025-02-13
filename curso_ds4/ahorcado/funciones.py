import string
import unicodedata
from random import choice

def carga_archivo(archivo:str) -> list:
    '''
    Carga un archivo de texto y devuelve una lista
    con las oraciones del archivo
    '''
    with open(archivo,'r',encoding='utf-8') as file:
        oraciones =file.readlines()
    return oraciones

def carga_plantillas(nombre_plantilla:str) -> dict:
    '''
    carga las plantillas del juego a partir de un archivo de texto
    '''
    plantillas={}
    for i in range(6):
        plantillas[i]= carga_archivo(f'C:/Users/marti/Desktop/curso_python/curso_python/curso_ds4/ahorcado/plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict,nivel:int):
    '''
    Despliega una plantilla del juego
    '''
    if nivel in diccionario:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)

def obten_palabras(lista:list)-> list:
    '''
    Obtiene las palabras de un texto
    '''
    texto=' '.join(lista[120:])
    palabras = texto.split()
    minusculas =[palabra.lower() for palabra in palabras]
    set_palabras =set(minusculas)
    # removemos signos de puntuación y caracteres especiales
    set_palabras = {palabra.strip(string.punctuation) for palabra in set_palabras}
    #removemos números, paréntesis, corchetes y otros caracteres
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}
    #removemos acentos
    set_palabras = {unicodedata.normalize('NFKD',palabra).encode('ascii','ignore').decode('ascii') for palabra in set_palabras}
    return list(set_palabras)

def adivina_letra(abc:dict,palabra:str,letras_adivinadas:set,turnos:int):
    '''
    Adivina una letra de una palabra

    '''
    palabra_oculta=''
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta+='_'   
    print(f'Tienes {turnos} oportunidades de fallar')
    abcd = " ".join(abc.values())
    print(f'el abecedario es: {abcd}')
    print(f'la palabra es: {palabra_oculta}')
    letra = input('Ingresa una letra: ')
    letra = letra.lower()
    if letra in abc:
        if abc[letra] == "*":
            print('Ya adivinaste es letra')
        else:
            abc[letra] = "*"
            if letra in palabra:
                letras_adivinadas.add(letra)
            else:
                turnos -= 1

if __name__=='__main__':
    plantillas = carga_plantillas('plantilla')
    despliega_plantilla(plantillas,5)
    #despliega_plantilla(plantillas,4)
    #despliega_plantilla(plantillas,3)
    #despliega_plantilla(plantillas,2)
    #despliega_plantilla(plantillas,1)
    #despliega_plantilla(plantillas,0)
    #despliega_plantilla(plantillas,6)
   # lista_oraciones = carga_archivo('C:/Users/marti/Desktop/curso_python/curso_python/curso_ds4/ahorcado/datos/pg15532.txt')
    lista_oraciones = carga_archivo('./datos/pg15532.txt')
    #print(lista_oraciones[120:150])
    lista_palabras = obten_palabras(lista_oraciones)
    #print(lista_palabras[:50])
    p = choice(lista_palabras)
    print(p)
    print(len(lista_palabras))
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    t = 5 #oportunidades
    adivina_letra(abcdario,p,adivinadas,t)
    adivina_letra(abcdario,p,adivinadas,t)