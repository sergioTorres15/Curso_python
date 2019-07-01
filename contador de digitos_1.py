numeros_usuarios = []
numero_de_usuario = ""


while len(numeros_usuarios) < 10:
    while not numero_de_usuario.isdigit():
        numero_de_usuario = input("Dime un numero: ")
    numeros_usuarios.append(int(numero_de_usuario))
    numero_de_usuario = ""
    print("!numero añadido¡")
print("el total de digitos de tu arreglo son :{}".format(len(numeros_usuarios)))