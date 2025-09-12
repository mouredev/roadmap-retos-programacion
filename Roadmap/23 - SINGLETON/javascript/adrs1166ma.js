// 🔥 EJERCICIO:
// Explora el patrón de diseño "singleton" y muestra cómo crearlo
// con un ejemplo genérico.

class Configuracion {
    constructor() {
        // Verifica si ya existe una instancia
        if (Configuracion.instancia) {
            return Configuracion.instancia
        }
        // Si no existe, crea la instancia
        this.config = {}
        Configuracion.instancia = this
    }

    // Método para establecer configuraciones
    setConfig(key, value) {
        this.config[key] = value
    }

    // Método para obtener configuraciones
    getConfig(key) {
        return this.config[key]
    }

    // Método para mostrar todas las configuraciones
    mostrarConfiguraciones() {
        console.log(this.config)
    }
}

// Crear una instancia de Configuracion
const config1 = new Configuracion()
config1.setConfig("tema", "oscuro")
config1.setConfig("idioma", "es")

// Intentar crear otra instancia
const config2 = new Configuracion()

// Ambas variables apuntan a la misma instancia
console.log(config1 === config2) // true
config2.mostrarConfiguraciones() // { tema: 'oscuro', idioma: 'es' }

// 🔥 DIFICULTAD EXTRA (opcional): ----------------------------------------------------------------------------------
// Utiliza el patrón de diseño "singleton" para representar una clase que
// haga referencia a la sesión de usuario de una aplicación ficticia.
// La sesión debe permitir asignar un usuario (id, username, nombre y email),
// recuperar los datos del usuario y borrar los datos de la sesión.

// Clase SesionUsuario siguiendo el patrón Singleton
class SesionUsuario {
    constructor() {
        // Verifica si ya existe una instancia
        if (SesionUsuario.instancia) {
            return SesionUsuario.instancia
        }
        // Si no existe, crea la instancia
        this.usuario = null
        SesionUsuario.instancia = this
    }

    // Método para iniciar sesión
    iniciarSesion(id, username, nombre, email) {
        this.usuario = { id, username, nombre, email }
        console.log(`Sesión iniciada para el usuario: ${username}`)
    }

    // Método para recuperar los datos del usuario
    obtenerDatosUsuario() {
        if (this.usuario) {
            console.log("Datos del usuario:", this.usuario)
        } else {
            console.log("No hay sesión activa.")
        }
    }

    // Método para cerrar sesión
    cerrarSesion() {
        this.usuario = null
        console.log("Sesión cerrada.")
    }
}

// Crear una instancia de SesionUsuario
const sesion1 = new SesionUsuario()
sesion1.iniciarSesion(1, "juan123", "Juan Pérez", "juan@example.com")
sesion1.obtenerDatosUsuario()

// Intentar crear otra instancia
const sesion2 = new SesionUsuario()
sesion2.obtenerDatosUsuario() // Muestra los mismos datos que sesion1

// Cerrar sesión desde sesion2
sesion2.cerrarSesion()
sesion1.obtenerDatosUsuario() // No hay sesión activa