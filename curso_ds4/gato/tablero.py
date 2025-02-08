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

def usuario(simbolos:dict):
    '''Estrategia del usuario'''
    ocupado = True
    lista_numeros =[str(i) for i in range(1,10)]
    while ocupado is True:
        x= input('Elija un número del 1 al 9: ')
        if x in lista_numeros:
            if simbolos[x] not in ['X','O']:
                simbolos[x]= 'X'
                ocupado=False
            else:
                print('Ta ocupado')
        else:
            print('del 1 al 9, pesado')

def juego(simbolos:dict):
    '''juego del gato'''
    lista_combinaciones=[
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['1','4','7'],
        ['2','5','8'],
        ['3','6','9'],
        ['1','5','9'],
        ['3','5','7']]
    en_juego=True
    movimientos=0
    gana=None
    dibuja_tablero(simbolos)
    while en_juego:
        usuario(simbolos)
        dibuja_tablero(simbolos)
        movimientos +=1
        gana = checa_ganador(simbolos,lista_combinaciones)
        if gana is not None:
            en_juego = False
        if movimientos >=9:
            en_juego=False
            continue
        ia(simbolos)
        dibuja_tablero(simbolos)
        movimientos+=1
        gana = checa_ganador(simbolos,lista_combinaciones)
        if gana is not None:
            en_juego=False
        if movimientos >=9:
            en_juego=False
            continue
    return gana

def checa_ganador(simbolos:dict,combinaciones:list):
    '''Checa si hay un ganador'''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos[c[0]]
    return None

def actualizar_score(score:dict,ganador:str):
    '''Actualiza el score'''
    X=score["X"]
    O=score["O"]
    g = ganador
    if g is not None:
        print(f'El ganador es {g}')
        if g == 'X':
            X["G"]+=1
            O["P"]+=1
        elif g == 'O':
            O["G"]+=1
            X["P"]+=1
        else:
            X["E"]+=1
            O["E"]+=1
    else:
        print('Empate')
        X["E"]+=1
        O["E"]+=1

def despliega_tablero(score:dict):
    '''Despliega el tablero de score'''
    print(f'''
      X | G: {score["X"]["G"]} | P:{score["X"]["P"]} | E:{score["X"]["E"]}
      O | G: {score["O"]["G"]} | P:{score["O"]["P"]} | E:{score["O"]["E"]}
      ''')
    
if __name__== '__main__':
    numeros =[str(i) for i in range(1,10)]
    dic_simbolos={x:x for x in numeros}
    g = juego(dic_simbolos)
    if g is not None:
        print(f'El ganador es {g}')
    else:
        print(f'Empate')
    '''dibuja_tablero(dic_simbolos)
    ia(dic_simbolos)
    dibuja_tablero(dic_simbolos)
    usuario(dic_simbolos)
    dibuja_tablero(dic_simbolos)


    x = random.choice(numeros)
    numeros.remove(x)
    dic_simbolos[x]='X'
    dibuja_tablero(dic_simbolos)
    o= random.choice(numeros) 
    numeros.remove(o)
    dic_simbolos[o]='O'
    dibuja_tablero(dic_simbolos)
    print(numeros)'''  
