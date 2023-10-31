Bicho1 = ["Ida y vuelta","Doble rayo","Tijera X","Danza aleteo"]

def idaYVuelta():
    tipo = 1
    daño = 70
    precision = 100
    prioridad = 0
    usos = 20

def dobleRayo():
    tipo = 1
    daño = 75
    precision = 100
    prioridad = 0
    usos = 20

def tijeraX():
    tipo = 1
    daño = 80
    precision = 100
    prioridad = 0
    usos = 15

def danzaAleteo():
    tipo = 1
    daño = 0 
    precision = 100
    prioridad = 0
    usos = 10
    aumento = 50

Dragon2 =  ["Pulso dragón","Ráfaga escamas","Rayo infinito","Vasto impacto"]

def pulsoDragon():
    tipo = 2
    daño = 85
    precision = 100
    prioridad = 0
    usos = 10

def rafagaEscamas():
    tipo = 2
    daño = 25
    cantGolpes = 0
    precision = 100
    prioridad = 0
    usos = 32

def rayoInfinito():
    tipo = 2
    daño = 160
    precision = 90
    prioridad = 0
    usos = 8

def vastoImpacto():
    tipo = 2
    daño = 60
    precision = 90
    prioridad = 0
    usos = 15

Eletrico3 = ["Puños plasma","Rayo","Rayo carga","Rayo fusión"]

def puñosPlasma():
    tipo = 3
    daño = 100
    precision = 100
    prioridad = 0
    usos = 15

def rayo():
    tipo = 3
    daño = 90
    precision = 100
    prioridad = 0
    usos = 15

def rayoCarga():
    tipo = 3
    daño = 50
    precision = 90
    prioridad = 0
    usos = 16

def rayoFusion():
    tipo = 3
    daño = 100
    precision = 10
    prioridad = 0
    usos = 5

Hada4= ["Geocontrol", "Luz aniquiladora", "Luz lunar", "Niebla aromática"]

def geocontrol():
    tipo = 4
    daño = 0
    precision = 100
    prioridad = 0
    usos = 10

def luzAniquiladora():
    tipo = 4
    daño = 140
    precision = 90
    prioridad = 0
    usos = 8

def luzLunar():
    tipo = 4
    daño = 80
    precision = 100
    prioridad = 0
    usos = 30

def nieblaAromatica():
    tipo = 4
    daño = 0
    precision = 100
    prioridad = 0
    usos = 10
    bajada = 30


Lucha5 = ["Golpe roca","Inversión", "Llave corsé", "Lanza Roca"]

def golpeRoca():
    tipo = 5
    daño = 40
    precision = 100
    prioridad = 0
    usos = 14
    bajada = 20

def inversion():
    tipo = 5
    daño = 150
    precision = 70
    prioridad = 0
    usos = 10

def llaveCorse():
    tipo = 5
    daño = 80
    precision = 100
    prioridad = 0
    usos = 10

def lanzaRoca():
    tipo = 5
    daño = 70
    precision = 100
    prioridad = 1
    usos = 15

Fuego6= ["Puño fuego","Rueda fuego","Sofoco","Lanzallamas"]
    
def puñoFuego():
    tipo = 6
    daño = 75
    precision = 100
    prioridad = 0
    usos = 15
    quemar = 10

def ruedaFuego():
    tipo = 6
    daño = 60
    precision = 100
    prioridad = 0
    usos = 24
    quemar = 10

def sofoco():
    tipo = 6
    daño = 130
    precision = 90
    prioridad = 0
    usos = 8
    quemar = 10

def lanzaLLamas():
    tipo = 6
    daño = 90
    precision = 100
    prioridad = 0
    usos = 20
    quemar = 10

Volador7 = ["Ataque aéreo","Ataque ala","Golpe aéreo","Pico taladro"]

def ataqueAereo():
    tipo = 7
    daño = 140
    precision = 90
    prioridad = 0
    usos = 5

def ataqueAla():
    tipo = 7
    daño = 60
    precision = 100
    prioridad = 0
    usos = 40

def golpeAereo():
    tipo = 7
    daño = 10
    precision = 30
    prioridad = 0
    usos = 8

def picoTaladro():
    tipo = 7
    daño = 80
    precision = 100
    prioridad = 0
    usos = 20

Fantasma8 =  ["Puño sombra","Puño fuego","Bola sombra","Impresionar"]

def puñoSombra():
    tipo = 8
    daño = 60
    precision = 100
    prioridad = 0
    usos = 24

def robaSombra():
    tipo = 8
    daño = 80
    precision = 80
    prioridad = 0
    usos = 20
    cura = 200

def bolaSombra():
    tipo = 8
    daño = 80
    precision = 100
    prioridad = 0
    usos = 20
    menosDef = 20

def impresionar():
    tipo = 8
    daño = 30
    precision = 100
    prioridad = 0
    usos = 12
    asustar = 20

Planta9 = ["Llueve hojas","Látigo cepa","Drenadoras","Espora"]

def llueveHojas():
    tipo = 9
    daño = 130
    precision = 80
    prioridad = 0
    usos = 5

def latigoCepa():
    tipo = 9
    daño = 45
    precision = 100
    prioridad = 0 
    usos = 40

Tierra10 = ["Bofetón lodo","Bomba fango","Excavar","Terremoto"]

def bofetonLodo():
    tipo = 10
    daño =  30
    precision = 100
    prioridad = 0
    menosPrecision = 15
    usos = 8

def bombaFango():
    tipo = 10
    daño = 65
    precision = 85
    prioridad = 0
    menosPrecision = 30
    usos = 8

def excavar():
    tipo = 10
    daño = 85
    precision = 100
    prioridad = 0
    usos = 20

def terremoto():
    tipo = 10
    daño = 130
    precision = 90
    prioridad = 0
    usos = 10

Hielo11 =  ["Lanza glacial","Martillo hielo","Puño hielo","Bola hielo"]

Normal12 = ["Arañazo","Ataque rápido","Agarre","Tambor"]

Veneno13 = ["Búnker","Carga tóxica","Envenenar","Bomba ácida"]

Psiquico14 = ["Agilidad","Bola neblina","Danza lunar","Psicoataque"]

Roca15 = ["Pedrada","Lanzarrocas","Tumba rocas","Roca veloz"]

Acero16 = ["Giro bola","Puño bala","Cuerpo pesado","Garra metal"]

Agua17 = ["Burbuja","Pistola de agua","Hidrobomba","Hidropulso"]
