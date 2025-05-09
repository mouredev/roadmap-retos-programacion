
/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 */


class SingletonExample {
  constructor(nombre) {
    this.nombre = nombre;
    if (SingletonExample._instance) {
      return SingletonExample._instance;
    }
    SingletonExample._instance = this;
   
  }
}

var instanceOne = new SingletonExample('instanceOne') // Se ejecuta exitosamente
console.log("Nombre: instanceOne", instanceOne);

var instanceTwo = new SingletonExample('instanceTwo') // Arroja error
console.log("Nombre instanceTwo", instanceTwo);

console.log("instanceOne === instanceTwo:" , instanceOne === instanceTwo);


/* DIFICULTAD EXTRA (opcional):
* Utiliza el patrón de diseño "singleton" para representar una clase que
* haga referencia a la sesión de usuario de una aplicación ficticia.
* La sesión debe permitir asignar un usuario (id, username, nombre y email),
* recuperar los datos del usuario y borrar los datos de la sesión.
*/

class SesionUsuario {
  constructor(id, username, name, email) {
    this.id = id;
    this.username = username;
    this.name = name;
    this.email = email;
    if (SesionUsuario._instance) {
      return SesionUsuario._instance;
    }
    SesionUsuario._instance = this;   
  }

  recuperarUsuario() {
    return `Id: ${this.Id}  UserName: ${this.username}  Name: ${this.name} email: ${this.email} `
  }

  borrarSesion() {
    this.id = null;
    this.username = null;
    this.name = null;
    this.email = null;
  }

}

var miUsuario = new SesionUsuario(1, 'userX', 'Manolo', "manolito@gmail.com");
console.log(">>Con datos: 1, userX, Manolo, manolito@gmail.com");
console.log(miUsuario.recuperarUsuario());

var miOtroUsuario = new SesionUsuario(5, 'userB', 'Ramira', "rrocha@gmail.com");
console.log(">>Con datos: 5, userB, Ramira, rrocha@gmail.com");
console.log(miOtroUsuario.recuperarUsuario());

console.log("miUsuario === miOtroUsuario: ", miUsuario === miOtroUsuario);

miUsuario.borrarSesion();
console.log(">>Luego de borrar usuario:");
console.log(miUsuario.recuperarUsuario());

