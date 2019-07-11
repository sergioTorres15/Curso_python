def subrayar_texto(texto):
    rayado = "-"
    while len(rayado) < len(texto):
            rayado += "-"
    print(texto)
    print(rayado)



subrayado_palabra = subrayar_texto("hola perro")