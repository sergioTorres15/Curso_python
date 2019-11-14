import datetime

year = int(input("dime el año : "))
month = int(input("dime el mes :"))
day = int(input("dime el dia :"))

user_date = datetime.datetime(year=year, month=month, day=day)

time_remaining = user_date - datetime.datetime.now()

print("faltan {} dias y {} horas".format(time_remaining.days, int(time_remaining.seconds / 3600 )))