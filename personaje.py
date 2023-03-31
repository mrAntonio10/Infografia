import time
import numpy as np
class Personaje:
    '''
    La clase personaje nos permite definir un "ENTE"
    que tenga nombre, vidalidad: se presente y diga si esta viva
    '''
    #Constructor para definir un personaje
    def __init__(self, nombre, vitalidad):
        self.nombre = nombre
        self.vitalidad = vitalidad
    
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def esta_vivo(self):
        return self.vitalidad > 0

class Jugador(Personaje):
    '''
    Un Jugador hereda nombre y vitalidad de lo que es un personaje
    A diferencia que este tiene habilidades
    v2: el jugador ahora tiene la opcion de devolver un contraataque
    Nuevo atributo, ataque.
    '''
    #Constructor para definir un jugador
    def __init__(self, nombre, vitalidad, habilidades, ataque):
        #Heredamos los metodos de un personaje
        super().__init__(nombre, vitalidad)
        self.habilidades = habilidades
        self.ataque = ataque

    def recibir_daño(self, daño):
        self.vitalidad -= daño

    def listar_habilidades(self):
        for h in self.habilidades:
            print(f"Puedo {h}")
    #El contraataque va a tener un 25% de probabilidad critico
    def contraataque(self, jugador):
        #probabilidad de critico
        crit = np.random.randint(1,5)
        if (crit<4):
            #creo una variable de self.danio aleatoria entre el rango definido
            dmg = np.random.randint(self.ataque[0], self.ataque[1])
            print(f"Jugador {self.nombre} realiza un contraataque al enemigo {jugador.nombre} con daño: {dmg}\n")
            jugador.recibir_daño(dmg)
        else:
        #creo una variable de self.danio aleatoria entre el rango definido
            dmg = np.random.randint(self.ataque[0], self.ataque[1])
            print(f"Jugador {self.nombre} realiza un contraataque CRITICO al enemigo {jugador.nombre} con daño: 70\n")
            jugador.recibir_daño(70)

class Enemigo(Personaje):
    def __init__(self, nombre, vitalidad, daño, ataque_esp):
        super().__init__(nombre, vitalidad)
        self.daño = daño
        self.ataque_esp = ataque_esp

    def recibir_daño(self, daño):
        self.vitalidad -= daño
    
    def atacar_jugador(self, jugador):
        #creo una variable de self.danio aleatoria entre el rango definido
        dmg = np.random.randint(self.daño[0], self.daño[1])
        print(f"Enemigo {self.nombre} atacando a jugador {jugador.nombre} con daño: {dmg}\n")
        jugador.recibir_daño(dmg)

#danio de los personajes: entre 0 - 50
dmg = [0,51]

#Jugador maneja variables nombre - vida - habilidades - ataque
jugador = Jugador("Juan", 90, ["atacar", "volar", "esquivar"], dmg)
jugador.listar_habilidades()
jugador.saludo()

print(f'\n\n\n ----SECCION DE COMBATE----\n')

#Nombre - vida - danio - ataque_esp
enemigo = Enemigo("Raul", 100, dmg, 70)


while jugador.esta_vivo() and enemigo.esta_vivo():
    enemigo.atacar_jugador(jugador)
    print(f"vitalidad {jugador.nombre}: {jugador.vitalidad}")
    time.sleep(2)
    
    jugador.contraataque(enemigo)
    print(f"vitalidad {enemigo.nombre}: {enemigo.vitalidad}")
    #Mostramos los displays cada 2 seg :o
    time.sleep(2)

if (jugador.esta_vivo()):
    print(f"El Enemigo {enemigo.nombre} ha muerto")
else:
    print(f"El jugador {jugador.nombre} ha muerto")

# EJERCICIO:
# Modificar este programa para agregar las siguientes caracteristicas:
# 1. Agregar logica de daño aleatorio al enemigo.
# 2. Agregar lógica de contraataque del jugador.
# 3. Agregar posibilidad de daño crítico en contra ataque del jugador.

