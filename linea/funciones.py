'''
funciones auxiliares para el programa "Linea"
'''
def calcular_y(x,m,b):
    '''
    calcula "y" de acuerdo a la pendiente "m" y el punto de intersección en y "b"
    Retorna el valor de "y"
    '''
    return m*x + b

if __name__== "__main__":
    x = 0
    m = 3
    b = 2
    y = calcular_y(x,m,b)
    if y== 2:
        print("Te luciste pá")
    else:
        print("estás mal bro")

    