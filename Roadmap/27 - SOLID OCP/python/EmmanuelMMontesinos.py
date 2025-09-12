"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 */
"""
'Sin Aplicar'
class Programador_0:
    def __init__(self,nombre,salario,puesto) -> None:
        self.nombre = nombre
        self.salario = salario
        self.puesto = puesto


    def pagar_nomina(self):
        print(f"{self.nombre} recibe su nomina de {self.puesto}: {self.salario}€")

# Prueba

emmanuel = Programador_0("Emmanuel",1000,"Traini")
emmanuel.pagar_nomina()

moure = Programador_0("Brais",5000,"Senior")
moure.pagar_nomina()

'Aplicado'
class Programador:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    def pagar_nomina(self):
        raise NotImplementedError("Esta es la clase base")
    
class Traini(Programador):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.salario = 1000
    def pagar_nomina(self):
        print(f"{self.nombre} recibe su nomina de Traini: {self.salario}€")

class Senior(Programador):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.salario = 5000
    def pagar_nomina(self):
        print(f"{self.nombre} recibe su nomina de Senior: {self.salario + 200}€")

# Prueba
emmanuel = Traini("Emmanuel")
emmanuel.pagar_nomina()

moure = Senior("Brais")
moure.pagar_nomina()

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
class Calculo:
    def __init__(self) -> None:
        self.operaciones = {}

    def agregar_operacion(self,nombre,operacion):
        self.operaciones[nombre] = operacion

    def resultado(self,a,b,operacion):
        print(f"Resultado de {operacion}: {self.operaciones[operacion].hacer_calculo(a,b)}")
        
class Operacion:
    def hacer_calculo(self,a,b):
        raise NotImplementedError("Clase Base de operaciones")
    
class Sumar(Operacion):
    def hacer_calculo(self, a, b):
        return a + b
    
class Restar(Operacion):
    def hacer_calculo(self, a, b):
        return a - b
    
class Multiplicar(Operacion):
    def hacer_calculo(self, a, b):
        return a * b
    
class Dividir(Operacion):
    def hacer_calculo(self, a, b):
        return a / b

class Potencia(Operacion):
    def hacer_calculo(self, a, b):
        return a ** b

# Pruebas

calculadora = Calculo()
calculadora.agregar_operacion("sumar",Sumar())
calculadora.agregar_operacion("restar",Restar())
calculadora.agregar_operacion("multiplicar",Multiplicar())
calculadora.agregar_operacion("dividir",Dividir())
calculadora.agregar_operacion("potencia",Potencia())

calculadora.resultado(5,5,"sumar")
calculadora.resultado(5,5,"restar")
calculadora.resultado(5,5,"multiplicar")
calculadora.resultado(5,5,"dividir")
calculadora.resultado(5,5,"potencia")