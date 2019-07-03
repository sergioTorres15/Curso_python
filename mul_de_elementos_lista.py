lista_numeros = [1,2,3,4,5]
lista =[]

import operator
import functools

resultado = functools.reduce(operator.mul, [1, 2, 3, 4, 5,], 1)

print(resultado)