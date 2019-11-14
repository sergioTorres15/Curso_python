
salida = False
agenda = []
while not salida:

    accion = input("Que quieres hacer? [[A] Añadir un telefono / [B] Consultar un telefono] Salir [S] : ")
    #Accion añadir
    if accion == "A":
        print("Vamos añadir un numero telefonico")
        print("-----------------------------------")
        nombre = input("Nombre :")
        numero = input("Numero :")
        agenda.append([nombre,numero])

    #Accion consultar
    elif accion == "B":
        print("Vamos a consultar un numero ")
        print("-----------------------------------")
        nombre = input("De quien quieres saber el numero:")
        for nombre_numero in agenda:
            if nombre_numero[0] == nombre:
                print(nombre_numero[1])


    #Accion salir
    elif accion == "S":
        salida = True


