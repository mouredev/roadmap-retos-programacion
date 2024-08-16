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
    def __init__(self, name: str):
        self.name = name
        self.medallas = {"Oro": 0, "Plata": 0, "Bronce": 0}
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return self.name == other.name
    
    def get_total_medallas(self)-> int:
        total = self.medallas["Oro"] + self.medallas["Plata"] + self.medallas["Bronce"]
        return total
    
    def __str__(self):
        return f"{self.name} - O: {self.medallas['Oro']} P: {self.medallas['Plata']} B: {self.medallas['Bronce']}"
    

class Participante:
    
    def __init__(self, name: str, country: Pais):
        self.name = name
        self.country = country
    
    def __hash__(self):
        # Genera un valor hash basado en el nombre del participante + el country
        return hash(self.name + self.country.name)
    
    def __eq__(self, other):
        # Compara dos participantes basándose en su nombre y país
        return self.name == other.name and self.country == other.country
    
class Evento: 
    
    def __init__(self, name: str, participantes: list[Participante]):
        self.name=name
        self.resultados = {}
        if(len(participantes)>= 3):
            self.participantes = participantes
            for participante in participantes:
                self.resultados[participante] = 0 #self.resultados = {participante: 0 for participante in participantes}
        else:
            raise ("Los eventos deben tener mínimo 3 participantes")
    
    def simular(self):
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
            
                        

    def ranking(self):
        posicion=0
        for resultado in self.resultados:
            print(f"{posicion+1} - {resultado[0].name} ({resultado[0].country.name}): {resultado[1]}")
            posicion+=1
        
    def get_ganadores(self):
        return self.resultados[:3]

class Olimpiadas:
    def __init__(self):
        self.eventos = []
        self.paises = []
        self.participantes = []
    
    def registrar_pais(self, name: str):
        self.paises.append(Pais(name))
    
    def registrar_participante(self, name: str, country: Pais):
        self.participantes.append(Participante(name, country.name))
        
    def registrar_evento(self, name: str, participantes: list[Participante]):
        self.eventos.append(Evento(name, participantes))
    
    def ordenar_paises_por_medallas(self):
        # Ordena los países utilizando una clave que considera primero el oro, luego la plata, y finalmente el bronce
        paises_ordenados = sorted(self.paises, key=lambda pais: (pais.medallas["Oro"], pais.medallas["Plata"], pais.medallas["Bronce"]), reverse=True)
        return paises_ordenados
    
    def iniciar_olimpiadas(self):
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

#Creo un menu 
while(True):
    #Borro la pantalla
    clear_screen()
    print("Menú de opciones:")
    print("1. Registrar país")
    print("2. Registrar participante")
    print("3. Registrar evento")
    print("4. Simular eventos")
    print("5. Mostrar ranking de países")
    print("7. Mostrar Resultado de evento")
    print("9. Salir")
    
    #Pido la opción
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre_pais = input("Ingrese el nombre del país: ")
        olimpiadas.registrar_pais(nombre_pais)
    elif opcion == "2":
        nombre_participante = input("Ingrese el nombre del participante: ")
        nombre_pais = input("Ingrese el nombre del país: ")
        pais = Pais(nombre_pais)
        olimpiadas.registrar_participante(nombre_participante, pais)
    elif opcion == "3":
        nombre_evento = input("Ingrese el nombre del evento: ")
        print("Participantes:")
        for participante in olimpiadas.participantes:
            print(participante.name)
        participantes = []
        #Selecciona 3 participantes por rapidez, se puede mejorar
        for i in range(3):
            nombre_participante = input(f"Ingrese el nombre del participante {i+1}: ")
            for participante in olimpiadas.participantes:
                if participante.name == nombre_participante:
                    participantes.append(participante)
        olimpiadas.registrar_evento(nombre_evento, participantes)
    elif opcion == "4":
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
    elif opcion == "5":
        print("\nRanking de países:")
        olimpiadas.paises = olimpiadas.ordenar_paises_por_medallas()
        for pais in olimpiadas.paises:
            print(f"{pais.name}: Oro {pais.medallas['Oro']}, Plata {pais.medallas['Plata']}, Bronce {pais.medallas['Bronce']}")
    elif opcion == "7":
        print("\nResultados de eventos:")
        for evento in olimpiadas.eventos:
            print(f"\n{evento.name}")
        
        evento_sel = input("Seleccione el evento a mostrar:")   
        for evento in olimpiadas.eventos:
            if evento.name == evento_sel:
                print(f"\n{evento.name}")
                evento.ranking()
        input("Presiona una tecla para continuar...")
    
    elif opcion == "9":
        break
    
"""
SUGERENCIAS DE MEJORA:

1 Utiliza la clase Enum para representar tipos de medallas y opciones del menú.

2 Implementa un mejor manejo de errores para entradas inválidas del usuario.

3 Añade más validaciones, como verificar si un país ya existe antes de registrarlo.

4 Implementa un sistema para guardar y cargar datos, por ejemplo, usando JSON o una base de datos simple.

5Mejora la interfaz de usuario:
Usa una biblioteca como rich para mejorar la presentación en la terminal.
Usa type hints de manera consistente:
Aplica anotaciones de tipo en todos los métodos y funciones.
Usa métodos de clase y estáticos:
Para operaciones que no necesitan acceder a atributos de instancia.
Mejora la selección de participantes para eventos:
Implementa un sistema más robusto para seleccionar participantes al crear eventos.
"""