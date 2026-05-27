# ```
# /*
#  * EJERCICIO:
#  * ¡Los JJOO de París 2024 han comenzado!
#  * Crea un programa que simule la celebración de los juegos.
#  * El programa debe permitir al usuario registrar eventos y participantes,
#  * realizar la simulación de los eventos asignando posiciones de manera aleatoria
#  * y generar un informe final. Todo ello por terminal.
#  * Requisitos:
#  * 1. Registrar eventos deportivos.
#  * 2. Registrar participantes por nombre y país.
#  * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
#  * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
#  * 5. Mostrar los ganadores por cada evento.
#  * 6. Mostrar el ranking de países según el número de medallas.
#  * Acciones:
#  * 1. Registro de eventos. ✅
#  * 2. Registro de participantes. ✅
#  * 3. Simulación de eventos. ✅
#  * 4. Creación de informes.
#  * 5. Salir del programa. ✅
#  */
# ```

import random

class Participante:
    def __init__(self, nombre, pais, evento):
        self.nombre = nombre
        self.pais = pais
        self.evento = evento

    def get_info(self):
        return f'{self.nombre} de {self.pais} participante: {self.evento}'

eventosDeportivos = {}
medallas = { "oro": {} , "plata": {}, "bronce": {}}

def registrarEvento():
    evento = input("Ingrese el nombre del evento: ")
    if evento not in eventosDeportivos:
        eventosDeportivos[evento] = []
    else:
        print(f"El evento '{evento}' ya esta dentro de los eventos registrados")

def registrarParticipante():
    try:
        if not eventosDeportivos:
            print('Aun no hay eventos registrados 😞')
            print('Intenta agregar uno primero para continuar')
            return

        print("Elige el evento al que quieres registrar un participante")

        for i, ev in enumerate(eventosDeportivos):
            print(f"{i + 1}. {ev}")

        eventoParticipante = int(input('Ingrese el evento seleccionado: '))

        if eventoParticipante > 0 and eventoParticipante <= (len(eventosDeportivos) + 1):
            eventoSeleccionado = list(eventosDeportivos.keys())[(eventoParticipante - 1)]
            print(f'Agregar participante para {eventoSeleccionado}')
            nombre = input("Nombre del participante: ")
            pais = input("Pais del participante: ")

            participante = Participante(nombre, pais, eventoSeleccionado)
            print(participante.get_info())
        else:
            print('Elegiste una opcion fuera de rango')
            return

        if eventoSeleccionado in eventosDeportivos:
            eventosDeportivos[eventoSeleccionado].append(participante)
        else:
            eventosDeportivos[eventoSeleccionado] = []
            eventosDeportivos[eventoSeleccionado].append(participante)
    except (ValueError, TypeError) as error:
        print('Error al registrar participante: ', error)

def simularEventos():
    
    if not eventosDeportivos:
        print("No hay eventos registrados")
        return

    for e, v in eventosDeportivos.items():
        
        if len(v) < 3:
            print(f'{e} no cumple con los participantes minimos')
            continue

        random.shuffle(v)
                
def agregarMedalla(puesto, pais):
    if pais in medallas[puesto]:
        medallas[puesto][pais] += 1
    else:
        medallas[puesto][pais] = 1

def crearInformes():
    for e, v in eventosDeportivos.items():
        if len(v) < 3:
            print(f'El evento {e} fue cancelado por incumplir con el minimo de participantes...')
            continue

        print(f'\nPosiciones finales de {e}')
        for puesto, ganador in enumerate(v[:3]):
            print(f'Puesto #{puesto + 1}: {ganador.get_info()}')
            pais = ganador.pais
            match puesto:
                case 0: 
                    agregarMedalla("oro", pais)
                case 1: 
                    agregarMedalla("plata", pais)
                case 2: 
                    agregarMedalla("bronce", pais)

    # Posiciones de paises por medallas
    for medalla, paises in medallas.items():
        posicionPaises = sorted(paises.items(),
                key=lambda item: item[1]
                ,reverse=True)
        print(f'\nRanking Paises medalla de {medalla}')
        for pais in posicionPaises:
            print(f'{pais[0]}: {pais[1]}')
    

while (True):

    print("""\nEs hora de entrar en modo JJOO!! Llego el Paris 2024\n
            Elige una de las siguientes opciones: \n
            1. Registrar Evento\n
            2. Registrar Participantes\n
            3. Simular JJOO\n
            4. Creacion de informes\n
            5. Salir
        """)

    try: 
        opcion = int(input("Ingrese una opcion: "))

        match opcion:
            case 1:
                registrarEvento()
            case 2:
                registrarParticipante()                
            case 3:
                simularEventos()
            case 4:
                crearInformes()
            case 5:
                break
            case _:
                print("Opcion equivocada")
    except (ValueError, TypeError) as error:
        print("Error", error)
