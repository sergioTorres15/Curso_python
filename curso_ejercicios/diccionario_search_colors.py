colors = {"rojo": "red",
          "azul": "blue",
          "amarillo": "yellow"}

print("buscador de traduccion de color a english")
print("********************************************")
buscar = input("Que color quieres buscar la traduccion? : ")
traduccion = (colors[buscar])
print("La traduccion del color {} a ingles es : {}".format(buscar,traduccion))