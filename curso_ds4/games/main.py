'''
Archivo Principal del juego Game

'''
from Athlete import Athlete
from Sport import Sport
from Team import Team
from game import Game
import json

def main(archivo_torneo:str):
    '''
    Función principal del juego
    '''

    if archivo_torneo != "":
        with open(archivo_torneo,"r",encoding='utf8') as file:
            torneo =json.load(file)
            
    else:
        players_mexico= [
            'Chicharito','Piojo','Chucky','Tecatito','Gullit'
            ,'Ochoa','Guardado','Herrera', 'Layun','Moreno', 'Araujo'
        ]
        players_espania=['Casillas','Ramos','Pique','Alba','Iniesta','Silva','Isco','Busquets'
                         ,'Costa','Morata','Asensio']
        
        players_brazil =['Neymar','Coutinho','Marcelo','Casemiro','Alisson','Jesus','Paulinho','Thiago',
                         'Silva','Firminho','Danilo']
        players_argentina=['Messi','Aguero','Di Maria','Mascherano','Higuain','Dybala','Otamendi','Romero'
                           ,'Rojo','Banega','Fazio']
        
        lista_brazil =[Athlete(x) for x in players_brazil]
        lista_argentina =[Athlete(x) for x in players_argentina]
        lista_mexico = [Athlete(x) for x in players_mexico ]
        lista_espania = [Athlete(x) for x in players_espania]
        soccer = Sport("Soccer",11,"FIFA")
        mexico = Team("Mexico",soccer,lista_mexico)
        espania = Team("España",soccer,lista_espania)
        brazil =Team("Brazil",soccer,lista_brazil)
        argentina = Team("Argentina",soccer,lista_argentina)
        equipos =[mexico,espania,brazil,argentina]
        d ={}
        for local in equipos:
            for visitantes in equipos:
                if local != visitantes:
                    juego = Game(local,visitantes)
                    partido = f'{local}-{visitantes}'
                    partido2 = f'{visitantes}-{local}'
                    if partido not in d and partido2 not in d:
                        d[partido] = juego.to_json()

       
        torneo = list(d.values())
        #juego = Game(mexico,espania)
        #torneo = [juego.to_json()]
        archivo_torneo = "torneo.json"
        with open(archivo_torneo,"w",encoding='utf8') as f:
            json.dump(torneo,f,ensure_ascii=False,indent=4)
        print(f"se escribió el archivo {archivo_torneo} con un torneo de {len(torneo)} juego(s)")
    # Jugar todos los juegos del torneo
    for juego in torneo:
        A = Team(juego['A']['name'], Sport(juego['A']['sport']['name'],juego['A']['sport']['players'],juego['A']['sport']['league']),[Athlete(x['name']) for x in juego['A']['players']])
        B = Team(juego['B']['name'], Sport(juego['B']['sport']['name'],juego['B']['sport']['players'],juego['B']['sport']['league']),[Athlete(x['name']) for x in juego['B']['players']])
        game= Game(A,B)
        game.play()
        print(game)
        print('--------------------------------------')


if __name__ == '__main__':
    archivo_torneo ="torneo.json"
    main(archivo_torneo)