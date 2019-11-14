numeros_usuarios = []
numero_de_usuario = ""


while len(numeros_usuarios) < 10:
    while not numero_de_usuario.isdigit():
        numero_de_usuario = input("Dime un numero: ")
    numeros_usuarios.append(int(numero_de_usuario))
    numero_de_usuario = ""
    print("!numero añadido¡")
print(numeros_usuarios)

numero_menor = numeros_usuarios[0]
for numero in numeros_usuarios:
    if numero <  numero_menor:
        numero_menor = numero

print("El numero mas menor es {}".format(numero_menor))