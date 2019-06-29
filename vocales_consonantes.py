
frase_del_usuario = input("introduze una frase :")

vocales = ["a","e","i","o","u"]

n_vocales = 0
n_consonantes = 0

for letra in frase_del_usuario:
    if letra in vocales:
        n_vocales += 1
    else:
        n_consonantes += 1

print("el num. de vocales son :{}".format(n_vocales))
print("el num. de consonantes son : {}".format(n_consonantes))
