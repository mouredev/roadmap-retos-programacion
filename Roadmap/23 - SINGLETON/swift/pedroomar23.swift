import Foundation 

x/*
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

 class Singlenton {
    static let shared: Singleton = Singlenton() 

    private init() {}

    func someMethod() {
        print("Este es un metodo generico Singlenton")
    }
 }

// Ejemplo genérico de Singleton
class GenericSingleton {
    static let shared = GenericSingleton()
    
    private init() {}
    
    func someMethod() {
        print("This is a method of the Singleton")
    }
}

// Ejemplo de Singleton para una sesión de usuario
class UserSession {
    static let shared = UserSession()
    
    private init() {}
    
    private var user: User?
    
    struct User {
        let id: String
        let username: String
        let name: String
        let email: String
    }
    
    func assignUser(id: String, username: String, name: String, email: String) {
        user = User(id: id, username: username, name: name, email: email)
    }
    
    func getUserData() -> User? {
        return user
    }
    
    func clearSession() {
        user = nil
    }
}
