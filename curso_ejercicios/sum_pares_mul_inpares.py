
#elabora un programa que sume los numeros pares y multiplique los impares

numbers_list = []
numbers_input = ""
pares = []
inpares = []
while len(numbers_list) < 10:
    numbers_input = input("dime un numero : ")
    numbers_list.append(numbers_input)
print("\nnumeros usuario = {}".format(numbers_list))

for num in numbers_list:
    if int(num) % 2 == 0:
        pares.append(num)
    else:
        inpares.append(num)

print("Numeros pares = {}".format(pares))
print("Numeros impares = {}".format(inpares))

la_suma = 0
for i in pares:
    la_suma = la_suma + int(i)

print("\nla suma de los pares es : {}".format(la_suma))

mul = 1
for dato in inpares:
    mul = int(dato) * mul
print("La multiplicacion de los inpares es : {}".format(mul))
