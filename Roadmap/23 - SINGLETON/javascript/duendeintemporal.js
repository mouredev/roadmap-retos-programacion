//#23 - PATRONES DE DISEÑO: SINGLETON
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

let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #23.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #23. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #23'); 
});


/* 
The Singleton design pattern ensures that a class has a single instance and provides a global point of access to that instance. Below, I will show you how to implement the Singleton pattern in JavaScript, followed by an example that represents a class for managing user sessions.

                      Implementation of the Singleton Pattern
 */
 
class Singleton{    
    constructor() {
        if (Singleton.instance) {
            return Singleton.instance;
        }
        Singleton.instance = this;
        // Initialize any properties you need here
    }

    // Example method
    someMethod() {
        log("This is a method of the singleton.");
    }
}

// Using the Singleton
const instance1 = new Singleton();
const instance2 = new Singleton();

//Note: both variables point to the same instance
log(instance1 === instance2); // true  

//EXTRA DIFICULTY EXERCISE

class UserSession {
    constructor() {
        if (UserSession.instance) {
            return UserSession.instance;
        }
        UserSession.instance = this;
        this.user = null; 
    }

    setUser(id, username, name, email) {
        this.user = { id, username, name, email };
    }

    getUser() {
        return this.user;
    }

    clearSession() {
        this.user = null;
    }
}

const session1 = new UserSession();
session1.setUser(1, 'FritzCat', 'Fritz Cat', 'fritzcat@proton.me');

log(session1.getUser()); // Object { id: 1, username: "FritzCat", name: "Fritz Cat", email: "fritzcat@proton.me" }

const session2 = new UserSession();
log(session2.getUser()); // Object { id: 1, username: "FritzCat", name: "Fritz Cat", email: "fritzcat@proton.me" }

session2.clearSession();
log(session1.getUser()); // null
