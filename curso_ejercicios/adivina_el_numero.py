print("hola bienvenido")



numero_a_adivinar = input("¿que num. quieres que adivine tu amigo?")
print("ok...")
print("turno de amigo 2")
print("hola que tal amigo 2 ")
numero_probable = input("¿que num. crees que sea el que puso tu amigo?")


while numero_probable != numero_a_adivinar:
        print("lo siento fallaste")
        numero_probable =input("va de nuez ¿que num. crees que sea el que puso tu amigo?")


print("correcto lo adivinaste")
