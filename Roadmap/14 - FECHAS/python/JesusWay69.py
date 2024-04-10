import os
os.system('cls')
from datetime import datetime as DT
from datetime import date as D
from datetime import timedelta as TD
from datetime import timezone as TZ




""" * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)"""


week_days = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
months =["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
current_datetime = DT.now()#Con .now sobre datetime generamos un objeto datetime con la fecha y hora actual del sistema
utc_spain_timezone = TZ(TD(hours=+2))# Con el módulo timezone podemos definir una zona horaria uct concreta
sillicon_valley_time = current_datetime.astimezone(TZ(TD(hours=-7)))#Con .astimezone le pasamos el objeto timezone con la diferencia horaria definida
                                                                    # en un timedelta 
current_date = D.today()#Con .today sobre date generamos un objeto date con la fecha actual del sistema (similar a .now sobre datetime)
format_current_date = D.today().strftime('%A, %d-%B-%Y')#Con .strftime sobre date generamos un string formateado "a la carta"
format_manual_time = DT.strptime('20-05-1998 22:15:30', '%d-%m-%Y %H:%M:%S')#Con .strptime generamos un objeto datetime a partir de un string
format_manual_time2 = 'Formateo desde datetime: {}/{}/{}'.format(DT.now().day,DT.now().month,DT.now().year)
format_manual_time3 = 'Formateo desde date: {}/{}/{}'.format(D.today().day,D.today().month,D.today().year)
#Con .format a partir de una combinación de objetos datetime o date generamos la fecha, hora o ambas en string
week_day = week_days[format_manual_time.weekday()] #Con .weekday nos devuelve un número que corresponde al día de la semana donde 1 es el lunes..
current_week_day = week_days[current_date.weekday()]# Aplicando ese número como índice de una lista con los días podemos generar el día en texto

current_year = current_date.year #Cada objeto date nos permite acceder indivudualmente a cada componente de la fecha
current_month = months[current_date.month-1]# Como cada componente lo devuelve en un int podemos usarlo como índice de una lista
current_day = current_date.day
current_hour = current_datetime.hour# Con los objetos datetime tambien podemos acceder a cada componente de fecha y hora
current_minute = current_datetime.minute
current_second = current_datetime.second
my_age = current_datetime - format_manual_time#Podemos operar con 2 objetos datetime que nos devuelve la operación en un objeto timedelta
my_age_years = int(my_age.days//365.25)# El timedelta nos devuelve un objeto con el total del intervalo temporal en días, horas,minutos y segundos con decimales
#Los objetos timedelta tambien proveen de métodos para separar solo los días (.days) o la franja sobrante de tiempo en segundos (.seconds)


print("Fecha y hora en España:",current_datetime,"\n",
    "Fecha y hora en Sillicon Valley (USA):", sillicon_valley_time,"\n",
        current_hour, ":",
        current_minute, ":",
        current_second, "\n",
        format_current_date, "\n",
        format_manual_time, week_day, "\n",
        format_manual_time2 , "\n",
        format_manual_time3 , "\n",
        my_age_years, "años\n",
        "Objeto timedelta completo: ",my_age, '\n',
        my_age.days, "días\n",
        
        "Zona horaria España:", utc_spain_timezone , "\n",        
        "\n\n\n"
        )
os.system('pause')


def input_data()->D:
    while True:
        year = input("Escriba su año de nacimiento: ")
        if not year.isdigit or len(year)!=4:
            print ("ERROR: El año debe ser numérico de 4 cifras")
            continue
        elif int(year)<1900:
            print ("Aunque seas demasiado viejo no creo que hayas nacido antes de 1900, intenta otro año posterior")
            continue
        elif int(year)>=D.today().year -3 and int(year)<= D.today().year:
            print("Te has debido equivocar de año porque un bebé no sabe teclear en un ordenador, intenta de nuevo")
            continue
        elif int(year)>D.today().year:
            print("A no ser que vengas del futuro no puedes poner un año que aun no ha llegado, intenta de nuevo")
            continue
        while True:
            month = input("Escriba el mes de nacimiento: ")
            if  not month.isdigit or len(month)>2 or len(month)<=0:
                print ("ERROR: El mes debe ser numérico de 1 o 2 cifras")
                continue
            elif int(month)<1 or int(month)>12:
                print ("ERROR: El mes no debe ser menor a 0 ni mayor a 12")
                continue
            while True:
                day = input("Escriba el día de nacimiento: ")
                if not day.isdigit or len(day)>2 or len(day)<=0:
                   print ("ERROR: El día debe ser numérico de 1 o 2 cifras")
                   continue
                elif int(month)==4 or int(month)==6 or int(month)==9 or int(month)==11 and int(day)>30:
                    print (f"El mes de {months[int(month)-1]} no puede tener más de 30 días") 
                    continue
                elif int(day)<1 or int(day)>31:
                   print ("ERROR: El día no debe ser menor a 0 ni mayor a 31")
                   continue
                if ((int(year) % 4 != 0) and ((int(year) % 100 == 0) or (int(year) % 400 != 0)) and int(month)==2 and int(day)>28):
                    print (f"El año {year} no fue bisiesto y febrero no puede tener más de 28 días")
                    break
                return D(int(year),int(month),int(day))
  

def show_data(date_object:D):
    str_date = str(f"{date_object.day}-{date_object.month}-{date_object.year}")
    format_date = DT.strptime(str_date, '%d-%m-%Y')
    my_age = DT.now() - format_date
    my_age_years = int(my_age.days//365.25)
    beginning_year = D(D.today().year,1,1)
    days_passed = D.today() - beginning_year
    weeks_passed = days_passed.days//7+1

    print(f"\nHoy es {current_week_day} día {DT.now().day} de {current_month} de {DT.now().year}")
    print(f"Y son las {DT.now().hour} horas y {DT.now().minute} minutos\n")
    print(f"Estamos en la semana {weeks_passed} y en el día {days_passed.days+1} de {D.today().year}\n")
    if DT.now().hour>=6 and DT.now().hour<12:
      print("¡¡Buenos días!!\n")
    elif DT.now().hour>=12 and DT.now().hour<=20:
        print("¡¡Buenas tardes!!\n")
    else:
        print("¡¡Buenas noches!!\n")

    print(f"Como has indicado que naciste el día {date_object.day} de {months[date_object.month-1]} de {date_object.year} ...\n")
    print("... (por cierto naciste un", week_days[format_date.weekday()],")\n")
    if DT.now().day == date_object.day and DT.now().month == date_object.month:
            print(f"¡¡¡FELICIDADES!!! hoy cumples {my_age_years} años, casi nada\n")
    else:
            print(f"...tienes {my_age_years} años")

show_data(input_data())
