# 35 REPARTIENDO LOS ANILLOS DE PODER
import random
from sympy import isprime
from abc import ABC, abstractmethod


class Anillos(ABC):
    @abstractmethod
    def calcular(self, numero_anillos):
        pass


class AnillosElfos(Anillos):
    def calcular(self, cantidad_anillos):
        # Los elfos reciben un número impar de anillos
        if cantidad_anillos < 1:
            raise ValueError(
                "No hay suficientes anillos para asignar a los Elfos.")
        while True:
            elfos = random.randint(1, cantidad_anillos-2)
            if elfos % 2 == 1:
                return elfos


class AnillosEnanos(Anillos):
    def calcular(self, cantidad_anillos):
        # Los enanos reciben un número primo de anillos
        while True:
            primo = random.randint(2, cantidad_anillos-3)
            if isprime(primo):
                return primo


class AnillosHombres(Anillos):
    def calcular(self, cantidad_anillos):
        # Los hombres reciben un número par de anillos
        if cantidad_anillos < 2:
            raise ValueError(
                "No hay suficientes anillos para asignar a los hombres.")
        while True:
            hombres = random.randint(2, cantidad_anillos)
            if hombres % 2 == 0:
                return hombres


class RepartoAnillos:
    def __init__(self, numero_anillos):
        self.sauron = 1
        self.elfos = None
        self.enanos = None
        self.hombres = None
        self.numero_anillos = numero_anillos
        self.intentos = 0

    def repartir_anillos(self):
        while True:
            self.intentos += 1
            calculador_elfos = AnillosElfos()
            calculador_enanos = AnillosEnanos()
            calculador_hombres = AnillosHombres()

            self.enanos = calculador_enanos.calcular(
                self.numero_anillos - self.sauron)
            self.elfos = calculador_elfos.calcular(
                self.numero_anillos - self.sauron - self.enanos)
            self.hombres = calculador_hombres.calcular(
                self.numero_anillos - self.sauron - self.enanos - self.elfos)

            if self.calcular_suma_total() == self.numero_anillos:
                print(f"Solución encontrada en {self.intentos} intentos")
                break

            if self.intentos > 2000:
                print("No se encontró solución después de 2000 intentos")
                break

    def calcular_suma_total(self):
        return self.sauron + self.elfos + self.enanos + self.hombres

    def __str__(self):
        if self.intentos > 2000:
            return (f"\nReparto de anillos:\nSauron: \nElfos: \n"
                    f"Enanos: \nHombres: ")
        else:
            return (f"\nReparto de anillos:\nSauron: {self.sauron}\nElfos: {self.elfos}\n"
                    f"Enanos: {self.enanos}\nHombres: {self.hombres}")


# Ejecutar el reparto de anillos
numero_anillos = int(input("Ingrese el número total de anillos: "))
anillos_del_poder = RepartoAnillos(numero_anillos)
anillos_del_poder.repartir_anillos()
print(anillos_del_poder)
