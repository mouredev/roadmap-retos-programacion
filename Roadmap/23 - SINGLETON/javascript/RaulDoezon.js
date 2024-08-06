/*
  EJERCICIO:
  Explora el patrón de diseño "singleton" y muestra cómo crearlo
  con un ejemplo genérico.
*/

console.log("+++++++++ EJEMPLO DE SINGLETON +++++++++");

class Singleton {
  constructor(name, age) {
    this.name = name;
    this.age = age;

    if (typeof Singleton.instance === "object") {
      return Singleton.instance;
    }

    Singleton.instance = this;
    return this;
  }
}

const singleton1 = new Singleton("Raúl", 32);
const singleton2 = new Singleton("Armando", 33);

console.log(singleton1);
console.log(singleton2);

/*
  DIFICULTAD EXTRA (opcional):
  Utiliza el patrón de diseño "singleton" para representar una clase que
  haga referencia a la sesión de usuario de una aplicación ficticia.
  La sesión debe permitir asignar un usuario (id, username, nombre y email),
  recuperar los datos del usuario y borrar los datos de la sesión.
*/

console.log("\n+++++++++ SESIÓN DE USUARIO +++++++++");

class UserSession {
  constructor(id, username, name, email) {
    this.data = {
      id: id,
      username: username,
      name: name,
      email: email,
    }

    if (UserSession.instance) {
      return UserSession.instance;
    }

    UserSession.instance = this;

    return this;
  }

  getsessionData() {
    if (this.data === undefined) {
      return `Los datos de la sesión fueron eliminados: ${this.data}`;
    }

    const userData = `- ID: ${this.data.id}\n- Usuario: ${this.data.username}\n- Nombre: ${this.data.name}\n- Correo electrónico: ${this.data.email}`

    return userData;
  }

  deleteSessionData() {
    delete this.data;
  }
}

const session1 = new UserSession(310392, "RaulDoezon", "Raúl", "raul@mail.mx");
const session2 = new UserSession(920331, "Armando", "Armando", "armando@mail.mx");

console.log(session1.getsessionData());
console.log(session2.getsessionData());

session1.deleteSessionData();

console.log(session1.getsessionData());
console.log(session2.getsessionData());
