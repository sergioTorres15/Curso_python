print("hola bienvenido al contar de frases")

frase_usuario = input("introduze una frase :")

n_espacios = frase_usuario.count(" ")
n_puntos = frase_usuario.count(".")
n_comas = frase_usuario.count(",")


print("num. espacios en la frase : {}".format(n_espacios))
print("num. de puntos en la frase : {}".format(n_puntos))
print("num. de comas en la frase : {}".format(n_comas))