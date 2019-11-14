pokemon_elegido = input("contra que pokemons quieres luchar? (squirtle / charmander / balbasuer) : ")

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0


if pokemon_elegido == "squirtle":
    vida_enemigo = 90
    nombre_pokemon = "squirtle"
    ataque_pokemon = 8

elif pokemon_elegido == "charmander":
    vida_enemigo = 80
    nombre_pokemon = "charmander"
    ataque_pokemon = 7

elif pokemon_elegido == "balbasuer":
    vida_enemigo = 100
    nombre_pokemon = "balbasuer"
    ataque_pokemon = 10




while vida_pikachu > 0 and vida_enemigo > 0:

    ataque_elegido = input("que ataque vas usar? ( chispazo / bolavoltio)")
    if ataque_elegido == "chispazo":
        vida_enemigo -= 10
    elif ataque_elegido == "bolavoltio":
        vida_enemigo -= 12

    print("la vida de {} ahora es :{} ".format(nombre_pokemon ,vida_enemigo))



    print("{}te hace daño de {} puntos".format(nombre_pokemon , ataque_pokemon))
    vida_pikachu -= ataque_pokemon


    print("la vida de pikachu es ahora : {}".format(vida_pikachu))

    if vida_enemigo <0:
        print ("pikachu ha ganado")

    if vida_pikachu <0:
        print("has perdido")

print("el combate termino")


