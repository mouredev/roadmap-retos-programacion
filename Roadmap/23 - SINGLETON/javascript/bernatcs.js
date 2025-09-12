// ** EJERCICIO

class Singleton {
    constructor() {
        if (Singleton.instance) {
            return Singleton.instance;
        }
        this.data = "Información del Singleton"; // Propiedades de la instancia
        Singleton.instance = this; // Guardar la instancia
        Object.freeze(this); // Congelar la instancia para evitar modificaciones
    }
}

const instance = new Singleton();
const instance2 = new Singleton()