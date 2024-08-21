'''
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
'''



if __name__ == '__main__':
    print("Simulación de Juegos Olímpicos")
    while True:

        print("""
        1. Registro de eventos.
        2. Registro de participantes.
        3. Simulación de eventos.
        4. Creación de informes.
        5. Salir del programa.
        """)

        option = input("Seleccione una opción: ")

        match option:
            case "1":
                print("Registro de eventos")
            case "2":
                print("Registro de participantes")
            case "3":
                print("Simulación de eventos")
            case "4":
                print("Creación de informes")
            case "5":
                print("Saliendo del simulador...")
                break
            case _:
                print("Opción no válida, seleccione una opción del menú")