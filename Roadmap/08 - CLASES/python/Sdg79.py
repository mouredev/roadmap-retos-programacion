
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def persona_info(self):
        return f"La persona de nombre {self.nombre} y apellido {self.apellido} tiene {self.edad} años."

    def imprimir(self):
        print(datos.persona_info())   

datos = Persona("Sergio", "Sanchez", "40")
datos.imprimir()

"""
 * DIFICULTAD EXTRA:
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""

class Pila:
    def __init__(self, contenido: list):
        self.contenido = contenido
        
    def añadir(self, libro):
        self.contenido.append(libro)
    
    def eliminar(self):
        self.contenido.pop(-1)

    def cantidad(self):
        return len(self.contenido)
        
    def imprimir(self):
        print(self.contenido)

libros = Pila(["Python", "Visual Basic", "C++"])
libros.añadir("Pascal")
libros.imprimir()
libros.eliminar()
libros.imprimir()
print(libros.cantidad())


class Cola:
    def __init__(self, contenido: list):
        self.contenido = contenido
        
    def añadir(self, documento):
        self.contenido.append(documento)
    
    def eliminar(self):
        self.contenido.pop(0)

    def cantidad(self):
        return len(self.contenido)
        
    def imprimir(self):
        print(self.contenido)

documentos = Cola([".pdf", ".doc", ".xlsx"])
documentos.añadir("web")
documentos.imprimir()
documentos.eliminar()
documentos.imprimir()
print(documentos.cantidad())