from datetime import datetime
import locale


def main():
    now = datetime.now()
    birth = datetime(1977, 6, 11, 9, 0)
    delta_years = now.year - birth.year

    if (now.month, now.day) < (birth.month, birth.day):
        delta_years -= 1

    print(f"Mi edad es {delta_years} años")


def extra():
    """
    Fun fact: en mi actual trabajo tenemos un cliente cuyos emails (presuntamente generados automáticamente),
    parseamos automáticamente. Estos emails contienen fechas que queremos extraer. No exagero si en los últimos
    100 emails, han usado mínimo 25 formatos DIFERENTES de fechas. Ni queriendo soy yo capaz de inventarme
    tantos formatos diferentes. Este ejercicio me trae flashes de Vietnam :)
    """
    locale.setlocale(locale.LC_ALL, "es_ES.utf8")
    birth = datetime(1977, 6, 11, 21, 0)
    print(f"Nací el {birth.strftime('%Y/%m/%d')}")
    print(f"Nací el {birth.isoformat()}")
    print(f"Nací el {birth.strftime('%d de %B de %Y')}")
    print(f"Nací el {birth.strftime('%Y-%b-%d')}")
    print(f"Nací un {birth.strftime('%A %d de %B')}")
    print(f"Nací a las {birth.strftime('%H:%M')}")
    ampm = "PM" if birth.hour > 12 else "AM"  # por alguna razón la directiva %p no me hace esto
    print(f"Nací a las {birth.strftime(f'%I:%M:%S {ampm}')}")
    print(f"Nací a los {birth.minute} minutos tras las {birth.hour}h")
    print(f"Nací el {birth.strftime('%m/%d/%y')} (ahora adivina cuál es més y cuál es día)")
    print(f"Nací un {birth.strftime('%A')} de {birth.year}, el mes de {birth.strftime('%B')}")


if __name__ == "__main__":
    main()
    extra()
