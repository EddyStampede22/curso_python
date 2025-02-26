'''
CLASE SPORT
'''
class Sport:
    '''
    CLASE PARA REPRESENTAR UN DEPORTE
    '''
    def __init__(self,name:str,players:int,league:str):
        '''
        constructor de la clase Sport
        '''
        self.name=name
        if isinstance(players,int):
            #VERIFICAMOS QUE SEA UN ENTERO
            self.players = players
        else:
            self.players = int(players) # CONVERTIMOS A ENTERO 
        self.league=league
    
    def __str__(self):
        '''
        Método para representar la clase como string
        '''
        return f"Sport: {self.name}, {self.players}, {self.league}"
    
    def __repr__(self):
        '''método para representar la clase como string'''
        return f"Sport(name='{self.name}',players={self.players},league='{self.league}')"
    
    def to_json(self) -> dict:
        '''
        Método para representar la clase como diccionario
        '''
        return{"name":self.name,"players":self.players,"league":self.league}
    

if __name__=='__main__':
    s=Sport("Soccer",11,"FIFA")
    #print(s)
    #print(repr(s))
    #print(s.to_json())
    nfl=Sport('Football','11','NFL')
    lmp=Sport('Baseball',9,'LMP')
    mlb=Sport('Baseball',9,'MLB')
    lmx=Sport('Soccer',11,'Liga Mx')
    nba = Sport('Basketball',5,'NBA')
    lista_deportes =[nfl,lmp,lmx,nba,s]
    archivo_deportes = "deportes.txt"

    with open(archivo_deportes,"w") as file:
        for d in lista_deportes:
            file.write(repr(d)+"\n")

    sport_list = []
    with open (archivo_deportes,"r") as file:
        for line in file:
            d= eval(line)
            sport_list.append(d)
    

    #print(sport_list)
    #print(sport_list[0].to_json())
    # Escribiremos el archivo en formato JSON 
    import json
    archivo_json = "deportes.json"
    #with open(archivo_json,"w") as file:
    #       json.dump(d.to_json(),file)
    #        file.write("\n")
    # Leemos el archivo JSON
    sports_json = [sport.to_json() for sport in sport_list]
    with open(archivo_json, "w", encoding='utf8') as file:
        json.dump(sports_json, file, indent=4)

    # Leer archivo Json

    sport_list_json =[]
    with open(archivo_json,"r") as file:
        sport_list_json = json.load(file)
    print(sport_list_json)
    print(repr(sport_list_json[0]))
    



    