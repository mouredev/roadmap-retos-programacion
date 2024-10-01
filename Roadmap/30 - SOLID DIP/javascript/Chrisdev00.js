/*
* EJERCICIO:
* Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
* Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
* de forma correcta e incorrecta.
*
* DIFICULTAD EXTRA (opcional):
* Crea un sistema de notificaciones.
* Requisitos:
* 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
* 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
* Instrucciones:
* 1. Crea la interfaz o clase abstracta.
* 2. Desarrolla las implementaciones específicas.
* 3. Crea el sistema de notificaciones usando el DIP.
* 4. Desarrolla un código que compruebe que se cumple el principio.
*/

// Forma Incorrecta de aplicar el principio DIP

class Backend {
    getData() {
      return "Datos del backend";
    }
}

class Frontend {
    constructor() {
      this.backend = new Backend();
    }
  
    displayData() {
      console.log(this.backend.getData());
    }
}

const frontend1 = new Frontend();
frontend1.displayData();


// Forma Correcta de implementar el principio DIP

class DataService {
    getData() {
      throw new Error("Método no implementado");
    }
}

class Backend extends DataService {
    getData() {
      return "Datos del backend";
    }
}

class Frontend {
    constructor(dataService) {
      this.dataService = dataService;
    }
  
    displayData() {
      console.log(this.dataService.getData());
    }
}

const backend = new Backend();
const frontend = new Frontend(backend);
frontend.displayData();
  
  
//////////////////// ----------------------------- EXTRA ---------------------------------------- ///////////////


// Clase abstracta NotificationService
class NotificationService {
    sendNotification(message) {
      throw new Error("Método no implementado");
    }
}

class EmailNotification extends NotificationService {
    sendNotification(message) {
      console.log(`Enviando email con mensaje: ${message}`);
    }
}

class PushNotification extends NotificationService {
    sendNotification(message) {
      console.log(`Enviando notificación PUSH con mensaje: ${message}`);
    }
}

class SMSNotification extends NotificationService {
    sendNotification(message) {
      console.log(`Enviando SMS con mensaje: ${message}`);
    }
}

class NotificationSystem {
    constructor(notificationService) {
      this.notificationService = notificationService;
    }
  
    notify(message) {
      this.notificationService.sendNotification(message);
    }
}

const emailService = new EmailNotification();
const emailNotificationSystem = new NotificationSystem(emailService);
emailNotificationSystem.notify("Este es un mensaje de prueba por Email.");

const pushService = new PushNotification();
const pushNotificationSystem = new NotificationSystem(pushService);
pushNotificationSystem.notify("Este es un mensaje de prueba por PUSH.");

const smsService = new SMSNotification();
const smsNotificationSystem = new NotificationSystem(smsService);
smsNotificationSystem.notify("Este es un mensaje de prueba por SMS.");

  
  
  