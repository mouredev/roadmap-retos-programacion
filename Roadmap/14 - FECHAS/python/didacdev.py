from datetime import datetime, date

date = datetime.now()
birth = datetime(1996, 3, 10, 20, 0)

years = int((date - birth).total_seconds() // (365.25*24*60*60))
print(f"{years} años")

print(f"{birth.day}-{birth.month}-{birth.year}")
print(f"{birth.hour}h {birth.minute}min {birth.second}s")

week_day = birth.weekday()

match week_day:
    case 0:
        print("Lunes")
    case 1:
        print("Martes")
    case 2:
        print("Miércoles")
    case 3:
        print("Jueves")
    case 4:
        print("Viernes")
    case 5:
        print("Sábado")
    case 6:
        print("Domingo")

month = birth.month

match month:
    case 1:
        print("Enero")
    case 2:
        print("Febrero")
    case 3:
        print("Marzo")
    case 4:
        print("Abril")
    case 5:
        print("Mayo")
    case 6:
        print("Junio")
    case 7:
        print("Julio")
    case 8:
        print("Agosto")
    case 9:
        print("Septiembre")
    case 10:
        print("Octubre")
    case 11:
        print("Noviembre")
    case 12:
        print("Diciembre")
