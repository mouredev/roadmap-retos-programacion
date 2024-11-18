class Singleton {
    // Atributo estático que mantendrá la instancia única
    private static instance: Singleton;

    // Un ejemplo de un atributo de la clase
    public data: string;

    // Constructor privado para evitar instancias directas
    private constructor() {
        this.data = "Singleton Instance Data";
    }

    // Método estático para obtener la instancia única
    public static getInstance(): Singleton {
        if (!Singleton.instance) {
            Singleton.instance = new Singleton();
        }
        return Singleton.instance;
    }

    // Un método ejemplo de la clase Singleton
    public displayData(): void {
        console.log(this.data);
    }
}

// Intentando obtener la instancia del Singleton
const singleton1 = Singleton.getInstance();
const singleton2 = Singleton.getInstance();

// Modificando el atributo data a través de la primera instancia
singleton1.data = "New Data";

// Ambas instancias deberían ser iguales y reflejar el mismo estado
singleton1.displayData(); // Output: New Data
singleton2.displayData(); // Output: New Data

// Verificando que ambas referencias son iguales
console.log(singleton1 === singleton2); // Output: true


/************************************************ */

interface User {
    id: number;
    username: string;
    nombre: string;
    email: string;
}

class UserSession {
    // Atributo estático que mantendrá la instancia única
    private static instance: UserSession;

    // Atributo que almacenará los datos del usuario
    private user: User | null = null;

    // Constructor privado para evitar instancias directas
    private constructor() {}

    // Método estático para obtener la instancia única
    public static getInstance(): UserSession {
        if (!UserSession.instance) {
            UserSession.instance = new UserSession();
        }
        return UserSession.instance;
    }

    // Método para asignar un usuario a la sesión
    public setUser(user: User): void {
        this.user = user;
    }

    // Método para recuperar los datos del usuario
    public getUser(): User | null {
        return this.user;
    }

    // Método para borrar los datos de la sesión
    public clearSession(): void {
        this.user = null;
    }
}

// Uso de la clase UserSession
const session1 = UserSession.getInstance();
const session2 = UserSession.getInstance();

// Verificando que ambas referencias son iguales
console.log(session1 === session2); // Output: true

// Asignando un usuario a la sesión
session1.setUser({
    id: 1,
    username: "john_doe",
    nombre: "John Doe",
    email: "john.doe@example.com"
});

// Recuperando los datos del usuario
console.log(session1.getUser()); // Output: { id: 1, username: 'john_doe', nombre: 'John Doe', email: 'john.doe@example.com' }
console.log(session2.getUser()); // Output: { id: 1, username: 'john_doe', nombre: 'John Doe', email: 'john.doe@example.com' }

// Borrando los datos de la sesión
session1.clearSession();

// Verificando que los datos se han borrado
console.log(session1.getUser()); // Output: null
console.log(session2.getUser()); // Output: null
