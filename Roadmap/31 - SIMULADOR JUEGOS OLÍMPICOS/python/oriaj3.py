"""
30 - SIMULADOR JUEGOS OLÍMPICOS
Autor de la solución: oriaj3
 
 EJERCICIO:
 ¡Los JJOO de París 2024 han comenzado!
 Crea un programa que simule la celebración de los juegos.
 El programa debe permitir al usuario registrar eventos y participantes,
 realizar la simulación de los eventos asignando posiciones de manera aleatoria
 y generar un informe final. Todo ello por terminal.
 Requisitos:
 1. Registrar eventos deportivos.
 2. Registrar participantes por nombre y país.
 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 5. Mostrar los ganadores por cada evento.
 6. Mostrar el ranking de países según el número de medallas.
 Acciones:
 1. Registro de eventos.
 2. Registro de participantes.
 3. Simulación de eventos.
 4. Creación de informes.
 5. Salir del programa.
 */
"""
import random

class Pais:
    name: str
    medallas: dict[str, int]

    def __init__(self, name: str)-> None:
        self.name = name
        self.medallas = {"Oro": 0, "Plata": 0, "Bronce": 0}
    
    def __hash__(self)-> int:
        return hash(self.name)
    
    def __eq__(self, other: "Pais"):
        return self.name == other.name
    
    def get_total_medallas(self)-> int:
        total = self.medallas["Oro"] + self.medallas["Plata"] + self.medallas["Bronce"]
        return total
    
    def __str__(self)-> str:
        return f"{self.name} - O: {self.medallas['Oro']} P: {self.medallas['Plata']} B: {self.medallas['Bronce']}"
    
class Participante:
    name: str
    country: Pais

    def __init__(self, name: str, country: Pais)-> None:
        self.name = name
        self.country = country
    
    def __hash__(self)-> int:
        # Genera un valor hash basado en el nombre del participante + el country
        return hash(self.name + self.country.name)
    
    def __eq__(self, other)-> bool:
        # Compara dos participantes basándose en su nombre y país
        return self.name == other.name and self.country == other.country
    
class Evento: 
    name: str
    resultados: dict[Participante, int]
    
    def __init__(self, name: str, participantes: list[Participante]):
        self.name=name
        self.resultados = {}
        if(len(participantes)>= 3):
            self.participantes = participantes
            for participante in participantes:
                self.resultados[participante] = 0 #self.resultados = {participante: 0 for participante in participantes}
        else:
            raise ("Los eventos deben tener mínimo 3 participantes")
    
    def simular(self)-> None:
        set_resultados = set()
        for participante in self.participantes:
            resultado = random.randint(0, 100)
            # Generar un nuevo resultado si ya está en el conjunto
            while resultado in set_resultados:
                resultado = random.randint(0, 100)
            # Agregar el resultado al conjunto y al diccionario
            set_resultados.add(resultado)
            self.resultados[participante] = resultado
            
        #Ordena los resultados
        self.resultados = sorted(self.resultados.items(), key=lambda x: x[1], reverse=True)
        
        medallas = ["Oro", "Plata", "Bronce"]
        for i in range(3):
            self.resultados[i][0].country.medallas[medallas[i]] += 1
            
                        

    def ranking(self)-> None:
        posicion=0
        for resultado in self.resultados:
            print(f"{posicion+1} - {resultado[0].name} ({resultado[0].country.name}): {resultado[1]}")
            posicion+=1
        
    def get_ganadores(self)-> list[tuple[Participante, int]]:
        return self.resultados[:3]

class Olimpiadas:
    eventos: list[Evento]
    paises: list[Pais]
    participantes: list[Participante]

    def __init__(self)-> None:
        self.eventos = []
        self.paises = []
        self.participantes = []
    
    def registrar_pais(self, name: str)-> None:
        if name not in [pais.name for pais in self.paises]:
            self.paises.append(Pais(name))
    
    def registrar_participante(self, name: str, country: Pais)-> None:
        if country not in self.paises:
            raise ValueError("El país no está registrado")
        elif name not in [participante.name for participante in self.participantes]:
            for pais in self.paises:
                if pais.name == country.name:
                    self.participantes.append(Participante(name, pais))
        else:
            raise ValueError("El participante ya está registrado")
        
    def registrar_evento(self, name: str, participantes: list[Participante])-> None:
        if len(participantes) < 3:
            raise ValueError("Los eventos deben tener mínimo 3 participantes")
        elif name not in [evento.name for evento in self.eventos]:
            self.eventos.append(Evento(name, participantes))
        else:
            raise ValueError("El evento ya está registrado")   
        
    def ordenar_paises_por_medallas(self)-> list[Pais]:
        # Ordena los países utilizando una clave que considera primero el oro, luego la plata, y finalmente el bronce
        paises_ordenados = sorted(self.paises, key=lambda pais: (pais.medallas["Oro"], pais.medallas["Plata"], pais.medallas["Bronce"]), reverse=True)
        return paises_ordenados
    
    def iniciar_olimpiadas(self)-> None:
        self.paises.append(Pais("Jamaica")) #0
        self.paises.append(Pais("USA"))     #1
        self.paises.append(Pais("España"))  #2
        self.paises.append(Pais("Francia")) #3
        self.paises.append(Pais("Alemania"))#4    
        self.paises.append(Pais("China"))   #5
                
        # 100 metros planos
        self.participantes.append(Participante("Usain Bolt", self.paises[0]))  # Jamaica
        self.participantes.append(Participante("Carl Lewis", self.paises[1]))  # USA
        self.participantes.append(Participante("Bruno Hortelano", self.paises[2]))  # España
        self.participantes.append(Participante("Christophe Lemaitre", self.paises[3]))  # Francia
        self.participantes.append(Participante("Julian Reus", self.paises[4]))  # Alemania
        self.participantes.append(Participante("Su Bingtian", self.paises[5]))  # China
        #Registrar evento
        self.eventos.append(Evento("100m", self.participantes[-6:])) # Selecciona los últimos 6 participantes

        # Tiro con arco
        self.participantes.append(Participante("Dwayne McKenzie", self.paises[0]))  # Jamaica (Nombre ficticio)
        self.participantes.append(Participante("Brady Ellison", self.paises[1]))  # USA
        self.participantes.append(Participante("Miguel Alvariño", self.paises[2]))  # España
        self.participantes.append(Participante("Jean-Charles Valladont", self.paises[3]))  # Francia
        self.participantes.append(Participante("Florian Unruh", self.paises[4]))  # Alemania
        self.participantes.append(Participante("Xing Yu", self.paises[5]))  # China
        # Registrar evento
        self.eventos.append(Evento("Tiro con arco", self.participantes[-6:]))  # Selecciona los últimos 6 participantes

        # Natación - 200 metros estilo libre
        self.participantes.append(Participante("Michael Phelps", self.paises[1]))  # USA
        self.participantes.append(Participante("Ryan Lochte", self.paises[1]))  # USA
        self.participantes.append(Participante("Mireia Belmonte", self.paises[2]))  # España
        self.participantes.append(Participante("Yannick Agnel", self.paises[3]))  # Francia
        self.participantes.append(Participante("Paul Biedermann", self.paises[4]))  # Alemania
        self.participantes.append(Participante("Sun Yang", self.paises[5]))  # China
        # Registrar evento
        self.eventos.append(Evento("Natacion", self.participantes[-6:]))  # Selecciona los últimos 6 participantes

        # Esgrima - Florete individual
        self.participantes.append(Participante("Aliona Edwards", self.paises[0]))  # Jamaica (Nombre ficticio)
        self.participantes.append(Participante("Mariel Zagunis", self.paises[1]))  # USA
        self.participantes.append(Participante("Carlos Llavador", self.paises[2]))  # España
        self.participantes.append(Participante("Ysaora Thibus", self.paises[3]))  # Francia
        self.participantes.append(Participante("Peter Joppich", self.paises[4]))  # Alemania
        self.participantes.append(Participante("Lei Sheng", self.paises[5]))  # China
        # Registrar evento
        self.eventos.append(Evento("Esgrima", self.participantes[-6:]))  # Selecciona los últimos 6 participantes

        # Gimnasia artística - Final de suelo
        self.participantes.append(Participante("Simone Biles", self.paises[1]))  # USA
        self.participantes.append(Participante("Nadia Comăneci", self.paises[1]))  # USA (originalmente de Rumanía, pero dejémoslo para ejemplo)
        self.participantes.append(Participante("Rayderley Zapata", self.paises[2]))  # España
        self.participantes.append(Participante("Samir Aït Saïd", self.paises[3]))  # Francia
        self.participantes.append(Participante("Fabian Hambüchen", self.paises[4]))  # Alemania
        self.participantes.append(Participante("Liu Yang", self.paises[5]))  # China
        # Registrar evento
        self.eventos.append(Evento("Gimnasia", self.participantes[-6:]))
        
        #Lista los eventos
        print("Eventos registrados:")
        for evento in self.eventos:
            print(evento.name)
            
        #Simula los eventos
        print("\nSimulación de eventos:")
        for evento in self.eventos:
            print(f"\n{evento.name}")
            evento.simular()
            evento.ranking()
        
        #Muestra el ranking de países
        print("\nRanking de países:")
        self.paises = self.ordenar_paises_por_medallas()
        for pais in self.paises:
            print(f"{pais.name}: Oro {pais.medallas['Oro']}, Plata {pais.medallas['Plata']}, Bronce {pais.medallas['Bronce']}")

#Creo una instancia de las olimpiadas y las inicio
olimpiadas = Olimpiadas()
olimpiadas.iniciar_olimpiadas()

input("Presiona una tecla para iniciar el menú...")

#Función para limpiar la pantalla
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Funciones auxiliares para mostrar el menú y sus opciones
from enum import Enum

class MenuOpciones(Enum):
    REGISTRAR_PAIS = 1
    REGISTRAR_PARTICIPANTE = 2
    REGISTRAR_EVENTO = 3
    SIMULAR_EVENTOS = 4
    MOSTRAR_RANKING_PAISES = 5
    MOSTRAR_RESULTADO_EVENTO = 7
    SALIR = 9

def mostrar_menu()-> None:
    for opcion in MenuOpciones:
        print(f"{opcion.value}. {opcion.name.replace('_', ' ').capitalize()}")
    print("")

def mostrar_participantes(participantes: list[Participante])-> None:
    clear_screen()
    print("Participantes disponibles:")
    for i, participante in enumerate(participantes, 1):
        print(f"{i}. {participante.name} ({participante.country.name})")

def seleccionar_participantes(olimpiadas: Olimpiadas, num_participantes:int =3) -> list[Participante]:
    participantes_seleccionados = []
    while len(participantes_seleccionados) < num_participantes:
        mostrar_participantes(olimpiadas.participantes)
        try:
            indice = int(input(f"Seleccione el participante {len(participantes_seleccionados) + 1} (número): ")) - 1
            if 0 <= indice < len(olimpiadas.participantes):
                participante = olimpiadas.participantes[indice]
                if participante not in participantes_seleccionados:
                    participantes_seleccionados.append(participante)
                    print(f"Seleccionado: {participante.name}")
                else:
                    print("Este participante ya ha sido seleccionado. Por favor, elija otro.")
            else:
                print("Número de participante no válido. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    return participantes_seleccionados


while(True):
    #Borro la pantalla
    clear_screen()
    mostrar_menu()
    
    #Pido la opción
    try:
        opcion = MenuOpciones(int(input("Seleccione una opción: ")))
    except ValueError:
        print("Opción no válida. Por favor, intente de nuevo.")
        input("Presione Enter para continuar...")
        continue
    
    match opcion:
        case MenuOpciones.REGISTRAR_PAIS:
            try:
                nombre_pais = input("Ingrese el nombre del país: ")
                olimpiadas.registrar_pais(nombre_pais)
            except ValueError as e:
                print(e)
        case MenuOpciones.REGISTRAR_PARTICIPANTE:
            try:
                nombre_participante = input("Ingrese el nombre del participante: ")
                nombre_pais = input("Ingrese el nombre del país: ")
                pais = Pais(nombre_pais)
                olimpiadas.registrar_participante(nombre_participante, pais)
            except ValueError as e:
                print(e)
        case MenuOpciones.REGISTRAR_EVENTO:
            try:
                nombre_evento = input("Ingrese el nombre del evento: ")
                participantes = seleccionar_participantes(olimpiadas)
                olimpiadas.registrar_evento(nombre_evento, participantes)
                print(f"Evento '{nombre_evento}' registrado con éxito con los siguientes participantes:")
                for p in participantes:
                    print(f"- {p.name} ({p.country.name})")
            except ValueError as e:
                print(f"Error al registrar el evento: {e}")
            input("Presione Enter para continuar...")
        case MenuOpciones.SIMULAR_EVENTOS:
            print("\nSimulación de eventos:")
            for evento in olimpiadas.eventos:
                print(f"\n{evento.name}")
            evento_sel = input("Seleccione el evento a simular: ")
            for evento in olimpiadas.eventos:
                if evento.name == evento_sel:
                    print(f"\n{evento.name}")
                    evento.simular()
                    evento.ranking()
                    input("Presiona una tecla para continuar...")
        case MenuOpciones.MOSTRAR_RANKING_PAISES:
            print("\nRanking de países:")
            olimpiadas.paises = olimpiadas.ordenar_paises_por_medallas()
            for pais in olimpiadas.paises:
                print(f"{pais.name}: Oro {pais.medallas['Oro']}, Plata {pais.medallas['Plata']}, Bronce {pais.medallas['Bronce']}")
            input("Presiona una tecla para continuar...")
        case MenuOpciones.MOSTRAR_RESULTADO_EVENTO:
            print("\nResultados de eventos:")
            for evento in olimpiadas.eventos:
                print(f"\n{evento.name}")
            
            evento_sel = input("Seleccione el evento a mostrar:")   
            for evento in olimpiadas.eventos:
                if evento.name == evento_sel:
                    print(f"\n{evento.name}")
                    evento.ranking()
            input("Presiona una tecla para continuar...")
        
        case MenuOpciones.SALIR:
            break