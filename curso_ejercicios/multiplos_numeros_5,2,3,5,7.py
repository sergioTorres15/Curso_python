numeros_usuarios = [1,10,70,30,50,55]
multiplos_dos = []
multiplos_3 = []
multiplos_5 = []
multiplos_7 = []

for indice in range(len(numeros_usuarios)):
    dato = numeros_usuarios[indice]
    if dato % 2 ==0 and dato % 3 == 0 :
        multiplos_dos.append(dato)
        multiplos_3.append(dato)

    elif dato % 2 == 0:
        multiplos_dos.append(dato)
    elif dato % 3 == 0:
        multiplos_3.append(dato)

    if dato % 5 == 0 and dato % 7 == 0:
        multiplos_5.append(dato)
        multiplos_7.append(dato)

    elif dato % 5 == 0:
        multiplos_5.append(dato)
    elif dato % 7 == 0:
        multiplos_7.append(dato)




print("numeros que ingresaste : {}".format(numeros_usuarios))
print("..............................")
print("los multiplos de 2 son : {}".format(multiplos_dos))
print("los multiplos de 3 son : {}".format(multiplos_3))
print("los multiplos de 5 son : {}".format(multiplos_5))
print("los multiplos de 7 son : {}".format(multiplos_7))