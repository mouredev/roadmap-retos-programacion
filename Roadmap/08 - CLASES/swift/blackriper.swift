/*
  En swift hay dos tipos para representar un tipo complejo:
  - Struct
    -Puede tener metodos y atributos
    -No necesita un constructor para  inicializarlos
    -Actuan como un Value Type quiere decir que cada vez que se crea uno este tiene diferentes
     espacios de memoria 
  - Class
    -Puede tener metodos y atributos
    -Debe tener un constructor para inicializarlos
    -Actuan como un Reference Type quiere decir que cada vez que se crea uno el comparten un espacio de memoria
    -Pueden tener herencia 
 */
 
 class Person{
   let name: String
   let age:Int
   let city: String

   init(name: String, age: Int, city: String){
     self.name = name
     self.age = age
     self.city = city
   }

   func sayHello(){
     print("Hello, my name is \(name) and I am \(age) years old and I live in \(city)") 
   }
 }

  let person=Person(name: "Diego", age: 31, city: "Madrid")
  person.sayHello()
  
  struct Phone{
    let brand: String
    let model: String
    let color: String

    func call(number:String) -> String {
      return "Calling \(number)"
    }
 
    func getMobileInfo() -> String {
      return "Brand: \(brand) \nModel: \(model) \nColor: \(color)"
    }
  } 

  let phone=Phone(brand: "iPhone", model: "X", color: "Black")
  print(phone.getMobileInfo())
  print(phone.call(number: "123456789"))
  
  // ejercicio extra
 struct Queue{
    var elements=[String]()

    mutating func add(element: String){
        elements.append(element)
    }

    mutating func addAll(itemsArray: [String]){
        self.elements=itemsArray
    }

    mutating func remove() -> String?{
        return elements.isEmpty ? nil : elements.removeFirst()
    }

    func peek() -> String?{
        return elements.isEmpty ? nil : elements.first
    }

    var isEmpty: Bool {
        return elements.isEmpty
    }
}

class Printer{
    private var  printerQueue=Queue()
    private var option:String=""

    init(itemsArray: [String]){
        self.printerQueue.addAll(itemsArray: itemsArray)
    }
    
    private func addDocument(document:String){
        printerQueue.add(element: document)
    }

    private func printNextDocument(){
        if let nextDocument=printerQueue.remove(){
            print("printing: \(nextDocument)")
            print("pending to print: \(printerQueue.elements)")
            
        }
    }

    func printDocuments(){
      repeat{
        print("1. Add document")
        print("2. Printdocument")
        print("3. Exit")
        print("Select an option: ", terminator: "")
        option=readLine()!
        switch option{
            case "1":
               print("Input the document name",terminator: "")
               let document=readLine()!
               addDocument(document: document)
            case "2":
                 if printerQueue.isEmpty {
                     print("No documents to print")  
                 }else {
                     printNextDocument()
                 }  
            default:
             if option != "3" {
                 print("Invalid option")   
             }
                 
        }
    }while option != "3"    
 
  }
}

let printer=Printer(itemsArray: ["document1","document2","document3"])
printer.printDocuments()

struct Stack{
    var elements=[String]()

    mutating func push(element: String){
        elements.append(element)
    }

    mutating func pop() -> String?{
        return elements.isEmpty ? nil : elements.popLast()
    }

    func peek() -> String?{
        return elements.isEmpty ? nil : elements.last
    }

    var isEmpty: Bool{
        return elements.isEmpty
    }
}

class WebNavigator {
    private var back=Stack()
    private var forward=Stack()

    func navigate(webPage:String){
        if back.isEmpty{
           forward.push(element: webPage)
           print("navigating to: \(webPage)")
        }
    }

    func goBack(){
        if !back.isEmpty{
            forward.push(element: back.pop()!)
            print("back to: \(back.peek()!)")
        }else{
            print("nothing to go back")
        }
    }    

    func goForward(){
        if !forward.isEmpty{
            back.push(element: forward.pop()!)
            print("forward to: \(forward.peek()!)")
        }else{
            print("nothing to go forward")
        }
    }
}

let webNavigator=WebNavigator()
webNavigator.navigate(webPage: "google.com")
webNavigator.navigate(webPage: "facebook.com")
webNavigator.navigate(webPage: "twitter.com")
webNavigator.goBack()
webNavigator.goForward()
