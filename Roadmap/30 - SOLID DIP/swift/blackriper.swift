/*
 inversion depedency principle 
 el principio establece dos partes 

 1.-Los módulos de alto nivel no deberían depender de los módulos de bajo nivel, ambos deben depender de abstracciones
 2.-Las abstracciones no deberían depender de los detalles, los detalles deben depender de las abstracciones

 */

//ejemplo de lo que no debe de hacerce  al cambiar por otro driver hay que destruir la clase 
class MySqlDatabase{
    private var host:String
    private var port:Int
    private var database:String

    init(server:String,port:Int,name:String){
        self.host=server
        self.port=port
        self.database=name
    }

    func connect()->String{
      return "connect to \(database) for \(host) and \(port)"
    }

    func executeQuery(_ rawString:String)->String{
        return "execute query : \(rawString)"
    }

    func disconnect()->String{
        return "disconnect MySqlDatabase"
    }

}

// aplicando inversion de dependencias 

//1.- definimos un protocolo que va tener elas abstracciones del comportamiento

protocol Database {
   func connect()->String
   func executeQuery(_ rawString:String)->String 
   func disconnect()->String  
}

//2.-Definimos los diferentes drivers de conexion 

class OracleDatabase:Database{
    private var host:String
    private var port:Int
    private var database:String

    init(_ server:String,_ port:Int,_ name:String){
        self.host=server
        self.port=port
        self.database=name
    }

    func connect()->String{
      return "connect to \(database) for \(host) and \(port)"
    }

   func executeQuery(_ rawString: String) -> String {
     return "execute query: \(rawString) "
   }
    func disconnect()->String{
        return "disconnect OracleDatabase"
    }

}

class PostgreSQLDatabase:Database{
    private var host:String
    private var port:Int
    private var database:String

    init(_ server:String,_ port:Int,_ name:String){
        self.host=server
        self.port=port
        self.database=name
    }

    func connect()->String{
      return "connect to \(database) for \(host) and \(port)"
    }

    func executeQuery(_ rawString:String)->String{
        return "execute query : \(rawString)"
    }

    func disconnect()->String{
        return "disconnect PostgreSQL"
    }

}

// como las clases no tienen que deondender de las capas inferiores creamos una nueva clase  

class ModelRepository{
    private var database:Database
     
     init(_ provider:Database){
        self.database=provider
    }


    func connectDatabase()->String{
       return database.connect()  
    }

    func executeSentence(sentence: String)->String{
        return database.executeQuery(sentence)
    }

    func disconnectDatabase()->String{
        return database.disconnect()
    }
}


let repo=ModelRepository(OracleDatabase("localhost",1521,"books"))
print(repo.connectDatabase())
print(repo.executeSentence(sentence: "SELECT id_book,title from books"))
print(repo.disconnectDatabase())

let repo1=ModelRepository(PostgreSQLDatabase("localhost",5432,"products"))
print(repo1.connectDatabase())
print(repo1.executeSentence(sentence: "SELECT * FROM products"))
print(repo1.disconnectDatabase())

// ejercicio extra 

protocol Notification{
    func buildNotification()->String
}

struct Email:Notification{
     let subject:String
     let to:String 
     let body:String

    func buildNotification() -> String {
    return """
       Subject: \(self.subject)
       To: \(self.to)

       \(self.body) 


    """
    }
}

struct SMS:Notification{
     let to: String
     let from:String
     let message:String 

    func buildNotification() -> String {
    return """
          To: \(self.to)
          From: \(self.from)

          \(self.message)

    """
    }
}


struct Push: Notification{
      let appName:String
      let title:String
      let content:String 

    func buildNotification() -> String {
    return  """
        \(self.appName)
     ___________________________________
     \(title)

     \(content)
    """
    }
}

struct NotificationFactory<T:Notification>:Notification{
    var notification: T 
    func buildNotification() -> String {
        return notification.buildNotification()
    }
}

let emailpush=NotificationFactory(notification: Email(subject: "dccomics@dccomics.com", to: "black@gmail.com", body: "your comics sold is processing"))
print(emailpush.buildNotification())

let push=NotificationFactory(notification: Push(appName: "youtube", title: "celebracion 6 años de freelance ", content: "directo para celebrar los seis años de desarrollador de brais moure "))
print(push.buildNotification())

let sms = NotificationFactory(notification: SMS(to: "citiBanamex", from: "blackriper", message: "Deposito de  $500 "))
print(sms.buildNotification())


