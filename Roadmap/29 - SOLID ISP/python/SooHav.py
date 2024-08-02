# 29 SOLID: PRINCIPIO DE SEGREGACIÓN DE INTERFACES (ISP)
# Ejercicio
# Ejemplo Pato sin ISP
from abc import ABC, abstractmethod


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


# Ejemplo Pato con ISP
class Volador (ABC):
    @abstractmethod
    def vuela(self):
        pass


class Nadador (ABC):
    @abstractmethod
    def nada(self):
        pass


class Hablador (ABC):
    @abstractmethod
    def dice(self):
        pass


class Flotador (ABC):
    @abstractmethod
    def flota(self):
        pass


class PatoSalvaje(Volador, Nadador, Hablador):
    def __init__(self, tipo):
        self.tipo = tipo

    def vuela(self):
        print(f"El {self.tipo} vuela.")

    def nada(self):
        print(f"El {self.tipo} nada.")

    def dice(self):
        print(f"El {self.tipo} dice Quack.")


class PatoDomestico(Nadador, Hablador):
    def __init__(self, tipo):
        self.tipo = tipo

    def nada(self):
        print(f"El {self.tipo} nada.")

    def dice(self):
        print(f"El {self.tipo} dice Quack.")


class PatoPlastico(Hablador, Flotador):
    def __init__(self, tipo):
        self.tipo = tipo

    def dice(self):
        print(f"El {self.tipo} dice Quick.")

    def flota(self):
        print(f"El {self.tipo} flota en la bañera.")


# Uso
print("Con ISP")
pato4 = PatoSalvaje("Pato Salvaje")
pato5 = PatoDomestico("Pato Domestico")
pato6 = PatoPlastico("Pato de plastico")

pato4.vuela()
pato4.nada()
pato4.dice()

pato5.nada()
pato5.dice()

pato6.dice()
pato6.flota()

# Extra


class Imprimir (ABC):
    @abstractmethod
    def imprime(self):
        pass


class Escanear (ABC):
    @abstractmethod
    def escanea(self):
        pass


class Enviar_Fax (ABC):
    @abstractmethod
    def envia(self):
        pass


class Impresora_ByN(Imprimir):
    def __init__(self, tipo):
        self.tipo = tipo

    def imprime(self):
        print(f"Se {self.imprime.__name__} documento en {self.tipo}.")


class Impresora_Color(Imprimir):
    def __init__(self, tipo):
        self.tipo = tipo

    def imprime(self):
        print(f"Se {self.imprime.__name__} documento en {self.tipo}.")


class Impresora_Multifuncion(Imprimir, Escanear, Enviar_Fax):
    def __init__(self, tipo):
        self.tipo = tipo

    def imprime(self):
        print(f"Se {self.imprime.__name__} documento en {self.tipo}.")

    def escanea(self):
        print(f"Se {self.escanea.__name__} documento en {self.tipo}.")

    def envia(self):
        print(f"Se {self.envia.__name__} fax en {self.tipo}.")

# Gestor de impresoras


class GestorImpresoras:
    def __init__(self):
        self.impresoras = []

    def agregar_impresora(self, impresora):
        self.impresoras.append(impresora)

    def listar_impresoras(self):
        print("\nListado de impresoras disponibles:")
        for id, impresora in enumerate(self.impresoras, start=1):
            print(f"{id}. {type(impresora).__name__} - {impresora.tipo}")

    def seleccionar_impresora(self):
        self.listar_impresoras()
        seleccion = int(
            input("Seleccione el número de la impresora que desea usar: "))
        if seleccion <= 0 or seleccion > len(self.impresoras):
            print("Selección inválida.")
            return None
        return self.impresoras[seleccion - 1]

    def imprimir_documento(self, impresora):
        if isinstance(impresora, Imprimir):
            impresora.imprime()
        else:
            print(f"La impresora {
                  type(impresora).__name__} no puede imprimir.")

    def escanear_documento(self, impresora):
        if isinstance(impresora, Escanear):
            impresora.escanea()
        else:
            print(f"La impresora {
                  type(impresora).__name__} no puede escanear.")

    def enviar_documento(self, impresora):
        if isinstance(impresora, Enviar_Fax):
            impresora.envia()
        else:
            print(f"La impresora {
                  type(impresora).__name__} no puede enviar fax.")


# Uso del gestor de impresoras
if __name__ == "__main__":
    gestor = GestorImpresoras()

    # Agregar impresoras
    impresora1 = Impresora_ByN("Impresora B/N 1")
    impresora2 = Impresora_Color("Impresora Color 1")
    impresora3 = Impresora_Multifuncion("Impresora Multifunción 1")
    impresora4 = Impresora_ByN("Impresora B/N Secretaría")

    gestor.agregar_impresora(impresora1)
    gestor.agregar_impresora(impresora2)
    gestor.agregar_impresora(impresora3)
    gestor.agregar_impresora(impresora4)

    gestor.listar_impresoras()
    gestor.seleccionar_impresora()

    gestor.imprimir_documento(impresora4)
    gestor.escanear_documento(impresora3)
    gestor.enviar_documento(impresora3)

"""
#Interacción
    while True:
        print("\n1. Agregar impresora")
        print("2. Visualizar listado de impresoras")
        print("3. Imprimir documento")
        print("4. Escanear documento")
        print("5. Enviar Fax")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Ingrese el tipo de impresora (ByN/Color/Multifuncion): ").lower()
            nombre = input("Ingrese el nombre de la impresora: ")
            if tipo == "byn":
                gestor.agregar_impresora(Impresora_ByN(nombre))
            elif tipo == "color":
                gestor.agregar_impresora(Impresora_Color(nombre))
            elif tipo == "multifuncion":
                gestor.agregar_impresora(Impresora_Multifuncion(nombre))
            else:
                print("Tipo de impresora no reconocido.")

        elif opcion == "2":
            gestor.listar_impresoras()

        elif opcion == "3":
            seleccionada = gestor.seleccionar_impresora()
            if seleccionada:
                gestor.imprimir_documento(seleccionada)

        elif opcion == "4":
            seleccionada = gestor.seleccionar_impresora()
            if seleccionada:
                gestor.escanear_documento(seleccionada)

        elif opcion == "5":
            seleccionada = gestor.seleccionar_impresora()
            if seleccionada:
                gestor.enviar_documento(seleccionada)

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

 """
