import Foundation
/*
 La Enumeracion define un grupo de un solo tipo de valor lo cual ayuda 
 a trabajar con los datos de forma mas eficiente.

 Las Enumeracion asocioan los valores de una variable o constante
 con un nombre de identificador.

 las enumeraciones en swift  son un tipo de  clase por lo cual pueden
 adoptar caracteristicas de las mismas

 Ejemplo de Enumeracion

 enum Direction {
     case north
     case south
     case east
     case west
 }
 */

enum DayoftheWeek:Int {
    case sunday=1
    case monday=2
    case tuesday=3
    case wednesday=4
    case thursday=5
    case friday=6
    case saturday=7
}

if let possibleday = DayoftheWeek(rawValue: 3){
    print(possibleday)
}

// extra exercise


enum State{
    case pending
    case sending
    case received
    case completed
    case canceled
 }


struct Order{
   let id : Int
   var state : State

  mutating func ChangeState(newState: State){
       if RuleChangeState(newState){
           self.state = newState           
       }          
   }


   private func RuleChangeState(_ newState: State)->Bool{
      // si la orden esta en estado pendiente este no puede pasar a recibido sin ser enviado
      if  self.state == .pending && newState == .received {
          return false
      }

     // si le orden ya fue enviada esta no puede estar en estado pendiente
     if self.state == .sending && newState == .pending{
         return false
     }
    
    // si la orden ya fue recibida esta no puede cambiar de estado a pendiente o enviada 
    if self.state == .received  && (newState == .pending || newState == .sending){
        return false
    }
     
     // si es cancelado este no puede cambiar de estado
      if self.state == .canceled{
          return false
        }
     return true
   }
}

// ejemplos 
var order1 :Order = Order(id: 1, state: .pending)
var order2 :Order = Order(id: 2, state: .pending)
var order3 :Order = Order(id: 3, state: .canceled)

// no se puede cambiar de estado por laa reglas definidas
order1.ChangeState(newState: .received)
print("Order \(order1.id) state: \(order1.state)")

// se actualiza el estado correctamente 
order2.ChangeState(newState: .sending)
print("Order \(order2.id) state: \(order2.state)")

// no se puede cambiar de estado porque la orden ya fue cancelada
order3.ChangeState(newState: .sending)
print("Order \(order3.id) state: \(order3.state)")


