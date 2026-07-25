/*
  * EJERCICIO:
  * Explora el patrón de diseño "singleton" y muestra cómo crearlo
  * con un ejemplo genérico.
*/

class Singleton {
  constructor(name) {
    if(Singleton.instance) {
      return Singleton.instance
    }

    this.name = name
    Singleton.instance = this
  }
}

const singleton1 = new Singleton('Jhon')
const singleton2 = new Singleton('Doe')
console.log(singleton1 === singleton2)

/*
  * DIFICULTAD EXTRA (opcional):
  * Utiliza el patrón de diseño "singleton" para representar una clase que
  * haga referencia a la sesión de usuario de una aplicación ficticia.
  * La sesión debe permitir asignar un usuario (id, username, nombre y email),
  * recuperar los datos del usuario y borrar los datos de la sesión.
*/

class Login{
  constructor(id, username, name, email) {
    if(Login.instance) {
      return Login.instance
    }
    this.id = id
    this.username = username
    this.name = name
    this.email = email
    Login.instance = this
  }

  getUsers() {
    return `Id: ${this.id}, Usuario: ${this.username}, Nombre: ${this.name}, Email: ${this.email}`
  }

  clearUsers() {
    this.id = null
    this.username = null
    this.name = null
    this.email = null
  }
}

const login_1 = new Login(1,'victorCasta', 'Victor', 'victorcasta@gmail.com')
console.log(login_1.getUsers())
const login_2 = new Login()
console.log(login_2.getUsers())
login_2.clearUsers()
console.log(login_2.getUsers())