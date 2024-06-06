import Foundation


// Creación de la clase UserInfo
class UserInfo {

    // Declaración de las propiedades de la clase.
    var id: String
    let name: String
    var userName: String
    var email: String
    var age: Int

    // Definición del inicializador de la clase.
    init(id: String, name: String, userName: String, email: String, age: Int) {
        self.id = id
        self.name = name
        self.userName = userName
        self.email = email
        self.age = age
    }
    // Definición de los metodos de la clasw.
    func showName() {
        print(name)
    }
    func showUserName() {
        print(userName)
    }
    func showEmail() {
        print(email)
    }
    func showAge() {
        print(age)
    }
}

// USER1
print("\nuser1\n")

// Crea el objeto user1 de la clase UserInfo().
var user1 = UserInfo(id: "01", name: "Raul", userName: "Ra01Mad", email: "raulrst@gmail.com", age: 39)

// Asigna la propiedad name de la clase a la variable user1Nmae.
let user1Name = user1.name
// Accede al metodo showName() del objeto user1.
user1.showName()

// Asigna la propiedad userName de la clase a la variable user1UserName.
var user1UserName = user1.userName
// Accede al metodo showUserName() del objeto user1.
user1.showUserName()

// Asigna la propiedad email de la clase a la variable user1Email.
var user1Email = user1.email
// Accede al metodo showEmail() del objwto user1.
user1.showEmail()

// Asigna la propiedad age de la clase a la variable user1Age.
var user1Age = user1.age
// Accede al metodo showAge() del objeto user1.
user1.showAge()

// uSER2
print("\nuser2\n")

// Crea el objeto user2 de la clase UserInfo().
var user2: UserInfo = UserInfo(id: "02", name: "Selvia", userName: "Silvi3", email: "silviarod@gmail.com", age: 27)

// Asigna la propiedad name de la clase a la variable user2Name.
let user2Name = user2.name
// Accede al metodo showName del objeto user2.
user2.showName()

// Asigna la propiedad userName de la clase a la variable user2UserName.
var user2UserName = user2.userName
// Accede al metodo showUserName() del objeto user2.
user2.showUserName()

// Asigna la propiedad email de la clase a la variable user2Email.
var user2Email = user2.email
// Accede al metodo showEmail() del objeto user2.
user2.showEmail()

// Asigna la propiedad age a la variable user2Age.
var user2Age = user2.age
// Accede al metodo showAge() del objeto user2.
user2.showAge()

// CAMBIOS EN USER1
print("\nCambios de user1\n")

// Cambia el valor de la propiedad userName del objeto user1.
user1.userName = "RaulitoEDLG"
// Accede al metodo showUserName() del objeto user1
user1.showUserName()

// Cambiar el valor de la propiedad age del objeto user1.
user1.age = 40
// Accede al metodo showAge() del objeto user1.
user1.showAge()

// CAMBIOS EN USER2
print("\nCambios de user2\n")

// Cambia el valor de la proiedad email del objeto user2.
user2.email = "sil07.via@gmail.com"
// Accede al metodo showEmail() del objeto user2
user2.showEmail()

// Cambia el valor de la propiedad age del objeto user2.
user2.age = 28
// Accede al metodo showAge() del objeto user2
user2.showAge()



// DIFICULTAD EXTRA

print("\nSTACK\n")
// Crea una clase Stack.
class Stack<T> {

    // Declaracion de la propiedad staxk
    private var stack: [T] = []
    
    // Definición del inicializador de la clase
    init(stack: [T]) {
        self.stack = stack
    }

    // Definicion del metodo push(), que añade elementos.
    func push(_ item: T) {
        stack.append(item)
    }
    
    // Definición del metodo pop(), que elimina el ultimo item de la lista y lo reotorna.
    func pop() -> T? {
        return stack.removeLast()
    }

    // Definición del metodo peek(), que retorna el ultimo item de la lista.
    func peek() -> T? {
        return stack.last
    }

    // Definición del metodo isEmpty(), que retorna si la lista esta vacio.
    func isEmpty() -> Bool {
        return stack.isEmpty
    }

    // Definición del metodo count(), que retorna la cantidad de items que tiene la lista.
    func count() -> Int {
        return stack.count
    }
}

// Crea el objeto myStack de la clase Stack().
var myStack = Stack(stack: ["Paris", "Madrid", "Tokio", "New York"])

// Añade un nuevo item a la lista usando el metodo push().
myStack.push("El Kaito")

// Elimina el ultimo item de la lista y lo devuelve en e imprime la variable pop usando el metodo pop().
if let pop = myStack.pop() {
    print(pop)
}

// Devuelve e imprime el ultimo item de la lista en la variable peek usando el metodo peek().
if let peek = myStack.peek() {
    print(peek)
}

// Devuelve si la lista esta vacia.
print(myStack.isEmpty())

// Devuelve la cantidad de items de la lista.
print(myStack.count())



print("\nQUEUE\n")
// Crea la clase Queue.
class Queue<T> {
    
    // Declaración de la propiedad queue.
    var queue: [T] = []

    // Definicion del inicializador de la clase.
    init(queue: [T]) {
        self.queue = queue
    }

    // Definición del metodo enqueue(), que anade un item al final de la lista.
    func enqueue(_ Item: T) {
        queue.append(Item)
    }

    // Definición del metodo dequeue(), que elimina y retorna el primer item de la lista.
    func dequeue() -> T? {
        return queue.removeFirst()
    }

    // Definición del metodo peek(), que retorna el primer item de la lista.
    func peek() -> T? {
        return queue.first
    }

    // Definición del metodo isEmpy(), que retorno si la lista esta vacia.
    func isEmpty() -> Bool {
        return queue.isEmpty
    }

    // Definición del metodo count(), que retorna el numero de items de la lista.
    func count() -> Int {
        return queue.count
    }
}

// Crea el objeto myQueue de la clase Queue().
var myQueue = Queue(queue: ["Roberto", "Alicia", "Ruben", "Almudena"])

// Añade un nuevo item a la lista usando el metodo enqueue().
myQueue.enqueue("Oliver")

// Elimina el ultimo item de la lista y lo devuelve e imprime la variable dequeue usando el metodo dequeue().
if let dequeue = myQueue.dequeue() {
    print(dequeue)
}

// Devuelve e imprime el ultimo item de la lista en la variable peek usando el metodo peek().
if let peek = myQueue.peek() {
    print(peek)
}

// Devuelve si la lista esta vacia.
print(myQueue.isEmpty())

// Devuelve la cantidad de items de la lista.
print(myQueue.count())