#Dada una lista mixta de enteros y strings, devolver dos listas, una con todos los enteros y otra con todas las strings##

lista_mixta = ["abc",55,99.9,"def",100,"gato",66,77,5.1,True]
string = ""
lista_tipos = []
lista_strings = []
lista_integer = []
lista_other = []

for dato in lista_mixta:
    if (type(dato)) == str:
        lista_strings.append(dato)
    elif (type(dato)) == int:
        lista_integer.append(dato)
    else: lista_other.append(dato)


print(lista_integer)
print(lista_strings)
print(lista_other)
