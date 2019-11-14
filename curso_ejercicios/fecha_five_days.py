import  datetime


fecha_ahora = datetime.datetime.now()
cinco = fecha_ahora - datetime.timedelta(days=5)

print("la fecha de hace 5 dias fue el  {}".format(cinco.strftime("%d del %m del año %Y en el dia %A")))