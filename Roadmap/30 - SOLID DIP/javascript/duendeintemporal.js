//#30 - Principio SOLID de Inversión de Dependencias (Dependency Inversion Principle (DIP))
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
//Bibliografy: The Web Development Glossary (Jens Oliver Meiert) (Z-Library)
//GPT

/* Dependency Inversion Principle
A specific form of decoupling software modules. When following this
principle, the conventional dependency relationships established from
high-level policy-setting modules to low-level dependency modules are
reversed, thus rendering high-level modules independent of the low-level
module implementation details. The principle states 1) that high-level
modules should not depend on low-level modules, but that both should
depend on abstractions (e.g., interfaces), and 2) that abstractions should
not depend on details, but that details (concrete implementations) should
depend on abstractions.

A class that contains methods for use by other classes without having to be
the parent class of those other classes. How those other classes gain access
to the mixin’s methods depends on the language. Mixins are sometimes
described as being “included” rather than “inherited.” Mixins encourage
code reuse and can be used to avoid the inheritance ambiguity that
multiple inheritance can cause, or to work around lack of support for
multiple inheritance in a language. A mixin can also be viewed as an
interface with implemented methods. This pattern is an example of
enforcing the Dependency Inversion Principle */

let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #30.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #30. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #30'); 
});

//Incorrect Example

class USABillingService1 {
    calculateCharge(duration) {
        return duration * 0.10; // $0.10 per minute
    }
}

class CallBillingService1 {
    constructor() {
        this.billingService = new USABillingService1(); // Direct dependency
    }

    billCall(duration) {
        const charge = this.billingService.calculateCharge(duration);
        log(`Total charge: ${charge.toFixed(2)}`);
    }
}

const callBillingService1 = new CallBillingService1();
callBillingService1.billCall(22); // Total charge: 2.20


//Correct Example

class IBillingService {
    calculateCharge(duration) {
        throw new Error("Method 'calculateCharge()' must be implemented for this Billing Service.");
    }
}

class USABillingService extends IBillingService {
    constructor(){
        super();
        this.location = 'USA';
    }

    calculateCharge(duration) {
        return duration * 0.10; 
    }
}

class EuropeBillingService extends IBillingService {
    constructor() {
        super();
        this.location = 'Europe';
    }

    calculateCharge(duration) {
        return duration * 0.15; 
    }
}

class AsiaBillingService extends IBillingService {
    constructor() {
        super();
        this.location = 'Asia';
    }

    calculateCharge(duration) {
        return duration * 0.05; 
    }
}

class CallBillingService {
    constructor(billingService) {
        this.billingService = billingService; // Dependency injection
    }

    billCall(duration) {
        const charge = this.billingService.calculateCharge(duration);
        log(`Total charge for ${this.billingService.location}: ${charge.toFixed(2)}`);
    }
}

const usaBillingService = new USABillingService();
const europeBillingService = new EuropeBillingService();
const asiaBillingService = new AsiaBillingService();

const callBillingServiceUSA = new CallBillingService(usaBillingService);
const callBillingServiceEurope = new CallBillingService(europeBillingService);
const callBillingServiceAsia = new CallBillingService(asiaBillingService);

callBillingServiceUSA.billCall(127.22); // Total charge for USA: 12.72
callBillingServiceEurope.billCall(17.56); // Total charge for Europe: 2.63
callBillingServiceAsia.billCall(45.23); // Total charge for Asia: 2.26


//Extra Dificulty Exercise
class INotificationService {
    send(message) {
        throw new Error("Method 'send()' must be implemented in this especific Notification Service.");
    }
}

class EmailService extends INotificationService {
    send(message) {
        log(`Sending email: ${message}`);
    }
}

class SMSService extends INotificationService {
    send(message) {
        log(`Sending SMS: ${message}`);
    }
}

class PushService extends INotificationService {
    send(message) {
        log(`Sending PUSH notification: ${message}`);
    }
}

class NotificationSystem {
    constructor(notificationService) {
        this.notificationService = notificationService;
    }

    notify(message) {
        this.notificationService.send(message);
    }
}

const emailService = new EmailService();
const smsService = new SMSService();
const pushService = new PushService();

const notificationSystemEmail = new NotificationSystem(emailService);
const notificationSystemSMS = new NotificationSystem(smsService);
const notificationSystemPush = new NotificationSystem(pushService);

notificationSystemEmail.notify("Testing sending a message via Email."); // Sending email: Testing sending a message via Email.
notificationSystemSMS.notify("Testing sending a message via SMS."); // Sending SMS: Testing sending a message via SMS.
notificationSystemPush.notify("Testing sending a message via PUSH."); // Sending PUSH notification: Testing sending a message via PUSH.
