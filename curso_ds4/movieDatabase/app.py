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

if __name__ == '__main__':
    app.run(debug=True)
