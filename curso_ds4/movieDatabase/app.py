'''PROGRAMA PRINCIPAL DE MOVIE DATABASE'''  
# Importamos las librerías necesarias
from flask import Flask, render_template, request, redirect, url_for
import random
import movie_clases as mc

app = Flask(__name__)
sistema = mc.SistemaCine()
actores_csv = 'datos/movies_db - actores.csv'
peliculas_csv = 'datos/movies_db - peliculas.csv'
relaciones_csv = 'datos/movies_db - relacion.csv'
users_csv = 'datos/movies_db - users.csv'
sistema.cargar_csv(actores_csv,mc.Actor)
sistema.cargar_csv(peliculas_csv,mc.Pelicula)
sistema.cargar_csv(relaciones_csv,mc.Relacion)
sistema.cargar_csv(users_csv,mc.User)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/actores')
def actores():
    '''Muestra la lista de actores'''
    lista_actores = sistema.actores.values()
    return render_template('actores.html',actores=lista_actores)

@app.route('/peliculas')
def peliculas():
    '''Muestra la lista de películas'''
    lista_peliculas = sistema.peliculas.values()
    return render_template('peliculas.html',peliculas=lista_peliculas)

if __name__ == '__main__':
    app.run(debug=True)
