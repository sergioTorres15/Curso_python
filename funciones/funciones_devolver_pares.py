def devolver_solo_pares():
    lista = []
    for numero in range(5):
        valor = int(input("ingrese un numero :"))
        lista.append(valor)
    return lista
def pares_comparacion(lista):
    pares_num = []
    for numero in lista:
        if numero % 2 == 0:
            pares_num.append(numero)
    return pares_num

lista = devolver_solo_pares()
fin = pares_comparacion(lista)

print("los numeros pares son {}".format(fin))