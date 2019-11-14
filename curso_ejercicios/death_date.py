import datetime

AVERAGE_LIFESPAN = 80
SMOOKER_PENALIZATION = 10
DRINKER_PENALIZATION = 10
SEDENTARY_PENALIZATION = 20

def print_with_underscores(message):
   print(message)
   print(len(message) * "-")

def ask_yes_or_not(message):
   response = None
   while response != "si" and response != "no":
      response = input(message + " [si / no] : ")
   return response == "si"

print_with_underscores("Averigua cuanto te queda de vida ")
print("Completa esta encuesta para saber cuanto te queda de vida ")

birth_date = input("Cual es tu fecha de nacimiento FORMATO : dd/mm/yyyy :")
birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")


years_lost = 0


if ask_yes_or_not("FUMAS?"):
   years_lost += SMOOKER_PENALIZATION

if ask_yes_or_not("BEBES?"):
   years_lost += DRINKER_PENALIZATION

if not ask_yes_or_not("HACES DEPORTE?"):
   years_lost += SEDENTARY_PENALIZATION

lifespan =  AVERAGE_LIFESPAN - years_lost

death_day = birth_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()

print("fecha de muerte {}, te  quedan {} dias  ".format(death_day.strftime("%d/%m/%Y"), days_to_death.days))
