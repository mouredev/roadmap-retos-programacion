// El Principio de Inversión de Dependencias establece dos reglas clave:

// Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.

// Las abstracciones no deben depender de los detalles. Los detalles (implementaciones concretas) deben depender de las abstracciones.

// El nivel alto y bajo dependen de la abstraccion comun




//abstracción 
class ServicioDeNotificacion {
    enviar(){console.log("enviando mensaje Desde Servicio De Notificacion" )}
}

// Tu módulo de alto nivel será un GestorDeNotificaciones. Su responsabilidad principal es enviar mensajes, sin importarle cómo se envían.
//nivel alto
class GestorDeNotificaciones {
    constructor(ServicioDeNotificacion){
    this.servicio= ServicioDeNotificacion
    }
    enviarNotificacion(mensaje){
        console.log(`Gestor: Intentando enviar notificación: "${mensaje}"`);
        return this.servicio.enviar(mensaje)
    }
}


//nivel bajo
class EmailService extends ServicioDeNotificacion{
    enviar(mensaje) { // ¡Nombre del método CORRECTO: 'enviar'!
        console.log(`[EmailService] Enviando correo electrónico: "${mensaje}"`);
    }
}

class SMSService extends ServicioDeNotificacion{
    enviarmensaje(){console.log("enviando mensaje SMS")}
}

const emailservice = new EmailService()

const gestionar = new GestorDeNotificaciones(emailservice)
gestionar.enviarNotificacion("Hola por email desde instancia")

const smsservice = new SMSService()
const gestionarsms = new GestorDeNotificaciones(smsservice)
gestionarsms.enviarNotificacion()
