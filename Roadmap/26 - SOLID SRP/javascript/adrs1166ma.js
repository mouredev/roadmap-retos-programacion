// 🔥 EJERCICIO:
// Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
// Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
// de forma correcta e incorrecta.

// * Ejemplo Incorrecto (viola SRP): Una sola clase maneja múltiples responsabilidades
// --------------------------------------------------------------------------------------------------------------

class SistemaIncorrecto {
    constructor() {
        this.usuarios = [];
        this.log = [];
    }

    // Responsabilidad 1: Registrar usuarios
    registrarUsuario(nombre, email) {
        this.usuarios.push({ nombre, email });
        this.log.push(`Usuario ${nombre} registrado.`);
    }

    // Responsabilidad 2: Autenticar usuarios
    autenticarUsuario(email, password) {
        const usuario = this.usuarios.find(u => u.email === email);
        if (usuario) {
            this.log.push(`Autenticación exitosa para ${email}.`);
            return true;
        }
        return false;
    }

    // Responsabilidad 3: Mostrar logs
    mostrarLogs() {
        console.log("Logs del sistema:", this.log);
    }
}

const sistemaIncorrecto = new SistemaIncorrecto();
sistemaIncorrecto.registrarUsuario("Anderson", "anderson@example.com");
sistemaIncorrecto.autenticarUsuario("anderson@example.com", "1234");
sistemaIncorrecto.mostrarLogs();


// * Ejemplo Correcto (cumple SRP): Clases separadas por responsabilidad
// --------------------------------------------------------------------------------------------------------------
class RegistroUsuarios {
    constructor() {
        this.usuarios = [];
    }

    registrarUsuario(nombre, email) {
        this.usuarios.push({ nombre, email });
        return `Usuario ${nombre} registrado.`;
    }
}

class Autenticacion {
    autenticarUsuario(email, password, usuarios) {
        const usuario = usuarios.find(u => u.email === email);
        if (usuario) {
            return `Autenticación exitosa para ${email}.`;
        }
        return "Autenticación fallida.";
    }
}

class Logger {
    constructor() {
        this.log = [];
    }

    agregarLog(mensaje) {
        this.log.push(mensaje);
    }

    mostrarLogs() {
        console.log("Logs del sistema:", this.log);
    }
}

const registro = new RegistroUsuarios();
const auth = new Autenticacion();
const logger = new Logger();

logger.agregarLog(registro.registrarUsuario("María", "maria@example.com"));
logger.agregarLog(auth.autenticarUsuario("maria@example.com", "1234", registro.usuarios));
logger.mostrarLogs();


// * 🔥 DIFICULTAD EXTRA: Sistema de biblioteca
// --------------------------------------------------------------------------------------------------------------

// 1. Clase que viola SRP (maneja libros, usuarios y préstamos)
class LibraryIncorrecta {
    constructor() {
        this.libros = [];
        this.usuarios = [];
        this.prestamos = [];
    }

    // Responsabilidad 1: Registrar libros
    agregarLibro(titulo, autor, copias) {
        this.libros.push({ titulo, autor, copias });
    }

    // Responsabilidad 2: Registrar usuarios
    agregarUsuario(nombre, identificacion, email) {
        this.usuarios.push({ nombre, identificacion, email });
    }

    // Responsabilidad 3: Procesar préstamos
    prestarLibro(titulo, identificacionUsuario) {
        const libro = this.libros.find(libro => libro.titulo === titulo);
        if (!libro || libro.copias <= 0) return "Libro no disponible.";
        libro.copias--;
        this.prestamos.push({ titulo, identificacionUsuario });
        return `Libro "${titulo}" prestado.`;
    }

    // Responsabilidad 4: Devolver libros
    devolverLibro(titulo, identificacionUsuario) {
        const index = this.prestamos.findIndex(p => p.titulo === titulo && p.identificacionUsuario === identificacionUsuario);
        if (index === -1) return "Préstamo no encontrado.";
        const libro = this.libros.find(libro => libro.titulo === titulo);
        libro.copias++;
        this.prestamos.splice(index, 1);
        return `Libro "${titulo}" devuelto.`;
    }
}

// 2. Refactorización siguiendo SRP
class LibroManager {
    constructor() {
        this.libros = [];
    }

    agregarLibro(titulo, autor, copias) {
        this.libros.push({ titulo, autor, copias });
        return `Libro "${titulo}" agregado.`;
    }

    actualizarCopias(titulo, delta) {
        const libro = this.libros.find(libro => libro.titulo === titulo);
        if (libro) libro.copias += delta;
        return !!libro;
    }
}

class UsuarioManager {
    constructor() {
        this.usuarios = [];
    }

    agregarUsuario(nombre, identificacion, email) {
        this.usuarios.push({ nombre, identificacion, email });
        return `Usuario ${nombre} registrado.`;
    }
}

class PrestamoManager {
    constructor() {
        this.prestamos = [];
    }

    prestarLibro(titulo, identificacionUsuario, libroManager) {
        const libro = libroManager.libros.find(libro => libro.titulo === titulo);
        if (!libro || libro.copias <= 0) return "Libro no disponible.";
        libroManager.actualizarCopias(titulo, -1);
        this.prestamos.push({ titulo, identificacionUsuario });
        return `Libro "${titulo}" prestado.`;
    }

    devolverLibro(titulo, identificacionUsuario, libroManager) {
        const index = this.prestamos.findIndex(p => p.titulo === titulo && p.identificacionUsuario === identificacionUsuario);
        if (index === -1) return "Préstamo no encontrado.";
        libroManager.actualizarCopias(titulo, 1);
        this.prestamos.splice(index, 1);
        return `Libro "${titulo}" devuelto.`;
    }
}

class Library {
    constructor() {
        this.libroManager = new LibroManager();
        this.usuarioManager = new UsuarioManager();
        this.prestamoManager = new PrestamoManager();
    }
}

const library = new Library();
library.libroManager.agregarLibro("1984", "George Orwell", 3);
library.usuarioManager.agregarUsuario("Ana", "001", "ana@example.com");
console.log(library.prestamoManager.prestarLibro("1984", "001", library.libroManager));
console.log(library.prestamoManager.devolverLibro("1984", "001", library.libroManager));