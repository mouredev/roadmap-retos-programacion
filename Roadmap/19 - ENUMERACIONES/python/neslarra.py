"""
 EJERCICIO:
 Empleando tu lenguaje, explora la definición del tipo de dato
 que sirva para definir enumeraciones (Enum).
 Crea un Enum que represente los días de la semana del lunes
 al domingo, en ese orden. Con ese enumerado, crea una operación
 que muestre el nombre del día de la semana dependiendo del número entero
 utilizado (del 1 al 7).
 *
 DIFICULTAD EXTRA (opcional):
 Crea un pequeño sistema de gestión del estado de lista_de_pedidos.
 Implementa una clase que defina un pedido con las siguientes características:
 - El pedido tiene un identificador y un estado.
 - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 - Implementa una función para mostrar un texto descriptivo según el estado actual.
 - Crea diferentes lista_de_pedidos y muestra cómo se interactúa con ellos. 
"""
from enum import Enum

print(f"##  Explicación  {'#' * 30}\n")
print(r"""
Enumerar es nombrar cosas en un orden determinado, por ejemplo: nombrar los elementos de una colección, del primero al último, correspondiendole 
a cada elemento los número 1 a n. Ésto se puede hacer de diversas maneras.

Puedo "enumerar" los días de la semana utilizando un diccionario con clave el número de día y valor el nombre del día:
dias_de_senama = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}
print("Qué día de la semana podés ir al cine?")
for key, value in dias_de_senama.items():
    print(f"\t{key} - {value}")
dia = "_"
while not (dia.isnumeric() and int(dia) in range(1, 8)):
    dia = input("Decime cual [1-7] => ")
print(f"Ok, vamos al cine el día {dias_de_senama[int(dia)]}", end="\n\n")

También puedo hacerlo utilizando una lista y la función "enumerate" la cual devolverá el índice correspondiente a cada elemento de la lista
(como, para este caso, la pocisión 0 no será utilizada, inicio la lista con un valor dummy "_":
dias_de_senama = ["_", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Qué día querés ir al cine conmigo?")
for dia_num, dia in enumerate(dias_de_senama):
    print(f"\t{dia_num} - {dias_de_senama[dia_num]}")
dia = "_"
while not (dia.isnumeric() and int(dia) in range(1, 8)):
    dia = input("Decime cual [1-7 o 0 si no querés] => ")
print(f"Ok, vamos al cine el día {dias_de_senama[int(dia)]}", end="\n\n")

O puedo usar el módula Enum del paquete enum, el cual asigna un valor a cada uno de los nombres:
from enum import Enum
dias_de_senama = Enum(value="dias_de_la_semana", names=("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"))
print("Qué día te gusta ir al cine?")
for d in dias_de_senama:
    print(f"\t{d.value} - {d.name}")
dia = "_"
while not (dia.isnumeric() and int(dia) in [x for x in range(1, dias_de_senama.__len__() + 1)]):
    dia = input("Decime cual [1-7] => ")
print(f"Ok, vamos al cine el día {dias_de_senama(int(dia)).name}", end="\n\n")
""")

dias_de_senama = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}
print("Usando diccionario:\nQué día de la semana podés ir al cine?")
for key, value in dias_de_senama.items():
    print(f"\t{key} - {value}")
dia = "_"
while not (dia.isnumeric() and int(dia) in range(1, 8)):
    dia = input("Decime cual [1-7] => ")
print(f"Ok, vamos al cine el día {dias_de_senama[int(dia)]}", end="\n\n")

dias_de_senama = ["_", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Usando lista:\nQué día querés ir al cine conmigo?")
for dia_num, dia in enumerate(dias_de_senama):
    print(f"\t{dia_num} - {dias_de_senama[dia_num]}")
dia = "_"
while not (dia.isnumeric() and int(dia) in range(1, 8)):
    dia = input("Decime cual [1-7 o 0 si no querés] => ")
print(f"Ok, vamos al cine el día {dias_de_senama[int(dia)]}", end="\n\n")

dias_de_senama = Enum(value="dias_de_la_semana", names=("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"))
print("Usando Enum:\nQué día te gusta ir al cine?")
for d in dias_de_senama:
    print(f"\t{d.value} - {d.name}")
dia = "_"
while not (dia.isnumeric() and int(dia) in [x for x in range(1, dias_de_senama.__len__() + 1)]):
    dia = input("Decime cual [1-7] => ")
print(f"Ok, vamos al cine el día {dias_de_senama(int(dia)).name}", end="\n\n")

print(f"##  Dificultad extra  {'#' * 30}\n")


class Pedido:

    pedido_nro = 2384
    numeros_de_pedidos = Enum(value="numeros_de_pedidos", names=[])
    estado = Enum(value="estado", names=("PENDIENTE", "ENVIADO", "ENTREGADO", "CANCELADO"))
    acciones = Enum(value="acciones", names=("Listar", "Nuevo pedido", "Cambiar estado"))

    def __init__(self):
        self.pedido = Pedido.nuevo_pedido()
        self.estado = 1

    def __str__(self):
        return f"Pedido nro {self.pedido} con estado {Pedido.estado(self.estado).name}"

    def cambiar_estado(self, nuevo_estado: str) -> bool:
        estado = getattr(Pedido.estado, nuevo_estado).value
        if estado == self.estado + 1 or estado == 4:
            self.estado = estado
            return True
        return False

    @classmethod
    def nuevo_pedido(cls):
        cls.pedido_nro += 1
        nombres = [p.name for p in cls.numeros_de_pedidos] + [str(cls.pedido_nro)]
        cls.numeros_de_pedidos = Enum(value="numeros_de_pedidos", names=nombres)
        return cls.pedido_nro


def menu_estados() -> str:
    print("\nSeleccionar nuevo estado")
    for e in Pedido.estado:
        print(f"\t{e.value} - {e.name}")
    estado = "_"
    while not (estado.isnumeric() and int(estado) in [x for x in range(1, Pedido.estado.__len__() + 1)]):
        estado = input("Estado => ")
    return Pedido.estado(int(estado)).name


def menu_pedidos() -> int:
    print(f"\nMenu de lista_de_pedidos")
    for a in Pedido.acciones:
        print(f"\t{a.value} - {a.name}")
    print("\t0 - Salir")
    accion = "_"
    while not (accion.isnumeric() and int(accion) in [x for x in range(0, Pedido.acciones.__len__() + 1)]):
        accion = input(f"Seleccionar opcion [0-{Pedido.acciones.__len__()}] => ")
    return int(accion)


def seleccionar_pedido() -> int:
    print(f"\nSeleccionar pedido")
    for p in Pedido.numeros_de_pedidos:
        print(f"\t{p.value} - {p.name}")
    print("\t0 - Volver")
    item = "_"
    while not (item.isnumeric() and int(item) in [x for x in range(0, Pedido.numeros_de_pedidos.__len__() + 1)]):
        item = input(f"Seleccionar item [0-{Pedido.numeros_de_pedidos.__len__()}] => ")
    pedido_nro = Pedido.numeros_de_pedidos(int(item)).name
    return int(Pedido.numeros_de_pedidos(int(item)).name) if int(item) > 0 else 0


lista_de_pedidos = []
while True:
    accion = menu_pedidos()
    match accion:
        case 0:
            break
        case 1:
            for p in Pedido.numeros_de_pedidos:
                pedido = [pe for pe in lista_de_pedidos if pe.pedido == int(p.name)][0]
                print(f"\t{pedido}")
        case 2:
            pedido = Pedido()
            lista_de_pedidos.append(pedido)
            print(f"\tNuevo pedido => {pedido.__str__()}")
        case 3:
            pedido_nro = seleccionar_pedido()
            nuevo_estado = menu_estados()
            pedido = [p for p in lista_de_pedidos if p.pedido == pedido_nro][0]
            pedido.cambiar_estado(nuevo_estado)
            print(pedido)
