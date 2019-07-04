frase_usuario = input("introduce una frase")
valor_a_sustituir = ["VACA"]


for dato in valor_a_sustituir:
    frase_usuario = frase_usuario.replace("a",dato,1)
print(frase_usuario)
