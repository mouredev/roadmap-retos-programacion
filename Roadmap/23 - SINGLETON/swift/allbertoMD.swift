import Foundation



class Singleton {
    // Propiedad estática que contiene la única instancia de la clase
    static let shared = Singleton()
    
    // Inicializador privado para prevenir la creación de otras instancias
    private init() {}
    
    // Métodos y propiedades de la clase
    func sayHi(to name: String) {
        print("Hi, \(name)")
    }
}

// Acceso global desde cualquier parte del código
let instance1 = Singleton.shared
instance1.sayHi(to: "Charly")

let instance2 = Singleton.shared
instance2.sayHi(to: "Marta")

// Verificar que ambas referencias apuntan a la misma instancia
print(instance1 === instance2)  // true




// DIFICULTAD EXTRA
print("\nDificultad Extra.\n")


class UserSession {
    static let shared = UserSession()
    
    private init() {}
    
    var id: String = ""
    var userName: String = ""
    var name: String = ""
    var email: String = ""
    
    func assigntID(_ id: String) {
        self.id = id
    }
    
    func assigntUserName(_ userName: String) {
        self.userName = userName
    }
    
    func assigntName(_ name: String) {
        self.name = name
    }
    
    func assignEmail(_ email: String) {
        self.email = email
    }
    
    func showSessionInfo() {
        print("id: \(id)")
        print("User Name: \(userName)")
        print("Name: \(name)")
        print("email: \(email)")
    }
    
    func removeSession() {
        id = ""
        userName = ""
        name = ""
        email = ""
        print("\nSession Removed")
    }
}


let userSession = UserSession.shared

userSession.assigntID(UUID().uuidString)
userSession.assigntUserName("Teophilus")
userSession.assigntName("Pablo")
userSession.assignEmail("tphls@gmail.com")

userSession.showSessionInfo()
userSession.removeSession()




