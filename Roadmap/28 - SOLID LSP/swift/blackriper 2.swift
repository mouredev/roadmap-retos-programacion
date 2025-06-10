import Foundation
/*
 LSP liskov substitution principle
 El Principio de Substitución de Liskov es uno de los principios SOLID y hace referencia a cómo usamos
 la herencia de forma adecuada. El principio dice algo como lo siguiente si S es un subtipo de T , T
 puede ser reemplazado con objetos de tipo S sin alterar el comportamiento esperado en el programa.

  para mas informmacion 
   escrito: https://www.arquitecturajava.com/el-principio-de-substitucion-de-liskov/
   video: https://youtu.be/JQX7wrCzxFA?si=fr3SxQXPWeg0qyfN
 */

// ejemplo de  lo que no debe se hacerce

class Person{
   var dni:String?
   var fullName:String
   var creditCard:String?

   init(dni:String?,fullName:String,creditCard:String?) {
      self.dni = dni
      self.fullName = fullName
      self.creditCard = creditCard 
   }

   func realizePayment(){
     let dniPerson = self.dni ??  "dni is nil"
     let creditCardPerson = self.creditCard ?? "creditCard is nil"
     print("my dni is \(dniPerson) and payment with \(creditCardPerson) was done")
   }
}
// un niño no puede tener dni ni tarjeta  y para no modificar la superclase se usa nil
class Boy:Person{
    init(fullName:String) {
       super.init(dni: nil, fullName: fullName, creditCard: nil)
    }

    override func realizePayment() {
        print("iam a boy icant dni and creditCard")
        
    }
 }
// lo que debe de hacerce 

// la superclase people debe delegar comportamiento a alguna superclase 
class People {
  let name:String
  let lastName:String 

  init(name:String,lastName:String) {
    self.name = name
    self.lastName = lastName
  }
}

// ahora la subclase adulto agrega objetos S que no son parte de la superclase y ahora ya no es necesario
// que estos datos sean nulos ya que el adulto si cuenta con una tarjeta y dni
class Adult:People{
  var dni:String
  var creditCard:String

   init(name:String,lastName:String,dni:String,creditCard:String) {
     self.dni = dni
     self.creditCard = creditCard
     super.init(name: name, lastName: lastName)
   }

    func realizePayment() {
     print("my dni is \(self.dni) and payment with \(self.creditCard) was done")
   }
}

// ahora la subclase niño queda mas limpia y esta puede delegar e pago a las clase Adulto
 class Kid :People{
    var adult:Adult
    init(name:String,lastName:String,adul:Adult) {
      self.adult = adul  
      super.init(name: name, lastName: lastName)
    }
 }

// probando la implementacion
 let adult = Adult(name: "jose", lastName: "perez", dni: "12345678", creditCard: "123456789")
 adult.realizePayment()

 let kid = Kid(name: "rodolfo", lastName: "perez",adul: adult)
 kid.adult.realizePayment()


 // ejercicio extra 
 // nuestra superclase vehiculo 
 class Vehicle{
     var model :String 
     var speed : Int

     init(model:String,speed:Int) {
        self.model = model
        self.speed = speed
     }
    
    func accelerate() {
        print("The \(self.model) is accelerating \(self.speed) km/h")
    }

    func brake() {
        print("The \(self.model) is braking ")
    }
     
 }

// creamos nuestras subclases
 class Car:Vehicle{
    override init(model:String,speed:Int) {
       super.init(model: model, speed: speed)
    }
 }

 // como la clase truck necesita dejar su mercaderia estos nuevos objetos s no son parte de la superclase
 
 enum Burden {
  case Grave , Fruit, Metal ,Rocks 
 }

 class Truck:Vehicle{
    var burden: Burden
    init(model:String,speed:Int,burd:Burden) {
       self.burden = burd
       super.init(model: model, speed: speed)
    }

    func deliver() {
        print("The \(self.model) is delivering \(self.burden)")
    }
 }
// la clase bote puede anclar en algun lado por lo tanto este metodo se agrega 
class Boot:Vehicle{
    override init(model:String,speed:Int) {
       super.init(model: model, speed: speed)
    }

    func anchor() {
        print("The \(self.model) is anchoring in hawaii island")
    }
}


// comprobar que la clase principal puede ser consumida  por sus subclases

func consumeVehicle(vehicle:Vehicle){
  vehicle.accelerate()
  vehicle.brake()
}

let car = Car(model: "Bmw", speed: 120)
let truck = Truck(model: "Scania", speed: 100, burd: .Grave)
let boot = Boot(model: "Dometic", speed: 250)
consumeVehicle(vehicle: car)
consumeVehicle(vehicle: truck)
consumeVehicle(vehicle: boot)
truck.deliver()
boot.anchor()

