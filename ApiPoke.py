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
        #obtengo los ataques del tipo 1
        self.ataques = ataquesPorTipos[self.tipo1]
        #si tiene tipo2 obtengo los ataques y tengo que eliminar 2 aleatorios y agregar 2 aleatorios de ataque 2
        if self.tipo2:
            #creo dos listas para guardar las claves de los diccionarios de ataques para agregar y quitar
            listaQuitar = []
            listaAgregar = []
            #obtengo los ataques del tipo2
            self.ataques2 = ataquesPorTipos[self.tipo2]
            #mientras la listaQuitar tenga menos de dos elementos
            while len(listaQuitar) < 2:

                k = 0
                pos = random.randint(0, 3 - len(listaQuitar))
                for key in self.ataques:
                    if k == pos and key not in listaQuitar:
                        listaQuitar.append(key)
                    k += 1            
             
            while len(listaAgregar) < 2: 
                k2 = 0
                pos2 = random.randint(0, 3 - len(listaAgregar))
                for key2 in self.ataques2:
                    if k2 == pos2 and key2 not in listaAgregar:
                        listaAgregar.append(key2)
                    k2 +=1

            for j in range(2):
                self.ataques.pop(listaQuitar[j])
                self.ataques[listaAgregar[j]] = self.ataques2[listaAgregar[j]]
        

    def __repr__(self):
        return f'{self.nombre} - {self.id}'

if __name__ == '__main__':                
    #pk = Pokemon(1)
    pk2 = Pokemon(445)

