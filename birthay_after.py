import datetime


print("******************************")
print("dime la fecha de tu cumpleaños")
print("******************************")

dia = int(input("dime el dia : "))
mes = int(input("dime el mes : "))
year = int(input("dime el año : "))

user_day_birthday = datetime.datetime(day=dia, month=mes, year=year)

hoy = datetime.datetime.now()

tiempo_restante = user_day_birthday - hoy

print("faltan {} dias y {} horas para tu cumpelaños =D".format(tiempo_restante.days,int(tiempo_restante.seconds / 3600)))
print("y el dia de tu cumpleaños es el dia : {}".format(user_day_birthday.strftime("%A")))