/* 🔥 EJERCICIO:
Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
de forma correcta e incorrecta.
*/
console.log("----- EJEMPLO SIMPLE -----");

//  * Ejemplo Incorrecto (viola DIP): Dependencia directa
// --------------------------------------------------------------------------------------------------------------
class Bombilla {
    encender() {
        console.log("💡 Bombilla encendida.");
    }

    apagar() {
        console.log("💡 Bombilla apagada.");
    }
}

class InterruptorIncorrecto {
    constructor(bombilla) {
        this.bombilla = bombilla; // Dependencia directa a una implementación concreta
    }

    operar() {
        this.bombilla.encender();
    }
}

// Uso incorrecto
const bombilla = new Bombilla();
const interruptorIncorrecto = new InterruptorIncorrecto(bombilla);
interruptorIncorrecto.operar(); // Enciende la bombilla

// Problema: Si queremos usar otra cosa (como un ventilador), debemos modificar InterruptorIncorrecto

//  * Ejemplo Correcto (cumple DIP): Dependencia de abstracciones
// --------------------------------------------------------------------------------------------------------------
class Dispositivo {
    encender() {
        throw new Error("Método 'encender' no implementado");
    }

    apagar() {
        throw new Error("Método 'apagar' no implementado");
    }
}

class BombillaCorrecta extends Dispositivo {
    encender() {
        console.log("💡 Bombilla encendida correctamente.");
    }

    apagar() {
        console.log("💡 Bombilla apagada correctamente.");
    }
}

class Ventilador extends Dispositivo {
    encender() {
        console.log("💨 Ventilador encendido.");
    }

    apagar() {
        console.log("💨 Ventilador apagado.");
    }
}

class InterruptorCorrecto {
    constructor(dispositivo) {
        this.dispositivo = dispositivo; // Dependencia de una interfaz abstracta
    }

    operar() {
        this.dispositivo.encender();
    }
}

// Uso correcto
const bombillaCorrecta = new BombillaCorrecta();
const ventilador = new Ventilador();

const interruptorBombilla = new InterruptorCorrecto(bombillaCorrecta);
interruptorBombilla.operar(); // Enciende la bombilla

const interruptorVentilador = new InterruptorCorrecto(ventilador);
interruptorVentilador.operar(); // Enciende el ventilador

// --------------------------------------------------------------------------------------------------------------
/* 🔥 DIFICULTAD EXTRA (opcional):
Crea un sistema de notificaciones.
Requisitos:
1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
2. El sistema de notificaciones no puede depender de las implementaciones específicas.
Instrucciones:
1. Crea la interfaz o clase abstracta.
2. Desarrolla las implementaciones específicas.
3. Crea el sistema de notificaciones usando el DIP.
4. Desarrolla un código que compruebe que se cumple el principio.
*/
console.log("\n----- SISTEMA DE NOTIFICACIONES (DIP) -----");

// Interfaz abstracta
class ServicioNotificacion {
    enviar(mensaje) {
        throw new Error("Método 'enviar' no implementado");
    }
}

// Implementaciones específicas
class NotificacionEmail extends ServicioNotificacion {
    enviar(mensaje) {
        console.log(`📧 Enviando email: ${mensaje}`);
    }
}

class NotificacionPush extends ServicioNotificacion {
    enviar(mensaje) {
        console.log(`📱 Enviando notificación PUSH: ${mensaje}`);
    }
}

class NotificacionSMS extends ServicioNotificacion {
    enviar(mensaje) {
        console.log(`📲 Enviando SMS: ${mensaje}`);
    }
}

// Sistema de notificaciones
class GestorNotificaciones {
    constructor(servicios) {
        this.servicios = servicios; // Dependencia de una lista de interfaces abstractas
    }

    notificar(mensaje) {
        this.servicios.forEach(servicio => servicio.enviar(mensaje));
    }
}

// Ejemplos de uso
const emailService = new NotificacionEmail();
const pushService = new NotificacionPush();
const smsService = new NotificacionSMS();

const gestor = new GestorNotificaciones([emailService, pushService, smsService]);
gestor.notificar("¡Este es un mensaje importante!");

// Agregar un nuevo servicio sin modificar el gestor
class NotificacionWhatsApp extends ServicioNotificacion {
    enviar(mensaje) {
        console.log(`💬 Enviando WhatsApp: ${mensaje}`);
    }
}

const whatsappService = new NotificacionWhatsApp();
gestor.servicios.push(whatsappService); // Añadir WhatsApp al sistema
gestor.notificar("¡Nuevo mensaje añadido!");