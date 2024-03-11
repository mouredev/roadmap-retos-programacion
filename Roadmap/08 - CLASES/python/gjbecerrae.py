class helloPython:
   
    def __init__(self, name, lastName): 
        self.name = name #instance variable unique to each instance
        self.lastname = lastName

    def modParam(self, nameMod, lastNameMod):
        self.name = nameMod
        self.lastname = lastNameMod

    def printAtt(self): # class method
        print(f'{self.name} {self.lastname}')

hola = helloPython('Gabriel', 'Becerra')
#hola.printAtt()
#hola.modParam('Jaime', 'Eslava')
#hola.printAtt()

#### Dificultad Extra ######
class Pilas:

    def __init__(self, elementos:list) -> None:
        self.elementos = elementos

    def adicionarElemento(self, elementoExtra):
        self.elementos.append(elementoExtra)

    def eliminarElemento(self):
        self.elementos.pop()

    def numeroElementos(self):
        return len(self.elementos)

    def imprimirElementos(self):
        for i in self.elementos: print(i)

class Colas:

    def __init__(self, elementos) -> None:
        self.elementos = elementos

    def adicionarElemento(self, elementoExtra):
        self.elementos.append(elementoExtra)

    def eliminarElemento(self):
        self.elementos.pop(0)

    def numeroElementos(self):
        return len(self.elementos)

    def imprimirElementos(self):
        for i in self.elementos: print(i)

print('Pilas-------------------------\n')
miPila = Pilas(['goku'])
miPila.imprimirElementos()
miPila.adicionarElemento('Gohan')
miPila.adicionarElemento('Picoro')
numero = miPila.numeroElementos()
print(numero)
miPila.imprimirElementos()
miPila.eliminarElemento()
miPila.imprimirElementos()

print('\n\Colas-------------------------\n')
miCola = Colas(['goku'])
miCola.imprimirElementos()
miCola.adicionarElemento('Gohan')
miCola.adicionarElemento('Picoro')
numero = miCola.numeroElementos()
print(numero)
miCola.imprimirElementos()
miCola.eliminarElemento()
miCola.imprimirElementos()