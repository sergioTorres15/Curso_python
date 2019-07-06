frase_usuario = input("introduce una frase : ")
frase_final = ""

dato = ""

for indice in range(len(frase_usuario)):
    if frase_usuario[indice] in "aeiou":

        frase_final += str(indice)
    else:
        caracter = frase_usuario[indice]
        frase_final += caracter



print(frase_final)