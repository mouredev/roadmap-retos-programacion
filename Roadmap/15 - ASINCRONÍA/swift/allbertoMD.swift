import Foundation

/*
NOTA:
Para el correcto funcionamiento de este programa se debe ejecutar en un playground, no en consola.
*/

// Función para simular una ejecución asincrónica de una tarea que toma un cierto tiempo.
func execute(functionNmae name: String, durationInSeconds secondsDuration: Int) async {
    
    let start = Date()
    let formatter = DateFormatter()
    formatter.dateFormat = "HH:mm:ss" // Formato personalizado para la hora.
    
    print("Función \(name) iniciada a las \(formatter.string(from: start))")
    print("Duración estimada: \(secondsDuration) segundos")
    
    // Simulamos la ejecución de la función con un retraso.
    do {
        try await Task.sleep(for: .seconds(secondsDuration))
    } catch {
        print("Error durante la simulación: \(error)")
    }
    
    let end = Date()
    
    print("Función \(name) finalizada a las \(formatter.string(from: end))")
    print("Tiempo de ejecución de la función \(name): \(Int(end.timeIntervalSince(start))) segundos")
}

// Ejecutamos las funciones de forma asíncrona.
Task {
    await execute(functionNmae: "Tarea1", durationInSeconds: 5)
    print("Todas las funciones han finalizado!")
}

// Tiempo de margen para que le de tiempo a ejecutarse la función Tarea1.
sleep(10)




// DIFICULTAD EXTRA.
print("\nDIFICULTAD EXTRA.\n")




// Función para simular una ejecución asincrónica de una tarea que toma un cierto tiempo.
func executeTask(name: String, durationInSeconds secondsDuration: Int) async {
    
    let start = Date()
    let formater = DateFormatter()
    formater.dateFormat = "HH:mm:ss"
    
    print("Función \(name) iniciada a las \(formater.string(from: start)).")
    print("Tiempo estimado de la función \(name): \(secondsDuration).")
    
    do {
        try await Task.sleep(for: .seconds(secondsDuration))
    } catch {
        print("Error -> \(error)")
    }
    
    let end = Date()
    
    print("Funcion \(name) finalizada a las \(formater.string(from: end)).")
    print("Tiempo de ejecución de la función \(name): \(Int(end.timeIntervalSince(start)))" + (secondsDuration == 1 ? " segundo." : " segundos."))
}

// Función que ejecuta las tareas en paralelo y luego ejecuta la tarea D.
func executeTasks() async {
    
    // Ejecutar las funciones C, B y A en paralelo
    await withTaskGroup(of: Void.self) { group in
        group.addTask {
            await executeTask(name: "C", durationInSeconds: 3)
        }
        group.addTask {
            await executeTask(name: "B", durationInSeconds: 2)
        }
        group.addTask {
            await executeTask(name: "A", durationInSeconds: 1)
        }
    }
    
    // Cuando todas las tareas C, B y A han finalizado, ejecutar la función D.
    await executeTask(name: "D", durationInSeconds: 1)
}

// Ejecutar la función que lanza las funciones C, B y A en paralelo y luego la D.
Task {
    await executeTasks()
    print("Todas las funciones han finalizado!")
}
