from abc import ABC, abstractmethod

"""
Principio de sustitucion de Liskov

Cada clase que hereda de otra puede usarse como su padre sin necesidad de conocer las diferencias entre ellas. 

"""


# El siguiente ejemplo es un ejemplo erroneo donde no se cumple el principio

class ProductoWrong(ABC):

    def __init__(self, marca):
      self.marca = marca

    @abstractmethod
    def comer(self):
        print("Comiendo: " + self.marca)
    
class PolloAsadoWrong(ProductoWrong):

    def __init__(self, marca, calories):
        self.calories = calories
        self.marca = marca
    
    def comer(self):
        return super().comer()

class LejiaWrong(ProductoWrong):
    def __init__(self, marca, liters):
        self.liters = liters
        self.marca = marca

    def comer(self):
        raise ValueError("No puedes comer Lejia")
    

# A continuacion se deja expreso una version del mismo codigo pero que cumple el principio de sustitucion de liskov

class Producto(ABC):

    def __init__(self, name ,marca, price, categoria):
      self.name = name
      self.marca = marca
      self.price = price
      self.categoria =categoria
    
    @abstractmethod
    def comprar(self):
        print (f"Comprando {self.name} \nMarca: {self.marca} \nCategoria {self.categoria} \nPrecio ${self.price}")
        pass


class ProductoDeAseo(Producto):
    
    def __init__(self, name ,marca, price, categoria, porcentajeAccionDesinfectante):
        super().__init__(name ,marca, price, categoria)
        self.porcentajeAccionDesinfectante = porcentajeAccionDesinfectante
    
    def comprar (self):
        super().comprar()
        print(f"Accion desinfectante al %{self.porcentajeAccionDesinfectante}")

    def asear (self):
        print(f"Aseando con {self.name} al %{self.porcentajeAccionDesinfectante}")

class Comida(Producto):

    def __init__(self, name ,marca, price, categoria, calories):
        super().__init__(name ,marca, price, categoria)
        self.calories = calories

    def comprar(self):
        super().comprar()
        print(f"Calorias por porcion: {self.calories}\n")

    def comer(self):
        print(f"Comiendo {self.name} que aporta {self.calories} calorias por porción")


polloAsado = Comida("Pollo Asado 1 Kilo","Ariztia",5000,"Platos Preparados","800 Calorias")
pure = Comida("Pure Rustico con Bistec","Genial",3490,"Platos Preparados","600 Calorias")
abrillantadorPisoFlotante = ProductoDeAseo("Abrillantador de Piso Flotante","Brillantina",3200,"Pisos", 0)

"""
print("\n")
polloAsado.comprar()
print("\n")
pure.comprar()
print("\n")
abrillantadorPisoFlotante.comprar()

print("\n")
polloAsado.comer()
print("\n")
abrillantadorPisoFlotante.asear()
print("\n")
pure.comer()
"""




"""
Ejercicio Extra:

Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.

"""

class Vehiculo:
    def __init__(self, name, marca, category):
      self.name = name
      self.marca = marca
      self.category= category

    def frenar(self):
        print (f"Frenando: {self.name}")
        pass

    def acelerar(self):
        print(f"Acelerando: {self.name} ")
        pass



class VehiculoManual(Vehiculo):

    def __init__(self, name, marca, category, maxWeight, minimumAge):
        super().__init__(name, marca, category)
        self.maxWeight = maxWeight
        self.minimumAge = minimumAge
    
    def acelerar(self):
        print("Moviendo los pies muy rapido")
        super().acelerar()
    
    def frenar(self):
        print("Dejando de Acelerar y tratar de poner los pies en el piso")
        super().frenar()

    def subirAlVehiculo(self, weight, age):
        if(weight >= self.maxWeight):
            print("Atencion el vehiculo lleva mucho peso!")
        if(age < self.minimumAge):
            print(f"Eres muy pequeño para este Vehiculo")
        elif(age >= self.minimumAge and weight < self.maxWeight):
            print(f"Eres adecuado para este vehiculo, siga movilizandose! :)")


class VehiculoACombustion(Vehiculo):

    def __init__(self, name, marca, category, cilinders, fuelType):
        super().__init__(name, marca, category)
        self.cilinders = cilinders
        self.fuel = fuelType

    def acelerar(self):
        print("Pisando el Acelerador!")
        self.subirMarchas()
        super().acelerar()
    
    def frenar(self):
        print("Presionar el Pedal de freno y Lentamente el Embrague")
        self.bajarMarchas()
        super().frenar()

    def subirMarchas(self):
        print("Subiendo Marchas")
    
    def bajarMarchas(self):
        print("Bajando Marchas")

    
    
class VehiculoElectrico(Vehiculo):

    def __init__(self, name, marca, category, electricMotorsQuantity, fastCharge):
        super().__init__(name, marca, category)
        self.electricMotorsQuantity = electricMotorsQuantity
        self.fastCharge = fastCharge

    def acelerar(self):
        print("Pisando el Acelerador de forma Cool!")
        super().acelerar()
    
    def frenar(self):
        print("Presionando el Freno igual de Cool!")
        super().frenar()

    def cargarEnElPoste(self):
        print("Cargando el Vehiculo electrico de una forma muy Cool!")
        if(self.fastCharge): print("Wow!, tenemos Fast Charging!!!")
    


bicicleta = VehiculoManual("Bicicleta BMX","Oddysey","Deporte Extremo", 80, 15)
skate = VehiculoManual("Skate","Plan B","Deporte Extremo", 80, 5)

motocicleta = VehiculoACombustion("Motocicleta", "Honda", "City", 1, "Gasolina" )
auto = VehiculoACombustion("Skyline", "Nissan", "Sportcar", 8, "Gasolina")

tesla = VehiculoElectrico("Model S","Tesla","Cool Electric Car", 4, True)

print("Bicicleta BMX")
bicicleta.subirAlVehiculo(90,13)
bicicleta.acelerar()
bicicleta.frenar()

print("\nSkate PlanB")
skate.subirAlVehiculo(75, 15)
skate.acelerar()
skate.frenar()

print("\nMotocicleta Honda")
motocicleta.acelerar()
motocicleta.frenar()
print("\nNissan Skyline")
auto.acelerar()
auto.frenar()


print("\nTesla Model S")
tesla.cargarEnElPoste()
tesla.acelerar()
tesla.frenar()




    



    