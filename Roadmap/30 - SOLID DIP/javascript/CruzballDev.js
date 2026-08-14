/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
*/


// Ejemplo incorrecto

/* class MySQLDatabase {
    guardarPedido(pedido) {
        console.log(`Guardando pedido: ${pedido} en MySQL`)
    }
}

class PedidoService {
    constructor() {
        // Dependencia directa de una implementación concreta.
        // PedidoService, que es el módulo de alto nivel, conoce y crea directamente la
        // implementación de bajo nivel.
        this.database = new MySQLDatabase();
    }

    crearPedido(pedido) {
        console.log("Creando pedido...")
        this.database.guardarPedido(pedido)
    }
}

const servicio = new PedidoService()
servicio.crearPedido("Disco Duro M.2") */



// Ejemplo correcto

class MySQLDatabase {
    guardarPedido(pedido) {
        console.log(`Guardando pedido ${pedido} en MySQL.`)
    }
}

class MongoDatabase {
    guardarPedido(pedido) {
        console.log(`Guardando pedido ${pedido} en MongoDB.`)
    }
}

class PedidoService {
    constructor(database) {
        // Depende de una abstracción /contrato,
        // no es de una implementación concreta.
        this.database = database
    }

    crearPedido(pedido) {
        console.log("Creando pedido...")
        this.database.guardarPedido(pedido)
    }
}

// Podemos elegir la implementación que queramos.
const mysql = new MySQLDatabase() // Creamos el objeto MySQLDatabase y lo guardamos en la const mysql.
const servicioMySQL = new PedidoService(mysql)

// creamos el objeto PedidoService y le pasamos por parámetro la const mysql y lo guardamos
// en la const servicioMySQL y ahora ya podemos acceder al metodo crearPedido de la clase
// PedidoService, pasandole por parámetro el nombre del pedido.
servicioMySQL.crearPedido("Placa base MSI")

// Y lo mismo con mongodb.
const mongo = new MongoDatabase()
const servicioMongo = new PedidoService(mongo)

servicioMongo.crearPedido("Placa base MSI")



/*
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


// Al emular una clase abastracta como Notificador, usamos una excepción (throw new Error),
// porque es una forma de forzar a las clases hijas a proporcionar su propia implementación.
class Notificador {
    enviarNotificacion(notificacion) {
        throw new Error("El método enviarNotificacion debe ser implementado.") 
    }
}


class EnviarEmail extends Notificador {
    enviarNotificacion(notificacion) {
        console.log(`La notificación: ${notificacion} se envió por email.`)
    }
}

class EnviarPush extends Notificador {
    enviarNotificacion(notificacion) {
        console.log(`La notificación: ${notificacion} se envió por Push.`)
    }
}

class EnviarSms extends Notificador {
    enviarNotificacion(notificacion) {
        console.log(`La notificación: ${notificacion} se envió por SMS.`)
    }
}

class ServicioNotificaciones {
    constructor(Notificador) {
        this.Notificador = Notificador
    }

    enviarNotificacion(notificacion) {
        console.log("Enviando la notificación...")
        this.Notificador.enviarNotificacion(notificacion)
    }
}


const email = new EnviarEmail()
const servicioEmail = new ServicioNotificaciones(email)

servicioEmail.enviarNotificacion("pepito@gmail.com")

const push = new EnviarPush()
const servicioPush = new ServicioNotificaciones(push)

servicioPush.enviarNotificacion("Esto es un envio .push()")

const sms = new EnviarSms()
const servicioSms = new ServicioNotificaciones(sms)

servicioSms.enviarNotificacion("Esto es un mensaje ")


// TEST
function test(notificador) {
    if(!(notificador instanceof Notificador)) {
        throw new Error("El objeto no cumple con la abstracción Notificador.")
    }

    if(typeof notificador.enviarNotificacion !== "function") {
        throw new Error("El objeto no implementa enviarNotificacion().")
    }
    console.log("El notificador cumple con la abstracción.")
}

test(new EnviarEmail)
test(new EnviarPush)
test(new EnviarSms)

