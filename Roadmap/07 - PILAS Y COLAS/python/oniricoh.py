########################################################################
# PILA (stacks - LIFO)
# El ultimo en entrar en el ultimo en salir
########################################################################

# Con una lista:
pila = [1, 2, 3]

pila.append(4) #se agrega el elemento al final de la lista
pila.pop() #se elimina el ultimo elemento de la lista

#print(pila)

#Con una array:
stack_array = [[1,2,3],[4,5,6]]

stack_array.append([6, 7, 8])
stack_array.append([9, 10, 11])
stack_array.pop()

#print(stack_array)

########################################################################
# COLA (queue - FIFO) 
# El primero en entrar es el primero en salir
########################################################################

cola = [1, 2, 3]

cola.append(4)
cola.append(5)
cola.pop(0)

#print(cola)



########################################################################
########################################################################
# DIFICULTAD EXTRA 
########################################################################
########################################################################

#NAVEGADOR WED:

class Web:
    def __init__(self):
        self.pila = ["Introduccion", "Tutoriales", "Ejemplos", "Practicas", "Examen"]
        self.actual_pag = []
        
    def atras(self):
        if len(self.pila) > 1:
            pagina = self.pila.pop()
            self.actual_pag.append(pagina)
            print(f"Navegando a {self.pila[-1]}")
        else:
            print("No hay páginas anteriores en el historial.")

    def adelante(self):
        if self.actual_pag:
            pagina = self.actual_pag.pop(0)
            self.pila.append(pagina)
            print(f"Navegando a {self.pila[-1]}")
        else:
            print("No hay páginas siguientes en el historial.")

# Crear una instancia del navegador
navegador = Web()

# Ejemplo de uso
navegador.atras()
navegador.atras()
navegador.atras()
navegador.adelante()
navegador.atras()
navegador.atras()
navegador.atras()  


# IMPRESORA COMPARTIDA:

shared_printer = []

def enviar_documento(documento):
    shared_printer.append(documento)
    print(f"Enviando documento {documento} a la impresora compartida")

def imprimir_documento():
    if shared_printer:
        documento = shared_printer.pop(0)
        print(documento)
    else:
        print("No hay documentos en la cola") 
        

imprimir_documento()        
enviar_documento("doc1")
enviar_documento("doc4")
imprimir_documento()
imprimir_documento()
