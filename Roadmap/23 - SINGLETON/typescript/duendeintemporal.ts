//#23 { retosparaprogramadores } - PATRONES DE DISEÑO: SINGLETON
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

// Conditional check for browser environment
if (typeof window !== 'undefined') {
    window.addEventListener('load', () => {
        const body: HTMLBodyElement | null = document.querySelector('body');
        const title = document.createElement('h1');

        body?.style.setProperty('background', '#000');
        body?.style.setProperty('text-align', 'center');

        title.textContent = 'Retosparaprogramadores #23.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '100vh');

        body?.appendChild(title);

        setTimeout(() => {
            alert('Retosparaprogramadores #23. Please open the Browser Developer Tools.');
        }, 2000);
        log('Retosparaprogramadores #23');
    });
} else {
    log('This code is designed to run in a browser environment. Skipping window-related code.');
    log('Retosparaprogramadores #23');
}

/* 
The Singleton design pattern ensures that a class has a single instance and provides
a global point of access to that instance. Below, I will show you how to implement the 
Singleton pattern in TypeScript, followed by an example that represents a class for 
managing user sessions.
*/

class Singleton {
    private static instance: Singleton;

    private constructor() {
        // Initialize any properties you need here
    }

    public static getInstance(): Singleton {
        if (!Singleton.instance) {
            Singleton.instance = new Singleton();
        }
        return Singleton.instance;
    }

    // Example method
    public someMethod(): void {
        log("This is a method of the singleton.");
    }
}

// Using the Singleton
const instance1 = Singleton.getInstance();
const instance2 = Singleton.getInstance();

// Note: both variables point to the same instance
log(instance1 === instance2); // true  

// EXTRA DIFICULTY EXERCISE

class UserSession {
    private static instance: UserSession;
    private user: { id: number; username: string; name: string; email: string } | null;

    private constructor() {
        this.user = null; 
    }

    public static getInstance(): UserSession {
        if (!UserSession.instance) {
            UserSession.instance = new UserSession();
        }
        return UserSession.instance;
    }

    public setUser(id: number, username: string, name: string, email: string): void {
        this.user = { id, username, name, email };
    }

    public getUser(): { id: number; username: string; name: string; email: string } | null {
        return this.user;
    }

    public clearSession(): void {
        this.user = null;
    }
}

const session1 = UserSession.getInstance();
session1.setUser(1, 'FritzCat', 'Fritz Cat', 'fritzcat@proton.me');

log(session1.getUser()); // Object { id: 1, username: "FritzCat", name: "Fritz Cat", email: "fritzcat@proton.me" }

const session2 = UserSession.getInstance();
log(session2.getUser()); // Object { id: 1, username: "FritzCat", name: "Fritz Cat", email: "fritzcat@proton.me" }

session2.clearSession();
log(session1.getUser()); // null
