def numero_mas_grande(primero,segundo,tercero):
    mayor = ""
    if primero >= segundo and primero >= tercero:
        mayor = primero
    elif primero > segundo and primero > tercero:
         mayor = primero
    elif segundo > primero and segundo > tercero:
        mayor = segundo
    elif tercero > primero and tercero > segundo:
        mayor = tercero

    return mayor





numero_mayor = numero_mas_grande(primero=80,segundo=80,tercero=580)
print("El numero mayor de los 3 numeros es el {}".format(numero_mayor))



