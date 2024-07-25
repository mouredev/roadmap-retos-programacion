import Foundation

/*
 El patron singleton es un patron de diseño creacional que nos permite garantizar la unica instancia de una clase.
 para implementar este patron la clase o estructura debe cumplir los siguientes requisitos:

 1. Debe tener un constructor privado
 2. Debe tener un metodo de inicializacion estatico que devuelva una instancia de la clase

 para mas informacion puedes checar mi solucion en kotlin o visitar https://refactoring.guru/es/design-patterns/singleton 
 
 */

 class IngredientSinglenton {
    private var ingredients: [String] = []
    static let shared = IngredientSinglenton()
    private init() {}

    func add(ingredient: String) {
        ingredients.append(ingredient)
    }

    func showIngredients() {
        print(ingredients)
    }
 }

 // aunque creamos dos instancias diferentes  siguen utilizando la misma instancia de la clase IngredientSinglenton

 let singleton = IngredientSinglenton.shared
 singleton.add(ingredient: "onions")
 singleton.showIngredients()

 let singleton2 = IngredientSinglenton.shared
 singleton2.add(ingredient: "chicken")
 singleton2.showIngredients()


// ejercicio extra 

struct User{
  let id : UUID
  let username : String
  let name : String
  let email : String
}

let mockDatabase = [
  User(id: UUID(), username: "blackriper", name: "Rodolfo", email: "devswift@apple.com"),
  User(id: UUID(), username: "janedoe", name: "Jane", email: "janedoe@me.com")
]

enum MockError: Error {
  case userNotFound
}



class SessionSingleton {
  static let shared = SessionSingleton()
  var currentSessionUser : User?

  private init() {}

  func login(username: String) throws {
    if let user = mockDatabase.first(where: {$0.username == username}) {
      currentSessionUser = user
      print("logged in with session user: \(currentSessionUser!)")
    }
 }

  func logout() {
    currentSessionUser = nil
    print("logged out session user")
  }
}

do {
  let session = SessionSingleton.shared
  try session.login(username: "blackriper")
  session.logout()

  try session.login(username: "janedoe")
  session.logout()

} catch MockError.userNotFound {
  print("user not registered")
}
