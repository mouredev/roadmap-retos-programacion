# # # /*
# # #  * EJERCICIO:
# # #  * ¡Los JJOO de París 2024 han comenzado!
# # #  * Crea un programa que simule la celebración de los juegos.
# # #  * El programa debe permitir al usuario registrar eventos y participantes,
# # #  * realizar la simulación de los eventos asignando posiciones de manera aleatoria
# # #  * y generar un informe final. Todo ello por terminal.
# # #  * Requisitos:
# # #  * 1. Registrar eventos deportivos.
# # #  * 2. Registrar participantes por nombre y país.
# # #  * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
# # #  * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
# # #  * 5. Mostrar los ganadores por cada evento.
# # #  * 6. Mostrar el ranking de países según el número de medallas.
# # #  * Acciones:
# # #  * 1. Registro de eventos.
# # #  * 2. Registro de participantes.
# # #  * 3. Simulación de eventos.
# # #  * 4. Creación de informes.
# # #  * 5. Salir del programa.
# # #  */


# Importación de módulos necesarios
from abc import ABC, abstractmethod  # Para clases abstractas
from types import SimpleNamespace    # Para crear objetos dinámicos
import random                       # Para simulación aleatoria

# Clase que contiene datos iniciales de atletas y eventos
class VirtualDatos(ABC):
    pass

class Datos(VirtualDatos):
    # Lista de atletas predefinidos (nombre, país)
    def __init__(self, atleta, evento):
        self._atleta = atleta
        self._event = evento

# Clase fábrica para creación de objetos
class VirtualFabrica(ABC):
    @classmethod
    @abstractmethod
    def crear_evento(cls, *nombres):
        pass
    
    @classmethod
    @abstractmethod
    def crear_atleta(cls, *datos):
        pass
    
class Fabrica(VirtualFabrica):
    @classmethod
    def crear_evento(cls, *nombres):
        """
        Crea eventos deportivos a partir de nombres
        Args:
            *nombres: Nombres de los eventos a crear
        Returns:
            Lista de objetos CEventoDeportivo
        """
        instancia = SimpleNamespace()  # Objeto dinámico para almacenar eventos
        result = []                   # Lista de resultados
        
        for n in nombres:
            inst = CEventoDeportivo(n)  # Crea instancia de evento
            setattr(instancia, n, inst) # Asigna al namespace
            result.append(inst)         # Agrega a la lista
        return result

    @classmethod
    def crear_atleta(cls, *datos):
        """
        Crea participantes (atletas) a partir de datos
        Args:
            *datos: Tuplas con (nombre, país)
        Returns:
            Lista de objetos CParticipante
        """
        instancia = SimpleNamespace()  # Objeto dinámico para almacenar atletas
        result = []                   # Lista de resultados
        
        for d in datos:
            inst = CParticipante(*d)  # Crea instancia de participante
            nombre = d[0]             # Obtiene nombre
            setattr(instancia, nombre, inst)  # Asigna al namespace
            result.append(inst)        # Agrega a la lista
        return result

# INTERFACES ABSTRACTAS ------------------------------------------------------

# Interfaz para atletas
class VirtualAtleth(ABC):
    @abstractmethod
    def __init__(self, name: str, country: str):
        """Inicializa un atleta con nombre y país"""
        pass

# Interfaz para medallero
class VirtualMedallero(ABC):
    @abstractmethod
    def __init__(self):
        """Inicializa el medallero"""
        pass
       
    @abstractmethod
    def asignar_medallas(self, resultado: list[VirtualAtleth]):
        """Asigna medallas basado en resultados"""
        pass
        
    @abstractmethod
    def mostrar_medallero(self):
        """Muestra el medallero por países"""
        pass

# Interfaz para eventos deportivos
class VirtualEventoDeportivo(ABC): 
    @abstractmethod
    def __init__(self, name: str):
        """Inicializa evento con nombre"""
        pass
        
    @abstractmethod
    def agregar_participante(self, participante: VirtualAtleth):
        """Agrega participante al evento"""
        pass
        
    @abstractmethod
    def simular(self):
        """Simula la celebración del evento"""
        pass

# Interfaz para registro de eventos
class VirtualRegistroEventos(ABC):
    @abstractmethod
    def __init__(self):
        """Inicializa el registro"""
        pass
        
    @abstractmethod
    def get_eventos_registrados(self):
        """Obtiene lista de eventos registrados"""
        pass
        
    @abstractmethod
    def registrar_evento(self, evento: VirtualEventoDeportivo):
        """Registra un nuevo evento"""
        pass
        
    @abstractmethod
    def registrar_participante(self, evento: VirtualEventoDeportivo, 
                           atleta: VirtualAtleth, medallero: VirtualMedallero):
        """Registra participante en evento"""
        pass

# Interfaz para generación de informes
class VirtualInforme(ABC):
    @abstractmethod
    def mostrar_eventos_participantes(self, eventos_registrados: VirtualRegistroEventos):
        """Muestra eventos con sus participantes"""
        pass
        
    @abstractmethod
    def mostrar_ganadores(self, eventos_registrados: VirtualRegistroEventos):
        """Muestra ganadores por evento"""
        pass

# Interfaz para el gestor principal
class VirtualManagerOlimpicGames(ABC):
    @abstractmethod 
    def __init__(self, fabrica: VirtualFabrica, datos:VirtualDatos,eventos_registrados: VirtualRegistroEventos,
                medallero: VirtualMedallero, informe: VirtualInforme):
        """Inicializa el gestor con sus dependencias"""
        pass
    
    # Métodos abstractos del gestor
    @abstractmethod   
    def crear_eventos(self):
        """Crea eventos iniciales"""
        pass
        
    @abstractmethod 
    def crear_participantes(self):
        """Crea participantes iniciales"""
        pass
        
    @abstractmethod 
    def caso_registro_eventos(self):
        """Caso de uso 1: registro de eventos"""
        pass
        
    @abstractmethod 
    def caso_registro_participantes(self):
        """Caso de uso 2: registro de participantes"""
        pass
    
    @abstractmethod   
    def registrar_participante(self, evento: VirtualEventoDeportivo, 
                                atleta: VirtualAtleth):
        """Registra participante en evento"""
        pass
         
    @abstractmethod
    def registrar_evento(self, *evento):
        """Registra uno o más eventos"""
        pass

    @abstractmethod       
    def mostrar_eventos_participantes(self):
        """Muestra eventos con participantes"""
        pass
          
    @abstractmethod
    def simular_eventos(self):
        """Simula todos los eventos registrados"""
        pass
        
    @abstractmethod     
    def mostrar_ganadores(self):
        """Muestra ganadores"""
        pass
        
    @abstractmethod 
    def mostrar_medallero(self):
        """Muestra medallero"""
        pass

# IMPLEMENTACIONES CONCRETAS -------------------------------------------------

# Implementación concreta de participante
class CParticipante(VirtualAtleth):
    def __init__(self, name: str, country: str):
        """Inicializa participante con nombre y país"""
        self.name = name      # Nombre del atleta
        self.country = country  # País del atleta

# Implementación concreta de medallero
class CMedallero(VirtualMedallero):
    def __init__(self):
        """Inicializa medallero vacío"""
        self.country = {}  # Diccionario {país: [oro, plata, bronce]}

    def asignar_medallas(self, resultado: list[VirtualAtleth]):
        """
        Asigna medallas basado en resultados
        Args:
            resultado: Lista ordenada de participantes (1° oro, 2° plata, 3° bronce)
        """
        # Asigna medallas a los 3 primeros
        self.country[resultado[0].country][0] += 1  # Oro
        self.country[resultado[1].country][1] += 1  # Plata
        self.country[resultado[2].country][2] += 1  # Bronce

    def mostrar_medallero(self):
        """Muestra medallero ordenado por cantidad de medallas"""
        print("Medallero Por Paises\n\n")
        # Ordena por total de medallas (descendente)
        self.country = dict(sorted(self.country.items(), 
                                 key=lambda item: item[1], reverse=True))
        # Imprime cada país con sus medallas
        for c, m in self.country.items():
            print(f"{c}   Oro {m[0]} Plata {m[1]} Bronce {m[2]}") 

# Implementación concreta de evento deportivo
class CEventoDeportivo(VirtualEventoDeportivo):  
    def __init__(self, name: str):
        """Inicializa evento con nombre"""
        self.name = name            # Nombre del evento
        self.participantes = []     # Lista de participantes
        self.result = []            # Resultados (no usado actualmente)
        self.celebrado = False      # Estado del evento

    def agregar_participante(self, participante: VirtualAtleth):
        """Agrega participante al evento"""
        self.participantes.append(participante)
          
    def simular(self):
        """Simula el evento: mezcla participantes aleatoriamente"""
        random.shuffle(self.participantes)  # Resultado aleatorio
        print(f"Evento {self.name} celebrado correctamente")
        self.celebrado = True  # Marca como celebrado

# Implementación concreta de registro de eventos
class CRegistroEventos(VirtualRegistroEventos):
    def __init__(self):
        """Inicializa registro vacío"""
        self.eventos_deportivos_registrados = []  # Lista de eventos
      
    def get_eventos_registrados(self):
        """Obtiene lista de eventos registrados"""
        return self.eventos_deportivos_registrados

    def registrar_evento(self, evento: VirtualEventoDeportivo):
        """
        Registra un nuevo evento
        Args:
            evento: Evento a registrar
        """
        if evento.celebrado:
            print(f"Evento {evento.name} ya se ha celebrado, imposible agregarlo")
            return
         
        if evento in self.eventos_deportivos_registrados:
            print(f"Evento {evento.name} ya esta Registrado")
        else:
            self.eventos_deportivos_registrados.append(evento)
            print(f"Evento {evento.name} registrado correctamente")

    def registrar_participante(self, evento: VirtualEventoDeportivo, 
                           atleta: VirtualAtleth, medallero: VirtualMedallero):
        """
        Registra participante en evento
        Args:
            evento: Evento deportivo
            atleta: Participante a registrar
            medallero: Medallero para actualizar países
        """
        if evento.celebrado:
            print(f"Evento {evento.name} ya se ha celebrado, imposible agregar participantes")
            return
            
        # Si el país no está en medallero, lo inicializa
        if atleta.country not in medallero.country:
            medallero.country[atleta.country] = [0, 0, 0]  # [Oro, Plata, Bronce]

        if atleta in evento.participantes:
            print(f"Atleta {atleta.name} ya esta Registrado en evento {evento.name}")
        else:
            evento.agregar_participante(atleta)
            print(f"Participante {atleta.name} Agregado al evento {evento.name} correctamente")

# Implementación concreta de informe
class CInforme(VirtualInforme):
    def mostrar_eventos_participantes(self, eventos_registrados: VirtualRegistroEventos):
        """
        Muestra eventos con sus participantes
        Args:
            eventos_registrados: Gestor de eventos registrados
        """
        print("Eventos Registrados\n")
        for evento in eventos_registrados.get_eventos_registrados():
            print(f"{evento.name} ", end="")
            for p in evento.participantes:
                print(f"{p.name} ", end="")
            print()  # Nueva línea

    def mostrar_ganadores(self, eventos_registrados: VirtualRegistroEventos):
        """
        Muestra ganadores por evento
        Args:
            eventos_registrados: Gestor de eventos registrados
        """
        print("Ganadores por eventos\n")
        for evento in eventos_registrados.get_eventos_registrados():
            print(f"{evento.name}  1 {evento.participantes[0].name}")

# Implementación concreta del gestor principal
class ManagerOlimpicGames(VirtualManagerOlimpicGames):
    def __init__(self, fabrica: VirtualFabrica, datos: VirtualDatos, eventos_registrados: VirtualRegistroEventos,
                medallero: VirtualMedallero, informe: VirtualInforme):
        """
        Inicializa el gestor con sus dependencias
        Args:
            fabrica: Fábrica para crear objetos
            eventos_registrados: Gestor de eventos
            medallero: Medallero olímpico
            informe: Generador de informes
        """
        self.eventos_registrados = eventos_registrados
        self.medallero = medallero
        self.informe = informe
        self.fabrica = fabrica
        self.Datos = datos
         
    def crear_eventos(self):
        """Crea eventos usando datos predefinidos"""
        return self.fabrica.crear_evento(*self.Datos._event)
    
    def registrar_evento(self, *eventos):
        """Registra uno o más eventos"""
        for evento in eventos:
            self.eventos_registrados.registrar_evento(evento)

    def caso_registro_eventos(self):
        """Caso de uso 1: crea y registra eventos"""
        eventos = self.crear_eventos()
        self.registrar_evento(*eventos)
        self.mostrar_eventos_participantes()

    def caso_registro_participantes(self):
        """Caso de uso 2: registra participantes en todos los eventos"""
        atletas = self.crear_participantes()
                        
        for evento in self.eventos_registrados.get_eventos_registrados():
            for atleta in atletas:
                self.registrar_participante(evento, atleta)
        self.mostrar_eventos_participantes()

    def crear_participantes(self):
        """Crea participantes usando datos predefinidos"""
        return self.fabrica.crear_atleta(*self.Datos._atleta)
          
        
    def registrar_participante(self, evento: VirtualEventoDeportivo, atleta: VirtualAtleth):
        """Registra participante en evento"""
        self.eventos_registrados.registrar_participante(evento, atleta, self.medallero)

    def mostrar_eventos_participantes(self):
        """Muestra eventos con participantes"""
        self.informe.mostrar_eventos_participantes(self.eventos_registrados)
          
    def simular_eventos(self):
        """Simula todos los eventos registrados"""
        for evento in self.eventos_registrados.eventos_deportivos_registrados:
            if len(evento.participantes) < 3:
                print(f"Se necesitan minimo 3 participantes para celebrar el evento {evento.name}")
            else:
                evento.simular()
                self.medallero.asignar_medallas(evento.participantes)
         
    def mostrar_ganadores(self):
        """Muestra ganadores por evento"""
        self.informe.mostrar_ganadores(self.eventos_registrados)
        
    def mostrar_medallero(self):
        """Muestra medallero por países"""
        self.medallero.mostrar_medallero()

# Clase para menú de usuario
class MenuUsuario:
    def __init__(self):
        """Inicializa menú con opción por defecto 0"""
        self.option = 0
      
    def validar_entrada(self) -> bool:
        """
        Valida entrada numérica del usuario
        Returns:
            True si es válida, False si no
        """
        try:
            self.option = int(input())
        except ValueError:
            print("Debe teclear un numero\n")
            return False
        else:
            return True
                    
    def menu_principal(self, MOG: VirtualManagerOlimpicGames):
        """
        Muestra y gestiona menú principal
        Args:
            MOG: Gestor olímpico principal
        """
        print("Olimpic Simulator\n")

        while True:
            print("1. Registrar eventos deportivos.")
            print("2. Registrar participantes por nombre y país.")
            print("3. Simular eventos deportivos.")
            print("4. Creacion de Informe.")
            print("5. Salir del simulador")

            if not self.validar_entrada():
                continue
            else:
                match self.option:
                    case 1:  # Registrar eventos
                        MOG.caso_registro_eventos()
                    case 2:  # Registrar participantes
                        MOG.caso_registro_participantes()
                    case 3:  # Simular eventos
                        MOG.simular_eventos()
                        MOG.mostrar_eventos_participantes()
                    case 4:  # Generar informe
                        MOG.mostrar_ganadores()
                        MOG.mostrar_medallero()
                    case 5:  # Salir
                        break
                    case _:  # Opción inválida
                        print("Debe teclear un numero entre 1 y 7\n")

# INICIALIZACIÓN Y EJECUCIÓN -------------------------------------------------

# Creación de instancias principales
medallero = CMedallero()                     # Medallero olímpico
registro_eventos = CRegistroEventos()        # Registro de eventos
informe = CInforme()                         # Generador de informes
fabrica = Fabrica()                          # Fábrica de objetos

atleta = [("pepe", "Cuba"), ("ricardo","Spain"), ("federico", "France"), 
              ("vanessa", "Japon"), ("mijain","Rusia")]
   
evento = ["Atletismo", "Boxeo", "Natacion", "Ciclismo"]
datos = Datos(atleta, evento)
# Creación del gestor principal con sus dependencias
MOG = ManagerOlimpicGames(fabrica, datos, registro_eventos, medallero, informe)

# Creación y ejecución del menú principal
menu_usuario = MenuUsuario()
menu_usuario.menu_principal(MOG)


# Análisis SOLID Detallado (con foco en escalabilidad)
# 1. ✅ Single Responsibility Principle (SRP) - 9.5/10

# Puntos fuertes:

#     Cada clase tiene una única razón para cambiar:

#         CEventoDeportivo: Solo simula eventos.

#         CMedallero: Solo gestiona medallas.

#         ManagerOlimpicGames: Orquesta sin implementar lógica (👍 Correcto como coordinador).

# Mejora posible:

#     CRegistroEventos podría dividirse en:

#         RegistroEventos (guardar eventos).

#         RegistroParticipantes (añadir atletas).

# Ejemplo de escalabilidad:
# python

# class RegistroParticipantes:
#     def __init__(self, medallero: VirtualMedallero):
#         self._medallero = medallero
    
#     def agregar(self, evento: VirtualEventoDeportivo, atleta: VirtualAtleth):
#         if atleta.country not in self._medallero.country:
#             self._medallero.country[atleta.country] = [0, 0, 0]
#         evento.agregar_participante(atleta)

# 2. ✅ Open/Closed Principle (OCP) - 8/10

# Puntos fuertes:

#     Interfaces como VirtualEventoDeportivo permiten añadir nuevos tipos de eventos sin modificar código existente.

# Mejora posible:

#     Usar Strategy Pattern para simulación:

# python

# class EstrategiaSimulacion(ABC):
#     @abstractmethod
#     def simular(self, participantes: list): pass

# class SimulacionAleatoria(EstrategiaSimulacion):
#     def simular(self, participantes): 
#         random.shuffle(participantes)

# class SimulacionPorHabilidad(EstrategiaSimulacion):
#     def simular(self, participantes):
#         participantes.sort(key=lambda x: x.habilidad, reverse=True)

# # En CEventoDeportivo:
# def __init__(self, name: str, estrategia: EstrategiaSimulacion):
#     self._estrategia = estrategia
# def simular(self):
#     self._estrategia.simular(self.participantes)

# 3. ✅ Liskov Substitution (LSP) - 10/10

# Puntos fuertes:

#     Todas las subclases (CParticipante, CEventoDeportivo) pueden sustituir a sus padres sin romper el sistema.

#     Ejemplo:
#     python

#     def prueba_lsp(atleta: VirtualAtleth):
#         print(atleta.name)  # Funciona con cualquier implementación

# 4. ✅ Interface Segregation (ISP) - 9/10

# Puntos fuertes:

#     Interfaces pequeñas (VirtualInforme solo tiene 2 métodos).

#     Ejemplo de ISP bien aplicado:
#     python

#     class IReporteMedallas(ABC):
#         @abstractmethod
#         def generar_reporte_medallas(self): pass

#     # Clases que no usen medallas no están obligadas a implementarlo.

# Mejora:

#     VirtualRegistroEventos podría dividirse en:

#         IRegistroEventos (solo eventos).

#         IRegistroParticipantes (solo atletas).

# 5. ✅ Dependency Inversion (DIP) - 9/10

# Puntos fuertes:

#     ManagerOlimpicGames depende de abstracciones (VirtualFabrica, VirtualMedallero).

#     Inyección de dependencias:
#     python

#     def __init__(self, fabrica: VirtualFabrica, medallero: VirtualMedallero, ...):
#         self._fabrica = fabrica  # 👍 No depende de implementaciones concretas

# Mejora:

#     Usar inyección por constructor en todas las clases (evitar instanciar Fabrica() dentro de Manager).

# 📊 Puntuación Final SOLID
# Principio	Puntuación (10)	Comentario
# SRP	9.5	Manager como orquestador es correcto. Algunas clases podrían dividirse.
# OCP	8.0	Strategy Pattern mejoraría extensibilidad en simulación.
# LSP	10	Perfecto: subtipos sustituibles.
# ISP	9.0	Interfaces pequeñas, pero alguna podría dividirse.
# DIP	9.0	Alto nivel de abstracción, pero hay oportunidades para más inyección.
# Total	9.1	Excelente base, con espacio para patrones avanzados.
# 🚀 Ejemplo de Escalabilidad

# Contexto: Queremos añadir deportes con reglas de simulación diferentes (ej: Atletismo vs. Natación).
# Solución con Patrones:
# python

# # 1. Strategy Pattern para simulación
# class EstrategiaSimulacion(ABC):
#     @abstractmethod
#     def simular(self, participantes: list): pass

# class SimulacionCarrera(EstrategiaSimulacion):
#     def simular(self, participantes):
#         # Lógica específica para carreras (ej: tiempo + habilidad)
#         participantes.sort(key=lambda x: x.tiempo)

# # 2. Factory Method para eventos
# class FabricaEventosEspecificos(VirtualFabrica):
#     def crear_evento(self, nombre: str) -> VirtualEventoDeportivo:
#         if nombre == "Natacion":
#             return CNatacion(nombre, SimulacionCarrera())
#         elif nombre == "Boxeo":
#             return CBoxeo(nombre, SimulacionPorGolpes())

# # 3. Uso en el sistema
# natacion = FabricaEventosEspecificos().crear_evento("Natacion")
# natacion.simular()  # Usa SimulacionCarrera

# Beneficios:

#     OCP: Añadir nuevos deportes no requiere modificar CEventoDeportivo.

#     SRP: Cada estrategia maneja una única lógica.

#     DIP: El alto nivel (Manager) no depende de detalles de simulación.

# 🔧 Áreas Clave de Mejora

#     Inyección de Dependencias:

#         Mover la creación de Fabrica y otros componentes al main (fuera de Manager).

#     Manejo de Errores:

#         Usar excepciones personalizadas (EventoNoValidoError, ParticipanteDuplicadoError).

#     Patrón Observer:

#         Notificar cambios (ej: cuando un evento termina, actualizar UI o bases de datos).

# python

# # Ejemplo Observer
# class Observador(ABC):
#     @abstractmethod
#     def actualizar(self, evento): pass

# class LogObservador(Observador):
#     def actualizar(self, evento):
#         print(f"Evento {evento.name} completado!")

# # En CEventoDeportivo:
# def simular(self):
#     random.shuffle(self.participantes)
#     for observador in self._observadores:
#         observador.actualizar(self)

# 🎯 Conclusión Final

# Tu diseño es robusto y bien estructurado, con un claro enfoque en SOLID. Para escalar:

#     Patrones recomendados: Strategy, Factory Method, Observer.

#     Inyección explícita: Delegar la creación de objetos al nivel más alto.

#     Documentar extensiones: Usar type hints y docstrings para nuevas funcionalidades.

# Puntuación final: 9.1/10 — ¡Excelente trabajo! 👏



# *******************************

# Análisis de POO del Simulador de JJOO

# (Abstracción, Encapsulación, Herencia, Polimorfismo y Asociación)
# 1. ✅ Abstracción (9/10)

# Puntos fuertes:

#     Interfaces claras (VirtualEventoDeportivo, VirtualAtleth) definen contratos bien estructurados.

#     Clases abstractas (VirtualDatos, VirtualFabrica) establecen una base sólida para extensiones.

#     Ejemplo destacado:
#     python

#     class VirtualEventoDeportivo(ABC):
#         @abstractmethod
#         def simular(self): pass  # Obliga a implementar lógica específica en subclases

# Mejora:

#     Añadir más métodos abstractos para comportamientos comunes (ej: validar_participantes() en VirtualEventoDeportivo).

# 2. ✅ Encapsulación (8.5/10)

# Puntos fuertes:

#     Atributos como _atleta y _evento en Datos están protegidos.

#     Métodos públicos bien definidos (ej: agregar_participante(), simular()).

# Mejoras:

#     Usar propiedades (@property) para atributos como participantes en CEventoDeportivo:
#     python

#     @property
#     def participantes(self) -> list:
#         return self._participantes  # Atributo privado _participantes

#     Ejemplo de error: En CMedallero, self.country es un diccionario público (debería ser privado _country).

# 3. ✅ Herencia (9/10)

# Puntos fuertes:

#     Jerarquía clara:

#     VirtualAtleth (Padre)  
#     └── CParticipante (Hijo)  

#     Uso correcto de herencia para especialización (ej: VirtualFabrica → Fabrica).

# Mejora:

#     Evitar herencia múltiple si se escala (preferir composición).

# 4. ⚠️ Polimorfismo (7.5/10)

# Puntos fuertes:

#     Métodos como simular() se implementan de forma distinta en cada evento (aunque actualmente todos usan random.shuffle).

#     Ejemplo básico:
#     python

#     # Todos los eventos implementan simular()
#     atletismo = CEventoDeportivo("Atletismo")
#     natacion = CEventoDeportivo("Natación")
#     atletismo.simular()  # Polimorfismo en acción
#     natacion.simular()

# Mejoras:

#     Polimorfismo avanzado: Usar estrategias de simulación diferentes por deporte (como en el análisis SOLID con EstrategiaSimulacion).

#     Ejemplo de mejora:
#     python

#     class CEventoNatacion(CEventoDeportivo):
#         def simular(self):
#             # Lógica específica para natación (ej: ordenar por tiempo)
#             self.participantes.sort(key=lambda x: x.tiempo)

# 5. ✅ Asociación/Composición (9/10)

# Puntos fuertes:

#     Composición fuerte: ManagerOlimpicGames usa CRegistroEventos, CMedallero, etc., sin heredar de ellos.

#     Ejemplo clave:
#     python

#     class ManagerOlimpicGames:
#         def __init__(self, registro: VirtualRegistroEventos, medallero: VirtualMedallero):
#             self._registro = registro  # Composicion (Manager "tiene un" Registro)
#             self._medallero = medallero

# Mejora:

#     Documentar relaciones claramente (ej: "Un Manager tiene un Medallero").

# 📊 Puntuación Final POO
# Concepto	Puntuación (10)	Comentario
# Abstracción	9.0	Interfaces sólidas, pero podrían ser más descriptivas.
# Encapsulación	8.5	Mayor uso de propiedades y atributos privados mejoraría.
# Herencia	9.0	Bien aplicada, sin abuso.
# Polimorfismo	7.5	Funcional pero básico. Estrategias lo elevarían.
# Asociación	9.0	Composiciones bien diseñadas.
# Total	8.6	Excelente base con oportunidades para profundizar.
# 🚀 Ejemplo de Escalabilidad con POO

# Objetivo: Añadir deportes de equipo (ej: Fútbol) con comportamientos únicos.
# Implementación con Polimorfismo y Composicón:
# python

# # 1. Nueva clase para equipos (Composición)
# class CEquipo(VirtualAtleth):
#     def __init__(self, nombre: str, pais: str, integrantes: list):
#         super().__init__(nombre, pais)
#         self._integrantes = integrantes  # Lista de CParticipante

# # 2. Evento de equipo (Polimorfismo)
# class CEventoEquipo(CEventoDeportivo):
#     def simular(self):
#         # Lógica específica para equipos (ej: suma de habilidades)
#         self.participantes.sort(key=lambda equipo: sum(p.habilidad for p in equipo._integrantes))

# # 3. Uso en el sistema
# equipo1 = CEquipo("Argentina", "ARG", [CParticipante("Messi", "ARG"), ...])
# futbol = CEventoEquipo("Fútbol")
# futbol.agregar_participante(equipo1)
# futbol.simular()  # ¡Polimorfismo en acción!

# Beneficios POO:

#     Extensibilidad: Añadir nuevos tipos de eventos no rompe el código existente.

#     Reutilización: CEquipo reutiliza VirtualAtleth pero con nueva funcionalidad.

#     Mantenibilidad: Cada clase maneja su propia lógica.

# 🔍 Recomendaciones Clave

#     Patrón Strategy: Para variar algoritmos de simulación sin modificar clases.

#     Properties: Proteger atributos críticos (ej: _participantes, _country).

#     Type Hints: Mejorar documentación y autocompletado.
#     python

#     def agregar_participante(self, participante: VirtualAtleth) -> None: ...

#     Exceptions: Personalizar errores (ej: EventoNoValidoError).

# Puntuación final POO: 8.6/10 — ¡Buen diseño, listo para escalar! 🏆