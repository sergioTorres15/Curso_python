frase_usuario = input("introduce una frase :")


indice = 0

n_mayusculas = 0
n_minusculas = 0

while indice < len(frase_usuario)and frase_usuario != " ":
    letra = frase_usuario[indice]

    if letra.isupper() == True:
        n_mayusculas += 1
        indice += 1
    else:
        n_minusculas += 1
        indice += 1

print("el total de mayusculas en la frase son :{}".format(n_mayusculas))
print("el total de minusculas en la frase son :{}".format(n_minusculas))