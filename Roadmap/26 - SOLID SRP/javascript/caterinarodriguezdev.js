/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
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

// Uso incorrecto del SRP, esta función tiene más de una razón para cambiar:
// 1. Imprimir el usuario
// 2. Devolver un objeto usuario
const imprimirUsuario = (nombre, edad, hobby) => {
  console.log(
    `El usuario se llama ${nombre} tiene ${edad} años y le gusta ${hobby}`
  );
  return {
    nombre: nombre,
    edad: edad,
    hobby: hobby,
  };
};

// Uso correcto del SRP, estas 2 funciones tienen una única responsabilidad
const imprimirUsuarioSRP = (nombre, edad, hobby) => {
  console.log(
    `El usuario se llama ${nombre} tiene ${edad} años y le gusta ${hobby}`
  );
};

const crearUsuarioSRP = (nombre, edad, hobby) => {
  return {
    nombre: nombre,
    edad: edad,
    hobby: hobby,
  };
};

// Uso incorrecto
const usuario = imprimirUsuario("JJ", "20", "motocross");

// Uso correcto
imprimirUsuarioSRP("JJ", "20", "motocross");
const usuarioSRP = crearUsuarioSRP("JJ", "20", "motocross");

console.log("-------------DIFICULTAD EXTRA-----------");
// CLASES NO SRP
class Library {
  constructor() {
    this.libros = [];
    this.usuarios = [];
    this.prestamos = [];
  }

  registrarLibro(titulo, autor, copiasDisponibles) {
    this.libros.push({
      titulo: titulo,
      autor: autor,
      copiasDisponibles: copiasDisponibles,
    });
    console.log("Libro registrado");
  }

  registrarUsuario(nombre, dni, email) {
    this.usuarios.push({
      nombre: nombre,
      dni: dni,
      email: email,
    });
    console.log("Usuario registrado");
  }

  prestarLibro(libro, usuario) {
    const libroEncontrado = this.libros.find((l) => l.titulo === libro);
    const usuarioEncontrado = this.usuarios.find((u) => u.dni === usuario);

    if (
      libroEncontrado &&
      usuarioEncontrado &&
      libroEncontrado.copiasDisponibles > 0
    ) {
      this.prestamos.push({
        libro: libroEncontrado,
        usuario: usuarioEncontrado,
      });
      libroEncontrado.copiasDisponibles--;
      console.log(
        `Se ha prestado el libro ${libro} para el usuario ${usuario}`
      );
    } else {
      console.log(
        "Error, no se ha encontrado el libro y/o usuario o no existen copias disponibles"
      );
    }
  }

  devolverLibro(libro, usuario) {
    const index = this.prestamos.find(
      (p) => p.libro.titulo === libro && p.usuario.dni === usuario
    );
    const libroEncontrado = this.libros.find(l => l.titulo === libro);

    if (index !== -1) {
      this.prestamos.splice(index, 1);
      libroEncontrado && libroEncontrado.copiasDisponibles++;
      console.log("El libro ha sido devuelto y el préstamo cancelado, gracias");
    } else {
      console.log("No se ha encontrado el préstamo");
    }
  }
}

// CLASES SRP
class LibrarySRP {
  constructor() {
    this.libros = [];
    this.usuarios = [];
    this.prestamos = [];
  }

  registrarUsuario(nombre, dni, email) {
    const newUser = new User(nombre, dni, email);
    this.usuarios.push(newUser);
  }

  registrarLibro(titulo, autor, copiasDisponibles) {
    const newLibro = new Book(titulo, autor, copiasDisponibles);
    this.libros.push(newLibro);
  }

  prestarLibro(libro, usuario) {
    const libroEncontrado = this.libros.find((l) => l.titulo === libro);
    const usuarioEncontrado = this.usuarios.find((u) => u.dni === usuario);

    if (
      libroEncontrado &&
      usuarioEncontrado &&
      libroEncontrado.copiasDisponibles > 0
    ) {
      this.prestamos.push({
        libro: libroEncontrado,
        usuario: usuarioEncontrado,
      });
      libroEncontrado.copiasDisponibles--;
      console.log(
        `Se ha prestado el libro ${libro} para el usuario ${usuario}`
      );
    } else {
      console.log(
        "Error, no se ha encontrado el libro y/o usuario o no existen copias disponibles"
      );
    }
  }

  devolverLibro(libro, usuario) {
    const index = this.prestamos.find(
      (p) => p.libro.titulo === libro && p.usuario.nombre === usuario
    );
    const libroEncontrado = this.libros.find(l => l.titulo === libro);

    if (index !== -1) {
      this.prestamos.splice(index, 1);
      libroEncontrado && libroEncontrado.copiasDisponibles++;
      console.log("El libro se ha devuelto correctamente");
    } else {
      console.log("Préstamo no encontrado");
    }
  }
}

class Book {
  constructor(titulo, autor, copiasDisponibles) {
    this.titulo = titulo;
    this.autor = autor;
    this.copiasDisponibles = copiasDisponibles;
  }
}

class User {
  constructor(nombre, dni, email) {
    this.nombre = nombre;
    this.dni = dni;
    this.email = email;
  }
}

console.log('-------------Ejemplo con la clase NO SRP-----------');

const biblioteca = new Library();

// Registrar libros
biblioteca.registrarLibro('1984', 'George Orwell', 3);
biblioteca.registrarLibro('El Principito', 'Antoine de Saint-Exupéry', 2);

// Registrar usuarios
biblioteca.registrarUsuario('Juan Pérez', '123456', 'juan@example.com');
biblioteca.registrarUsuario('María López', '654321', 'maria@example.com');

// Prestar libros
biblioteca.prestarLibro('1984', '123456'); // Juan toma prestado '1984'
biblioteca.prestarLibro('El Principito', '654321'); // María toma prestado 'El Principito'

// Intentar prestar un libro que no está disponible
biblioteca.prestarLibro('1984', '654321'); // María intenta tomar '1984', pero no hay copias disponibles

// Devolver libros
biblioteca.devolverLibro('1984', '123456'); // Juan devuelve '1984'
biblioteca.devolverLibro('El Principito', '654321'); // María devuelve 'El Principito'

console.log('-------------Ejemplo con la clase SRP-----------');

const bibliotecaSRP = new LibrarySRP();

// Registrar libros
bibliotecaSRP.registrarLibro('Cien años de soledad', 'Gabriel García Márquez', 5);
bibliotecaSRP.registrarLibro('Crónica de una muerte anunciada', 'Gabriel García Márquez', 2);

// Registrar usuarios
bibliotecaSRP.registrarUsuario('Carlos Ruiz', '111222', 'carlos@example.com');
bibliotecaSRP.registrarUsuario('Ana Torres', '333444', 'ana@example.com');

// Prestar libros
bibliotecaSRP.prestarLibro('Cien años de soledad', '111222'); // Carlos toma prestado 'Cien años de soledad'
bibliotecaSRP.prestarLibro('Crónica de una muerte anunciada', '333444'); // Ana toma prestado 'Crónica de una muerte anunciada'

// Intentar prestar un libro que no está disponible
bibliotecaSRP.prestarLibro('Cien años de soledad', '333444'); // Ana intenta tomar 'Cien años de soledad', pero no hay copias disponibles

// Devolver libros
bibliotecaSRP.devolverLibro('Cien años de soledad', '111222'); // Carlos devuelve 'Cien años de soledad'
bibliotecaSRP.devolverLibro('Crónica de una muerte anunciada', '333444'); // Ana devuelve 'Crónica de una muerte anunciada'
