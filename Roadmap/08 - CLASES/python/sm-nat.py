class Libro:
    
    categoria = "Literatura"

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def descripcion(self):
        print(f"'{self.titulo}' es un libro de {self.paginas} páginas escrito por {self.autor}.")

    def es_largo(self):
        if self.paginas > 500:
            print(f"'{self.titulo}' es un libro largo.")
        else:
            print(f"'{self.titulo}' no es un libro largo.")

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
libro2 = Libro("Guerra y paz", "León Tolstói", 1225)

print(libro1.titulo)  
print(libro2.autor)  

libro1.descripcion()  
libro2.descripcion()  

libro1.es_largo()   
libro2.es_largo()     

print(Libro.categoria)  

#EXTRA
"""Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido."""

class Cola:
    def __init__(self):
        self.items = []

    def vacia(self):
        return len(self.items) == 0

    def añadir(self, item):
        self.items.append(item)

    def eliminar(self):
        if not self.vacia():
            return self.items.pop(0)
        else:
            return None

    def tamaño(self):
        return len(self.items)

    def imprimir(self):
        print("Contenido de la cola:", self.items)


cola = Cola()
cola.añadir(1)
cola.añadir(2)
cola.añadir(3)
cola.imprimir() 
print("Elemento eliminado:", cola.eliminar()) 
cola.imprimir() 
print("Tamaño de la cola:", cola.tamaño())  
