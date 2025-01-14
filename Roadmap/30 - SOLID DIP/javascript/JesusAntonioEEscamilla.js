/** #30 - JavaScript -> Jesus Antonio Escamilla */

/**
 * Este principio establece dos reglas clave:
 * 1-. Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones (interfaces).
 * 2-. Las abstracciones no deben depender de detalles. Los detalles deben depender de abstracciones.
 */

//---EJERCIÓ---
//INCORRECTO
// Creamos un modelo para usarlo
class PdfReport__{
   generate(content){
      console.log(`Generating PDF report with content: ${content}`);
   }
}

// Creamos un objeto
class ReportGenerator__{
   constructor(pdfReport){
      this.pdfReport = pdfReport;
   }

   generateReport(content){
      this.pdfReport.generate(content);
   }
}

// El uso Incorrecto de DIP
const pdfReport__ = new PdfReport__();
const reportGenerator__ = new ReportGenerator__(pdfReport__);
reportGenerator__.generateReport("Annual Financial Report");


//CORRECTO
// Interfaz del Report
class IReport{
   generate(content){
      throw new Error("Method 'generate()' must be implemented");
   }
}

// Implementación Correcta de DIP
class PdfReport extends IReport{
   generate(content){
      console.log(`Generating PDF report with content: ${content}`);
   }
}

class HtmlReport extends IReport{
   generate(content){
      console.log(`Generating HTML report with content: ${content}`);
   }
}

class ReportGenerator{
   constructor(report){
      // Dependencia de la abstraction
      if (!(report instanceof IReport)) {
         throw new Error("Invalid report service");
      }
      this.report = report;
   }

   generateReport(content){
      this.report.generate(content);
   }
}

// El uso Correcto de DIP
const pdfReport = new PdfReport();
const htmlReport = new HtmlReport();

const reportGenerator = new ReportGenerator(pdfReport);
reportGenerator.generateReport("Monthly Financial Report");

const htmlReportGenerator = new ReportGenerator(htmlReport);
htmlReportGenerator.generateReport("Weekly Financial Report")



/**-----DIFICULTAD EXTRA-----*/

// Interfaz
class INotificacionService{
   sendNotificacion(user, message){
      throw new Error("Method 'sendNotificacion()' must be implemented");
   }
}

// Implementación Especifica
class EmailService extends INotificacionService{
   sendNotificacion(user, message){
      console.log(`Sending Email to ${user.email}: ${message}`);
   }
}

class PushService extends INotificacionService{
   sendNotificacion(user, message){
      console.log(`Sending Email to ${user.deviceId}: ${message}`);
   }
}

class SmsService extends INotificacionService{
   sendNotificacion(user, message){
      console.log(`Sending Email to ${user.phoneNumber}: ${message}`);
   }
}

// Sistema de Notificacion
class NotificationSystem{
   constructor(notificationService){
      if (!(notificationService instanceof INotificacionService)) {
         throw new Error("Invalid notification service");
      }
      this.notificationService = notificationService;
   }

   notify(user, message){
      this.notificationService.sendNotificacion(user, message);
   }
}

// Creando un usuario
const user = {
   email: "jesus@example.com",
   deviceId: "antonio123",
   phoneNumber: "1234567890"
}

// Instanciando servicios
const emailService = new EmailService();
const pushService = new PushService();
const smsService = new SmsService();

// Creando sistema de notificaciones
const emailNotificationSystem = new NotificationSystem(emailService);
const pushNotificationSystem = new NotificationSystem(pushService);
const smsNotificationSystem = new NotificationSystem(smsService);

// Usando el sistema
emailNotificationSystem.notify(user, "Welcome via Email!");
pushNotificationSystem.notify(user, "Welcome via PUSH notificacion!");
smsNotificationSystem.notify(user, "Welcome via SMS!");

/**-----DIFICULTAD EXTRA-----*/