"""
/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
 */
"""
from enum import Enum


class DiasDeLaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

    def mostrar_dia_semana(num):
        if num == 1:
            return DiasDeLaSemana.LUNES.name
        elif num == 2:
            return DiasDeLaSemana.MARTES.name
        elif num == 3:
            return DiasDeLaSemana.MIERCOLES.name
        elif num == 4:
            return DiasDeLaSemana.JUEVES.name
        elif num == 5:
            return DiasDeLaSemana.VIERNES.name
        elif num == 6:
            return DiasDeLaSemana.SABADO.name
        elif num == 7:
            return DiasDeLaSemana.DOMINGO.name
        else:
            print("Error, elige el numero del dia de la semana, del 1 al 7")


dias = DiasDeLaSemana.mostrar_dia_semana(3)
print(dias)
