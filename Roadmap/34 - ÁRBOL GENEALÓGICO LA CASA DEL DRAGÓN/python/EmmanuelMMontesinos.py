"""
/*
 * EJERCICIO:
 * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026! 
 * ¿Alguien se entera de todas las relaciones de parentesco
 * entre personajes que aparecen en la saga?
 * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 * Requisitos:
 * 1. Estará formado por personas con las siguientes propiedades:
 *    - Identificador único (obligatorio)
 *    - Nombre (obligatorio)
 *    - Pareja (opcional)
 *    - Hijos (opcional)
 * 2. Una persona sólo puede tener una pareja (para simplificarlo).
 * 3. Las relaciones deben validarse dentro de lo posible.
 *    Ejemplo: Un hijo no puede tener tres padres.
 * Acciones:
 * 1. Crea un programa que permita crear y modificar el árbol.
 *    - Añadir y eliminar personas
 *    - Modificar pareja e hijos
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 * 
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
 */
"""

class Personas:
    numero_personas = 0
    arbol = {}
    
    def __init__(self,nombre) -> None:
        Personas.numero_personas += 1
        self.id = Personas.numero_personas
        self.nombre = nombre.lower()
        self.pareja = None
        self.padres = [None,None]
        self.hijos = []
        self.estado = True
        self.asesino = None
        Personas.arbol[self.nombre] = self

    def mostrar_arbol(self):
        print("---Arbol Moure---")
        for num, personas in enumerate(Personas.arbol.values()):
            print(f"{num} - {personas.nombre}")

    def matar_persona(self,asesino=None):
        if asesino:
            self.asesino = asesino.nombre
        else:
            self.asesino = "forma natural"

        del Personas.arbol[self.nombre]
        self.estado = False
        print(f"{self.nombre} ha muerto por {self.asesino}")

    def mostrar_datos(self):
        if self.estado:
            print("Vivo/a")
        else:
            print(f"Muerto/a por {self.asesino}")
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        if self.pareja:
            print(f"Pareja: {self.pareja.nombre}")
        for padre in self.padres:
            if padre != None:
                print(f"Progenitor: {padre.nombre}")
        if self.hijos:
            print("Hijos:")
            for hijo in self.hijos:
                print(f"{hijo.nombre}")
        print()
    def mostrar_pareja(self):
        print(f"{self.nombre} esta actualmente casado/a con {self.pareja.nombre}")
    
    def tener_hijos(self,hijo):
        if hijo.padres[0] == None:
            hijo.padres[0] = self
            self.hijos.append(hijo)
        elif hijo.padres[1] == None:
            hijo.padres[1] = self
            self.hijos.append(hijo)


    def cambiar_pareja(self,pareja,ambos=False):
        self.pareja = None
        self.pareja = pareja
        if ambos:
            pareja.cambiar_pareja(self)

        print(f"Cambio realizado: {self.nombre} casado/a con {self.pareja.nombre}")

    def casamiento(self,pareja):
        if self.pareja and pareja.pareja:
            self.mostrar_pareja()
            pareja.mostrar_pareja()
            cambio = input(f"Quiere cambiar la pareja a {pareja.nombre}\n1-Si 2-No: ")
            match cambio:
                case "1":
                    self.cambiar_pareja(pareja,ambos=True)

                case "2":
                    print("Cambio cancelado")
        elif self.pareja or pareja.pareja:
            if self.pareja:
                self.mostrar_pareja()
                cambio = input(f"Quiere cambiar la pareja a {pareja.nombre}\n1-Si 2-No: ")
                match cambio:
                    case "1":
                        self.cambiar_pareja(pareja)

                    case "2":
                        print("Cambio cancelado")
            else:
                pareja.mostrar_pareja()
                cambio = input(f"Quiere cambiar la pareja a {self.nombre}\n1-Si 2-No: ")
                match cambio:
                    case "1":
                        self.cambiar_pareja(pareja,ambos=True)

                    case "2":
                        print("Cambio cancelado")
        else:
            self.cambiar_pareja(pareja,ambos=True)

class Consola:
    def bucle(self):
        salir = False
        while not salir:
            print("1-Añadir pj 2-Añadir pareja a pj 3-Añadir hijo a pj 4- Matar pj 5-Mostrar_datos 6-Salir:")
            seleccion = input("")
            match seleccion:
                case "1":
                    self.add_pj()
                    
                case "2":
                    self.add_pareja()
                    
                case "3":
                    self.add_hijo()
                    
                case "4":
                    self.matar()

                case "5":
                    self.mostrar_datos()
                    
                case "6":
                    salir = True

    def mostrar_datos(self):
        self.mostrar_arbol()
        try:
            seleccion = input("Nombre: ")
            nombre = Personas.arbol[seleccion.lower()]
            nombre.mostrar_datos()
        except Exception as e:
            print(f"Error: {e}")
                
    def add_pj(self):
        nombre = input("Nombre: ")
        pj = Personas(nombre.lower())
        print(f"{pj.nombre} añadido al arbol")
    
    def add_pareja(self):
        self.mostrar_arbol()
        try:
            seleccion_1 = input("Nombre del primer pj: ")
            pj_1 = Personas.arbol[seleccion_1.lower()]

            seleccion_2 = input("Nombre del segundo pj: ")
            pj_2 = Personas.arbol[seleccion_2.lower()]

            pj_1.casamiento(pj_2)
        except Exception as e:
            print(f"Error: {e}")

    def add_hijo(self):
        self.mostrar_arbol()
        try:
            padre = input("Nombre del padre: ")
            padre = Personas.arbol[padre.lower()]

            hijo = input("Nombre del hijo: ")
            hijo = Personas.arbol[hijo.lower()]
        except Exception as e:
            print(f"Error: {e}")
    def matar(self):
        self.mostrar_arbol()
        try:
            victima = input("Nombre víctima")
            victima = Personas.arbol[victima.lower()]
            asesino = input("Nombre asesino(enter si es por forma natural)")
            if asesino:
                victima.matar_persona(asesino=asesino)
            else:
                victima.matar_persona()
        except Exception as e:
            print(f"Error: {e}")

    def mostrar_arbol(self):
        Personas.mostrar_arbol(Personas)

# Pruebas

# Creación de personajes
ned = Personas("Ned Stark")
catelyn = Personas("Catelyn Stark")
jon = Personas("Jon Snow")
arya = Personas("Arya Stark")
sansa = Personas("Sansa Stark")
bran = Personas("Bran Stark")
robb = Personas("Robb Stark")
rickon = Personas("Rickon Stark")
tyrion = Personas("Tyrion Lannister")
daenerys = Personas("Daenerys Targaryen")

# Matrimonios
daenerys.casamiento(tyrion)
ned.casamiento(catelyn)

# Hijos
catelyn.tener_hijos(arya)
catelyn.tener_hijos(sansa)
ned.tener_hijos(robb)
ned.tener_hijos(bran)
ned.tener_hijos(rickon)

# Eliminar personajes
ned.matar_persona(tyrion)
catelyn.matar_persona(daenerys)

# Mostrar datos
ned.mostrar_datos()
catelyn.mostrar_datos()
arya.mostrar_datos()
jon.mostrar_datos()
sansa.mostrar_datos()
bran.mostrar_datos()
robb.mostrar_datos()
rickon.mostrar_datos()
tyrion.mostrar_datos()
daenerys.mostrar_datos()

# Mostrar Arbol actual
Personas.mostrar_arbol(Personas)

consola = Consola()
consola.bucle()