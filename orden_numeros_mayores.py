
print("Ordenamiento en Mayor de numeros\n\n")
def ask(number):
    while not (number.isdigit() and int(number.isdigit())):
        number = input("dime un NUMERO NO una LETRA : ")
    return int(number)




num1 = ask(input("dime un numero : "))
num2 = ask(input("Dime otro numero : "))
num3 = ask(input("Dime el tercer numero : "))




print("Tus numeros ingresados son {},{},{}".format(num1,num2,num3))
lista_numbers = []

if num1 < num2:
    lista_numbers.append(num1)
    if num2 < num3:
        lista_numbers.append(num2)
        lista_numbers.append(num3)
        print("el orden de los numeros es ",format(lista_numbers))
    else:
        lista_numbers.append(num3)
        lista_numbers.append(num2)
        print("el orden de los numeros es ", format(lista_numbers))

elif num2 < num1 and num2 < num3:
    lista_numbers.append(num2)
    if num3 < num1:
        lista_numbers.append(num3)
        lista_numbers.append(num1)
        print("el orden de los numeros es ", format(lista_numbers))
    else:
        lista_numbers.append(num1)
        lista_numbers.append(num3)
        print("el orden de los numeros es ", format(lista_numbers))
elif num3 < num1 and num3 < num2:
    lista_numbers.append(num3)
    if num2 < num1:
        lista_numbers.append(num2)
        lista_numbers.append(num1)
        print("el orden de los numeros es ", format(lista_numbers))
    else:
        lista_numbers.append(num1)
        lista_numbers.append(num2)
        print("El orden de los numeros es {}".format(lista_numbers))
else:
    lista_numbers.append(num1)
    lista_numbers.append(num3)
    print("El orden de los numeros es {}".format(lista_numbers))