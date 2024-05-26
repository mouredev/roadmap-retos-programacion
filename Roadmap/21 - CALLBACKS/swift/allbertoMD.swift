import Foundation

// Para el correcto funcionamiento del script se debe usar en un playground.

func fetchData(from url: URL, completion: @escaping (Data?, Error?) -> Void) {
    let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
        completion(data, error)
    }
    task.resume()
}

if let url = URL(string: "https://swift.org") {
    fetchData(from: url) { (data, error) in
        if let error = error {
            print("Error al fetch data: \(error)")
        }
        guard let dataResponse = data else {
            fatalError()
        }
        if let dataSting = String(data: dataResponse, encoding: .utf8) {
            print(dataSting)
        }
    }
}




// DIFICULTAD EXTRA
print("\nDIFICULTAD EXTRA.")


func order(name order: String, confirmation: @escaping (String) -> Void, done: @escaping (String) -> Void, delivery: @escaping (String) -> Void) {
    
    print("El pedido de \(order) ha sido realizado.")
    
    DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
        confirmation(order)
    }
    
    DispatchQueue.main.asyncAfter(deadline: .now() + 9) {
        done(order)
    }
    
    DispatchQueue.main.asyncAfter(deadline: .now() + 15) {
        delivery(order)
    }
}



order(name: "Alitas de pollo") { orderConfirmate in
    print("\(orderConfirmate) confirmado.")
} done: { orderDone in
    print("\(orderDone) listo.")
} delivery: { orderDelivery in
    print("\(orderDelivery) entregado.")
}

