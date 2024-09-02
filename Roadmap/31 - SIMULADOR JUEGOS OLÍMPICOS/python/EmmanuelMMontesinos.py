"""
/*
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
 */
"""
from random import choice

class Participantes:
    lista = []

    def __init__(self, nombre:str, pais:str) -> None:
        self.nombre = nombre
        self.pais = pais

        # Agrega el nuevo participante a lista
        Participantes.lista.append(self)

        # Si no esta el pais en top_paises lo crea
        if pais not in Medallas.top_paises:
            Medallas.top_paises[pais] = {"oro":0,"plata":0,"bronce":0}

class Medallas:
    top_paises = {}

    def __init__(
            self,nombre:str, oro:Participantes, plata:Participantes, bronce:Participantes
            ) -> None:
        self.evento = nombre
        self.oro = oro
        self.plata = plata
        self.bronce = bronce

class Eventos:
    lista = []

    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
        self.finalizado = False
        Eventos.lista.append(self)
    
    def decidir_ganador(self):
        lista_participantes = Participantes.lista.copy()

        if not self.finalizado:
            try:
                ganadores = []

                for n in range(3):
                    elegido = choice(lista_participantes)
                    lista_participantes.remove(elegido)
                    ganadores.append(elegido)

                oro, plata, bronce = ganadores
                registro = Medallas(self.nombre,oro,plata,bronce)
                self.finalizado = True
                return registro
            
            except Exception as e:
                print(f"Se necesitan al menos 3 participantes\nNº de participantes actuales: {len(Participantes.lista)}")
                print(e)

class Juegos:
    registro_finalizados = []
    eventos_finalizados = []
    def registrar_evento(self,nombre:str):
        nuevo_evento = Eventos(nombre)
        print(f"Evento {nuevo_evento.nombre} se ha registrado")

    def registrar_participante(self,nombre:str,pais:str):
        nuevo_participante = Participantes(nombre,pais)
        print(f"{nuevo_participante.nombre} de {pais} se ha registrado")

    def simular_evento(self,nombre_evento:str):
        evento = None
        for eventos in Eventos.lista:
            if eventos.nombre == nombre_evento:
                evento = eventos
        if evento:
            medallas = evento.decidir_ganador()
            if medallas:
                print(f"Resultado del evento {medallas.evento}")
                print(f"Oro - {medallas.oro.nombre.title()} de {medallas.oro.pais.upper()}")
                print(f"Plata - {medallas.plata.nombre.title()} de {medallas.plata.pais.upper()}")
                print(f"Bronce - {medallas.bronce.nombre.title()} de {medallas.bronce.pais.upper()}\n")
                
                Medallas.top_paises[medallas.oro.pais]["oro"] += 1
                Medallas.top_paises[medallas.plata.pais]["plata"] += 1
                Medallas.top_paises[medallas.bronce.pais]["bronce"] += 1

                Juegos.registro_finalizados.append(medallas)
                Juegos.eventos_finalizados.append(nombre_evento)
        else:
            print(f"{nombre_evento} no esta registrado")

    def generar_informe(self):
        for medalla in Juegos.registro_finalizados:
            print(f"Resultado del evento {medalla.evento}")
            print(f"Oro - {medalla.oro.nombre} de {medalla.oro.pais}")
            print(f"Plata - {medalla.plata.nombre} de {medalla.plata.pais}")
            print(f"Bronce - {medalla.bronce.nombre} de {medalla.bronce.pais}\n")

        print()
        print("Lista de Paises")
        # Ranking de paises por medallas de oro
        for pais,n_medallas in sorted(Medallas.top_paises.items(),key=lambda item: item[1]["oro"],reverse=True):
            print(f"{pais.title()} ---> Oro: {n_medallas["oro"]}, Plata: {n_medallas["plata"]}, Bronce: {n_medallas["bronce"]}")

def hacer_olimpiadas():
    juego = Juegos()
    salir = False
    print("Bienvenido a las olimpiadas")
    while not salir:
        print("\nSelecciona una opcion:")
        print("1- Registrar Evento")
        print("2- Registrar Participante")
        print("3- Empezar Evento")
        print("4- Mostrar Informe")
        print("5- Salir")
        seleccion = input("")

        if seleccion == "1":
            nombre_evento = input("Ponga el nombre del Evento:\n")
            juego.registrar_evento(nombre_evento.lower())
            print(f"{nombre_evento} ha sido registrado")
            
        elif seleccion == "2":
            nombre_participante = input("Ponga el nombre del participante:\n")
            pais_participante = input("Ponga el nombre del pais:\n")
            juego.registrar_participante(nombre_participante.lower(),pais_participante.lower())
            print(f"{nombre_participante} de {pais_participante} ha sido registrado")
            
        elif seleccion == "3":
            for evento in Eventos.lista:
                if evento.nombre not in Juegos.eventos_finalizados:
                    print(f"{evento.nombre.title()}")
                
            seleccion_evento = input("Indique el nombre de un evento ya registrado:\n")
            if seleccion_evento not in Juegos.eventos_finalizados:
                juego.simular_evento(seleccion_evento.lower())

            else:
                print(f"{seleccion_evento} ya se ha simulado")
        elif seleccion == "4":
            juego.generar_informe()
        elif seleccion == "5":
            salir = True
        else:
            print("Seleccione una de las opciones anteriores\n")

if __name__ == "__main__":
    hacer_olimpiadas()