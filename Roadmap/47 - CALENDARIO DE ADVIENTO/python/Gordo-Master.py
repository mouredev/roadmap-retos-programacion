# 47 - Calendario de Adviento
class EventCalendar:
    def __init__(self):
        self.gifs = [f"{x:02}" for x in range(1,25)]

    def show_calendar(self):
        for y in range(0,24,6):
            print("**** "*6)
            for x in range(6):
                print("*"+self.gifs[x+y]+"* ", end="")
            print()
            print("**** "*6)
            print()
            
    def select_day(self):
        day = input("Ingrese el día a describrir (o escribe 'salir' para finalizar): ")
        if day.lower() == 'salir':
            print("Saliendo del calendario de adviento...")
            return 
        if not day.isdigit() or int(day)<=0  or int(day) > 24:
            print("Valor invalido, debe ser un numero entero entre 1 y 24!")
            return True
        try:
            day = f"{int(day):02}"
            self.gifs[self.gifs.index(day)] = "**"
        except ValueError:
            print("Ya se ha abierto ese día!")
            return True
        input(f"Se ha abierto el día {day}!")
        return True
    
    def verify_list_exist_int(self):
        for day in self.gifs:
            if day.isdigit():
                return True
        return False

    def run_adviento(self):
        while True:    
            self.show_calendar()
            ok = self.select_day()
            if not ok:
                    break
            if not self.verify_list_exist_int():
                break

adviento = EventCalendar()
adviento.run_adviento()