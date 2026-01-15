#19 - Python
# 
# EJERCICIO:
# Empleando tu lenguaje, explora la definición del tipo de dato
# que sirva para definir enumeraciones (Enum).
# Crea un Enum que represente los días de la semana del lunes
# al domingo, en ese orden. Con ese enumerado, crea una operación
# que muestre el nombre del día de la semana dependiendo del número entero
# utilizado (del 1 al 7).
# 
# DIFICULTAD EXTRA (opcional):
# Crea un pequeño sistema de gestión del estado de pedidos.
# Implementa una clase que defina un pedido con las siguientes características:
# - El pedido tiene un identificador y un estado.
# - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
# - Implementa las funciones que sirvan para modificar el estado:
#   - Pedido enviado
#   - Pedido cancelado
#   - Pedido entregado
#   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
# - Implementa una función para mostrar un texto descriptivo según el estado actual.
# - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
# /
from random import randint
import datetime
class Counter:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

def serparacion(cadena) -> str:
    global contador
    print(f'\nEjercicio {next(contador)}. {cadena * 20}')

def basic() -> None:
    serparacion("_:_")
    week_days = enumerate(('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'),start=1)
    for contday in range(7):
        print(next(week_days))
    serparacion("_:_")
    search_day = randint(1,7)
    for num_day, day in enumerate(('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'),start=1):
        if search_day == num_day:
            print(f'El día de la semana {search_day} es {day}')

class Pedido:
    
    def __init__(self):
        self.identifier = self.gen_cod_ped()
        # El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
        self.states = ('PENDIENTE', 'ENVIADO', 'ENTREGADO', 'TERMINADO', 'CANCELADO', 'FINALIZADO')
        self.change_order = enumerate(self.states,start=1)
        self.state = next(self.change_order)

    def __str__(self):
        return f'El pedido "{self.identifier}" se encuentra "{self.state}"'
    
    def __repr__(self):
        return f'Pedido({self.identifier}, {self.state})'
    
    def gen_cod_ped(self) -> str:
        tnw = datetime.datetime.now()
        code=f'{tnw.strftime("%Y")}{tnw.strftime("%V")}{tnw.strftime("%m")}{tnw.strftime("%d")}{tnw.strftime("%j"):03}{tnw.strftime("%w")}{tnw.strftime("%H")}{tnw.strftime("%M")}{tnw.strftime("%S")}{tnw.strftime("%f")}'
        return code
    
    def change_state(self):
        try:
            self.state = next(self.change_order)
        except StopIteration:
            print('Ya está en el estado final, no se puede cambiar el estado.')

    def force_state(self, state: str) -> bool:
        if state not in self.states:
            print(f'El valor introducido "{state}" no es correcto.\nSolo se aceptan "{self.states}"')
            return False
        for ind, expre in enumerate(self.states,start=1):
            if expre == state:
                if (ind - 1) in self.state:
                    self.state = next(self.change_order)
                    print(self)
                    return True
                elif state == 'CANCELADO':
                    while 'CANCELADO' not in self.state:
                        self.state = next(self.change_order)
                    print(self)
                    return True
                else:
                    print(f'No se permite pasar de {self.state} a {state}')
                    return False
    def print_item(self):
        print(self)

def extra() -> None:
    
    serparacion("_:_")
    pedidos=[]

    def search_ped(option) -> None:
        ped_id = input('\nIntroduzca el número de pedido.\nPedido: ')
        for pedido in pedidos:
            if pedido.identifier == ped_id:
                if option == "3":
                    pedido.change_state()
                elif option == "4":
                    ped_state = (input('Introduzca el nuevo estado del pedido.\nEstado: ')).upper()
                    if pedido.force_state(ped_state): print('Operación exitosa.')
                else:
                    print('El pedido no existe.')
    
    while True:
        print("\nSelecciona una de las siguientes opciones:")
        print('1) Para añadir un pedido.')
        print('2) Para listar los pedidos.')
        print('3) Para modificar estado de un pedido.')
        print('4) Para forzar el estado de un pedido.')
        print('0) Para Salir.')
        option = input('Opcion: ')
        match option:
            case "0":
                print("Programa finlizado.")
                break
            case "1":
                pedidos.append(Pedido())
            case "2":
                for pedido in pedidos:
                    pedido.print_item()
            case "3":
                search_ped(option)
            case "4":
                search_ped(option)
            case _:
                print('Seleccione una opción correcta.')

def main() -> None:
    basic()
    extra()

contador = iter(Counter())

if __name__ == "__main__":
    main()
