from abc import ABC, abstractmethod


# El principio Solid de Segregacion de Interfaces comprende que una interfaz es un contrato que se debe cumplir por lo que una clase que herede de la interfaz no puede omitir sus metodos
# o levantar excepciones/errores en su implementacion

#Implementacion incorrecta
class AnimalesWrong (ABC):
    
    @abstractmethod
    def caminar(self):
        pass
    @abstractmethod
    def comer(self):
        pass
    
class PerroWrong (AnimalesWrong):
    def __init__(self, name):
      self.name = name
    
    def caminar(self):
        print (f"{self.name} esta Caminando")
    
    def comer(self):
        print (f"{self.name} esta Comiendo")

class PezWrong (AnimalesWrong):
    
    def __init__(self, especie):
      self.especie = especie
    
    def caminar(self):
        raise Exception('Los Peces no caminan')
    
    def comer(self):
        print(f"{self.especie} esta Comiendo")
    
    def nadar(self):
        print(f"{self.especie} esta Nadando")
        
        
#Implementacion correcta

class funcionesGenerales(ABC):
    
    @abstractmethod
    def alimentarse():
        pass

class funcionesTerrestres(ABC):
    
    @abstractmethod
    def caminar(self):
        pass

class funcionesAcuaticas(ABC):
    
    @abstractmethod
    def nadar(self):
        pass

class Perro(funcionesGenerales,funcionesTerrestres):
    def __init__(self, name):
      self.name = name
    
    def caminar(self):
        print (f"{self.name} esta Caminando")
    
    def alimentarse(self):
        print (f"{self.name} esta Comiendo")

class Pez(funcionesGenerales,funcionesAcuaticas):
    
    def __init__(self, especie):
      self.especie = especie
    
    def nadar(self):
        print (f"{self.especie} esta Nadando")
    
    def alimentarse(self):
        print(f"{self.especie} esta Comiendo")
        
class Cocodrilo(funcionesGenerales,funcionesAcuaticas,funcionesTerrestres):
    
    def __init__(self, especie):
      self.especie = especie
    
    def nadar(self):
        print (f"{self.especie} esta Nadando")
    
    def alimentarse(self):
        print(f"{self.especie} esta Comiendo")
        
    def caminar(self):
        print (f"{self.especie} esta Caminando")
        
        
# Ejercicio Extra Gestor de Impresoras


class funcionesBasicas(ABC):
    
    def imprimirBYN(self):
        pass

class funcionesAvanzadas(ABC):
    
    def imprimirAColor(self):
        pass
    

class funcionesExtra(ABC):
    
    def enviarFax(self):
        pass
    
    def escanearDocumento(self):
        pass
    

class impresoraBasica(funcionesBasicas):
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def imprimirBYN(self,documento):
        print (f'Marca: {self.marca} Modelo: {self.modelo}')
        print(f"Imprimiendo {documento} a Blanco y Negro")
    
class impresoraModerna(funcionesAvanzadas):
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def imprimirAColor(self,documento):
        print (f'Marca: {self.marca} Modelo: {self.modelo}')
        print(f"Imprimiendo {documento} a Color")

class impresoraMultifuncional(funcionesBasicas,funcionesAvanzadas,funcionesExtra):
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def imprimirBYN(self,documento):
        print (f'Marca: {self.marca} Modelo: {self.modelo}')
        print(f"Imprimiendo {documento} a Blanco y Negro")
        
    def imprimirAColor(self,documento):
        print (f'Marca: {self.marca} Modelo: {self.modelo}')
        print(f"Imprimiendo {documento} a Color")
        
    def escanearDocumento(self, path):
        print (f'Marca: {self.marca} Modelo: {self.modelo}')
        print(f"Escaneando documento hacia {path}")
    
    def enviarFax(self, documento):
        print (f'Marca: {self.marca} Modelo: {self.modelo}')
        print(f"Enviando {documento} en Fax")



print('\n')
impresora1 = impresoraBasica('Epson', 'Ecotank M1120')
impresora1.imprimirBYN('HOLA MUNDO.docx')


print('\n')
impresora2 = impresoraModerna('Epson', 'Ecotank L121')
impresora2.imprimirAColor('HOLA MUNDO.docx')


print('\n')
impresora3 = impresoraMultifuncional('Epson', 'Ecotank L3560')
impresora3.imprimirBYN('HOLA MUNDO.docx')   
impresora3.imprimirAColor('HOLA MUNDO.docx')   
impresora3.escanearDocumento('C:/users/usuario/documents/HOLA_MUNDO.txt')   
impresora3.enviarFax('HOLA MUNDO.docx')   