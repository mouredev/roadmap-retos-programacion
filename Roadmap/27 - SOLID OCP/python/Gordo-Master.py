# 27 - Solid OCP

# Significado de Abierto-Cerrado (Open-Close Principle, OCP):
# La clase debe estar cerrado a modificación, pero abierto a ampliacion del codigo.

# Incorrecta

from abc import ABC, abstractmethod

"""
class CalculadoraEnvio():
    
    def calcular(self, tipo_envio, peso: float):
        
        if tipo_envio == "Normal":
            return f"{1.05 * peso :.2f}"
        
        elif tipo_envio == "Express":
            return f"{1.1 * peso:.2f}"
        
        else:
            return False
        

cal_envios = CalculadoraEnvio()

print(cal_envios.calcular("Normal", 20.5))
print(cal_envios.calcular("Express",20.5))
print(cal_envios.calcular("VIP", 20.5))
"""

# Correcta

class Envio(ABC):

    @abstractmethod
    def cal_costo(self, peso):
        pass


class EnvioNormal(Envio):

    def cal_costo(self, peso):
        return f"{1.05 * peso :.2f}"
    


class EnvioExpress(Envio):

    def cal_costo(self, peso):
        return f"{1.5 * peso :.2f}"
    

print(EnvioNormal().cal_costo(20.5))
print(EnvioExpress().cal_costo(20.5))

print()


"""
Ejercicio Extra
"""

class Operat(ABC):

    @abstractmethod
    def operation(self, num_1, num_2):
        pass


class Suma(Operat):

    def operation(self, num_1, num_2):
        return num_1 + num_2


class Resta(Operat):

    def operation(self, num_1, num_2):
        return num_1 - num_2
    

class Multiplicacion(Operat):

    def operation(self, num_1, num_2):
        return num_1 * num_2
    

class Division(Operat):

    def operation(self, num_1, num_2):
        return num_1 / num_2
    

class Calculadora():

    def calc(self, operat: Operat, num_1, num_2):
        return operat.operation(num_1,num_2)
    

calculdora = Calculadora()

print(calculdora.calc(Suma(), 5, 8))
print(calculdora.calc(Resta(), 5, 8))
print(calculdora.calc(Multiplicacion(), 5, 8))
print(calculdora.calc(Division(), 5, 8))

class Potencia(Operat):

    def operation(self, num_1, num_2):
        return num_1 ** num_2
    
print(calculdora.calc(Potencia(), 5, 8))