import Foundation



// Definición del enum de los dias de la semana.
enum WeekDays: Int {
    case monday = 1
    case tuesday = 2
    case wednesday = 3
    case thursday = 4
    case  friday = 5
    case saturday = 6
    case sunday = 7
}

// Pide por consola el número del dia de la semana que quieres comprobar.
print("\n[+] - Introduce el número del dia de la semana:")
guard let input = readLine(), let numberOfTheDay = Int(input) else {
    fatalError()
}

// Inserta el número añadido al valor del enum.
if let weekDays = WeekDays(rawValue: numberOfTheDay) {
    // Comprueva que dia de la semana corresponde al número introducido.
    switch weekDays {
    
    case .monday:
        print("Es lunes.")
    
    case .tuesday:
        print("Es martes.")
    
    case .wednesday:
        print("Es miercoles.")
    
    case .thursday:
        print("Es jueves.")
    
    case .friday:
        print("Es viernes.")
    
    case .saturday:
        print("Es sabado.")
    
    case .sunday:
        print("Es domingo.")
    }
} else {
    print("[!] - Numero no valido.")
}




// DIFICULTAD EXTRA
print("\nDIFICULTAD EXTRA.")
// Espera 4 segundos antes de ejecutar la dificultad extra.
sleep(4)



// Definición de la clase para manejar el estatus de un pedido.
class Order {
    let id: String // Declara la propiedad id.
    var orderStatus: Status // Declara la propiedad orderStatus
    
    // Define el inicializador para las dos propiedades, el parametro id tiene valor por defecto.
    init(id: String = UUID().uuidString, orderStatus: Status) {
        self.id = id
        self.orderStatus = orderStatus
    }
    
    // Definición del enum con los estados del producto.
    enum Status {
        case pending
        case shipped
        case delivered
        case cancelated
    }
    
    // Definición de la función para enviar el pedido, el parametro shippedStatus con valor por defecto.
    func shippedOrder(forOrder order: Order, shippedStatus: Status = .shipped) {
        if orderStatus == .shipped {
            print("\nEl pedido \(order.id) esta enviado.")
            
        } else if orderStatus == .pending {
            print("\nEl pedido \(order.id) esta aun pendiente.")
            
        } else if orderStatus == .delivered {
            print("\nEl pedido \(order.id) aun no se ha entregado.")
            
        } else if orderStatus == .cancelated {
            print("\nEl pedido \(order.id) se ha cancelado.")
        }
    }
    
    // Definición de la función para entregra el pedido, el parametro deliveredStatus con valor por defecto.
    func deliveredOrder(forOrder order: Order, deliveredStatus: Status = .delivered) {
        if orderStatus == .delivered {
            print("El pedido \(order.id) fue entregado.")
            
        } else if orderStatus == .pending {
            print("\nEl pedido \(order.id) aun esta pendiente.")
            
        } else if orderStatus == .shipped {
            print("\nEl pedido \(order.id) este de camino.")
            
        } else if orderStatus == .cancelated {
            print("\nEl pedido \(order.id) fue cancelado.")
        }
    }
    
    // Definición de la función para cancelar el pedido, el parametro cancelatedStatus con valor por defecto.
    func cancelatedOrder(forOrder order: Order, cancelatedStatus: Status = .cancelated) {
        if orderStatus == .cancelated {
            print("\nPedido \(order.id) cancelado.")
            
        } else if orderStatus == .pending {
            print("\nPedido \(order.id) cancelado.")
            
        } else if orderStatus == .shipped {
            print("\nEl pedido \(order.id) esta de camino, no se puede cancelar")
            
        } else if orderStatus == .delivered {
            print("\nEl pedido \(order.id) fue entregado, no se puede cancelar.")
        }
    }
    
    // Definición de la función para imprimir el estado del producto.
    func printOrderInfo(forOrder order: Order) {
        switch order.orderStatus {
            
        case .pending:
            print("El pedido \(order.id) esta pendiente.")
        
        case .shipped:
            print("El pedido \(order.id) esta de camino.")
        
        case .delivered:
            print("El pedido \(order.id) fue entregado.")
        
        case .cancelated:
            print("El pedido \(order.id) fue cancelado.")
        }
    }
}

// Ejemplos con la clase.
let order1 = Order(orderStatus: .pending)
order1.shippedOrder(forOrder: order1)
order1.printOrderInfo(forOrder: order1)

let order2 = Order(orderStatus: .shipped)
order2.deliveredOrder(forOrder: order2)
order2.printOrderInfo(forOrder: order2)

let order3 = Order(orderStatus: .delivered)
order3.cancelatedOrder(forOrder: order3)
order3.printOrderInfo(forOrder: order3)

let order4 = Order(orderStatus: .cancelated)
order4.deliveredOrder(forOrder: order4)
order4.printOrderInfo(forOrder: order4)

