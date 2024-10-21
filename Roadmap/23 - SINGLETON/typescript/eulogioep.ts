// Ejemplo básico del patrón Singleton
// ===================================
// El patrón Singleton asegura que una clase tenga una única instancia y proporciona
// un punto de acceso global a ella. Esto es útil cuando exactamente un objeto 
// necesita coordinar acciones en todo el sistema.

class BasicSingleton {
    // Instancia privada estática para almacenar la única instancia de la clase
    private static instance: BasicSingleton;
    
    // Constructor privado para evitar la creación de instancias con 'new'
    private constructor() {}
    
    // Método público estático que controla el acceso a la instancia
    public static getInstance(): BasicSingleton {
        // Si no existe la instancia, la crea
        if (!BasicSingleton.instance) {
            BasicSingleton.instance = new BasicSingleton();
        }
        // Retorna la instancia única
        return BasicSingleton.instance;
    }
}

// Ejercicio Extra: Singleton para Sesión de Usuario
// ===============================================

// Interfaz para definir la estructura de un usuario
interface User {
    id: number;
    username: string;
    name: string;
    email: string;
}

class UserSession {
    // Instancia privada estática
    private static instance: UserSession;
    
    // Datos del usuario actual
    private userData: User | null = null;
    
    // Constructor privado
    private constructor() {}
    
    // Método para obtener la instancia
    public static getInstance(): UserSession {
        if (!UserSession.instance) {
            UserSession.instance = new UserSession();
        }
        return UserSession.instance;
    }
    
    // Método para establecer los datos del usuario
    public setUser(user: User): void {
        this.userData = user;
    }
    
    // Método para obtener los datos del usuario
    public getUser(): User | null {
        return this.userData;
    }
    
    // Método para cerrar la sesión
    public logout(): void {
        this.userData = null;
    }
}

// Ejemplo de uso:
// =============

// Ejemplo básico
const singleton1 = BasicSingleton.getInstance();
const singleton2 = BasicSingleton.getInstance();
console.log(singleton1 === singleton2); // true

// Ejemplo de sesión de usuario
const session = UserSession.getInstance();

// Crear un usuario de ejemplo
const user: User = {
    id: 1,
    username: "john_doe",
    name: "John Doe",
    email: "john@example.com"
};

// Iniciar sesión
session.setUser(user);
console.log(session.getUser()); // Muestra los datos del usuario

// Obtener la misma instancia en otro lugar del código
const anotherSessionReference = UserSession.getInstance();
console.log(anotherSessionReference.getUser()); // Muestra los mismos datos

// Cerrar sesión
session.logout();
console.log(session.getUser()); // null