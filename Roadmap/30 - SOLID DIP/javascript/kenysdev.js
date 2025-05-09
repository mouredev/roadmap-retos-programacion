/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#30 SOLID: PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS (DIP)
-------------------------------------------------------
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
// ________________________________________________________
// SIN APLICAR DIP
// ---------------
// Clase concreta
class FileStorage_ {
    save(data) {
        console.log(`Datos guardados en archivo: ${data}`);
    }
}

// Clase de alto nivel 
class DataManager_ {
    constructor() {
        // Dependencia directa de la clase concreta.
        this.fileStorage = new FileStorage_();
    }

    storeData(data) {
        this.fileStorage.save(data);
    }
}

// ________________________________________________________
// APLICANDO DIP
// ---------------
// Abstracción
class AbcStorage {
    save(data) {
        throw new Error("El método 'save' debe ser implementado.");
    }
}

// Implementación concreta
class FileStorage extends AbcStorage {
    save(data) {
        console.log(`Guardado en archivo: ${data}`);
    }
}

// Implementación concreta
class DatabaseStorage extends AbcStorage {
    save(data) {
        console.log(`Guardado en base de datos: ${data}`);
    }
}

// Clase de alto nivel
class DataManager {
    constructor(storage) {
        // Dependencia de la abstracción
        if (!(storage instanceof AbcStorage)) {
            throw new Error("La dependencia debe implementar AbcStorage");
        }
        this.storage = storage;
    }

    storeData(data) {
        this.storage.save(data);
    }
}

// Uso
const dataToStore = "Ejemplo de datos x";
const fileStorage = new FileStorage();
const dataManagerFile = new DataManager(fileStorage);
dataManagerFile.storeData(dataToStore);
const databaseStorage = new DatabaseStorage();
const dataManagerDatabase = new DataManager(databaseStorage);
dataManagerDatabase.storeData(dataToStore);

// ________________________________________________________
// DIFICULTAD EXTRA
// ----------------

// Abstracción
class AbcMessageService {
    send(to, message) {
        throw new Error("El método 'send' debe ser implementado.");
    }
}

// Implementación: Email
class EmailService extends AbcMessageService {
    send(to, message) {
        console.log("Correo enviado a:", to);
        console.log("Mensaje:", message);
    }
}

// Implementación: PUSH
class PUSHService extends AbcMessageService {
    send(to, message) {
        console.log("Notificación PUSH enviada a:", to);
        console.log("Mensaje:", message);
    }
}

// Implementación: SMS
class SMSService extends AbcMessageService {
    send(to, message) {
        console.log("Mensaje SMS enviado a:", to);
        console.log("Mensaje:", message);
    }
}

// Módulo de alto nivel
class NotificationSystem {
    constructor(service) {
        if (!(service instanceof AbcMessageService)) {
            throw new Error("La dependencia debe implementar AbcMessageService");
        }
        this.service = service;
    }

    notify(to, message) {
        this.service.send(to, message);
    }
}

// Inyección de dependencias
function testNotificationSystem(to, message, service) {
    const serviceNotifier = new NotificationSystem(service);
    serviceNotifier.notify(to, message);
}

console.log("\nDIFICULTAD EXTRA");

// Asignación
const emailService = new EmailService();
const pushService = new PUSHService();
const smsService = new SMSService();

// Comprobación:
testNotificationSystem("ejm@gg.com", "abcdsf", emailService);
testNotificationSystem("user01", "123456", pushService);
testNotificationSystem(123456789, "aeiou", smsService);
