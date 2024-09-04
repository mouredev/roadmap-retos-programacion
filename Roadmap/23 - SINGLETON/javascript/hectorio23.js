// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

/*
- EJERCICIO:
Explora el patrón de diseño "singleton" y muestra cómo crearlo
con un ejemplo genérico.

- DIFICULTAD EXTRA (opcional):
Utiliza el patrón de diseño "singleton" para representar una clase que
haga referencia a la sesión de usuario de una aplicación ficticia.
La sesión debe permitir asignar un usuario (id, username, nombre y email),
recuperar los datos del usuario y borrar los datos de la sesión.
*/

/////////////////////////////////////////////////
/////////////////// EJERCICIO 1 /////////////////
/////////////////////////////////////////////////

class NotDuplicity {
    constructor() {
        if (NotDuplicity.instance) {
            return NotDuplicity.instance;
        }
        NotDuplicity.instance = this;
        return this;
    }
}

const obj1 = new NotDuplicity();
const obj2 = new NotDuplicity();

console.log(`ID Objeto 1 => ${obj1}`);
console.log(`ID Objeto 2 => ${obj2}`);
console.log(`¿Los objetos 1 y 2 son iguales? ${obj1 === obj2}`);

console.log("\n********************************\n");

/////////////////////////////////////////////////
///////////////// EJERCICIO EXTRA ///////////////
/////////////////////////////////////////////////

class UserSession {
    constructor() {
        if (UserSession.instance) {
            return UserSession.instance;
        }
        UserSession.instance = this;
        this._user_data = null;
        return this;
    }

    setUser(userId, username, name, email) {
        this._user_data = {
            id: userId,
            username: username,
            name: name,
            email: email
        };
    }

    getUser() {
        return this._user_data;
    }

    clearUser() {
        this._user_data = null;
    }
}

// Ejemplo de uso:
const session = new UserSession();
session.setUser(1, 'hectorio23', 'Adán', 'adan_example@example.com');

// Muestra los datos del usuario
console.log(session.getUser()); 

session.clearUser();

// Muestra null, ya que los datos han sido borrados
console.log(session.getUser()); 

// Verificación de singleton:
const anotherSession = new UserSession();

// True, ambas variables apuntan a la misma instancia
console.log(session === anotherSession); 