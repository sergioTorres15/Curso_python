
class Pokemon:
    vida_base = 100
    ataque = 10
    nombre = "pokemon"

    def __init__(self):
        self.vida = self.vida_base

    def atacar(self, enemigo):
        enemigo.recibir_danio(self.ataque)
    def recibir_danio(self, danio):
        self.vida -= danio
    def show_life(self):
        print("La vide de {} esde {}".format(self.nombre, self.vida))

class Charmander(Pokemon):
    vida_base = 100
    ataque = 10
    nombre = "Charmander"

class Pikachu(Pokemon):
    vida_base = 120
    ataque = 12
    nombre = "Pikachu"


class Bablasuer(Pokemon):
    vida_base = 90
    ataque = 7
    nombre = "Balbasuer"

mi_charmander = Charmander()
tu_pikachu = Pikachu()

mi_charmander.show_life()
tu_pikachu.show_life()

tu_pikachu.atacar(mi_charmander)
mi_charmander.show_life()

other_charmander = Charmander()
other_charmander.show_life()

mi_charmander.show_life()


