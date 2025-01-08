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

import Foundation

// Función asíncrona
func asyncFunction(name: String, duration: Int) {
    let startTime = Date()
    print("La función '\(name)' ha empezado a las \(startTime) y durará \(duration) segundos.")

    // Simula una tarea larga usando sleep
    sleep(UInt32(duration))
    
    let endTime = Date()
    print("La función '\(name)' ha terminado a las \(endTime).")
}

// Función que ejecuta la función asíncrona
func executeAsyncFunction(name: String, duration: Int) {
    DispatchQueue.global().async {
        asyncFunction(name: name, duration: duration)
    }
}

// Ejemplo de uso
executeAsyncFunction(name: "Tarea 1", duration: 5)
executeAsyncFunction(name: "Tarea 2", duration: 3)

// Mantén el programa en ejecución para que puedas ver el resultado de las funciones asíncronas
RunLoop.current.run(until: Date().addingTimeInterval(10))

//MARK: - DIFICULTAD EXTRA (opcional)

// Función asíncrona 👇
func asyncFunction(name: String, duration: Int, completion: @escaping () -> Void) {
    let startTime = Date()
    print("La función '\(name)' ha empezado a las \(startTime) y durará \(duration) segundos.")
    
    // Simula una tarea larga usando el metodo sleep
    sleep(UInt32(duration))
    
    let endTime = Date()
    print("La función '\(name)' ha terminado a las \(endTime).")
    
    // Llama al completion 'handler' al finalizar
    completion()
}

// Ejecuta la función asíncrona con un DispatchGroup
func executeAsyncFunction(name: String, duration: Int, group: DispatchGroup) {
    group.enter()
    DispatchQueue.global().async {
        asyncFunction(name: name, duration: duration) {
            group.leave()
        }
    }
}

// Crear un DispatchGroup para sincronizar las tareas
let group = DispatchGroup()

// Ejecutar funciones C, B y A en paralelo
executeAsyncFunction(name: "C", duration: 3, group: group)
executeAsyncFunction(name: "B", duration: 2, group: group)
executeAsyncFunction(name: "A", duration: 1, group: group)

// Ejecutar la función D después de que C, B y A hayan finalizado
group.notify(queue: DispatchQueue.global()) {
    asyncFunction(name: "D", duration: 1) {
        print("Todas las funciones han terminado.")
    }
}

// Mantén el programa en ejecución para ver los resultados
RunLoop.current.run(until: Date().addingTimeInterval(10))

