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
const manager__ = new Manager__();
manager__.work();
manager__.attendMeeting();

const developer__ = new Developer__();
developer__.work();
developer__.writeCode();


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

// Interfaces
class IPrinterBlackAndWhite{
   printBlackAndWhite(){
      throw new Error('Method not implement');
   }
}

class IPrinterColor{
   printColor(){
      throw new Error('Method not implement');
   }
}

class IScan{
   scan(){
      throw new Error('Method not implement');
   }
}

class IFax{
   sendFax(){
      throw new Error('Method not implement');
   }
}

// Implementado las Impresoras
class EpsonBlackAndWhiter extends IPrinterBlackAndWhite{
   printBlackAndWhite(){
      console.log('Epson => Imprimiendo documento a blanco y negro....');
   }
}

class CanonColor extends IPrinterBlackAndWhite{
   printColor(){
      console.log('Canon => Imprimiendo documento a color.....')
   }
}

class BrotherBlackAndWhiter extends IPrinterBlackAndWhite{
   printBlackAndWhite(){
      console.log('Brother => Imprimiendo documento a blanco y negro....');
   }
}

class BrotherColor extends IPrinterColor{
   printColor(){
      console.log('Brother => Imprimiendo documento a color....');
   }
}

class BrotherScan extends IScan{
   scan(){
      console.log('Brother => Escaneando el documento....');
   }
}

class BrotherFax extends IFax{
   sendFax(){
      console.log('Brother => Enviando el documento....');
   }
}

class MultiFunctionBrother{
   constructor() {
      this.black_white = new BrotherBlackAndWhiter();
      this.color = new BrotherColor();
      this.scan = new BrotherScan();
      this.fax = new BrotherFax();
   }

   printBlack_White(){
      this.black_white.printBlackAndWhite();
   }
   
   printColor(){
      this.color.printColor();
   }

   scanSend(){
      this.scan.scan();
   }

   faxSend(){
      this.fax.sendFax();
   }
}


// Comprobando que se cumpla ISP y correctamente
const Epson = new EpsonBlackAndWhiter();
const Cannon = new CanonColor();
const Brother = new MultiFunctionBrother();

Epson.printBlackAndWhite();
Cannon.printColor();
Brother.printBlack_White();
Brother.printColor();
Brother.scanSend();
Brother.faxSend();

/**-----DIFICULTAD EXTRA-----*/