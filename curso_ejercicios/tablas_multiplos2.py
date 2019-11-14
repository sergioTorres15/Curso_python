numero_tabla = int(input("de que num. quieres la tabla de multiplicar? :"))

multiplo = 2

for multiplo in range(1,11):
    if multiplo %2 == 0:
        print("{}x{}={}".format(numero_tabla,multiplo,numero_tabla*multiplo))

