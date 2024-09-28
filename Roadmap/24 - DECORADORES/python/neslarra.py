"""
 EJERCICIO:
 Explora el concepto de "decorador" y muestra cómo crearlo
 con un ejemplo genérico.
 DIFICULTAD EXTRA (opcional):
 Crea un decorador que sea capaz de contabilizar cuántas veces
 se ha llamado a una función y aplícalo a una función de tu elección.
"""

print(f"{'#' * 47}")
print(f"##  Explicación  {'#' * 30}")
print(f"{'#' * 47}")

print(r"""
Los decoradores son funciones que modifican el comportamiento de otras funciones. Pueden ser los que entrega Python por default (por ejemplo
staticmethod y classmethod) o funciones creadas para determinada función.

Por ejemplo, creo una clase Turno para entregar turnos de una tienda con varios sectores. La clase Turno tendrá tres métodos decorados:
  1- hora_de_emision decorado con  "staticmethod" indicando que es de clase PERO no recive ni entrega argumentos de la clase.
  2- localiza_sector decorado con "classmethod" indicanco que es de clase y entregando el contenido de una variable de la clase.
  3- entrega_de_turno decorado con "classmethod" indicando que es de clase y modificando y entregando una variable de clase.

Luego tenemos el decorador "asesor" el cual se encarga de ejecutar comandos pre y post callback de la función decorada (va a dar instrucciones
de localización, va a llamar a la función que muestra el turno y luego va a hacer un saludo final).

Los decoradores se invocan con un "@"<nombre_de_la_función_decoradora> justo antes de definir la función decorada.

    def mi_decorador(callback_func):
        def wrapper(*args, **kwargs)
            <ejecuto PRE operaciones>
            callback_func(*args, **kwargs)
            <ejecuto POST operaciones>
        return wrapper

    @mi_decorador
    def funcion_decorada():
        ...

Ejemplo:

from time import sleep


class Turno:
    turno: int = 1000
    ubicacion = {"Farmacia": "por pasillo central al fondo",
                 "Perfumería": "por escalera primer piso",
                 "Gabinete": "por pasillo de la derecha"}

    def __init__(self, sector):
        self.sector = sector
        self.hora = self.hora_de_emision()
        self.turno = Turno.entrega_turno()

    @staticmethod
    def hora_de_emision():
        from datetime import datetime
        return datetime.now().strftime('%H:%M:%S')

    @classmethod
    def localiza_sector(cls, sector):
        return cls.ubicacion[sector]

    @classmethod
    def entrega_turno(cls):
        cls.turno += 1
        return cls.turno


def asesor(funcion_decorada):
    def wrapper(*args, **kwargs):
        # *args, **kwargs son los argumentos de la función decorada "ver_turno: args[0] = nombre y args[1] L instancia del objeto Turno"
        print(f"{args[0]} dirijase {args[1].localiza_sector(args[1].sector)}")
        funcion_decorada(*args, **kwargs)
        print("Gracias por su visita.\n")

    return wrapper


@asesor
def ver_turno(nombre, turno):
    print(f"Tiene el turno {turno.turno} de la hora {turno.hora} para {turno.sector}")


nestor = Turno("Farmacia")
sleep(1)
neslarra = Turno("Farmacia")
sleep(1)
nesla = Turno("Perfumería")
sleep(1)
otro_nestor = Turno("Gabinete")

ver_turno("Néstor", nestor)
ver_turno("Neslarra", neslarra)
ver_turno("Nesla", nesla)
ver_turno("Otro Néstor", otro_nestor)

Ésto devuelve:

Néstor dirijase por pasillo central al fondo                # decorador PRE operación
Tiene el turno 1001 de la hora 18:28:14 para Farmacia       # función decorada
Gracias por su visita.                                      # decorador POST operación

Neslarra dirijase por pasillo central al fondo              # decorador PRE operación
Tiene el turno 1002 de la hora 18:28:15 para Farmacia       # función decorada
Gracias por su visita.                                      # decorador POST operación

Nesla dirijase por escalera primer piso                     # decorador PRE operación
Tiene el turno 1003 de la hora 18:28:16 para Perfumería     # función decorada
Gracias por su visita.                                      # decorador POST operación

Otro Néstor dirijase por pasillo de la derecha              # decorador PRE operación
Tiene el turno 1004 de la hora 18:28:17 para Gabinete       # función decorada
Gracias por su visita.                                      # decorador POST operación
""")

print(f"{'#' * 52}")
print(f"##  Dificultad Extra  {'#' * 30}")
print(f"{'#' * 52}\n")

def contador_de_ejecuciones(funcion):
    ejecuciones = {}
    def wrapper(*args, **kwargs):
        ejecuciones[funcion.__name__] = ejecuciones[funcion.__name__] if funcion.__name__ in ejecuciones.keys() else 0
        print(f"Ejecutando {funcion.__name__}", end="\n\t")
        funcion(*args)
        ejecuciones[funcion.__name__] += 1
        print(f"{funcion.__name__} se ha ejecutado {ejecuciones[funcion.__name__]} veces.\n")
    return wrapper


@contador_de_ejecuciones
def saludo_espaniol(nombre):
    print(f"{nombre} Hola Mundo")


@contador_de_ejecuciones
def saludo_ingles(nombre):

    print(f"{nombre} Hello World")
@contador_de_ejecuciones
def saludo_frances(nombre):
    print(f"{nombre} Alo Monde")

@contador_de_ejecuciones
def saludo_italiano(nombre):
    print(f"{nombre} Ciao Mondo")


saludo_ingles("Pete")
saludo_italiano("Peppo")
saludo_ingles("Joe")
saludo_ingles("Jhonny")
saludo_espaniol("Tonio")
saludo_espaniol("Pepe")
saludo_italiano("Gianni")
saludo_frances("Peppete")
saludo_frances("Jean")
saludo_italiano("Carletto")
