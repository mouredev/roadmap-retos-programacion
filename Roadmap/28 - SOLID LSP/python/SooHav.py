# 28 SOLID: PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP)
from abc import ABC, abstractmethod
# Ejercicio


class Pato:
    def __init__(self, tipo):
        self.tipo = tipo


class Pato_Acciones(Pato):
    def vuela(self):
        if self.tipo in ["domestico", "salvaje"]:
            print(f"El pato {self.tipo} vuela.")
        else:
            print(f"El pato {self.tipo} no puede volar.")

    def nada(self):
        if self.tipo in ["domestico", "salvaje"]:
            print(f"El pato {self.tipo} nada.")
        else:
            print(f"El pato {self.tipo} no puede nadar.")

    def dice(self):
        if self.tipo in ["domestico", "salvaje", "plastico"]:
            print(f"El pato {self.tipo} dice Quack.")
        else:
            print(f"El pato {self.tipo} no puede hacer Quack.")


# Uso
print("Sin LSP")
pato1 = Pato_Acciones(tipo="salvaje")
pato2 = Pato_Acciones(tipo="domestico")
pato3 = Pato_Acciones(tipo="plastico")

pato1.vuela()
pato1.nada()
pato1.dice()

pato2.vuela()
pato2.nada()
pato2.dice()

pato3.vuela()
pato3.nada()
pato3.dice()

# Ejemplo Pato con LSP


class Pato (ABC):
    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def vuela(self):
        pass

    @abstractmethod
    def nada(self):
        pass

    @abstractmethod
    def dice(self):
        pass


class PatoSalvaje(Pato):
    def __init__(self):
        super().__init__("salvaje")

    def vuela(self):
        print("El pato salvaje vuela.")

    def nada(self):
        print("El pato salvaje nada.")

    def dice(self):
        print("El pato salvaje dice Quack.")


class PatoDomestico(Pato):
    def __init__(self):
        super().__init__("domestico")

    def vuela(self):
        print("El pato doméstico vuela.")

    def nada(self):
        print("El pato doméstico nada.")

    def dice(self):
        print("El pato doméstico dice Quack.")


class PatoPlastico(Pato):
    def __init__(self):
        super().__init__("plastico")

    def vuela(self):
        print("El pato de plástico no puede volar.")

    def nada(self):
        print("El pato de plástico no puede nadar.")

    def dice(self):
        print("El pato de plástico dice Squeak.")


# Uso
print("Con LSP")
pato1 = PatoSalvaje()
pato2 = PatoDomestico()
pato3 = PatoPlastico()

pato1.vuela()
pato1.nada()
pato1.dice()

pato2.vuela()
pato2.nada()
pato2.dice()

pato3.vuela()
pato3.nada()
pato3.dice()

# Extra


class Vehiculo (ABC):
    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def acelera(self, velocidad, tiempo):
        pass

    @abstractmethod
    def frena(self, velocidad, tiempo):
        pass


class Moto(Vehiculo):
    def __init__(self):
        super().__init__("moto")

    def acelera(self, velocidad_inicial, tiempo):
        aceleracion = 25  # km/h/s
        velocidad_final = velocidad_inicial + aceleracion * tiempo
        return min(velocidad_final, 220)

    def frena(self, velocidad_inicial, tiempo):
        desaceleracion = 30  # km/h/s
        velocidad_final = velocidad_inicial - desaceleracion * tiempo
        return max(velocidad_final, 0)


class Auto(Vehiculo):
    def __init__(self):
        super().__init__("auto")

    def acelera(self, velocidad_inicial, tiempo):
        aceleracion = 15  # km/h/s
        velocidad_final = velocidad_inicial + aceleracion * tiempo
        return min(velocidad_final, 240)

    def frena(self, velocidad_inicial, tiempo):
        desaceleracion = 25  # km/h/s
        velocidad_final = velocidad_inicial - desaceleracion * tiempo
        return max(velocidad_final, 0)


class Camion(Vehiculo):
    def __init__(self):
        super().__init__("camion")

    def acelera(self, velocidad_inicial, tiempo):
        aceleracion = 4  # km/h/s
        velocidad_final = velocidad_inicial + aceleracion * tiempo
        return min(velocidad_final, 110)

    def frena(self, velocidad_inicial, tiempo):
        desaceleracion = 12  # km/h/s
        velocidad_final = velocidad_inicial - desaceleracion * tiempo
        return max(velocidad_final, 0)


# Uso
print("Con LSP")
moto = Moto()
auto = Auto()
camion = Camion()

# Ejemplo  para acelerar y frenar
velocidad_inicial = 25
tiempo_acelerar = 4
tiempo_frenar = 2

velocidad_acelerada = moto.acelera(velocidad_inicial, tiempo_acelerar)
velocidad_frenada = moto.frena(velocidad_acelerada, tiempo_frenar)
print(f"La velocidad de la moto después de acelerar durante {
      tiempo_acelerar} segundos es de {velocidad_acelerada} km/h")
print(f"La velocidad de la moto después de frenar durante {
      tiempo_frenar} segundos es de {velocidad_frenada} km/h")

velocidad_acelerada = auto.acelera(velocidad_inicial, tiempo_acelerar)
velocidad_frenada = auto.frena(velocidad_acelerada, tiempo_frenar)
print(f"La velocidad del auto después de acelerar durante {
      tiempo_acelerar} segundos es de {velocidad_acelerada} km/h")
print(f"La velocidad del auto después de frenar durante {
      tiempo_frenar} segundos es de {velocidad_frenada} km/h")

velocidad_acelerada = camion.acelera(velocidad_inicial, tiempo_acelerar)
velocidad_frenada = camion.frena(velocidad_acelerada, tiempo_frenar)
print(f"La velocidad del camion después de acelerar durante {
      tiempo_acelerar} segundos es de {velocidad_acelerada} km/h")
print(f"La velocidad del camion después de frenar durante {
      tiempo_frenar} segundos es de {velocidad_frenada} km/h")
