Bicho1 = ["Ida y vuelta","Doble rayo","Tijera X","Danza aleteo"]



idaYVuelta = {"tipo": 1,"danio": 70,"precision": 100,"prioridad": 0,"usos": 20}

dobleRayo = {"tipo": 1,"danio": 75,"precision": 100,"prioridad": 0,"usos": 20}
    
tijeraX = {"tipo": 1,"danio": 80,"precision": 100,"prioridad": 0,"usos": 15}

danzaAleteo = {"tipo": 1,"danio": 0,"precision": 100,"prioridad": 0,"usos": 10,"aumento": 50}

Dragon2 =  ["Pulso dragón","Ráfaga escamas","Rayo infinito","Vasto impacto"]



pulsoDragon = {"tipo": 2,"danio": 85,"precision": 100,"prioridad": 0,"usos": 10}

rafagaEscamas = {"tipo": 2,"danio": 25,"cantGolpes": 0,"precision": 100,"prioridad": 0,"usos": 32}

rayoInfinito = {"tipo": 2,"danio": 160,"precision": 90,"prioridad": 0,"usos": 8}

vastoImpacto = {"tipo": 2, "danio": 60, "precision": 90, "prioridad": 0, "usos": 15}


Eletrico3 = ["Puños plasma","Rayo","Rayo carga","Rayo fusión"]



puñosPlasma = {"tipo": 3, "danio": 100, "precision": 100, "prioridad": 0, "usos": 15}

rayo = {"tipo": 3, "danio": 90, "precision": 100, "prioridad": 0, "usos": 15}

rayoCarga = {"tipo": 3, "danio": 50, "precision": 90, "prioridad": 0, "usos": 16}

rayoFusion = {"tipo": 3, "danio": 100, "precision": 10, "prioridad": 0, "usos": 5}


Hada4= ["Geocontrol", "Luz aniquiladora", "Luz lunar", "Niebla aromática"]


geocontrol = {"tipo": 4, "danio": 0, "precision": 100, "prioridad": 0, "usos": 10}

luzAniquiladora = {"tipo": 4, "danio": 140, "precision": 90, "prioridad": 0, "usos": 8}

luzLunar = {"tipo": 4, "danio": 80, "precision": 100, "prioridad": 0, "usos": 30}

nieblaAromatica = {"tipo": 4, "danio": 0, "precision": 100, "prioridad": 0, "usos": 10, "bajada": 30}



Lucha5 = ["Golpe roca","Inversión", "Llave corsé", "Lanza Roca"]



golpeRoca = {"tipo": 5, "danio": 40, "precision": 100, "prioridad": 0, "usos": 14, "bajada": 20}

inversion = {"tipo": 5, "danio": 150, "precision": 70, "prioridad": 0, "usos": 10}

llaveCorse = {"tipo": 5, "danio": 80, "precision": 100, "prioridad": 0, "usos": 10}

lanzaRoca = {"tipo": 5, "danio": 70, "precision": 100, "prioridad": 1, "usos": 15}


Fuego6= ["Puño fuego","Rueda fuego","Sofoco","Lanzallamas"]
    


puñoFuego = {"tipo": 6, "danio": 75, "precision": 100, "prioridad": 0, "usos": 15, "quemar": 10}

ruedaFuego = {"tipo": 6, "danio": 60, "precision": 100, "prioridad": 0, "usos": 24, "quemar": 10}

sofoco = {"tipo": 6, "danio": 130, "precision": 90, "prioridad": 0, "usos": 8, "quemar": 10}

lanzaLLamas = {"tipo": 6, "danio": 90, "precision": 100, "prioridad": 0, "usos": 20, "quemar": 10}


Volador7 = ["Ataque aéreo","Ataque ala","Golpe aéreo","Pico taladro"]



ataqueAereo = {"tipo": 7, "danio": 140, "precision": 90, "prioridad": 0, "usos": 5}

ataqueAla = {"tipo": 7, "danio": 60, "precision": 100, "prioridad": 0, "usos": 40}

golpeAereo = {"tipo": 7, "danio": 10, "precision": 30, "prioridad": 0, "usos": 8}

picoTaladro = {"tipo": 7, "danio": 80, "precision": 100, "prioridad": 0, "usos": 20}


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

def lanzaGlacial():
    tipo = 11
    daño = 120
    precision = 100
    prioridad = 0
    usos = 5

def martilloHielo():
    tipo = 11
    daño = 100
    precision = 90
    prioridad = 0
    usos = 16

def puñoHielo():
    tipo = 11
    daño = 75
    precision = 100
    prioridad = 0
    usos = 20

def bolaHielo():
    tipo = 11
    daño = 40
    precision = 100
    prioridad = 0
    usos = 10
    congelar = 10

Normal12 = ["Arañazo","Ataque rápido","Agarre","Tambor"]

def arañazo():
    tipo = 12
    daño = 40
    precision = 100
    prioridad = 0
    usos = 20

def ataqueRapido():
    tipo = 12
    daño = 40
    precision = 100
    prioridad = 1
    usos = 30

def tambor():
    tipo = 12
    dañopropio = 0.5
    prioridad = 0
    usos = 8
    aumento = 2

def agarre():
    tipo = 12
    daño = 100
    precision = 100
    prioridad = 0
    usos = 20
     


Veneno13 = ["Búnker","Carga tóxica","Envenenar","Bomba ácida"]

def bunker():
    tipo = 13
    daño = 0
    precision = 100
    dañorival = 0
    prioridad = 1
    usos = 8

def cargaToxica():
    tipo = 13
    daño = 45
    precision = 100
    prioridad = 0
    usos = 30

def envenenar():
    tipo = 13
    daño = 20
    aumentoDeDaño = 2
    precision = 80
    prioridad = 0
    usos = 10

def bombaAcida():
    tipo = 13
    daño = 50
    precision = 100
    prioridad = 0
    usos = 20

Psiquico14 = ["Agilidad","Bola neblina","Danza lunar","Psicoataque"]

def agilidad():
    tipo = 14
    daño = 0
    aumento = 2
    prioridad = 0
    precision = 100
    usos = 4

def bolaNeblina():
    tipo = 14
    daño = 120
    precision = 80
    prioridad = 0
    usos = 8

def danzaLunar():
    tipo = 14
    daño = 0
    precision = 100
    prioridad = 0
    usos = 8
    aumento = 1.5

def psicoAtaque():
    tipo = 14
    daño = 80
    precision = 100
    prioridad = 0 
    usos = 20

Roca15 = ["Pedrada","Lanzarrocas","Tumba rocas","Roca veloz"]

def pedrada():
    tipo = 15
    daño = 90
    precision = 100
    prioridad = 0
    usos = 20

def lanzaRocas():
    tipo = 15
    daño = 30
    precision = 100
    prioridad = 0
    usos = 15

def tumbaRocas():
    tipo = 15
    daño = 150
    precision = 60
    prioridad = 0
    usos = 8

def rocaVeloz():
    tipo = 15
    daño = 50
    precision = 100
    prioridad = 1
    usos = 20

Acero16 = ["Giro bola","Puño bala","Cuerpo pesado","Garra metal"]

def giroBola():
    tipo = 16
    daño = 80
    precision = 100
    prioridad = 0
    usos = 15

def puñoBala():
    tipo = 16
    daño = 100
    precision = 100
    prioridad = 0
    usos = 10

def cuerpoPesado():
    tipo = 16
    daño = 200
    precision = 100
    prioridad = 0
    usos = 2

def garraMetal():
    tipo = 16
    daño = 40
    precision = 100
    prioridad = 1
    usos = 10

Agua17 = ["Burbuja","Pistola de agua","Hidrobomba","Hidropulso"]

def burbuja():
    tipo = 17
    daño = 0
    precision = 100
    prioridad = 0
    usos = 4
    aumento = 1.5

def pistolaDeAgua():
    tipo = 17
    daño = 60
    precision = 100
    prioridad = 1
    usos = 30

def hidroBomba():
    tipo = 17
    daño = 100
    precision = 100
    prioridad = 0
    usos = 20

def hidroPulso():
    tipo = 17
    daño = 150 
    precision = 80
    prioridad = 0
    usos = 5

def calcularEfectividad():
    