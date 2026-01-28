# EJERCICIO:
# Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
# y crea un ejemplo simple donde se muestre su funcionamiento
# de forma correcta e incorrecta.
from abc import ABC, abstractmethod

"""
Explicación del Principio de Sustitución de Liskov (LSP):
Este principio establece que los objetos de una clase padre deben poder ser reemplazados
por objetos de sus subclases sin alterar el correcto funcionamiento del programa.
En otras palabras, si la clase B es una subclase de la clase A, entonces deberíamos
poder usar instancias de B en cualquier lugar donde se espere una instancia de A
sin que el código falle o se comporte de manera inesperada.
"""

# --- Ejemplo INCORRECTO ---
print("--- Ejemplo INCORRECTO ---")


class Ave:
    def volar(self):
        return "Estoy volando!"


class Pato(Ave):
    def volar(self):
        return "Estoy volando!"


class Pinguino(Ave):
    def volar(self):
        # Los pingüinos no vuelan, así que esto rompe la expectativa de la clase padre
        raise Exception("Los pingüinos no pueden volar")


def hacer_volar_ave(ave: Ave):
    try:
        print(ave.volar())
    except Exception as e:
        print(f"Error: {e}")


pato = Pato()
pinguino = Pinguino()

hacer_volar_ave(pato)  # Funciona: "Estoy volando!"
hacer_volar_ave(pinguino)  # Falla


# --- Ejemplo CORRECTO (Cumpliendo LSP) ---
print("\n--- Ejemplo CORRECTO ---")


class AveV2:
    """Clase abstracta para todos los tipos de aves"""

    @abstractmethod
    def comer(self) -> str:
        pass

    @abstractmethod
    def moverse(self) -> str:
        """metodo mas generico, todas las aves pueden moverse"""
        pass


class AveVoladora(AveV2):
    """subclase para aves que pueden volar"""

    def volar(self) -> str:
        return "Estoy volando!"

    def moverse(self) -> str:
        return "Estoy moviendome volando!"

    def comer(self) -> str:
        return "Estoy comiendo!"


class AveNoVoladora(AveV2):
    """subclase para aves que no pueden volar"""

    def moverse(self) -> str:
        return "Estoy moviendome caminando!"

    def comer(self) -> str:
        return "Estoy comiendo!"


class Aguila(AveVoladora):
    def moverse(self) -> str:
        return "Estoy moviendome volando!"


class PinguinoV2(AveNoVoladora):
    def moverse(self) -> str:
        return "Estoy moviendome nadando!"


def mover_ave(ave: AveV2):
    print(f"ave: {ave.__class__.__name__} - {ave.moverse()}")
    print(f"ave: {ave.__class__.__name__} - {ave.comer()}")


# Ejemplo de uso
aguila = Aguila()
pinguino = PinguinoV2()
mover_ave(aguila)
mover_ave(pinguino)


# DIFICULTAD EXTRA (opcional):
# Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
# cumplir el LSP.
# Instrucciones:
# 1. Crea la clase Vehículo.
# 2. Añade tres subclases de Vehículo.
# 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
# 4. Desarrolla un código que compruebe que se cumple el LSP.


class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self._velocidad = 0
        self._velocidad_maxima = 0

    @abstractmethod
    def acelerar(self) -> str:
        return "Acelerando"

    @abstractmethod
    def frenar(self) -> str:
        return "Frenando"

    def get_velocidad(self):
        return self._velocidad

    def get_info(self):
        return f"{self.__class__.__name__} - {self.marca} {self.modelo}"


class Coche(Vehiculo):
    def __init__(self, marca: str, modelo: str):
        super().__init__(marca, modelo)
        self._velocidad_maxima = 200

    def acelerar(self, incremento: int = 10) -> str:
        velocidad_anterior = self._velocidad
        self._velocidad = min(self._velocidad + incremento, self._velocidad_maxima)

        if self._velocidad == self._velocidad_maxima:
            return f"Velocidad máxima alcanzada: {self._velocidad} km/h"
        else:
            return f"Acelerando de {velocidad_anterior} a {self._velocidad} km/h"

    def frenar(self, decremento: int = 10) -> str:
        velocidad_anterior = self._velocidad
        self._velocidad = max(self._velocidad - decremento, 0)

        if self._velocidad == 0:
            return f"Coche frenando: {velocidad_anterior} -> {self._velocidad} km/h (Detenido)"

        return f"Coche frenando: {velocidad_anterior} -> {self._velocidad} km/h"


class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str):
        super().__init__(marca, modelo)
        self._velocidad_maxima = 180

    def acelerar(self, incremento: int = 10) -> str:
        velocidad_anterior = self._velocidad
        self._velocidad = min(self._velocidad + incremento, self._velocidad_maxima)

        if self._velocidad == self._velocidad_maxima:
            return f"Velocidad máxima alcanzada: {self._velocidad} km/h"
        else:
            return f"Acelerando de {velocidad_anterior} a {self._velocidad} km/h"

    def frenar(self, decremento: int = 10) -> str:
        velocidad_anterior = self._velocidad
        self._velocidad = max(self._velocidad - decremento, 0)

        if self._velocidad == 0:
            return f"Moto frenando: {velocidad_anterior} -> {self._velocidad} km/h (Detenido)"

        return f"Moto frenando: {velocidad_anterior} -> {self._velocidad} km/h"


class Camion(Vehiculo):
    def __init__(self, marca: str, modelo: str, carga_maxima: int):
        super().__init__(marca, modelo)
        self._velocidad_maxima = 110
        self._carga_maxima = carga_maxima
        self._carga = 0

    def acelerar(self, incremento: int = 10) -> str:
        velocidad_anterior = self._velocidad
        self._velocidad = min(self._velocidad + incremento, self._velocidad_maxima)

        if self._velocidad == self._velocidad_maxima:
            return f"Velocidad máxima alcanzada: {self._velocidad} km/h"
        else:
            return f"Acelerando de {velocidad_anterior} a {self._velocidad} km/h"

    def frenar(self, decremento: int = 10) -> str:
        velocidad_anterior = self._velocidad
        self._velocidad = max(self._velocidad - decremento, 0)

        if self._velocidad == 0:
            return f"Camion frenando: {velocidad_anterior} -> {self._velocidad} km/h (Detenido)"

        return f"Camion frenando: {velocidad_anterior} -> {self._velocidad} km/h"

    def cargar(self, carga: int) -> str:
        self._carga += carga
        return f"Carga actual: {self._carga}"

    def descargar(self) -> str:
        self._carga = 0
        return "Carga descargada"


def probar_vehiculo(vehiculo: Vehiculo) -> None:
    """
    Funcion que trabaja con cualquier tipo de vehiculo.
    """
    print(f"Probando {vehiculo.__class__.__name__}:")
    print(f"Velocidad inicial: {vehiculo.get_velocidad()}")
    print("Acelerando 3 veces:")
    for i in range(3):
        print(f"Acelerando {i + 1} vez: {vehiculo.acelerar()}")

    print(f"Velocidad actual: {vehiculo.get_velocidad()}")

    print("Frenando 3 veces:")
    for i in range(3):
        print(f"Frenando {i + 1} vez: {vehiculo.frenar()}")

    print(f"Velocidad actual: {vehiculo.get_velocidad()}")

    print(f"Info: {vehiculo.get_info()}")


def verificar_lsp() -> None:
    """
    Funcion que verifica el LSP.
    """
    vehiculos: list[Vehiculo] = [
        Coche("Renault", "Clio"),
        Moto("Zanella", "Zanella 350"),
        Camion("Fiat", "Doblò", 10000),
    ]

    # si es un camion, cargar 5000kg
    if isinstance(vehiculos[2], Camion):
        vehiculos[2].cargar(5000)

    # pruebo cada vehiculo con la misma funcion
    for vehiculo in vehiculos:
        probar_vehiculo(vehiculo)

    print("Verificacion del LSP:")
    print("Todas las subclases pueden sustituir a la clase base")
    print("La función probar_vehiculo() funciona con cualquier vehículo")
    print("No hay excepciones ni comportamientos inesperados")
    print("Se cumple el Principio de Sustitución de Liskov")


if __name__ == "__main__":
    verificar_lsp()
