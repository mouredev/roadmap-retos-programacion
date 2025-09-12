//  * EJERCICIO:
//  * Explora el patrón de diseño "singleton" y muestra cómo crearlo


//  * con un ejemplo genérico.
class Sigleton {
    constructor() {
    
        if(Sigleton.instance) { return Sigleton.instance} 
        this.time = Date.now() 

        Sigleton.instance= this

        return this
        
    }

    static getInstance () {
       if (!Sigleton.instance) {Sigleton.instance = new Sigleton()}
       return Sigleton.instance 
    }
    

}

const singleton1 = new Sigleton();
const singleton2 = new Sigleton();
console.log(singleton1 === singleton2); // true

// * DIFICULTAD EXTRA (opcional):
//  * Utiliza el patrón de diseño "singleton" para representar una clase que
//  * haga referencia a la sesión de usuario de una aplicación ficticia.
//  * La sesión debe permitir asignar un usuario (id, username, nombre y email),
//  * recuperar los datos del usuario y borrar los datos de la sesión.
//  */

class Sesion {
    constructor() {
        if(Sesion.instance){
            return Sesion.instance;
        }

        // Inicializar datos de sesión vacíos
        this.userData = null;
        
        Sesion.instance = this;
        return this;
    }

    // Asignar usuario a la sesión
    setUser(id, username, name, email) {
        this.userData = {
            id: id,
            username: username,
            name: name,
            email: email
        };
        console.log('Usuario asignado a la sesión');
    }
    
    // Recuperar datos del usuario
    getUser() {
        if (!this.userData) {
            console.log('No hay usuario en la sesión');
            return null;
        }
        return this.userData;
    }

    // Borrar datos de la sesión
    clearSession() {
        this.userData = null;
        console.log('Sesión borrada');
    }

    // Verificar si hay usuario logueado
    isLoggedIn() {
        return this.userData !== null;
    }

    static getInstance() {
        if(!Sesion.instance){
            Sesion.instance = new Sesion();
        }
        return Sesion.instance;
    }
}

// Ejemplo de uso
const sesion1 = new Sesion();
const sesion2 = Sesion.getInstance();


console.log(sesion1 === sesion2); // true - misma instancia

// Uso de la sesión
sesion1.setUser(1, 'juan123', 'Juan Pérez', 'juan@email.com');
console.log('Datos desde sesion1:', sesion1.getUser());
console.log('Datos desde sesion2:', sesion2.getUser()); // Mismo usuario

console.log('¿Está logueado?', sesion1.isLoggedIn()); // true

sesion2.clearSession();
console.log('Después de borrar:', sesion1.getUser()); // null
console.log('¿Está logueado?', sesion1.isLoggedIn()); // false
