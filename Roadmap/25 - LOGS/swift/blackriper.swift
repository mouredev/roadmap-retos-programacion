/*
 Logs 
 Los logs  son mensajes que sirven como historial de eventos de nuestra aplicacion en el tiempo 
 los logs se clasifican en 
 - debug
 - info
 - warning
 - error

 para mas informacion te invito a revisar mi ejercicio blackriper.kt donde explico mas sobre los logs
 
 recursos 

 documentacion https://www.swift.org/documentation/server/guides/libraries/log-levels.html
 package swift log https://github.com/apple/swift-log

 */
 
 import Logging
 
 

 
  func exampleWithLogging() {
         // declaramos la clase Logger y pasamos el paquete/nombre del archivo
         let logger = Logger(label: "blackriper ")
  
        // seguimiento de un evento 
        logger.trace("Trace message")
        // informar sobre alguna prueba 
        logger.debug("Debug message")
        // informar sobre un evento 
        logger.info("Info message")
        // notifcar sobre algo ocurrido
        logger.notice("Notice message")
        //informar sobre algun evento que eventualmente puede causar un errorº
        logger.warning("Warning message")
        // informar sobre un error
        logger.error("Error message")
        // informar sobre un error critico maxima prioridad
        logger.critical("Critical message")
        
    }
    
    exampleWithLoggin()
    
    
    // ejercicio extra 
    
    protocol ManagerTask{
    func addTask(_ task:Task)->Bool
    func removeTask(name:String)->Bool
    func completeTask(name:String)->Bool
 }

 struct Task{
      let name :String 
      let description :String
      var done :Bool = false
    }


class TaskManager:ManagerTask{
    private let logger = Logger(label: "logs ")
    var tasks:[Task] = []

    func addTask(_ task:Task)->Bool{
      tasks.append(task)
      logger.notice("Task \(task.name) added")
      return true
    }
    func removeTask(name:String)->Bool{
     tasks.removeAll(where: {$0.name == name})
     logger.notice("Task \(name) removed")
     return true
    }
    func completeTask(name:String)->Bool{
       if var task = tasks.first(where: {$0.name == name}){
           task.done = true
           logger.info("Task \(name) completed")
           return true
       }
       logger.error("Task \(name) not found")
        return false
    }
}
    
let manager = TaskManager()    
manager.addTask(Task( name:"Swift Data module",description: "write module swift data"))
manager.addTask(Task(name: "Swift UI module", description: "write module swift ui"))
manager.completeTask(name: "Swift UI module")
manager.completeTask(name: "Kotlin")

    
    
    
