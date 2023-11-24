import requests
import random
from Ataques import *

lista = []

class Pokemon():
    nombre = ""
    vida = 0
    velocidad = 0
    tipo1 = ""
    tipo2 = ""
    atk = 0
    specialAtk = 0
    specialDefensa = 0
    defensa = 0
    id = 0
    img = ""
    imgEspalda = ""
    ataques = {}
        
    

    def __init__(self,id):
        self.obtenerDatosPoke(id)
        #print(f"datos obtenidos pokemon {self.nombre}")
        self.obtenerAtaque()
        

    def obtenerDatosPoke(self, id):
        self.id = id
        res = ""
        while "200" not in str(res):
            #self.id = random.randint(1, 1281)
            
            url = f"https://pokeapi.co/api/v2/pokemon/{self.id}/"

            res = requests.get(url)
            if "200" in str(res):
                data = res.json()
                self.img = data['sprites']['front_default']
                self.nombre = data['forms'][0]['name']
                self.vida = data['stats'][0]['base_stat']
                self.velocidad = data['stats'][5]['base_stat']
                self.atk = data['stats'][1]['base_stat']
                self.specialAtk = data['stats'][3]['base_stat']
                self.defensa = data['stats'][2]['base_stat']
                self.tipo1 = data['types'][0]['type']['name']
                self.specialDefensa = data['stats'][4]['base_stat']
                self.imgEspalda = data['sprites']['back_default']
                if len(data["types"]) > 1:
                    self.tipo2 = data['types'][1]['type']['name']
    
    def obtenerAtaque(self):
        if self.tipo2:  # Si el Pokémon tiene tipo 2 obtiene ataques de ambos tipos de elemento
           self.ataques = {} # Diccionario vacio de ataques para almacenar donde la clave del diccionario es el nombre del ataque y el valor es el ataque en sí mismo.
           ataques_tipo1 = ataquesPorTipos[self.tipo1]  # Obtiene los ataques del tipo 1 y 2 del diccionario ataquesPorTipos{}
           ataques_tipo2 = ataquesPorTipos[self.tipo2] 

        # Obtiene 2 ataques aleatorios del Pokemontipo 2 (Ejemplo 2 ataques de water y 2 de rock)
           ataques_elegidos_tipo1 = random.sample(list(ataques_tipo1.keys()), 2) # Elige random 2 ataques del tipo 1 y 2 almacena sus claves en la lista.
           ataques_elegidos_tipo2 = random.sample(list(ataques_tipo2.keys()), 2) # list convierte las claves (nombres de ataques) del diccionario ataques_tipo1 en una lista.
        #La función sample() del módulo random selecciona elementos de la lista de claves sin repetición y los devuelve como una lista (ataques_elegidos_tipo1 en este caso).
        
        
        # Agregar los ataques elegidos del tipo 1 y tipo 2 al diccionario de ataques{} del pokemon.
           for ataque_tipo1 in ataques_elegidos_tipo1: # recorren los ataques elegidos de cada tipo
                self.ataques[ataque_tipo1] = ataques_tipo1[ataque_tipo1] # los agrega al diccionario 
           for ataque_tipo2 in ataques_elegidos_tipo2:
                self.ataques[ataque_tipo2] = ataques_tipo2[ataque_tipo2] # Esto se hace para incluir los ataques seleccionados en el conjunto total de ataques del Pokémon.
        else:
            self.ataques = ataquesPorTipos[self.tipo1]  # Si el Pokémon es de tipo 1 va a obtener los 4 ataques de ese unico tipo.
        

    def __repr__(self):
        return f'{self.nombre} - {self.id}'

if __name__ == '__main__':                
    #pk = Pokemon(1)
    pk2 = Pokemon(445)

