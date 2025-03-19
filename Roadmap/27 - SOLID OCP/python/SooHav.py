# 27 SOLID: PRINCIPIO ABIERTO-CERRADO (OCP)
from abc import ABC, abstractmethod
import logging

# Ejercicio
# Ejemplo Pato sin SRP


class Pato():

    def __init__(self, nombre):
        self.nombre = nombre

    def vuela(self):
        print(f"{self.nombre} vuela.")

    def nada(self):
        print(f"{self.nombre} nada.")

    def dice(self) -> str:
        return "Quack"

    def saluda(self, pato2):
        print(f"{self.nombre}: {self.dice()}, hola {pato2.nombre}")


# Uso
print("Sin SRP")
pato1 = Pato(nombre="Daisy")
pato2 = Pato(nombre="Donald")
pato1.vuela()
pato1.nada()
pato1.saluda(pato2)
print("\n")

# Ejemplo Pato con SRP


class Pato():
    """Clase que define los patos"""

    def __init__(self, nombre):
        self.nombre = nombre

    def vuela(self):
        print(f"{self.nombre} vuela.")

    def nada(self):
        print(f"{self.nombre} nada.")

    def dice(self) -> str:
        return "Quack"


class Dialogo():
    """Clase que define la comunicacion entre patos"""

    def __init__(self, formato):
        self.formato = formato

    def conversacion(self, pato1: Pato, pato2: Pato):
        frase1 = f"{pato1.nombre}: {pato1.dice()}, ¡Ay, {
            pato2.nombre}! ¡Casi me caigo al intentar atrapar un pez!"
        frase2 = f"{pato2.nombre}: {pato2.dice()}, ¡Otra vez, {
            pato1.nombre}? Ten más cuidado la próxima vez."
        conversacion = [frase1, frase2]
        print(*conversacion,
              f"(Extracto de {self.formato})",
              sep='\n')


# Uso
print("Con SRP")
pato1 = Pato(nombre="Donald")
pato2 = Pato(nombre="Daisy")
pato1.vuela()
pato2.nada()
formato1 = Dialogo(formato="historieta")
formato1.conversacion(pato1, pato2)

# Ejemplo Pato con SRP y OCP


class Pato():
    """Clase que define los patos"""

    def __init__(self, nombre, color, edad):
        self.nombre = nombre
        self.color = color
        self.edad = edad

    def vuela(self) -> str:
        print(f"{self.nombre} vuela.")

    def nada(self) -> str:
        print(f"{self.nombre} nada.")

    def dice(self) -> str:
        return "Quack"

    def describe(self) -> str:
        print(f"{self.nombre} es un pato de color {
              self.color} de {self.edad} años.")


class Dialogo(ABC):
    """Clase base abstracta que define la comunicación entre patos"""
    @abstractmethod
    def conversacion(self, pato1: Pato, pato2: Pato, mensaje1: str, mensaje2: str):
        pass


class DialogoHistorieta(Dialogo):
    """Clase para el diálogo en formato historieta"""

    def conversacion(self, pato1: Pato, pato2: Pato, mensaje1: str, mensaje2: str):
        frase1 = f"{pato1.nombre}: {pato1.dice()}, {mensaje1}"
        frase2 = f"{pato2.nombre}: {pato2.dice()}, {mensaje2}"
        conversacion = [frase1, frase2]
        print(*conversacion,
              f"(Extracto de historieta)",
              sep='\n')


class DialogoFormal(Dialogo):
    """Clase para el diálogo en un formato más formal"""

    def conversacion(self, pato1: Pato, pato2: Pato, mensaje1: str, mensaje2: str):
        frase1 = f"{pato1.nombre}: Buen día, {pato2.nombre}. {mensaje1}"
        frase2 = f"{pato2.nombre}: Estoy bien, {pato1.nombre}. {mensaje2}"
        conversacion = [frase1, frase2]
        print(*conversacion,
              f"(Extracto de diálogo formal)",
              sep='\n')


# Uso
print("Con SRP y OCP")
pato1 = Pato(nombre="Donald", color="blanco", edad=5)
pato2 = Pato(nombre="Daisy", color="amarillo", edad=4)
pato1.vuela()
pato2.nada()
pato1.describe()
print()

# DialogoHistorieta
formato_historieta = DialogoHistorieta()
formato_historieta.conversacion(pato1, pato2,
                                mensaje1="¡Ay, Daisy! ¡Casi me caigo al intentar atrapar un pez!",
                                mensaje2="¡Otra vez, Donald? Ten más cuidado la próxima vez.")
print()
# DialogoFormal
formato_formal = DialogoFormal()
formato_formal.conversacion(pato1, pato2,
                            mensaje1="¿Cómo estás?",
                            mensaje2="Gracias por preguntar.")
print()

"""
Observaciones:
Implementar ABC, y en particular abstractmethod, en las clases ayuda a seguir el principio OCP,
porque define clases que pueden agregar nuevas funcionalidades sin alterar el código existente
mediante un diseño modular.

Al usar clases abstractas, se definen comportamientos comunes en una clase base y
se permite que las clases derivadas personalicen o extiendan esos comportamientos.
Esto facilita la adición de nuevas funcionalidades sin modificar el código existente.
"""

# Extra

# Configurar Logger
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Calculadora(ABC):
    """Clase base abstracta que define la aplicación de cálculos"""
    @abstractmethod
    def operacion(self):
        pass

    @abstractmethod
    def impresion(self):
        pass


def redondeo(funcion):
    def nueva_funcion(*args, **kwargs):
        logging.debug("Implementando funcion de redondeo")
        try:
            resultado = funcion(*args, **kwargs)
            if resultado is None:
                return None
            elif isinstance(resultado, tuple):
                return tuple(round(val, 2) for val in resultado)
            else:
                return round(resultado, 2)
        except Exception as e:
            logging.error(f"Error en la función '{funcion.__name__}': {e}")
            return None
    return nueva_funcion


class Suma(Calculadora):
    logging.debug("Implementando funcion de Suma")

    def __init__(self, sumando1: float, sumando2: float) -> float:
        self.sumando1 = sumando1
        self.sumando2 = sumando2

    @redondeo
    def operacion(self):
        try:
            suma_total = self.sumando1 + self.sumando2
            return suma_total
        except Exception as e:
            logging.error(f"Error al calcular la suma: {e}")
            return None

    def impresion(self):
        suma_total = self.operacion()
        if suma_total is not None:
            print(f"La suma de {self.sumando1} y {
                  self.sumando2} dio como resultado {suma_total}")
            logging.debug("La implementación de suma fue exitosa")
        else:
            logging.warning("No se pudo realizar la suma.")


class Resta(Calculadora):
    logging.debug("Implementando funcion de Resta")

    def __init__(self, minuendo: float, sustraendo: float) -> float:
        self.minuendo = minuendo
        self.sustraendo = sustraendo

    @redondeo
    def operacion(self):
        try:
            resto = self.minuendo - self.sustraendo
            return resto
        except Exception as e:
            logging.error(f"Error al calcular la resta: {e}")
            return None

    def impresion(self):
        resto = self.operacion()
        if resto is not None:
            print(f"La resta de {self.minuendo} y {
                  self.sustraendo} dio como resultado {resto}")
            logging.debug("La implementación de resta fue exitosa")
        else:
            logging.warning("No se pudo realizar la resta.")


class Multiplicacion(Calculadora):
    logging.debug("Implementando funcion de Multiplicación")

    def __init__(self, factor1: float, factor2: float) -> float:
        self.factor1 = factor1
        self.factor2 = factor2

    @redondeo
    def operacion(self):
        try:
            producto = self.factor1 * self.factor2
            return producto
        except Exception as e:
            logging.error(f"Error al calcular la multiplicación: {e}")
            return None

    def impresion(self):
        producto = self.operacion()
        if producto is not None:
            print(f"La multiplicación de {self.factor1} y {
                  self.factor2} dio como resultado {producto}")
            logging.debug("La implementación de multiplicació fue exitosa")
        else:
            logging.warning("No se pudo realizar la multiplicación.")


class Division(Calculadora):
    logging.debug("Implementando funcion de división")

    def __init__(self, dividendo: float, divisor: float) -> float:
        self.dividendo = dividendo
        self.divisor = divisor

    @redondeo
    def operacion(self):
        try:
            if self.divisor == 0:
                raise ValueError("División por cero no está permitida.")
            cociente = self.dividendo / self.divisor
            resto = self.dividendo % self.divisor
            return cociente, resto
        except Exception as e:
            logging.error(f"Error al calcular la división: {e}")
            return None

    def impresion(self):
        resultado = self.operacion()
        if resultado is not None:
            cociente, resto = resultado
            print(f"La división de {self.dividendo} y {
                  self.divisor} dio como resultado cociente {cociente} y resto {resto}")
            logging.debug("La implementación de división fue exitosa")
        else:
            logging.warning(f"No se puede realizar la división de {
                            self.dividendo} por {self.divisor}.")


class Potencia(Calculadora):
    logging.debug("Implementando funcion de potencia")

    def __init__(self, base: int, exponente: float) -> float:
        self.base = base
        self.exponente = exponente

    @redondeo
    def operacion(self):
        try:
            resultado = self.base ** self.exponente
            return resultado
        except Exception as e:
            logging.error(f"Error al calcular la potencia: {e}")
            return None

    def impresion(self):
        resultado = self.operacion()
        if resultado is not None:
            print(f"La potenciación de {self.base} y {
                  self.exponente} dio como resultado {resultado}.")
            logging.debug("La implementación de potencia fue exitosa")
        else:
            logging.warning("No se pudo realizar la potenciación.")


# Uso
s = Suma(4, 5)
s.impresion()

r = Resta(9, 3)
r.impresion()

m = Multiplicacion(7, 6)
m.impresion()

d = Division(20, 0)
d.impresion()

d = Division(20, 4)
d.impresion()

p = Potencia(2, 2)
p.impresion()
