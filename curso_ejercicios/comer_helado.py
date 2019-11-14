
apetece_helado_input = input("te apetece un helado (si / no):")
tiene_diner_input = input("tienes dinero para un helado (si / no):")
esta_el_senor_helados_input = input("esta el señor de los helados (si / no):")
esta_su_tia = input("estas cob tu tia")


apetece_helado = apetece_helado_input == "si"
puede_permitirselo = tiene_diner_input == "si" or esta_su_tia == "si"
esta_el_senor_helados = esta_el_senor_helados_input == "si"
if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print("pues comprate un helado")

else:
    print("pues nada")
