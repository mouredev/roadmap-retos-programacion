/** #29 - JavaScript -> Jesus Antonio Escamilla */

/**
 * El ISP establece que una clase no debe estar obligada a implementar interfaces que no utiliza.
 * En otras palabras, es mejor tener interfaces más pequeñas y específicas que interfaces grandes y generales.
 */

//---EJERCIÓ---
// INCORRECTO
// Interfaz general
class IWorker{
   work(){
      throw new Error("Method not implemented");
   }

   attendMeeting(){
      throw new Error("Method not implemented");
   }

   writeCode(){
      throw new Error("Method not implemented");
   }
}

// Clase que implementa interfaz general
class Manager__ extends IWorker{
   work(){
      console.log("Manager working on project management");
   }

   attendMeeting(){
      console.log("Manager attending a meeting");
   }

   writeCode(){
      throw new Error("Manager does not write code");
   }
}

class Developer__ extends IWorker{
   work(){
      console.log("Developer working on coding");
   }

   attendMeeting(){
      throw new Error("Developer does not attend meetings");
   }

   writeCode(){
      console.log("Developer writing code");
   }
}

// Uso Incorrecto de ISP
const basicPrinter__ = new Manager__();
basicPrinter__.work();
basicPrinter__.attendMeeting();

const advancedPrinter = new Developer__();
advancedPrinter.work();
advancedPrinter.writeCode();


// CORRECTO
// Interfaz general
class IWork{
   work(){
      throw new Error("Method not implemented");
   }
}

class IAttendMeeting{
   attendMeeting(){
      throw new Error("Method not implemented");
   }
}

class IWriteCode{
   writeCode(){
      throw new Error("Method not implemented");
   }
}

// Clase que implementa interfaz general
class Manager extends IWork{
   work(){
      console.log("Manager working on project management");
   }
}

class ManagerMeeting extends IAttendMeeting{
   attendMeeting(){
      console.log("Manager attending a meeting");
   }
}

class Developer extends IWriteCode{
   work(){
      console.log("Developer working on coding");
   }
}

class DeveloperCoding extends IWriteCode{
   writeCode(){
      console.log("Developer writing code")
   }
}

// Uso Correcto de ISP
const manager = new Manager();
manager.work();

const managerMeeting = new ManagerMeeting();
managerMeeting.attendMeeting();

const developer = new Developer();
developer.work();

const developerCoding = new DeveloperCoding();
developerCoding.writeCode();



/**-----DIFICULTAD EXTRA-----*/

// Pendiente

/**-----DIFICULTAD EXTRA-----*/