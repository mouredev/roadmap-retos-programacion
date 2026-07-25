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
import uuid

#from graphviz import Digraph


class Persona:
    def __init__(self, nombre, apellido):
        self.id = str(uuid.uuid4())  # Generación automática de ID único
        self.nombre = nombre
        self.apellido = apellido
        self.parejas = [] # Lista de parejas
        self.hijos = {}    # Diccionario de listas de hijos por pareja
    
    def __str__(self):
        # Devuelve el nombre de la persona, su id, el nombre de sus parejas y sus hijos, sólo si tiene pareja o hijos
        nombre_parejas = ", ".join([persona.nombre for persona in self.parejas])
        hijos_str = {pareja.nombre: ", ".join([hijo.nombre for hijo in hijos]) for pareja, hijos in self.hijos.items()}
        nombre_hijos = "\n".join([f"{pareja}: {hijos}" for pareja, hijos in hijos_str.items()]) if hijos_str else "Ninguno"
        if self.parejas and self.hijos:
            return f"{self.nombre} {self.apellido}\n [Hijos=> {nombre_hijos}]\n"
        else:
            return " "
        
                
class ArbolGenealogico:
    def __init__(self):
        self.personas = {}
    
    def crear_persona(self, nombre, apellido):
        persona = Persona(nombre, apellido)
        self.personas[persona.id] = persona
        return persona.id
        
    def buscar_persona(self, id):
            return self.personas.get(id, None)
    
    def agregar_pareja(self, id_persona, id_pareja):
        if id_persona == id_pareja:
            print("Una persona no puede ser su propia pareja.")
            return
        
        persona = self.buscar_persona(id_persona)
        pareja = self.buscar_persona(id_pareja)

        if persona and pareja:
            if id_pareja in persona.parejas or id_persona in pareja.parejas:
                print("Estas personas ya están vinculadas como pareja.")
                return
            
            persona.parejas.append(pareja)
            pareja.parejas.append(persona)
            # Inicializa la lista de hijos para esta pareja
            persona.hijos[pareja] = []
            pareja.hijos[persona] = []
        else:
            print("Persona no encontrada")
    
    def agregar_hijo(self, id_padre, id_madre, id_hijo):
        padre = self.buscar_persona(id_padre)
        madre = self.buscar_persona(id_madre)
        hijo = self.buscar_persona(id_hijo)
        
        if padre and madre and hijo:
            if madre in padre.hijos:
                padre.hijos[madre].append(hijo)
            if padre in madre.hijos:
                madre.hijos[padre].append(hijo)
        else:
            print("Padre, madre o hijo no encontrado")
    #Formato de impresión de árbol con /tab para tabular los niveles/generaciones        
    def imprimir_arbol(self):
        set_visitados = set()

        def mostrar_persona(persona: Persona, nivel=0):
            identacion = "\t" * nivel
            if persona.id in set_visitados:
                return
            else:                              
                print(f"{identacion} - {persona.nombre} {persona.apellido}")
                set_visitados.add(persona.id)
                if persona.parejas:
                    for pareja in persona.parejas:
                        print(f"{identacion} Pareja: {pareja.nombre} {pareja.apellido}")
                        for hijo in persona.hijos.get(pareja, []):
                            mostrar_persona(hijo, nivel + 1)

        for persona in self.personas.values():
            mostrar_persona(persona)
            
    def buscar_por_nombre(self, nombre):
        return [persona for persona in self.personas.values() if persona.nombre.lower() == nombre.lower()]

    
    def eliminar_persona(self, id):
        persona = self.buscar_persona(id)
        if persona:
            # Desvincula las parejas
            for pareja in persona.parejas:
                pareja.parejas.remove(persona)
                if persona in pareja.hijos:
                    del pareja.hijos[persona]
            
            # Elimina a la persona de los hijos de cualquier padre
            for padre in self.personas.values():
                for pareja, hijos in padre.hijos.items():
                    if persona in hijos:
                        hijos.remove(persona)
            
            # Elimina a la persona
            del self.personas[id]
            print(f"Persona {id} eliminada.")
        else:
            print("Persona no encontrada")
    
    def generar_arbol_grafico(self):
        dot = Digraph(comment='Árbol Genealógico')
        
        # Añadir nodos
        for persona in self.personas.values():
            dot.node(persona.id, f'{persona.nombre} {persona.apellido}')
        
        # Añadir conexiones (flechas) entre padres e hijos
        for persona in self.personas.values():
            for pareja, hijos in persona.hijos.items():
                for hijo in hijos:
                    dot.edge(persona.id, hijo.id, color='blue')  # Conectar padre con hijo
        
        dot.render('arbol_genealogico_hijos', format='png', cleanup=True)
        print("Árbol genealógico generado como 'arbol_genealogico_hijos.png'.")

        # Añadir flecha para cada pareja
        ya_conectado = set()
        for persona in self.personas.values():
            for pareja in persona.parejas:
                if (persona.id, pareja.id) not in ya_conectado and (pareja.id, persona.id) not in ya_conectado:
                    dot.edge(persona.id, pareja.id, color='red', style='dashed')  # Conectar parejas
                    ya_conectado.add((persona.id, pareja.id))                    
        
        dot.render('arbol_genealogico_relaciones', format='png', cleanup=True)
        print("Árbol genealógico generado como 'arbol_genealogico_relaciones.png'.")
#Crear arbol genealogico
arbol = ArbolGenealogico()


# Crear personas

#Baratheon - Targaryan
jocelyn = arbol.crear_persona("Jocelyn", "Baratheon")
aemon = arbol.crear_persona("Aemon", "Targaryan")

#Targaryaen - Velaryon
corlys = arbol.crear_persona("Corlys", "Velaryon")
rhaenys = arbol.crear_persona("Rhaenys", "Targaryen")

arbol.agregar_pareja(jocelyn, aemon)
arbol.agregar_hijo(jocelyn, aemon, rhaenys)
arbol.agregar_pareja(corlys, rhaenys)

laena = arbol.crear_persona("Laena", "Velaryon")
laenor = arbol.crear_persona("Laenor", "Velaryon")

arbol.agregar_hijo(corlys, rhaenys, laena)
arbol.agregar_hijo(corlys, rhaenys, laenor)

#Targaryen - Arryn
daella = arbol.crear_persona("Daella", "Targaryen")
rodrik = arbol.crear_persona("Rodrik", "Arryn")

#Targaryen - Targaryen
baelon = arbol.crear_persona("Baelon I", "Targaryen")
alyssa = arbol.crear_persona("Alyssa", "Targaryen")

#Targaryen - Hihgtower
aemma = arbol.crear_persona("Aemma", "Arryn")
viserys_i = arbol.crear_persona("Viserys I", "Targaryen")
alicent = arbol.crear_persona("Alicent", "Hightower")

arbol.agregar_pareja(daella, rodrik)
arbol.agregar_hijo(daella, rodrik, aemma)
arbol.agregar_pareja(baelon, alyssa)
arbol.agregar_hijo(baelon, alyssa, viserys_i)

arbol.agregar_pareja(viserys_i, aemma)
rhaenyra = arbol.crear_persona("Rhaenyra", "Targaryen")

arbol.agregar_hijo(viserys_i, aemma, rhaenyra)


arbol.agregar_pareja(viserys_i, alicent)
aegon_ii = arbol.crear_persona("Aegon II", "Targaryen")
helaena = arbol.crear_persona("Helaena", "Targaryen")
aemond = arbol.crear_persona("Aemond", "Targaryen")
daeron = arbol.crear_persona("Daeron", "Targaryen")

arbol.agregar_hijo(viserys_i, alicent, aegon_ii)
arbol.agregar_hijo(viserys_i, alicent, helaena)
arbol.agregar_hijo(viserys_i, alicent, aemond)
arbol.agregar_hijo(viserys_i, alicent, daeron)

#Daemon
daemon = arbol.crear_persona("Daemon", "Targaryen")
arbol.agregar_pareja(daemon, laena)

baela = arbol.crear_persona("Baela", "Targaryen")
rhaena = arbol.crear_persona("Rhaena", "Targaryen")

arbol.agregar_hijo(daemon, laena, baela)
arbol.agregar_hijo(daemon, laena, rhaena)

#Rhaenyra
arbol.agregar_pareja(rhaenyra, laenor)

jacaerys = arbol.crear_persona("Jacaerys", "Velaryon")
lucerys = arbol.crear_persona("Lucerys", "Velaryon")
joffrey = arbol.crear_persona("Joffrey", "Velaryon")

arbol.agregar_hijo(rhaenyra, laenor, jacaerys)
arbol.agregar_hijo(rhaenyra, laenor, lucerys)
arbol.agregar_hijo(rhaenyra, laenor, joffrey)

#Rhaenyra - Daemon
arbol.agregar_pareja(rhaenyra, daemon)

viserys_ii = arbol.crear_persona("Viserys II", "Targaryen")
visenya = arbol.crear_persona("Visenya", "Targaryen")
aegon_iii = arbol.crear_persona("Aegon III", "Targaryen")

arbol.agregar_hijo(rhaenyra, daemon, viserys_ii)
arbol.agregar_hijo(rhaenyra, daemon, visenya)
arbol.agregar_hijo(rhaenyra, daemon, aegon_iii)

#Aegon II - Helaena
arbol.agregar_pareja(aegon_ii, helaena)

jaehaera = arbol.crear_persona("Jaehaera", "Targaryen")
jaehaerys = arbol.crear_persona("Jaehaerys", "Targaryen")
maelor = arbol.crear_persona("Maelor", "Targaryen")

arbol.agregar_hijo(aegon_ii, helaena, jaehaera)
arbol.agregar_hijo(aegon_ii, helaena, jaehaerys)
arbol.agregar_hijo(aegon_ii, helaena, maelor)

#Muestra el arbol
arbol.imprimir_arbol()

#Imprime el arbol en png
#arbol.generar_arbol_grafico()
