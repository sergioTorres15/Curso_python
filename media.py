numeros_usuarios = []
numero_de_usuario = ""


while len(numeros_usuarios) < 10:
    while not numero_de_usuario.isdigit():
        numero_de_usuario = input("Dime un numero: ")
    numeros_usuarios.append(int(numero_de_usuario))
    numero_de_usuario = ""
    print("!numero añadido¡")
print(numeros_usuarios)



total = sum(numeros_usuarios)

n_dividir = len(numeros_usuarios)

media = total/n_dividir

print("la media es : {}".format(media))
