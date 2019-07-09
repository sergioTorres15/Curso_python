
def input_con_confirmacion(pregunta):
    confirmacion = False
    dato_usuario = ""
    nombre = ""
    while not confirmacion:
        dato_usuario = input(pregunta)
        seguro = input("has dicho {}, estas seguro? (si / no) :".format(nombre))
        if seguro == "si":
            confirmacion = True
    return dato_usuario


nombre = input_con_confirmacion("como te llamas? : ")
print("has confirmado que te llamas {}".format(nombre))

numero = input_con_confirmacion("dime un numero : ")
print("has confirmado que el numero  es {}".format(numero))