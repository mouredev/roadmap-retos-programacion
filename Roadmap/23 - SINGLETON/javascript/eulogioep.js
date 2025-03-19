/**
 * EJEMPLO BÁSICO DEL PATRÓN SINGLETON
 * ==================================
 * Implementación del patrón Singleton usando una clase ES6
 */

// Implementación básica usando clase ES6
class BasicSingleton {
    constructor() {
        // Verificar si ya existe una instancia
        if (BasicSingleton.instance) {
            return BasicSingleton.instance;
        }
        // Si no existe, guardar la instancia en la propiedad estática
        BasicSingleton.instance = this;
    }

    // Método estático para obtener la instancia
    static getInstance() {
        if (!BasicSingleton.instance) {
            BasicSingleton.instance = new BasicSingleton();
        }
        return BasicSingleton.instance;
    }
}

// Congelar el objeto para prevenir modificaciones
Object.freeze(BasicSingleton);

/**
 * EJERCICIO EXTRA: SINGLETON PARA SESIÓN DE USUARIO
 * ==============================================
 * Implementación de una clase de sesión de usuario usando el patrón Singleton
 * Se incluyen dos implementaciones: una usando clase ES6 y otra usando módulo
 */

// Implementación 1: Usando Clase ES6
class UserSession {
    constructor() {
        if (UserSession.instance) {
            return UserSession.instance;
        }

        // Inicializar propiedades privadas
        this._userData = null;
        UserSession.instance = this;
    }

    // Método estático para obtener la instancia
    static getInstance() {
        if (!UserSession.instance) {
            UserSession.instance = new UserSession();
        }
        return UserSession.instance;
    }

    // Método para establecer los datos del usuario
    setUser(user) {
        // Validar que el objeto tenga todas las propiedades requeridas
        const requiredFields = ['id', 'username', 'name', 'email'];
        const missingFields = requiredFields.filter(field => !(field in user));
        
        if (missingFields.length > 0) {
            throw new Error(`Campos requeridos faltantes: ${missingFields.join(', ')}`);
        }

        this._userData = { ...user };
    }

    // Método para obtener los datos del usuario
    getUser() {
        return this._userData ? { ...this._userData } : null;
    }

    // Método para cerrar la sesión
    logout() {
        this._userData = null;
    }
}

// Congelar el objeto para prevenir modificaciones
Object.freeze(UserSession);

// Implementación 2: Usando Módulo (IIFE)
const UserSessionModule = (function() {
    let instance;
    let userData = null;

    // Constructor privado
    function createInstance() {
        return {
            setUser(user) {
                const requiredFields = ['id', 'username', 'name', 'email'];
                const missingFields = requiredFields.filter(field => !(field in user));
                
                if (missingFields.length > 0) {
                    throw new Error(`Campos requeridos faltantes: ${missingFields.join(', ')}`);
                }

                userData = { ...user };
            },

            getUser() {
                return userData ? { ...userData } : null;
            },

            logout() {
                userData = null;
            }
        };
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

// Ejemplo de uso:
// =============

// Ejemplo básico
try {
    // Probar el singleton básico
    const singleton1 = BasicSingleton.getInstance();
    const singleton2 = BasicSingleton.getInstance();
    console.log('¿Son la misma instancia?:', singleton1 === singleton2); // true

    // Probar la sesión de usuario (Implementación con clase)
    console.log('\nProbando implementación con clase:');
    const session = UserSession.getInstance();

    const user = {
        id: 1,
        username: 'john_doe',
        name: 'John Doe',
        email: 'john@example.com'
    };

    session.setUser(user);
    console.log('Usuario actual:', session.getUser());

    const anotherSessionReference = UserSession.getInstance();
    console.log('¿Misma sesión?:', session === anotherSessionReference); // true
    console.log('Usuario desde otra referencia:', anotherSessionReference.getUser());

    session.logout();
    console.log('Después de logout:', session.getUser()); // null

    // Probar la sesión de usuario (Implementación con módulo)
    console.log('\nProbando implementación con módulo:');
    const sessionModule = UserSessionModule.getInstance();
    sessionModule.setUser(user);
    console.log('Usuario actual:', sessionModule.getUser());

    const anotherModuleReference = UserSessionModule.getInstance();
    console.log('¿Misma sesión?:', sessionModule === anotherModuleReference); // true
    
    sessionModule.logout();
    console.log('Después de logout:', sessionModule.getUser()); // null

} catch (error) {
    console.error('Error:', error.message);
}