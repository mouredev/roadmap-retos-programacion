import Foundation
/*
 La asincronia es  la capacidad de ejecutar una tarea en segundo plano, sin detener la ejecucion de la aplicacion.
 los conceptos mas comunes que podemos encontrar son:

  - Asincronia tarea no bloqueante que permite seguir ejecutando el hilo principal  sin que esta tarea 
    se haya concluido estos hilos secundarios siguen dependiendo del hilo principal.
   
   -Concurrencia:  tambien es una tarea no bloqueante que puede o no puede depender el hilo principal.
   a diferencia de la asincronia la concurrencia no ejecuta la tarea de forma ordenada.

   - Paralelismo: es la capacidad de ejecutar tareas de manera silmutanea a diferencia de las anteriores 
   esta se ejecuta de forma separada al hilo principal esto quiere decir que tiene su propio espacio en 
   memoria y procesamiento de computo.
  
 */

  func runTask(_ nameTask: String, duration:Double) async throws -> Bool {
      let clock = ContinuousClock()
      var isCompleted = false

      let time = try await clock.measure {
         print("Starting task: \(nameTask)")
         try await Task.sleep(for: .seconds(duration))
         print("Finished task: \(nameTask)")
         isCompleted = true
      } 
      print("Task \(nameTask) took \(time) seconds")
      return isCompleted
   }
 
   let completed = try await runTask("Task 1", duration: 1);if completed {
        print("Task completed")
    }
   
  // reto extra para correr alguna tarea en paralelo solo es necesario poner async antes de la tarea
   async let isCompletedC = runTask("Task C", duration: 3)
   async let isCompletedB = runTask("Task B", duration: 2)
   async let isCompletedA = runTask("Task A", duration: 1)
   
   // alamcenar los resultados de las tareas 
   let isCompleted =  try await [isCompletedA, isCompletedB, isCompletedC]

  // comprobar que todas las tareas se han completado si todos los valores son true ejecutara la ultima tarea 
   if isCompleted.allSatisfy({$0==true}){
       let isCompleted = try await runTask("Task D", duration: 1); if isCompleted{
           print("All tasks completed.")
        }
    } 




   
