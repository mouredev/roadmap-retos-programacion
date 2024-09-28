#En python podemos capturar excepciones mediante el bloque try/except

try:
    100/0

except: 
    print("Se ha producido una excepción")

#Se puede emplear un bloque except específico para una excepción
    
try:
    100/0
except ZeroDivisionError:
    print("Código específico de la excepción")

#Al añadir un bloque finally tendremos código que siempre se ejecutará
    
try:
    100/0
except ZeroDivisionError:
    print("Código de la excepción")
finally:
    print("Código que siempre se ejecutará")

#Se puede forzar una excepción mediante raise
    
i = 12

if i>10:
    raise ValueError("El número a de ser menor que 10")

#También puedes generar tu propia excepción heredando de la clase exception
class MiErrorPersonalizado(Exception):
    def __init__(self, mensaje="Ocurrió un error personalizado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Uso de la excepción personalizada
raise MiErrorPersonalizado("Error")
