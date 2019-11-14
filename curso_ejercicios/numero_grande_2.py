numeros = []
numeros_usuario = ""


while len(numeros) < 10:
    numeros_usuario =input("introduce un numero : ")
    numeros.append(numeros_usuario)

numero_grande = numeros[0]

for numero_conparar in numeros:
    if numero_conparar > numero_grande:
        numero_grande = numero_conparar


print("el numero mas grande de los diez es el : {}".format(numero_grande))