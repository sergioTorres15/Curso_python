
apariciones_palabras = dict()

frase_usuario = input("Ingresa una frase : ")
palabra = frase_usuario.split()

for dato in palabra:
    if dato in apariciones_palabras:
        apariciones_palabras[dato] += 1
    else:
        apariciones_palabras[dato] = 1

print(apariciones_palabras)