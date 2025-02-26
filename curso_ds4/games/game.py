'''

'''
from Athlete import Athlete
from Sport import Sport
from Team import Team
from random import choice
import json
class Game:
    '''
    Clase Game: Juego entre dos equipos
    '''
    sport_dict ={
            'LMP':[x for x in range(0,11)],
            'NBA':[x for x in range(50,136)],
            'NFL':[x for x in range(0,61)],
            'MLB':[x for x in range(0,21)],
            'MLX':[x for x in range(0,11)],
            'FIFA':[x for x in range(0,11)]
        }
    def __init__(self,A:Team,B:Team):
        '''
        Constructor de la clase Game
        '''
        self.A=A
        self.B=B
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0


    def play(self):
        '''
        Juego simulado entre dos equipos
        '''
        league = self.A.sport.league
        points = self.sport_dict[league]
        #print(points)
        a = choice(points)
        b = choice(points)
        self.score[self.A.name] = a
        self.score[self.B.name] = b

    def __str__(self):
        '''Metodo para representar la clase como string'''
        return f'Game: {self.A.name}: {self.score[self.A.name]} - {self.B.name}: {self.score[self.B.name]} '

    def __repr__(self):
        '''Metodo para representar la clase como string'''
        return f'Game(A={repr(self.A)}, B={repr(self.B)} score={self.score})'
    
    def to_json(self) -> dict:
        '''Metodo para representar la clase como diccionaraio '''
        return {'A':self.A.to_json(), 'B':self.B.to_json(), 'score':self.score}

if __name__ == '__main__':
    dt = ['Jordan','Johnson','Pipen','Bird','Kobe']
    cz = ['Bjovik','Czack','Pfeizer','Leonard','Kempfe']
    players_a = [Athlete(x) for x in dt]
    players_b = [Athlete(x) for x in cz]
    basketball = Sport('Basketball',5,'NBA')
    team_a = Team('Dream Team',basketball,players_a)
    team_b= Team('Czk. Rep.',basketball,players_b)
    juego =Game(team_a,team_b)
    print(juego)
    juego.play()
    print(juego)
    print('------------------------------------------------------------------------------')
    print(repr(juego))
    print(juego.to_json())
    filename_json = "game.json"
    with open(filename_json,"w",encoding='utf8') as f:
        json.dump(juego.to_json(),f, ensure_ascii=False,indent=4)
    print(f"Archivo {filename_json} guardado con éxito!")
        #f.write(str(juego.to_json()))

