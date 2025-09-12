"""
EJERCICIO:
*Explora el concepto de clase y crea un ejemplo que implemente un 
inicializador,

*atributos y una funcion que los imprima (teniendo en 
cuenta las posibilidades de tu lenguaje).

*Una vez implementada, creala, establece sus parametros, modificalos e
imprimelos utilizando una funcion.
.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
DIFICULTAD EXTRA (opcional):
- Implementa dos clases que representen las estructuras de Pila y 
Cola (estudiadas en el ejercicio numero 7 de la ruta de estudio)
- Deben poer inicializarse y disponer de operaciones para añadir, 
eliminar, retornar el número de elementos e imprimir todo su 
contenido.
"""

#creacion del molde de una persona promedio
class persona:

    #Datos personales
    def __init__(self, nombre,edad,direccion,afp,prevision): #se le atribuyen parametros como sus datos personales
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.afp = afp
        self.prevision = prevision
        
        self.red_social = [] #.-.-.- Lista la cual contendra redes sociales sea por nombre o url  .-.-.-
        self.contador_turno = 5 #Tiene 5 puntos de turno, cada accion le quitara uno y al llegar a 0 termina el turno
    
    #Mostrar datos por pantalla
    def mostrar_info(self):
        print(f'Nombre:{self.nombre} \nEdad:{self.edad} \nDireccion:{self.direccion}')
        print(f'Afp:{self.afp} \nprevision:{self.prevision}')

    #Mover al personaje
    def moverse(self, pasos):
        self.pasos = pasos
        if pasos < 0:
            print('No puede dar pasos negativos')
        elif pasos == 1:
            self.contador_turno -= 1
            print(f'{self.nombre} dio un paso...')
        else:
            self.contador_turno -= pasos
            print(f'{self.nombre} dio {pasos} pasos!')

    #El personaje canta        
    def cantar (self, cancion, banda):
        self.cancion = cancion
        print(f'{self.nombre} esta cantando {cancion} de {banda}! Como mola!')

    #Saltito
    def saltar(self, salto):
        self.salto = salto
        print(f'{self.nombre} ha dado {salto} salto/s ')

#Se crea el objeto (instanciar la clase)    
usuario = persona('pepito', 24, 'Calle maipu', 'vital', 'Isapre') 
usuario.mostrar_info() #datos personales

#Bucle que se rompe al terminar los turnos (o quedar en negativo)
while 1:
    if usuario.contador_turno <= 0:
        print('Fin del turno')
        break

    print(f'Seleccione su accion:')
    print(f'mover.-.- \ncantar.-.- \nsaltar.-.- \nfin del turno.-.-.-')

    alternativa = input('->')
    if alternativa == 'fin del turno':
        break
    elif alternativa == 'mover':
        usuario.moverse(int(input('Cuantos pasos?: ')))
        print(f'contador de turno: ,.,.{usuario.contador_turno},.,.')
    elif alternativa == 'cantar':
        usuario.cantar(input('Cancion:'), input('Banda:'))
        print(f'contador de turno: ,.,.{usuario.contador_turno},.,.')
    elif alternativa == 'saltar':
        usuario.saltar(input('Cuantos saltos? :'))
        print(f'contador de turno: ,.,.{usuario.contador_turno},.,.')

#Extra
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