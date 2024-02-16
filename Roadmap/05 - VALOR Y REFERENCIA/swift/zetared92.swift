import Foundation
// RETO #05 VALOR Y REFERENCIA

// Asignación por valor
var droid: String = "RD-D2"
var android = droid
droid = "C3-PO"
print(droid)
print(android)

// Variable por referencia

class Droid {
    var color = "White"
}

var android = Droid()
android.color = "Gold"
print(android.color)


// 🧩 DIFICULTAD EXTRA 🧩

// Intercambio de valores
func forValue(x: String, y: String) -> (String, String){
    return (y, x)
}

var droid = "RD-D2"
var android = "C3-PO"

let (droid2, android2) = forValue(x: droid2, y: android2)
print("First values: \(droid), \(android)")
print("New values: \(droid2), \(android2)")

// Intercambio por referencia
class SpaceShip {
    var ship: String

    init(ship: String) {
        self.ship = ship
    }
}

func forReference(x: SpaceShip, y: SpaceShip) {
    let newRef = x.ship
    x.ship = y.ship
    y.ship = newRef
}


var spaceShip1 = SpaceShip(ship: "X-Wing")
var spaceShip2 = SpaceShip(ship: "Millenium Falcon")

forReference(x: spaceShip1, y: spaceShip2)


print("First Spaceship: \(spaceShip1.ship), Second Spaceship: \(spaceShip2.ship)") 