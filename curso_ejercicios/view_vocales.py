frase_usuario =input("introduce una frase :")

vocales = ["a","e","i","o","u"]

for letra in frase_usuario:
    if letra in vocales:
        print("vocal {}".format(letra))


