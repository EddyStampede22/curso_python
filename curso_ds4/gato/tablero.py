'''
Tablero.py: Dibuja el tablero del juego del gato
'''
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
    if __name__== '__main__':
        numeros =[str(i) for i in range(1,10)]
        dic_simbolos={x:x for x in numeros}
        dibuja_tablero(dic_simbolos)
    