"""
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

# NO cumple OCP
# Si quiero ampliar otro tipo de cliente, debo modificar toda la clase.
class CalculadoraDescuentos:
    def calcular(self, tipo_cliente, monto):
        if tipo_cliente == "regular":
            return monto * 0.95
        elif tipo_cliente == "vip":
            return monto * 0.90
        elif tipo_cliente == "super_vip":
            return monto * 0.85
        else:
            return monto
        
discount = CalculadoraDescuentos()
monto = 18
cliente = "super_vip"
print(f"Calculado descuento: Monto total: {monto} - Tipo cliente: {cliente} - Total tras descuento: {discount.calcular(cliente, monto)}")


# Cumpliendo OCP

from abc import ABC, abstractmethod #Modulo que contiene clases, metodos y decoradores para crear clases abstractas
                                    #Estas sirven para crear como un contrato o interfaz y decirle a las subclases que deben
                                    #tener un metodo calcular

class EstrategiaDescuento(ABC): # Defino la clase como abstracta. No se puden crear instancias de ellas directamente, deben ser heredadas.
    @abstractmethod             # Indico que este metodo es abstracto y que debe ser implementado en las sublases.
    def calcular(self, monto):
        pass

class DescuentoRegular(EstrategiaDescuento): # Estrategis de descuento. Si quiero añadir blackFriday añado otra clase sin modificar nada.
    def calcular(self, monto):
        return monto * 0.95
    
class DescuentoVip(EstrategiaDescuento):
    def calcular(self, monto):
        return monto * 0.90
    
class DescuentoSuperVip(EstrategiaDescuento):
    def calcular(self, monto):
        return monto * 0.85
    
class CalculadoraDescuentos: # Clase calculadora que recibe una estrategia y llama al metodo calcular de esa estrategia.
    def __init__(self, estrategia: EstrategiaDescuento):
        self.estrategia = estrategia

    def calcular(self, monto): # No sabe a que esta llamando simplemente llama al metodo de la estrategia guardada.
        return self.estrategia.calcular(monto)
    
cliente_regular = DescuentoRegular()
cliente_vip = DescuentoVip()
cliente_super_vip = DescuentoSuperVip()

calculadora = CalculadoraDescuentos(cliente_regular)
print(f"Descuento regular: {calculadora.calcular(100)}")
calculadora = CalculadoraDescuentos(cliente_vip)
print(f"Descuento vip: {calculadora.calcular(100)}")
calculadora = CalculadoraDescuentos(cliente_super_vip)
print(f"Descuento super vip: {calculadora.calcular(100)}")


"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
"""

# Diccionario donde se van a registrar automáticamente las operaciones.
command_registry = {}

# Decorador que registra una clase comando con un símbolo (como "+", "-", etc.)
def register_command(symbol):
    def decorator(cls):
        command_registry[symbol] = cls() # Guarda una instancia de la clase
        return cls # Devuelve la clase sin modificarla para que se pueda seguir utilizando la clase en el reto del codigo despues de decorarla.
    return decorator

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

@register_command("+")      #Python realmente hace esto: AddCommand = register_command("+") -->decorator(AddCommand) --> AddComand
class AddCommand(Command):  # entonces Addcomand sigue siendo Addcomand aunque se haya decorado.
    def execute(self, a, b):
        return a + b

@register_command("-")    
class SubCommand(Command):
    def execute(self, a, b):
        return a - b

@register_command("*")    
class MulCommand(Command):
    def execute(self, a, b):
        return a * b

@register_command("/")    
class DivCommand(Command):
    def execute(self, a, b):
        return a / b

@register_command("**")    
class ExpCommand(Command):
    def execute(self, a, b):
        return a ** b
    
class Invoker:
    #def __init__(self):  ya no necesito el init para inicializar el diccionario de operaciones.
        #self.commands = {}

    #def add_command(self, name:str, command: Command): y tampoco el metodo para registraroperacione manualmente.
        #self.commands[name] = command

    def calculate(self, name, *args):
        if name in command_registry:
            return command_registry[name].execute(*args)
        else:
            raise ValueError(f"La operación {name} no esta soportada.")
    

num1 = 6
num2 = 3

calculator = Invoker()
#Ya no es necesario registrar las operaciones manualmente ya que se hace con el decorador de clase.
#calculator.add_command("+", AddCommand()) # Realmente no se pasa la clase, sino que se crea una instacia en el momento
#calculator.add_command("-", SubCommand())# Es como hacer add = Addition() y luego pasar add.
#calculator.add_command("*", MulCommand())
#calculator.add_command("/", DivCommand())
#calculator.add_command("**", ExpCommand())

try:
    print(f"{num1} + {num2} = {calculator.calculate("+", num1, num2)}")
    print(f"{num1} - {num2} = {calculator.calculate("-", num1, num2)}")
    print(f"{num1} * {num2} = {calculator.calculate("*", num1, num2)}")
    print(f"{num1} / {num2} = {calculator.calculate("/", num1, num2)}")
    print(f"{num1} ** {num2} = {calculator.calculate("**", num1, num2)}")
except ValueError as e:
    print(e)
