class stack:
    def __init__(self):
        self.stack = [] #se inicia como una lista vacia
    
    def push(self):
        dato = input('que desea agregar?: ')
        self.stack.append(dato) #se le agrega un valor 
        
    def pop(self):
        return self.stack.pop() #se elimina el ultimo valor agregado
    
    def view(self):
        return self.stack.copy() #retorna una copia

class queue:
    def __init__(self):
        self.queue = [] #se inicia como una lista vacia
    
    def push(self):
        self.stack.append()#incorporar valor a la cola
        
    def pop(self):
        return self.stack.remove(stack[0]) #eliminamos el primero en la cola
    
    def view(self):
        return self.stack.copy() #mostramos una copia

''' ###uso de la pila por terminal
stack = stack()
while 1:
    print('que desea hacer?\n 1.- ver\n 2.- agregar\n 3.- eliminar\n 4.- fin')
    opcion = int(input('-> '))

    if opcion == 1:
        print('pila ->', stack.view())
    elif opcion == 2:
        stack.push()
    elif opcion == 3:
        stack.pop()
    elif opcion == 4:
        print('adios.')
        break
    else:
        print('Opcion invalida.')
'''

###DIFICULTAD EXTRA###   """.-.- Incompleto, lo arreglare y completare una vez estudie mas, no he tenido tiempo esta semana :(  .-.-"""
class navegadorWeb: #Creo un objeto Navegador
    historial = []  #Historial en el que se guardaran las paginas por las que pase el usuario para despues retornar o regresar

    def __init__(self):
        pass
    
    def pagina_navegar(self, direccion):
        self.direccion = direccion
        print(f'Bienvenido a {direccion}!')
        return navegadorWeb.historial.append(direccion)   

    def pagina_anterior(self):

        return navegadorWeb.historial.pop().copy()
    
    def historial(self):
        return navegadorWeb.historial


navegador = navegadorWeb() 
print('NAVEGADOR') #titulo del navegador

while 1:
    print('1.- Navegar 2.- Pagina anterior 3.- Historial 4.-Cerrar ')
    opcion = int(input('Seleccione una accion: '))
    
    if opcion == 1:
        direccion = input('donde desea navegar?')
        navegador.pagina_navegar(direccion)
        print(navegador.historial)
    elif opcion == 2:
        navegador.pagina_anterior()
        print(navegadorWeb.historial[-1])
    elif opcion == 3:
        print(navegador.historial())
    elif opcion == 4:
        print('Que tenga buen dia')
        break
    else:
        print('Opcion no valida')
        break
    