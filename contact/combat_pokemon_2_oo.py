import sys
class Pokemon:
    vida_base = 100
    ataque = 10
    ataqueOne = 0
    nombre = "pokemon"


    def __init__(self):
        self.vida = self.vida_base


    def atacar(self, enemigo):
        enemigo.recibir_danio(self.ataque)

    def atacarOne(self, enemigo):
            enemigo.recibir_danio(self.ataqueOne)
    def recibir_danio(self, danio):
        self.vida -= danio
    def show_life(self):
        print("La vida de {} es de {}".format(self.nombre, self.vida))

class Charmander(Pokemon):
    vida_base = 100
    ataque = 50
    ataqueOne = 0
    nombre = "Charmander"
class Squirtle(Pokemon):
    vida_base = 100
    ataque = 35
    nombre = "Squirtle"
class Balbasuer(Pokemon):
    vida_base = 90
    ataque = 45
    ataqueOne = 0
    nombre = "Balbasuer"
class MiPokemon(Pokemon):
    vida_base = 120
    ataque = 30
    ataqueOne = 50
    nombre = "Pikachu"


elegido = input("Con que pokemon quieres luchar Charmander / Squirtle / Balbasuer : ")

if elegido == "charmander" or "balbasuer" or "squirtle":
    luchador = MiPokemon()
    luchador.show_life()

    if elegido == "charmander":
        contrincante = Squirtle()
    elif elegido == "balbasuer":
        contrincante = Balbasuer()
    elif elegido == "squirtle":
        contrincante = Squirtle()

    contrincante.show_life()
    while luchador.vida > 0 and contrincante.vida:
        ataque =input("Que ataque quieres usaar chispazo / bolavoltio : ")
        if ataque == "chispazo":
            luchador.atacar(contrincante)
        if ataque == "bolavoltio":
            luchador.atacarOne(contrincante)
            if contrincante.vida <= 0:
                print("combate finalizado GANASTE")
                contrincante.show_life()
                sys.exit()
            contrincante.show_life()
            print("***********\nahora ataca {}\n***********".format(elegido))
            contrincante.atacar(luchador)
            luchador.show_life()
            if luchador.vida <= 0:
                print("Has perdido")
                luchador.show_life()
                sys.exit()








