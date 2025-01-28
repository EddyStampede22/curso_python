'''
Archivo Principal de linea
'''
import argparse
import funciones
def main(m,b):
    X=[x/10.5 for x in range(1,101,10)]
    Y=[funciones.calcular_y(x,m,b) for x in X] 
    #print(X)
    #print(Y)
    coordenadas = list(zip(X,Y))
    print(coordenadas)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Calcula las coordenadas de una linea recta')
    parser.add_argument('-m',type=float,help='Pendiente de la linea',default=2.0)
    parser.add_argument('-b',type=float,help='Interseccion en y',default=3.0)
    args=parser.parse_args()
    main(args.m,args.b)
