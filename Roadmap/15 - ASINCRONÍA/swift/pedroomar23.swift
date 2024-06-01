import Foundation

/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado.
 */

func startProgram(_ name: String, duration: Double) async  {
    let iniciar = Date()
    let terminacion = Date()
    let formatter = DateFormatter()
    formatter.dateFormat = "HH:mm:ss"
    
    print("El programa dio comienzo a \(formatter.string(from: iniciar))")
    
    do {
        try await Task.sleep(for: .seconds(duration))
    } catch {
        print("Se ha encontrado un error en la ejecucion \(error.localizedDescription)")
    }
    
    print("El programa tuvo su conclusion \(formatter.string(from: terminacion))")
    print("El programa tuvo una duracion de \(duration)")
}




