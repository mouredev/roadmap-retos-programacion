// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

"use strict";

/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA:
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

// Interfaz para el servicio de notificación (usando clases abstractas en ES6)
class NotificationService {
    sendNotification(message) {
        throw new Error('Método no implementado');
    }
}

// Implementación específica para Email
class EmailNotification extends NotificationService {
    sendNotification(message) {
        console.log(`[+] - Enviando Email: ${message}`);
    }
}

// Implementación específica para PUSH
class PushNotification extends NotificationService {
    sendNotification(message) {
        console.log(`[+] - Enviando Push Notification: ${message}`);
    }
}

// Implementación específica para SMS
class SMSNotification extends NotificationService {
    sendNotification(message) {
        console.log(`[+] - Enviando SMS: ${message}`);
    }
}

// Sistema de Notificaciones usando DIP
class NotificationSystem {
    constructor() {
        this.services = [];
    }

    addService(service) {
        this.services.push(service);
    }

    notifyAll(message) {
        this.services.forEach(service => service.sendNotification(message));
    }
}

// Función principal para demostrar el DIP
(() => {
    // Correcto: El sistema de notificaciones no depende directamente de las implementaciones concretas
    const notificationSystem = new NotificationSystem();

    notificationSystem.addService(new EmailNotification());
    notificationSystem.addService(new PushNotification());
    notificationSystem.addService(new SMSNotification());

    notificationSystem.notifyAll('Mensaje de prueba.');

    // Incorrecto: Dependencia directa de las implementaciones concretas (violación del DIP)
    const emailNotification = new EmailNotification();
    emailNotification.sendNotification('Mensaje directo sin sistema de notificaciones.');
})();
