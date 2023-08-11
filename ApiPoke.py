import requests
import random

lista = []

class Pokemon():
    nombre = ""
    vida = 0
    velocidad = 0
    tipo1 = ""
    tipo2 = ""
    atk = 0
    specialAtk = 0
    defensa = 0
    id = 0

    def __init__(self):
        res = ""
        while "200" not in str(res):
            self.id = random.randint(1, 1281)
            
            url = f"https://pokeapi.co/api/v2/pokemon/{self.id}/"
            res = requests.get(url)
            if "200" in str(res):
                data = res.json()
                self.nombre = data['forms'][0]['name']
                self.vida = data['stats'][0]['base_stat']
                self.velocidad = data['stats'][5]['base_stat']
                self.atk = data['stats'][1]['base_stat']
                self.specialAtk = data['stats'][3]['base_stat']
                self.defensa = data['stats'][2]['base_stat']
                self.tipo1 = data['types'][0]['type']['name']
                if len(data["types"]) > 1:
                    self.tipo2 = data['types'][1]['type']['name']
                
                print(self.nombre, self.vida, self.id,self.velocidad,self.tipo1,self.tipo2)

for i in range(10):
    pk = Pokemon()
    lista.append(pk)

for i in lista:
    print(i.nombre)