# EJERCICIO:
# ¡Los JJOO de París 2024 han comenzado!
# Crea un programa que simule la celebración de los juegos.
# El programa debe permitir al usuario registrar eventos y participantes,
# realizar la simulación de los eventos asignando posiciones de manera aleatoria
# y generar un informe final. Todo ello por terminal.
# Requisitos:
# 1. Registrar eventos deportivos.
# 2. Registrar participantes por nombre y país.
# 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
# 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
# 5. Mostrar los ganadores por cada evento.
# 6. Mostrar el ranking de países según el número de medallas.
# Acciones:
# 1. Registro de eventos.
# 2. Registro de participantes.
# 3. Simulación de eventos.
# 4. Creación de informes.
# 5. Salir del programa.

# =======================================================
# Estructuras de datos
import random


class Medalla:
    """
    Clase que representa a una medalla de los juegos olímpicos
    """

    def __init__(self, tipo: str):
        self.tipo = tipo

    def get_tipo(self) -> str:
        return self.tipo

    def __eq__(self, other) -> bool:
        """
        Funcion que compara si dos medallas son iguales
        Parametros:
        - other: Medalla - Medalla a comparar
        Retorna:
        - bool - True si las medallas son iguales, False en caso contrario
        """
        if isinstance(other, Medalla):
            return self.tipo == other.tipo
        return False


class Event:
    """
    Clase que representa a un evento de los juegos olímpicos
    """

    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self) -> str:
        return self.nombre


class Eventos:
    """
    Clase que representa la lista de eventos de los juegos olímpicos
    """

    def __init__(self):
        self.eventos: list[Event] = []

    def add_event(self, evento: Event):
        if evento not in self.eventos:
            self.eventos.append(evento)

    def get_events(self) -> list[Event] | None:
        if len(self.eventos) == 0:
            return None
        return self.eventos

    def __len__(self) -> int:
        return len(self.eventos)


class Participante:
    """
    Clase que representa a un participante de los juegos olímpicos
    """

    def __init__(self, nombre: str, pais: str, deporte: str):
        self.nombre = nombre
        self.pais = pais
        self.deporte = deporte
        self.eventos: list[Event] = []
        self.medallas: list[Medalla] = []

    def add_evento(self, evento: Event):
        if evento not in self.eventos:
            self.eventos.append(evento)

    def add_medalla(self, medalla: Medalla):
        if medalla not in self.medallas:
            self.medallas.append(medalla)
        else:
            print(f"La medalla {medalla.get_tipo()} ya está asignada")

    def get_nombre(self) -> str:
        return self.nombre

    def get_eventos(self) -> list[Event]:
        return self.eventos

    def get_medallas(self) -> list[Medalla]:
        return self.medallas[:]

    def get_medallas_tipo(self, tipo: Medalla) -> int:
        """funcion que devuelve el numero de medallas de un tipo
        Parametros:
        - tipo: Medalla - Tipo de medalla
        Retorna:
        - int - Numero de medallas de un tipo
        """
        return len([medalla for medalla in self.medallas if medalla.get_tipo() == tipo])


class Participantes:
    """
    Clase que representa la lista de participantes de los juegos olímpicos
    """

    def __init__(self):
        self.participantes: list[Participante] = []
        self.medallas: list[Medalla] = []

    def add_participante(self, Participante: Participante):
        self.participantes.append(Participante)

    def get_participantes(self) -> list[Participante]:
        return self.participantes[:]

    def hay_participantes(self) -> bool:
        return len(self.participantes) > 0

    def add_medalla(self, medalla: Medalla):
        if medalla not in self.medallas:
            self.medallas.append(medalla)
        else:
            print(f"La medalla {medalla.get_tipo()} ya está asignada")

    def get_medallas(self) -> list[Medalla]:
        return self.medallas[:]


class Resultados:
    """
    Clase que representa la lista de resultados de los eventos
    """

    def __init__(self):
        self.resultados = []

    def add_resultado(self, resultado):
        self.resultados.append(resultado)

    def get_resultados(self):
        return self.resultados


class Medallero:
    """
    Clase que representa al medallero de los juegos olímpicos
    diccionario {país: {oro: numero, plata: numero, bronce: numero}}
    """

    def __init__(self):
        self.countries = {}

    def add_medalla(self, pais: str, tipo_medalla: str):
        if pais not in self.countries:
            self.countries[pais] = {"oro": 0, "plata": 0, "bronce": 0}
        self.countries[pais][tipo_medalla] += 1

    def get_ranking(self):
        return sorted(
            self.countries.items(),
            key=lambda x: x[1]["oro"] + x[1]["plata"] + x[1]["bronce"],
            reverse=True,
        )


# =======================================================
# funciones principales


def mostrar_menu() -> None:
    print("\n" + "=" * 50)
    print("SIMULADOR DE JUEGOS OLÍMPICOS - PARÍS 2024")
    print("=" * 50)
    print("1. Registro de eventos")
    print("2. Registro de participantes")
    print("3. Simulación de eventos")
    print("4. Creación de informes")
    print("5. Salir del programa")
    print("=" * 50)


def registrar_evento(eventos: Eventos) -> None:
    nombre_evento = input("Ingrese el nombre del evento: ").strip().lower()
    if not nombre_evento:
        print("El nombre del evento no puede estar vacío")
        return
    eventos_actuales = eventos.get_events()
    if eventos_actuales and nombre_evento in [
        event.get_nombre() for event in eventos_actuales
    ]:
        print(f"El evento {nombre_evento} ya está registrado")
        return
    eventos.add_event(Event(nombre_evento))
    print(f"Evento {nombre_evento} registrado correctamente")


def registrar_participante(participantes: Participantes, eventos: Eventos) -> None:
    nombre_participante = input("Ingrese el nombre del participante: ").lower().strip()
    pais_participante = input("Ingrese el país del participante: ").lower().strip()
    deporte_participante = (
        input("Ingrese el deporte del participante: ").lower().strip()
    )
    if not nombre_participante or not pais_participante or not deporte_participante:
        print("Los datos del participante no pueden estar vacíos")
        return

    eventos_actuales = eventos.get_events()
    if not eventos_actuales:
        print("No hay eventos registrados")
        return

    if nombre_participante in [
        participante.get_nombre() for participante in participantes.get_participantes()
    ]:
        print(f"El participante {nombre_participante} ya está registrado")
        return

    # mostrar los eventos disponibles
    for i, evento in enumerate(eventos_actuales, 1):
        print(f"{i}. {evento.get_nombre()}")

    print("\n Ingrese los numeros de eventos separados por comas, ej: 1,2,3,6")
    seleccion = input("Eventos: ").strip()

    if not seleccion:
        print("No se seleccionaron eventos")
        return

    eventos_seleccionados = []

    try:
        indices = [int(x.strip()) for x in seleccion.split(",")]
        for idx in indices:
            if 1 <= idx <= len(eventos_actuales):
                eventos_seleccionados.append(eventos_actuales[idx - 1])
            else:
                print(f"El evento {idx} no es válido")
        if not eventos_seleccionados:
            print("No se seleccionaron eventos válidos")
            return
    except ValueError:
        print("Los eventos seleccionados no son válidos")
        return

    nuevo_participante = Participante(
        nombre_participante, pais_participante, deporte_participante
    )

    for evento in eventos_seleccionados:
        nuevo_participante.add_evento(evento)

    participantes.add_participante(nuevo_participante)

    print(f"Participante {nombre_participante} registrado correctamente")


def simular_eventos(
    participantes: Participantes, eventos: Eventos, medallero: Medallero
) -> None:
    """
    Funcion que simula todos los eventos registrados
    Parametros:
    - participantes: Participantes - Lista de participantes registrados
    - eventos: Eventos - Lista de eventos registrados
    """
    lista_eventos = eventos.get_events()
    if not lista_eventos:
        print("No hay eventos registrados")
        return

    if not participantes.hay_participantes():
        print("No hay participantes registrados")
        return

    eventos_simulados = 0

    for evento in lista_eventos:
        # filtrar participantes inscriptos en este evento
        participantes_evento: list[Participante] = [
            participante
            for participante in participantes.get_participantes()
            if evento in participante.get_eventos()
        ]
        if len(participantes_evento) < 3:
            print(f"El evento {evento.get_nombre()} necesita al menos 3 participantes")
            continue

        # simular el evento(orden aleatorio de los participantes)
        random.shuffle(participantes_evento)
        oro, plata, bronce = participantes_evento[:3]

        # asignar las medallas a los participantes
        oro.add_medalla(Medalla("oro"))
        plata.add_medalla(Medalla("plata"))
        bronce.add_medalla(Medalla("bronce"))

        # actualizar medallero
        medallero.add_medalla(pais=oro.pais, tipo_medalla="oro")
        medallero.add_medalla(pais=plata.pais, tipo_medalla="plata")
        medallero.add_medalla(pais=bronce.pais, tipo_medalla="bronce")

        # mostrar resultados
        print(f"Evento {evento.get_nombre()} simulado")
        print(f"Oro: {oro.nombre} ({oro.pais})")
        print(f"Plata: {plata.nombre} ({plata.pais})")
        print(f"Bronce: {bronce.nombre} ({bronce.pais})")

        eventos_simulados += 1

    if eventos_simulados > 0:
        print(f"Se simularon {eventos_simulados} eventos")
    else:
        print("No se pudo simular ningun evento")


def generar_informe(
    participantes: Participantes, eventos: Eventos, medallero: Medallero
) -> None:
    lista_eventos = eventos.get_events()
    if not lista_eventos:
        print("No hay eventos registrados")
        return

    print("\n" + "=" * 60)
    print("INFORME FINAL - JUEGOS OLÍMPICOS PARÍS 2024")
    print("=" * 60)

    # Resumen general
    print("\nRESUMEN GENERAL:")
    print(f"Eventos registrados: {len(lista_eventos)}")
    print(f"Participantes registrados: {len(participantes.get_participantes())}")

    # Medallero
    if medallero.countries:
        print("\nMEDALLERO POR PAÍSES:")
        print(f"   {'País':<20} {'Oro':<10} {'Plata':<10} {'Bronce':<10} {'Total':<10}")
        print("   " + "-" * 60)

        ranking = sorted(
            medallero.countries.items(),
            key=lambda x: (x[1]["oro"], x[1]["plata"], x[1]["bronce"]),
            reverse=True,
        )

        for pais, medallas in ranking:
            total = medallas["oro"] + medallas["plata"] + medallas["bronce"]
            print(
                f"   {pais.capitalize():<20} {medallas['oro']:<10} {medallas['plata']:<10} {medallas['bronce']:<10} {total:<10}"
            )

    print("\n" + "=" * 60)


def cargar_datos_prueba(eventos: Eventos, participantes: Participantes) -> None:
    """
    Función que precarga datos de prueba para el simulador
    - 3 eventos deportivos
    - 10 participantes de diversos países
    """
    print("\nCargando datos de prueba...")

    # ========== EVENTOS ==========
    evento1 = Event("100m lisos")
    evento2 = Event("natación 200m")
    evento3 = Event("salto en largo")

    eventos.add_event(evento1)
    eventos.add_event(evento2)
    eventos.add_event(evento3)

    # ========== PARTICIPANTES ==========
    # Participante 1
    p1 = Participante("usain bolt", "jamaica", "atletismo")
    p1.add_evento(evento1)
    participantes.add_participante(p1)

    # Participante 2
    p2 = Participante("tyson gay", "estados unidos", "atletismo")
    p2.add_evento(evento1)
    participantes.add_participante(p2)

    # Participante 3
    p3 = Participante("yohan blake", "jamaica", "atletismo")
    p3.add_evento(evento1)
    participantes.add_participante(p3)

    # Participante 4
    p4 = Participante("justin gatlin", "estados unidos", "atletismo")
    p4.add_evento(evento1)
    participantes.add_participante(p4)

    # Participante 5
    p5 = Participante("michael phelps", "estados unidos", "natación")
    p5.add_evento(evento2)
    participantes.add_participante(p5)

    # Participante 6
    p6 = Participante("ryan lochte", "estados unidos", "natación")
    p6.add_evento(evento2)
    participantes.add_participante(p6)

    # Participante 7
    p7 = Participante("sun yang", "china", "natación")
    p7.add_evento(evento2)
    participantes.add_participante(p7)

    # Participante 8
    p8 = Participante("chad le clos", "sudáfrica", "natación")
    p8.add_evento(evento2)
    participantes.add_participante(p8)

    # Participante 9
    p9 = Participante("carl lewis", "estados unidos", "atletismo")
    p9.add_evento(evento1)  # También participa en 100m
    p9.add_evento(evento3)  # Salto en largo
    participantes.add_participante(p9)

    # Participante 10
    p10 = Participante("mike powell", "estados unidos", "atletismo")
    p10.add_evento(evento3)
    participantes.add_participante(p10)

    # Participantes adicionales para salto en largo (para completar mínimo 3)
    p11 = Participante("bob beamon", "estados unidos", "atletismo")
    p11.add_evento(evento3)
    participantes.add_participante(p11)

    p12 = Participante("ivan pedroso", "cuba", "atletismo")
    p12.add_evento(evento3)
    participantes.add_participante(p12)

    print("Datos de prueba cargados correctamente")
    print(f" Eventos: {len(eventos)}")
    print(f" Participantes: {len(participantes.get_participantes())}")
    print("\n Ahora puedes ir directamente a la opción 3 para simular eventos")


def main() -> None:
    """Función principal que ejecuta el simulador."""
    print("¡Bienvenido al Simulador de Juegos Olímpicos!")

    # Inicializar estructuras de datos
    eventos = Eventos()
    participantes = Participantes()
    medallero = Medallero()

    # cargar datos de prueba
    print("\n¿Desea cargar datos de prueba?")
    print("1. Sí - Cargar datos precargados (3 eventos, 12 participantes)")
    print("2. No - Comenzar con datos vacíos")

    opcion_inicial = input("\nSeleccione una opción (1 o 2): ").strip()

    if opcion_inicial == "1":
        cargar_datos_prueba(eventos, participantes)
    else:
        print(
            "\nIniciando con datos vacíos. Use el menú para registrar eventos y participantes."
        )

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ").strip()

        if opcion == "1":
            registrar_evento(eventos)
        elif opcion == "2":
            registrar_participante(participantes, eventos)
        elif opcion == "3":
            simular_eventos(participantes, eventos, medallero)
        elif opcion == "4":
            generar_informe(participantes, eventos, medallero)
        elif opcion == "5":
            print("\n¡Gracias por usar el simulador! Hasta pronto.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")


if __name__ == "__main__":
    main()
