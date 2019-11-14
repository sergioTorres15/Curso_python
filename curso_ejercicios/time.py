from curso_ejercicios.time import sleep
import datetime

NIGHT_START = 19
DAY_START = 8
HOUR_DURATION = 1


def main():
    current_time = datetime.datetime.now()
    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        is_night = False


        if current_time.hour > NIGHT_START or current_time.hour <= DAY_START and not is_night:
            is_night = True
        elif current_time.hour > DAY_START and current_time.hour < NIGHT_START and is_night :
            is_night = False
        with open("horas.txt", "a") as hours_file:
            time_text = "La hora actual es {} y es de {}\n".format(current_time, today)
            hours_file.write(time_text)
            print(time_text)


if __name__ == "__main__":
    main()

