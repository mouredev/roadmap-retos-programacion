// Ejercicio

/* Patrón de diseño singleton */

class Person {
  constructor(name, age) {
    if (typeof Person.instance === 'object') { /* Si la clase Person existe se devuelve la instancia creada */
      return Person.instance;
    } 
    /* Caso contrario se establecen las propiedades */
    this.name = name;
    this.age = age;

    Person.instance = this;
    return this;
  }
}

let person1 = new Person('José', 44);/* El objeto creado solo tendrá una instancia */
let person2 = new Person('María', 30);
console.log(person1); // Person { name: 'José', age: 44 }
console.log(person2); // Person { name: 'José', age: 44 }

// Extra

class UserSession {
  constructor() {

    if (!!UserSession.instance) {
      return UserSession.instance;
    }

    this.user = null;

    UserSession.instance = this;
  }

  setUser(id, username, name, mail) {
    this.user = {id, username, name, mail};
  }
  
  getUser() {
    return `${this.user.id} ${this.user.username} ${this.user.name} ${this.user.mail}`;
  }

  clearUser() {
    this.user.id = null;
    this.user.username = null;
    this.user.name = null;
    this.user.mail = null;
  }
}

let newSession = new UserSession();
newSession.setUser(212, 'parababire', 'Angel', 'angelnarvaez@gmail.com');
console.log(newSession.getUser());

let newSession2 = new UserSession();
console.log(newSession2.getUser());

let newSession3 = new UserSession();
newSession3.clearUser();
console.log(newSession3.getUser());

console.log(newSession2.getUser() === newSession.getUser()); // true