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

// INCORRECTO
class Efectivo {
    cobrar() {
        console.log('Cobrando en efectivo');
    }
}

class Caja {
    constructor() {
        this.efectivo = new Efectivo();
    }

    cobrar() {
        this.efectivo.cobrar();
    }
}

// CORRECTO
class ICobro {
    cobrar() {
        throw Error('Debe implementar el método cobrar');
    }
}

class EfectivoDIP extends ICobro {
    cobrar() {
        console.log('Cobrando en efectivo');
    }
}

class TarjetaDIP extends ICobro {
    cobrar() {
        console.log('Cobrando con tarjeta');
    }
}

class CajaDIP {
    constructor(service) {
        this.service = service;
    }

    cobrar() {
        this.service.cobrar();
    }
}

const efectivo = new EfectivoDIP();
const tarjeta = new TarjetaDIP();
const cajaE = new CajaDIP(efectivo);
const cajaT = new CajaDIP(tarjeta);
cajaE.cobrar();
cajaT.cobrar();

console.log('-----------DIFICULTAD EXTREMA------');

class IMessage {
    send() {
        throw Error('Debe implementar el método send');
    }
}

class SMS extends IMessage {
    send() {
        console.log('Mandando SMS');
    }
}

class Push extends IMessage {
    send() {
        console.log('Mandando PUSH');
    }
}

class Email extends IMessage {
    send() {
        console.log('Mandando email');
    }
}

class Notification {
    constructor(service) {
        this.service = service;
    }

    send() {
        this.service.send();
    }
}

const sms = new SMS();
const push = new Push();
const email = new Email();

const notificationSMS = new Notification(sms);
notificationSMS.send();

const notificationPush = new Notification(push);
notificationPush.send();

const notificationEmail = new Notification(email);
notificationEmail.send();