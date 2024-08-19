
#Arrays  o Tuplas
tupla = tuple(range(1,10))
print(tupla)
#No permite ninguna operacion por defecto, se pueden realizar pero su funcion no es esa

#Listas
lista = list(range(1,10,2))
lista.append(15)
lista.insert(-3, 23)
lista.pop(0)
print(lista)
lista.sort()
print(lista)

#Sets
set1 = {11,10,5,3,2,5}
set1.add(15)
set1.remove(3)
set1.pop()
print(set1)

#Diccionarios
diccionario = {'nombre': 'd0ubt0'}
diccionario['edad'] = 20
print(diccionario['edad'])
diccionario['lenguaje'] = 'Python'
del diccionario['lenguaje']
print(diccionario)

#EXTRA
import re
class Persona:
    def __init__(self,nombre:str,numero:str) -> None:
        self.nombre:str = nombre
        self.numero:str = numero

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}  Numero: {self.numero}'
    
class Agenda:
    def __init__(self) -> None:
        self.lista_personas :list[Persona] = []
        self.patron = r'^\d{1,11}$'
        print('Agenda creada')
        self.interfaz()

    def _crear_persona(self):
        nombre = input('Nombre de la persona: ')
        numero = self._preguntar_numero()
        return Persona(nombre,numero)
    
    def mostrar_personas(self):
        for i in self.lista_personas:
            print(i)


    def agregar_persona(self):
        persona = self._crear_persona()
        print('Persona Agregada')
        print(persona)
        self.lista_personas.append(persona)
        
    
    def _buscar_por_numero(self,numero:str):
        for i ,persona in enumerate(self.lista_personas):
            if persona.numero == numero:
                return i
            
    def _preguntar_numero(self):
        numero = input('Numero de telefono: ')
        while not bool(re.match(self.patron,numero)):
            print('Numero de telefono invalido.Intente de nuevo')
            numero = input('Numero de telefono: ')
        return numero
            
    def actualizar_persona(self,numero:str):
        index = self._buscar_por_numero(numero)
        if index == None:
            print('Persona no encontrada')
        else:
            print('Actualice los datos de ',self.lista_personas[index])
            persona = self._crear_persona()
            self.lista_personas[index] = persona
            print('Persona actualizada')

    def eliminar_persona(self,numero:str):
        index = self._buscar_por_numero(numero)
        if index == None:
            print('Persona no encontrada')
        else:
            del self.lista_personas[index]
            print('Persona eliminada')

    def interfaz(self):
        while True:
            print()
            accion  = input('Que accion quieres realizar: Agregar[0] , Eliminar[1] , Actualizar[2] , Eliminar[3] , Mostrar Agenda[4], Salir[5]\nAccion: ')
            if accion == '0':
                print('Agregar persona')
                self.agregar_persona()
            elif accion == '1':
                print('Eliminar persona por numero')
                n = self._preguntar_numero()
                self.eliminar_persona(n)
            elif accion == '2':
                print('Actualizar persona por numero')
                n = self._preguntar_numero()
                self.actualizar_persona(n)
            elif accion == '3':
                print('Actualizar persona por numero')
                n = self._preguntar_numero()
                self.eliminar_persona(n)
            elif accion == '4':
                print('Agenda completa')
                self.mostrar_personas()
            else:
                break
                

agenda = Agenda()
        



