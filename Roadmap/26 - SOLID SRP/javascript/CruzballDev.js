/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
*/

// Ejemplo Incorrecto

class Usuario {
    constructor(Usuario, email) {
        this.Usuario = Usuario
        this.email = email
    }

    validarEmail() {
        return this.email.includes("@")
    }

    guardarUsuario() {
        console.log(`Guardando ${this.Usuario} en la base de datos...`)
    }

    enviarEmail() {
        console.log(`Enviando el ${this.email} ...`)
    }
}

// Ejemplo Correcto

class Usuario {
    constructor(nombre, email) {
        this.nombre = nombre
        this.email = email
    }
}

class ValidarEmail {
    validar(Usuario) {
        return Usuario.email.includes("@")
    }
}

class GuardarUsuario {
    guardar(Usuario) {
        console.log(`Guardando ${Usuario.nombre} en la base da datos ...`)
    }
}

class EnviarEmail {
    enviar(Usuario) {
        console.log(`Enviando email al usuario:  ${Usuario.email} ...`)
    }
}

const usuario1 = new Usuario("Juan", "Juan@gmail.com")
console.log(usuario1)

/*
* DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
 * y el procesamiento de préstamos de libros.
 * Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
 * información básica como título, autor y número de copias disponibles.
 * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 * información básica como nombre, número de identificación y correo electrónico.
 * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
 * tomar prestados y devolver libros.
 * Instrucciones:
 * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * usuarios y procesamiento de préstamos).
 * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Única.
*/


// NO cumple los principios SRP


class Biblioteca {
    constructor() {
        this.libros = []
        this.usuarios = []
        this.prestamosDevoluciones = []

    }

    // Registrar libros
   anadirLibro(titulo, autor, copias) {
        const libro = {
            titulo,
            autor,
            copias
        }

        this.libros.push(libro)
        console.log(`Èl libro ${titulo} se ha añadido a la biblioteca.`)
    }

    // Registrar usuarios
    registrarUsuarios(nombre, id, email) {
        const usuario = {
            nombre,
            id,
            email
        }

        this.usuarios.push(usuario)
        console.log(`El ususario ${nombre} ha sido registrado.`)
    }


    // Procesar prestamos
    alquilarLibro(usuarioId, titulo) {
        const usuarioEncontrado = this.usuarios.find(usuario => usuario.id === usuarioId);
        const libroEncontrado = this.libros.find(libro => libro.titulo === titulo)

        if(!usuarioEncontrado) {
            console.log(`Este usuario ${usuarioId} no está registrado.`)
            return
        }

        if(!libroEncontrado) {
            console.log(`No se ha encontrado este ${titulo}.`)
            return
        }

        if(libroEncontrado.copias <= 0) {
            console.log("No quedan copias disponibles.")
            return
        }

        libroEncontrado.copias--;

        this.prestamosDevoluciones.push({usuarioId, titulo})
        console.log(`Este título ${titulo} ha sido alquilado por el ususario ${usuarioEncontrado.nombre}`)

    }

    devolverLibro(usuarioId, titulo) {
        const devolver = this.prestamosDevoluciones.find(
            prestamo => prestamo.usuarioId === usuarioId && prestamo.titulo === titulo
        )

        if(!devolver) {
            console.log("No existe este prestamo")
            return
        }

        const libro = this.libros.find(libro => libro.titulo === titulo)

        libro.copias++;

        this.prestamosDevoluciones = this.prestamosDevoluciones.filter(
            devolver => !(devolver.usuarioId === usuarioId && devolver.titulo === titulo)
        );

        console.log(`El libro ${titulo} ha sido devuelto.`)
        return
    }
}

const lector1 = new Biblioteca()

lector1.anadirLibro("Juego de tronos", "George R.R. Martin", 5);

lector1.registrarUsuarios("Eufrasio", 1, "Eufrasio@gmail.com")

lector1.alquilarLibro(1, "Juego de tronos")

lector1.devolverLibro(1, "Juego de tronos")



// SI cumple los principios SRP
class Biblioteca {
    constructor() {
        this.registrarLibros = new RegistrarLibros();  // Es la plantilla o el molde para crear objetos.
        this.registrarUsuarios = new RegistrarUsuarios();

        this.prestamosDevoluciones = new PrestamosDevoluciones(
            this.registrarLibros,
            this.registrarUsuarios
        );
    }
}

class RegistrarLibros {
    constructor() {
        this.libros = [];
    }

    añadirLibro(titulo, autor, copias) {
        const libro = {
            titulo,
            autor,
            copias
        };

        this.libros.push(libro);

        console.log(
            `El libro con el título "${titulo}" se ha añadido a la biblioteca.`
        );
    }
}

class RegistrarUsuarios {
    constructor() {
        this.usuarios = [];
    }

    registrarUsuario(nombre, id, email) {
        const usuario = {
            nombre,
            id,
            email
        };

        this.usuarios.push(usuario);

        console.log(`El usuario ${nombre} se ha añadido correctamente.`);
    }
}

class PrestamosDevoluciones {
    constructor(registrarLibros, registrarUsuarios) { // Es la variable que almacena un objeto que ya fué creado en el constructor de Biblioteca.
        this.registrarLibros = registrarLibros;
        this.registrarUsuarios = registrarUsuarios;
        this.librosPrestados = [];
    }

    alquilarLibro(titulo, usuarioId) {
        const encontrarLibro = this.registrarLibros.libros.find(
            libro => libro.titulo === titulo
        );

        const usuarioEncontrado = this.registrarUsuarios.usuarios.find(
            usuario => usuario.id === usuarioId
        );

        if (!encontrarLibro) {
            console.log(
                `El libro con el título "${titulo}" no está en la biblioteca.`
            );
            return;
        }

        if (!usuarioEncontrado) {
            console.log(
                `El usuario ${usuarioId} no está registrado.`
            );
            return;
        }

        if (encontrarLibro.copias <= 0) {
            console.log(
                `No hay copias disponibles del título "${titulo}".`
            );
            return;
        }

        encontrarLibro.copias--;

        this.librosPrestados.push({
            usuarioId,
            titulo
        });

        console.log(
            `El libro "${titulo}" se ha prestado al usuario ${usuarioId}.`
        );
    }

    devolverLibro(titulo, usuarioId) {
        const prestamo = this.librosPrestados.find( // Aquí comprobamos si existe el prestamo;
            prestamo =>
                prestamo.titulo === titulo &&
                prestamo.usuarioId === usuarioId
        );

        if (!prestamo) {
            console.log(
                `El libro "${titulo}" no está prestado al usuario ${usuarioId}.`
            );
            return;
        }

        const libro = this.registrarLibros.libros.find( // Después buscamos el libro:
            libro => libro.titulo === titulo // Lo encontramos y hacemos:
        );

        libro.copias++; // El ++ suma uno. Antes: copias = 6;  Después:copias = 7; Devolvemos la copia y vuelve a estar disponible.


        // Ahora hay que eliminar el préstamo.
        this.librosPrestados = this.librosPrestados.filter( // .filter() crea un nuevo array manteniendo los elementos que cumplen la condición y por lo tanto eliminando el PRÉSTAMO que acabamos de devolver.
            prestamo =>                                     // Después [] Ya no hay un préstamo activo para ese usuario y libro.
                !(
                    prestamo.usuarioId === usuarioId &&
                    prestamo.titulo === titulo
                )
        );

        console.log(
            `El libro "${titulo}" se ha devuelto correctamente.`
        );
    }
}


// ==========================
// USO DE LAS CLASES
// ==========================

const lector2 = new Biblioteca();

// Registrar usuario
lector2.registrarUsuarios.registrarUsuario(
    "Edelmiro",
    2,
    "Edelmiro@gmail.com"
);

// Añadir libro
lector2.registrarLibros.añadirLibro(
    "Choque de Reyes",
    "George R.R. Martin",
    7
);

// Alquilar libro
lector2.prestamosDevoluciones.alquilarLibro(
    "Choque de Reyes",
    2
);

// Devolver libro
lector2.prestamosDevoluciones.devolverLibro(
    "Choque de Reyes",
    2
);