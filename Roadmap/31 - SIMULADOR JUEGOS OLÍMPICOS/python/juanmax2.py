"""
* EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
"""

import random

# Clase eventos
class Participante:
    
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        self.participantes = {}
    
    def __eq__(self, otro : object) -> bool:
        
        if isinstance(otro, Participante):
            return self.nombre == otro.nombre and self.pais == otro.pais
        return False
    
    def __hash__(self) -> int:
        return  hash(self.nombre, self.pais)
    
class Evento:
    
    def __init__(self):
        
        self.eventos = []
        self.participantes = {}
        self.resultados = {}
        self.medallas_pais = {}
    
    def registrar_evento(self):
        evento = input("Introduce el nombre del evento deportivo: ")
        
        if evento not in self.eventos:
            self.eventos.append(evento)
            print(f"El evento {evento} registrado.")
        else:
            print("Evento ya existente")
    
    def registrar_participantes(self):
        
        if not self.eventos:
            print("No hay eventos para participar")
            return
        
        nombre = input("Introduce el nombre del participante: ")
        pais = input("Introduce el pais del participante: ")
        participante = Participante(nombre, pais)
        
        
        print("Eventos disponibles")
        for index, evento in enumerate(self.eventos):
            print(f"{index + 1} - {evento}")
        
        eleccion_evento = int(input(
            "Selecciona el número del evento para asignar al participante: "
        )) - 1
        
        if eleccion_evento >= 0 and eleccion_evento < len(self.eventos):
            evento = self.eventos[eleccion_evento]
            
            if evento in self.participantes and participante in self.participantes[evento]:
                print(f"El participante {nombre}, {pais} ya esta registrado")
            
            else:
                if evento not in self.participantes:
                    self.participantes[evento] = []
                    
                self.participantes[evento].append(participante)
                print(f"El participante {participante.nombre} registrado correctamente en evento {evento}")

        else:
            print(
                "Selección del evento erronea"
            )
        
    def simular_eventos(self):
        
        if not self.eventos:
            print("No hay eventos registrados. Por favor, registra uno primero")
            return
        
        for evento in self.eventos:
            if len(self.participantes[evento]) < 3:
                print("No hay suficientes participantes para simular el evento")
                continue
            
            participantes_evento = random.sample(self.participantes[evento], 3)
            random.shuffle(participantes_evento)
            
            oro, plata, bronce = participantes_evento
            self.resultados[evento] = [oro, plata, bronce]
            
            self.actualizar_resultados_pais(oro.pais, "oro")
            self.actualizar_resultados_pais(plata.pais, "plata")
            self.actualizar_resultados_pais(bronce.pais, "bronce")
            
            print(f"Simulación del evento: {evento}")
            print(f"Oro: {oro.nombre} ({oro.pais})")
            print(f"Plata: {plata.nombre} ({plata.pais})")
            print(f"Bronce: {bronce.nombre} ({bronce.pais})")
            
    def actualizar_resultados_pais(self, pais, medalla):
        if pais not in self.medallas_pais:
            self.medallas_pais[pais] = {
                "oro" : 0, "plata" : 0, "bronce" : 0
            }
        self.medallas_pais[pais][medalla] += 1
    
    def mostrar_informe(self):
        
        print("Informe por evento")
        
        if self.resultados:
            for evento, ganador in self.resultados.items():
                print(f"Evento: {evento}")
                print(f"Oro: {ganador[0].nombre} ({ganador[0].pais})")
                print(f"Plata: {ganador[1].nombre} ({ganador[1].pais})")
                print(f"Bronce: {ganador[2].nombre} ({ganador[2].pais})")   
        
        else:
            print(f"No hay resultados que mostrar") 
        
        if self.medallas_pais:
            print("Informe por pais")
            
            for pais, medalla in sorted(self.medallas_pais.items(), key=lambda x: (
                x[1]["oro"], x[1]["plata"], x[1]["bronce"]), reverse=True):
                
                print(f"{pais}: Oro {medalla["oro"]}, Plata: {medalla["plata"]}, Bronce: {medalla["bronce"]}")
            
            
                
 
         
# Menu de opciones

def mostrar_menu():
    print(
        """
        1. Registro de eventos.
        2. Registro de participantes.
        3. Simulación de eventos.
        4. Creación de informes.
        5. Salir del programa.
        """
        )

# Seleccionar opción

def seleccionar_opcion():
    
    opcion = int(input("Selecciona la opción que quieres ejecutar: "))
    return opcion


evento = Evento()
continuar = True
while continuar == True:
    mostrar_menu()
    opcion = seleccionar_opcion()
    
    match opcion:
        case 1:
            evento.registrar_evento()
        case 2:
            evento.registrar_participantes()
        case 3:
            evento.simular_eventos()
        case 4:
            evento.mostrar_informe()
        case 5:
            print("Cerrando programa...")
            continuar = False
        case _:
            print("Opción invalida por favor selecciona una nueva")