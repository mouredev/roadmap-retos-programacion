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

class Singleton {
    constructor() {
        if (Singleton.instance) {
            return Singleton.instance;
        }

        Singleton.instance = this;
        return this;
    }
}


const singleton1 = new Singleton();
console.log(singleton1);

const singleton2 = new Singleton();
console.log(singleton2);

console.log(singleton1 === singleton2);  // true


/*
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */

class UserSession {
    id = undefined
    username = undefined
    name = undefined
    email = undefined

    constructor() {
        if (UserSession.instance) {
            return UserSession.instance;
        }

        UserSession.instance = this;
        return this;
    }

    setUser(id, username, name, email) {
        this.id = id;
        this.username = username;
        this.name = name;
        this.email = email;
    }

    getUser() {
        return `${this.id}, ${this.username}, ${this.name}, ${this.email}`;
    }

    removeData() {
        this.id = undefined;
        this.username = undefined;
        this.name = undefined;
        this.email = undefined;
    }
}


const session1 = new UserSession();
console.log(session1.getUser());
// undefined, undefined, undefined, undefined
session1.setUser(1, 'nlarrea', 'Naia', 'naia@gmail.com');
console.log(session1.getUser());
// 1, nlarrea, Naia, naia@gmail.com

const session2 = new UserSession();
console.log(session2.getUser());
// 1, nlarrea, Naia, naia@gmail.com

const session3 = new UserSession();
session3.removeData();
console.log(session3.getUser());
// undefined, undefined, undefined, undefined
console.log(session1.getUser());
// undefined, undefined, undefined, undefined