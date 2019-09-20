import random

class Periferico:
    def __init__(self):
        self.NumSerie = random.randrange(100, 1000)
        self.estado = 100


class MonitorPredator(Periferico):
    alto = 40
    ancho = 50
    profundidad = 10
    resolucion = 1080
    pulgadas = 27
    color = "negro"
    conectores = "hdmi"
    botones = "apagado"



monitor1 = MonitorPredator()
monitor2 = MonitorPredator()
monitor3 = MonitorPredator()

print(monitor1.estado)
print(monitor1.NumSerie)

class Teclado(Periferico):
    alto = 3
    ancho = 50
    num_teclas = 71
    color = "negro"
    idioma = "es"


teclado1 = Teclado()
print(teclado1.estado)
print(teclado1.NumSerie)