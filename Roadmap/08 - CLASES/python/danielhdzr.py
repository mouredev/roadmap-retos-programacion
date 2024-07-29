# #08 CLASES
#### Dificultad: Fácil | Publicación: 19/02/24 | Corrección: 26/02/24

## Ejercicio


""" 
* EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 
 """
 
def main():
    class my_class:
        """
        Funcion inicializadora __init__()
        Self hace referencia a la clase en si misma, y a todo lo que en ella hay guardado. Puedes llamarla como quieras
        """
        def __init__(self, name, last_name):
            # Los valores que asignaremos a los parametros se guardaran en las variables "nombre" y "apellido"
            self.nombre = name
            self.apellido = last_name

        # Creo un metodo para saludar. Accedo a las variables en mi clase mediante la sintaxis "clase.variable"
        def saludo(self):
            print(f"Hola, mi nombre completos es: {person.nombre} {person.apellido}")

    # Guardo mi clase y sus argumentos en una variable fuera de mi clase
    person = my_class("Daniel", "Hernandez")

    # Llamo a mi clase (guardada en la variable "person") y ejecuto el metodo saludo, 
    person.saludo()

    # Modifico los valores en las variables
    person.apellido = "Renteria"
    person.saludo()

    """
    DIFICULTAD EXTRA (opcional):
    Implementa dos clases que representen las estructuras de pila y Cola (estudiadas
    en el ejercicio número 7 de la ruta de estudio)
    Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
    retornar el número de elementos e imprimir todo su contenido.
    """

    # clase_pila
    class clase_pila:
        def __init__(self):
            # Variable que contendra nuestra clase_pila
            self.mi_pila = []

        def agregar(self, value):
            self.mi_pila.append(value)
            print(self.mi_pila)

        def eliminar(self):
            self.mi_pila.pop()
            print(self.mi_pila)
            
        def retornar(self):
            retorno = self.mi_pila.pop()
            print(f"Retorno: {(retorno)}")

        def imprimir(self):
            print(f"Pila final {self.mi_pila}")
    
    print("-----Pila-----")
    # Guardo la clase "clase_pila" en una variable
    pila = clase_pila()
    # Agrego
    pila.agregar(1)
    pila.agregar(2)
    pila.agregar(3)
    pila.agregar(4)
    pila.agregar(5)
    # Elimino el 5 (la pila ahora es de 4)
    pila.eliminar()
    # Retorno el 4, y la pila ahora es de 3
    pila.retornar()
    # Imprimo la pila final
    pila.imprimir()


    # Clase_cola
    class clase_cola:
        # Variable que contendra nuestra clase_cola
        def __init__(self) -> None:
            self.cola = []
        
        def agregar(self, value):
            self.cola.append(value)
            print(self.cola)

        def eliminar(self):
            self.cola.pop(0)
            print(self.cola)
            
        def retornar(self, ):
            retorno = self.cola.pop(0)
            print(f"Retorno: {(retorno)}")

        def imprimir(self):
            print(f"Cola final {self.cola}")

    print("-----Cola-----")
    # Guardo la clase "clase_cola" en una variable
    cola = clase_cola()
    # Agrego
    cola.agregar(1)
    cola.agregar(2)
    cola.agregar(3)
    cola.agregar(4)
    cola.agregar(5)
    # Elimino el 1 (index 0), la cola ahora es de 4 (index 0,1,2,3)
    cola.eliminar()
    # Retorno el 2 (index 0), y la cola ahora es: 3, 4, 5
    cola.retornar()
    # Imprimo la cola final
    cola.imprimir()

    
            
if __name__=="__main__":
    main()
