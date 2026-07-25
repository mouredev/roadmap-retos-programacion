/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */

class Dni {
  constructor(nombre, apellido) {
    this.nombre = nombre;
    this.apellido = apellido;

    if (typeof Dni.instance === "object") {
      return Dni.instance;
    }

    Dni.instance = this;
    return this;
  }

  getDni() {
    console.log(`Nombre: ${this.nombre}\nApellido: ${this.apellido}`);
  }
}

const dni01 = new Dni("caterina", "rodriguez");
const dni02 = new Dni("loki", "rodriguez");

dni02.getDni();

console.log("------------------DIFICULTAD EXTRA-----------------");

class Sesion {
  constructor(id, username, nombre, email) {
    this.id = id;
    this.username = username;
    this.nombre = nombre;
    this.email = email;

    if (typeof Sesion.instance === "object") {
      return Sesion.instance;
    }

    Sesion.instance = this;
    return this;
  }

  getDatos() {
    console.log(
      `El usuario ${this.username} con id ${this.id} se llama ${this.nombre} y su email es ${this.email}`
    );
  }

  borrarDatos() {
    this.id = "";
    this.username = "";
    this.nombre = "";
    this.email = "";
  }
}

const s1 = new Sesion("001", "gracedurum", "grace", "grace@grace.com");
s1.getDatos();
s1.borrarDatos();
s1.getDatos();
