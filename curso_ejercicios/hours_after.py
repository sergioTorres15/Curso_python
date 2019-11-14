import datetime

day = int(input("dime un dia : "))
month = int(input("dime un mes : "))
year = int(input("dime un año : "))

fecha_user = datetime.datetime(day=day, month=month, year=year)
now = datetime.datetime.now()


time_remainig = now - fecha_user

print("han pasado {} horas desde la fecha {}".format(int(time_remainig.days * 24) + int(time_remainig.seconds / 3600) ,fecha_user.strftime("%d del %m del %Y")))