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

class Singleton{
    constructor(){
        if(Singleton.instance){
            return Singleton.instance;
        }
        Singleton.instance = this;

        this.data = "Some data";
    }

    getData(){
        return this.data;
    }

    setData(data){
        this.data = data;
    }
}

const instance1 = new Singleton();
const instance2 = new Singleton();

console.log(instance1 === instance2);

instance1.setData("New Data");

console.log(instance2.getData());


// Otra forma de implementar Singleton usando IIFE

const Singleton = (function() {
    let instance;

    function createInstance() {        
        const object = new Object("I am the instance");
        return object;
    }

    return {
        getInstance: function() {
            if (!instance) {
                instance = createInstance();
            }
            return instance;
        }
    };
})();

const instance3 = Singleton.getInstance();
const instance4 = Singleton.getInstance();

console.log(instance3 === instance4);



///////////////// ---------------------------------- EXTRA ------------------------------ ///////////////////////

class UserSession{
    constructor(){
        if(UserSession.instance){
            return UserSession.instance;
        }
        UserSession.instance = this;

        this.data = null;
    }

    getData(){
        return this.data;
    }

    setData(userId, username, nombre, email){
        this.data = {
            id: userId,
            username: username,
            nombre: nombre,
            email: email
        };
    }

    clearSession(){
        this.data = null;
    }
}

const session1 = new UserSession();
const session2 = new UserSession();

console.log(session1 === session2);

session1.setData(1, "jhon00", "Jhon", "john.doe@example.com");

console.log(session2.getData());

session2.clearSession();

console.log(session1.getData());