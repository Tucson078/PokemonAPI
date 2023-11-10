
idaYVuelta = {"tipo": 1,"danio": 70,"precision": 100,"prioridad": 0,"usos": 20}
dobleRayo = {"tipo": 1,"danio": 75,"precision": 100,"prioridad": 0,"usos": 20}  
tijeraX = {"tipo": 1,"danio": 80,"precision": 100,"prioridad": 0,"usos": 15}
danzaAleteo = {"tipo": 1,"danio": 0,"precision": 100,"prioridad": 0,"usos": 10,"aumento": 50}

ataquesPorTipos = {
    'bug' : {"idaYVuelta":idaYVuelta,"dobleRayo":dobleRayo,"tijeraX":tijeraX,"danzaAleteo":danzaAleteo}
}

print(ataquesPorTipos['bug']["dobleRayo"])