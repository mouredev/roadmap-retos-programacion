/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#23 PATRONES DE DISEÑO: SINGLETON
---------------------------------------
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
// ________________________________________________________

class Singleton {
    constructor() {
        if (Singleton.instance) {
            return Singleton.instance;
        }
        Singleton.instance = this;
    }
}

const singleton1 = new Singleton();
const singleton2 = new Singleton();

console.log(singleton1 === singleton2); // true

// ________________________________________________________
console.log("\nDIFICULTAD EXTRA\n");

class UserSession {
    constructor() {
        if (UserSession.instance) {
            return UserSession.instance;
        }
        this.user = null;
        UserSession.instance = this;
    }

    setUser(userId, username, name, email) {
        this.user = {
            id: userId,
            username,
            name,
            email,
        };
    }

    getUser() {
        return this.user;
    }

    logout() {
        this.user = null;
    }
}

const session1 = new UserSession();
session1.setUser(1, "Zoe_1", "Zoe", "Zoe@gm.com");
console.log(session1.getUser());
session1.logout();

const session2 = new UserSession();
session2.setUser(2, "Ben_1", "Ben", "Ben@gm.com");
console.log(session2.getUser());
session2.logout();
