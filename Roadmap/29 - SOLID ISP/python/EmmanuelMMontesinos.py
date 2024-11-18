"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 */
"""
'Sin Aplicar'
class Caja:
    def __init__(self,nombre) -> None:
        self.estado = False
        self.password = ""
        self.alarma = False
        self.intentos = 0
        self.nombre = nombre
    
    def abrir(self):
        if self.estado != True:
            self.estado = True
        else:
            print(f"{self.nombre} ya esta abierta")
        self.mostrar_estado()
    
    def cerrar(self):
        if self.estado != False:
            self.estado = False
        else:
            print(f"{self.nombre} ya esta cerrada")
            return
        self.mostrar_estado()

    def cambiar_password(self,old,new):
        if self.verificar(password=""):
            if old.lower() == self.password.lower():
                self.password = new
            else:
                self.intentos += 1
                print(f"La contraseña de {self.nombre} no coincide con la proporcionada: nivel de alerta {self.intentos}/3")
            if self.intentos >= 3:
                self.alarma = True
        else:
            print(f"{self.nombre} esta bloqueado")


    def verificar(self,password):
        if self.alarma == False:
            if self.password.lower() == password.lower():
                return True
        else:
            return False
        
    def mostrar_estado(self):
        if self.estado:
            print(f"{self.nombre} esta abierta")
        else:
            print(f"{self.nombre} esta cerrada")

class CajaCarton(Caja):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
    
    def abrir(self):
        if self.verificar():
            super().abrir()
    
    def cerrar(self):
        super().cerrar()
    
    def cambiar_password(self, old, new):
        pass

    def mostrar_estado(self):
        super().mostrar_estado()
    
    def verificar(self):
        return True
    
class CajaFuerte(Caja):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
    
    def abrir(self,password):
        if self.verificar(password):
            super().abrir()
        else:
            print(f"{password} no es la contraseña correcta")
    
    def cerrar(self):
        super().cerrar()
    
    def cambiar_password(self, old, new):
        super().cambiar_password(old, new)

    def mostrar_estado(self):
        super().mostrar_estado()
    
    def verificar(self,password):
        return super().verificar(password)

mi_caja_carton = CajaCarton("Caja de Carton")
mi_caja_fuerte = CajaFuerte("Caja Fuerte")

mi_caja_carton.abrir()
mi_caja_fuerte.abrir("")
print()

mi_caja_carton.cerrar()
mi_caja_fuerte.cerrar()
print()

mi_caja_carton.cambiar_password("","1234")
mi_caja_fuerte.cambiar_password("","1234")

print()

mi_caja_carton.abrir()
mi_caja_fuerte.abrir("4321")
print()

mi_caja_carton.cerrar()
mi_caja_fuerte.cerrar()

'Aplicado'
class CajaGenerica:
    def __init__(self,nombre) -> None:
        self.estado = False
        self.nombre = nombre
    
    def abrir(self):
        if self.estado != True:
            self.estado = True
        else:
            print(f"{self.nombre} ya esta abierta")
        self.mostrar_estado()
    
    def cerrar(self):
        if self.estado != False:
            self.estado = False
        else:
            print(f"{self.nombre} ya esta cerrada")
            return
        self.mostrar_estado()
        
    def mostrar_estado(self):
        if self.estado:
            print(f"{self.nombre} esta abierta")
        else:
            print(f"{self.nombre} esta cerrada")

class CajaCarton2(CajaGenerica):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

class CajaFuerte2(CajaGenerica):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.password = ""
        self.alarma = False
        self.intentos = 0
    
    def abrir(self,password):
        if self.verificar(password):
            super().abrir()
        else:
            print(f"{password} no es la contraseña correcta")
    
    def cambiar_password(self,old,new):
        if self.verificar(password=""):
            if old.lower() == self.password.lower():
                self.password = new
            else:
                self.intentos += 1
                print(f"La contraseña de {self.nombre} no coincide con la proporcionada: nivel de alerta {self.intentos}/3")
            if self.intentos >= 3:
                self.alarma = True
        else:
            print(f"{self.nombre} esta bloqueado")

    def verificar(self,password):
        if self.alarma == False:
            if self.password.lower() == password.lower():
                return True
        else:
            return False
        
# Prueba
mi_caja_carton2 = CajaCarton2("Caja de Carton 2")
mi_caja_fuerte2 = CajaFuerte2("Caja Fuerte 2")

mi_caja_carton2.abrir()
mi_caja_fuerte2.abrir("")

mi_caja_carton2.cerrar()
mi_caja_fuerte2.cerrar()

mi_caja_carton2.abrir()
mi_caja_fuerte2.abrir("")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
"""
class ImpresoraBase:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
    def imprimir_bn(self,documento):
        print(f"Imprimiendo desde {self.nombre} en blanco y negro: {documento}\n")

class ImpresoraColor(ImpresoraBase):
    def imprimir_cl(self,documento):
        print(f"Imprimiendo desde {self.nombre} en color: {documento}\n")

class Multifuncion(ImpresoraColor):
    def escanear(self,documento):
        print(f"Escaneando desde {self.nombre}: {documento}\n")

    def enviar_fax(self,documento):
        print(f"Enviando Fax desde {self.nombre}: {documento}\n")

# Prueba
def test_impresoras(documento):
    base = ImpresoraBase("Base")
    color = ImpresoraColor("Color")
    multi = Multifuncion("Multi")

    base.imprimir_bn(documento)

    color.imprimir_bn(documento)
    color.imprimir_cl(documento)

    multi.imprimir_bn(documento)
    multi.imprimir_cl(documento)
    multi.escanear(documento)
    multi.enviar_fax(documento)

test_impresoras("Curriculum Vitae")