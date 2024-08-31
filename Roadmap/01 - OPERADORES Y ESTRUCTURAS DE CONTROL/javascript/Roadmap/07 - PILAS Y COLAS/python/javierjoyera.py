class Pila:
    def __init__(self): 
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "La pila está vacía"
    def is_empty(self):
        return len (self.items) == 0
    def is_the_top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "La pila está vacía"
    
class Cola:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "La cola está vacía"
    def is_empty(self):
        return len(self.items) == 0
    

class NavegadorWeb:
    def __init__(self):
        self.historial = Pila()
        self.adelante = Pila()

    def ver_pagina(self, pagina):
        print("Estás viendo la página: %s" % pagina)
        self.historial.push(pagina)
        self.adelante = Pila()
    
    def retroceder(self):
        if self.historial.is_empty():
            print("No hay páginas para retroceder")
        else:
            pagina = self.historial.pop()
            self.adelante.push(pagina)
            if self.historial.is_empty():
                print("Estás en la página de inicio")
            else:
                print("Estás viendo la página: %s" % self.historial.is_the_top())

    def ir_adelante(self):
        if self.adelante.is_empty():
            print("No hay páginas hacia adelante")
        else:
            pagina = self.adelante.pop()
            self.historial.push(pagina)
            print("Estás viendo la página: %s" % pagina)



navegador = NavegadorWeb()
navegador.ver_pagina("google.com")
navegador.ver_pagina("youtube.com")
navegador.ver_pagina("retosdeprogramacion.com")

navegador.retroceder()
navegador.retroceder()
navegador.retroceder()
navegador.retroceder()
navegador.ir_adelante()
navegador.ir_adelante()

class Impresora:
    def __init__(self):
        self.cola_impresion = Cola()
    
    def agregar_documento(self, documento):
        self.cola_impresion.enqueue(documento)
        print("Documento %s agregado a la cola de impresión" % documento)
    
    def imprimir(self):
        if not self.cola_impresion.is_empty():
            documento = self.cola_impresion.dequeue()
            print("Imprimiendo documento: %s" % documento)
        else:
            print("No hay documentos en cola.")

# Ejemplo de uso
impresora = Impresora()
impresora.agregar_documento("Documento1.pdf")
impresora.agregar_documento("Foto_12.png")
impresora.imprimir()
impresora.imprimir()


