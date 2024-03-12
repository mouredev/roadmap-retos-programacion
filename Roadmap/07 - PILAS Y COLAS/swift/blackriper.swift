/*
   Colas (Primero en Entrar , Primero en Salir)FIFO
   -cada elemento nuevo va al final de la misma
   -primero tiene que salir el primer elemento del mismo y hasta que este salga
    podra salir otro elemento de la lista
   - en swift se puede crear este comportamiento usando un array y una struct 
*/

// crendo estruct con una lista en este caso de tipo String pero se puede usar un generico para cualquier tipo de dato

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

// ejemplo de uso 
var taskDay=["wake up", "eat breakfast", "go to work", "go to bed"]
var myQueue=Queue()
myQueue.addAll(itemsArray: taskDay)
print(myQueue.peek()!)
print(myQueue.remove()!)
print(myQueue.peek()!)
print("task pending: \(myQueue.elements)")

//reto extra 
func printerDocuments(){
    var  printerQueue=Queue()
    var option:String
    
    func addDocument(document:String){
        printerQueue.add(element: document)
    }

    func printNextDocument(){
        if let nextDocument=printerQueue.remove(){
            print("printing: \(nextDocument)")
            print("pending to print: \(printerQueue.elements)")
            
        }
    }
    
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

printerDocuments()

/*
  Pila (Last in First Out) LIFO(Ultimo en entrar , primero en salir)
  - el último que entra es el primero que sale
  - apilar coloca un objeto en la pila
  - desapilar saca el último objeto de la pila
  - hasta que se desapila el ultimo elemento  se puede acceder al elemnto que se apilo con anterioridad
  */

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

// ejemplo de uso 
 var awsStack=Stack()
 awsStack.push(element: "AWSLambda")
 awsStack.push(element: "AWSRDS")
 awsStack.push(element: "AWSCLOUDFRONT")
 print(awsStack.peek()!)
 print(awsStack.pop()!)
 print(awsStack.peek()!)
 print("task pending: \(awsStack.elements)")

 //ejercicio extra

 func simulateNavigator(){
    var back=Stack()
    var forward=Stack()

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

  navigate(webPage: "google.com")
  navigate(webPage: "stackoverflow.com")
  navigate(webPage: "github.com")
  goBack()
  goBack()
  goForward()
    
 }

 simulateNavigator()

