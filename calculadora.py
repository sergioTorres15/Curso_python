

saludo = print("hola bienvenido")
volver = "si"
while volver == "si":

    print("a) suma")
    print("b) resta")
    print("c) multplicacion")
    print("d) division")

    opcion = input("elige una opcion :")

    numero = int(input("inserta un numero :"))
    numero_dos = int(input("inserta otro numero :"))

    if opcion == "a":
        suma = numero + numero_dos
        print("el resultado es {}".format(suma))
        volver = input("quieres volver a iniciar? (si / no) :")

    elif opcion == "b":
        resta = numero - numero_dos
        print("el resultado es {}".format(resta))
        volver = input("quieres volver a iniciar? (si / no) :")

    elif opcion == "c":
        multiplicacion = numero * numero_dos
        rint("el resultado es {}".format(multiplicacion))
        volver = input("quieres volver a iniciar? (si / no) :")

    elif opcion == "d":
        division = numero / numero_dos
        print("el resultado es {}".format(division))
        volver = input("quieres volver a iniciar? (si / no) :")





print("adios")











