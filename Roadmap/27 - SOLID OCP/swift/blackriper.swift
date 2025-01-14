import Foundation

/*
Open Closed Principle

Este principio establece que una entidad de software (clase, módulo, función, etc)
debe quedar abierta para su extensión, pero cerrada para su modificación.

Con abierta para su extensión, nos quiere decir que una entidad de software debe tener la capacidad
de adaptarse a los cambios y nuevas necesidades de una aplicación, pero con la segunda parte de “cerrada
para su modificación” nos da a entender que la adaptabilidad de la entidad no debe darse
como resultado de la modificación del core de dicha entidad si no como resultado de un diseño
que facilite la extensión sin modificaciones.

*/

// lo que  no debe de hacerce
enum DriverDatabase {
    case sqlite
    case postgres
    case mysql
}

struct Product {
    let id:UUID=UUID() 
    let name: String
    let price: Double
}


final class DatabaseService{

   func saveProduct(product: Product, database: DriverDatabase) {
       switch database {
       case .sqlite:
             insertProductinSQLite(product: product)
       case .postgres:
             insertProductinPostgres(product: product)
       case .mysql:
             insertProductinMySQL(product: product)
           
       }
   }

}

extension DatabaseService {
    func insertProductinSQLite(product: Product) {
        print("Insert \(product) in SQLite")
    }
    func insertProductinPostgres(product: Product) {
        print("Insert \(product) in Postgres")
    }
    func insertProductinMySQL(product: Product) {
        print("Insert \(product) in MySQL")
    }
}

/* las desventaja es que al  querer hacer un cambio hay que modificar el core de la clase */

let db = DatabaseService()
db.saveProduct(product: Product(name: "macbook pro", price: 100.0), database: .sqlite)


// aplicando el principio open closed principle esto se puede usar aplicando protocolos, herencia , polimorfismo

// usando herencia creamos nuestra clase padre 
class DatabaseRepository{
    func saveProduct(product: Product) {
        print("Insert \(product) in database")
    }
}

// creamos los diferentes drivers como subclases de la clase padre 
class MongoDB: DatabaseRepository{
    override func saveProduct(product: Product) {
        print("Insert product id \(product.id) in MongoDB")
    }
}

class RedisDB: DatabaseRepository{
    override func saveProduct(product: Product) {
        print("Insert product id \(product.id) in Redis")
    }
}

class cockroachDB: DatabaseRepository{
    override func saveProduct(product: Product) {
        print("Insert product id \(product.id) in cockroachDB")
    }
}

// creamos la clase que implementa la logica 
class DatabaseServiceOPC {
        func saveDataInDatabase(product: Product, database: DatabaseRepository) {
            database.saveProduct(product: product)
        }
 }
// utlizaando el principio podemos extender la clase sin modificar su core 
let dbOPC = DatabaseServiceOPC()
dbOPC.saveDataInDatabase(product: Product(name: "macbook pro", price: 100.0), database: MongoDB())
dbOPC.saveDataInDatabase(product: Product(name: "iphone15", price: 400.00), database: RedisDB())

// ejercicio extra 

// implemementar operaciones y manteniendo el principio cerrado  controlado mediante un protocolo
protocol Operation{
    func executeOperation(num1:Int, num2:Int)->Int
}

struct Add:Operation{
        func executeOperation(num1: Int, num2: Int) -> Int {
           return num1+num2
        }
}

struct Sub:Operation{
    func executeOperation(num1: Int, num2: Int) -> Int {
       return num1-num2
    }
}

struct Mul:Operation{
    func executeOperation(num1: Int, num2: Int) -> Int {
       return num1*num2
    }
}

struct Div:Operation{
    func executeOperation(num1: Int, num2: Int) -> Int {
       return num1/num2
    }
}

class Calculator{
    func calculate(num1:Int, num2:Int, operation:Operation) -> Int {
        return operation.executeOperation(num1: num1, num2: num2)
    }
}

// primera implementacion 
let calc = Calculator()
let sum = Add()
let res = Sub()
let mul = Mul()
let div = Div()
print("Sum: \(calc.calculate(num1: 10, num2: 5, operation: sum))")
print("Res: \(calc.calculate(num1: 10, num2: 5, operation: res))")
print("Mult: \(calc.calculate(num1: 10, num2: 5, operation: mul))")
print("Div: \(calc.calculate(num1: 10, num2: 5, operation: div))")

// agregando nueva operacion  sin alterar el core de la clase por lo que el principio n se cumple

struct MathPow:Operation{
    func executeOperation(num1: Int, num2: Int) -> Int {
      return Int(pow(Double(num1), Double(num2)))
      
    }
}

// segunda implementacion
let powM = MathPow()
print("Pow: \(calc.calculate(num1: 2, num2: 4, operation: powM))")
