'''
Tablero.py: Dibuja el tablero del juego del gato
'''
import random 
def dibuja_tablero(simbolos:dict):
    '''
    Dibuja el tablero del juego del gato
    '''
    print(f'''
          {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
          ---------
          {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
          ---------
          {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
          '''
    )
def ia(simbolos:dict):
    '''Estrategia de la computadora'''
    ocupado = True
    while ocupado is True:
        x=random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x]='O'
            ocupado = False

if __name__== '__main__':
    contador =0
    numeros =[str(i) for i in range(1,10)]
    dic_simbolos={x:x for x in numeros}
    dibuja_tablero(dic_simbolos)
    ia(dic_simbolos)
    dibuja_tablero(dic_simbolos)


    '''x = random.choice(numeros)
    numeros.remove(x)
    dic_simbolos[x]='X'
    dibuja_tablero(dic_simbolos)
    o= random.choice(numeros) 
    numeros.remove(o)
    dic_simbolos[o]='O'
    dibuja_tablero(dic_simbolos)
    print(numeros)'''  
