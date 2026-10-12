/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
*/

// Versión básica
class Singleton {
    constructor() {
        if(Singleton.instancia) {
            return Singleton.instancia
        }
        Singleton.instancia = this
    }
}

const objeto1 = new Singleton()
const objeto2 = new Singleton()

// Una vesión más completa
class Configuracion {
    constructor() {
        if(Configuracion.instancia) {
            return Configuracion.instancia
        }
        this.tema = "oscuro"
        this.idioma = "es"

        Configuracion.instancia = this
    }
}

const config1 = new Configuracion()
const config2 = new Configuracion()

config1.tema = "claro"

console.log(`El tema de config2 es: ${config2.tema}`)

console.log(`config1 y config2 son iguales: ${config1 === config2}`)


class SesionUsuario {
    constructor(id, username, nombre, email) {
        if(SesionUsuario.instancia) {
            return SesionUsuario.instancia
        }

        this.id = id
        this.username = username
        this.nombre = nombre
        this.email = email


        SesionUsuario.instancia = this
    }

    clear() { // Para eliminar todos los datos dejamos todas las propiedades en null.
        this.id = null
        this.username = null
        this.nombre = null
        this.email = null
    }
}

const user1 = new SesionUsuario()
const user2 = new SesionUsuario()

console.log(user1 === user2) // true


user1.id = 1
user1.username = "cruzballDev"
user1.nombre = "Antonio"
user1.email = "cruzballDev@gmail.com"
console.log(user1)

console.log(user1.username)
console.log(user2.username)

user1.clear()

console.log(user1)
console.log(user2)