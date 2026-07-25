"""
#31 - Simulador juegos olimpicos
"""

"""
EJERCICIO:
"""

# Crea un programa que simule la celebración de los juegos.
# El programa debe permitir al usuario registrar eventos y participantes,
# realizar la simulación de los eventos asignando posiciones de manera aleatoria
# y generar un informe final. Todo ello por terminal.

"""
Requesitos:
"""
# 1. Registrar eventos deportivos.
# 2. Registrar participantes por nombre y país.
# 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
# 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
# 5. Mostrar los ganadores por cada evento.
# 6. Mostrar el ranking de países según el número de medallas.

"""
Acciones
"""
# 1. Registro de eventos.
# 2. Registro de participantes.
# 3. Simulación de eventos.
# 4. Creación de informes.
# 5. Salir del programa.


from abc import ABC, abstractmethod
import random

class JuegosOlimpicos(ABC):
    @abstractmethod
    def registro_evento(self):
        pass

    @abstractmethod
    def registro_participante(self):
        pass

    @abstractmethod
    def simulacion_evento(self):
        pass

    @abstractmethod
    def creacion_informe(self):
        pass


class SimuladorOlimpico(JuegosOlimpicos):
    def __init__(self):
        self.eventos = {}  # {nombre_evento: [lista_participantes]}
        self.participantes = {}  # {nombre: pais}
        self.resultados = {}  # {nombre_evento: [(oro, plata, bronce)]}
        self.medallero = {}  # {pais: {oro: 0, plata: 0, bronce: 0}}

    def registro_evento(self):
        evento = input("Ingrese el nombre del evento: ")
        if evento in self.eventos:
            print(f"El evento '{evento}' ya está registrado.")
        else:
            self.eventos[evento] = []
            print(f"Evento '{evento}' registrado correctamente.")

    def registro_participante(self):
        if not self.eventos:
            print("Primero debe registrar al menos un evento.")
            return

        nombre = input("Ingrese el nombre del participante: ")
        pais = input("Ingrese el país del participante: ")
        
        if nombre in self.participantes:
            print(f"El participante '{nombre}' ya está registrado.")
            return
            
        self.participantes[nombre] = pais
        
        print("Eventos disponibles:")
        for i, evento in enumerate(self.eventos.keys(), 1):
            print(f"{i}. {evento}")
            
        seleccion = input("Seleccione el número del evento en el que participará (o 'todos'): ")
        
        if seleccion.lower() == 'todos':
            for evento in self.eventos:
                self.eventos[evento].append(nombre)
            print(f"{nombre} registrado en todos los eventos.")
        else:
            try:
                indice = int(seleccion) - 1
                evento = list(self.eventos.keys())[indice]
                self.eventos[evento].append(nombre)
                print(f"{nombre} registrado en {evento}.")
            except (ValueError, IndexError):
                print("Selección inválida.")

    def simulacion_evento(self):
        if not self.eventos:
            print("No hay eventos registrados.")
            return
            
        print("Eventos disponibles para simular:")
        for i, evento in enumerate(self.eventos.keys(), 1):
            print(f"{i}. {evento}")
            
        seleccion = input("Seleccione el número del evento a simular: ")
        
        try:
            indice = int(seleccion) - 1
            evento = list(self.eventos.keys())[indice]
            
            participantes = self.eventos[evento]
            if len(participantes) < 3:
                print(f"El evento {evento} necesita al menos 3 participantes.")
                return
                
            # Simular el evento (aleatoriamente)
            podio = random.sample(participantes, 3)
            oro, plata, bronce = podio
            
            print("\n=== RESULTADOS ===")
            print(f"ORO: {oro} ({self.participantes[oro]})")
            print(f"PLATA: {plata} ({self.participantes[plata]})")
            print(f"BRONCE: {bronce} ({self.participantes[bronce]})")
            
            # Guardar resultados
            self.resultados[evento] = (oro, plata, bronce)
            
            # Actualizar medallero
            for medalla, participante in zip(['oro', 'plata', 'bronce'], podio):
                pais = self.participantes[participante]
                if pais not in self.medallero:
                    self.medallero[pais] = {'oro': 0, 'plata': 0, 'bronce': 0}
                self.medallero[pais][medalla] += 1
                
        except (ValueError, IndexError):
            print("Selección inválida.")

    def creacion_informe(self):
        if not self.resultados:
            print("No se ha simulado ningún evento todavía.")
            return
            
        print("\n===== INFORME DE RESULTADOS =====")
        
        # Mostrar ganadores por evento
        print("\n--- Ganadores por Evento ---")
        for evento, podio in self.resultados.items():
            print(f"\nEvento: {evento}")
            oro, plata, bronce = podio
            print(f"ORO: {oro} ({self.participantes[oro]})")
            print(f"PLATA: {plata} ({self.participantes[plata]})")
            print(f"BRONCE: {bronce} ({self.participantes[bronce]})")
        
        # Mostrar ranking de países
        print("\n--- Ranking de Países ---")
        paises_ranking = sorted(
            self.medallero.items(), 
            key=lambda x: (x[1]['oro'], x[1]['plata'], x[1]['bronce']),
            reverse=True
        )
        
        for i, (pais, medallas) in enumerate(paises_ranking, 1):
            print(f"{i}. {pais}: {medallas['oro']} oro, {medallas['plata']} plata, {medallas['bronce']} bronce")


def main():
    simulador = SimuladorOlimpico()
    
    while True:
        print("\n===== SIMULADOR DE JUEGOS OLÍMPICOS =====")
        print("1. Registro de eventos")
        print("2. Registro de participantes")
        print("3. Simulación de eventos")
        print("4. Creación de informes")
        print("5. Salir del programa")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            simulador.registro_evento()
        elif opcion == "2":
            simulador.registro_participante()
        elif opcion == "3":
            simulador.simulacion_evento()
        elif opcion == "4":
            simulador.creacion_informe()
        elif opcion == "5":
            print("Gracias por usar el simulador. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()