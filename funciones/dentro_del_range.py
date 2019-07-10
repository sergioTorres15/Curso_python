def numero_en_rango(numero,min,max):
    respuesta = ""
    if numero in range(min,max):
        respuesta = "True"
    else:
        respuesta = "False"
    return respuesta



range = numero_en_rango(numero = 185, min = 1 , max = 100)
print("el numero esta dentro del rango : {}".format(range))