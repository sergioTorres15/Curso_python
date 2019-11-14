frase_usuario_a_cambiar = input("introduce una frase :")
inicio = 0
dato = ""
frase_usuario_final = ""

while inicio < len(frase_usuario_a_cambiar):
    if frase_usuario_a_cambiar[inicio] in "aeiou":
        dato = "i"

    else:
        dato = frase_usuario_a_cambiar[inicio]
    frase_usuario_final += dato
    inicio += 1

print(frase_usuario_a_cambiar)
print(frase_usuario_final)
