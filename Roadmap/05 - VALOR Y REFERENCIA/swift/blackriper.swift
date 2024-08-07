import Foundation


// variables por valor 
var x = 10
var y = x // y es una copia de x
x = 20
print(x)
print(y)

// variables por referencia 
var z = "hello"
var a = z
z = "goodbye"
print(z)
print(a)

// reto extra 

// Asignación por valor
func forValue(x: String, y: String) -> (String, String){
    return (y, x)
}

var droid = "RD-D2"
var android = "C3-PO"
var (droid1, android1) = forValue(x: droid, y: android)
print("original values \(droid) and \(android)")
print("new values \(droid1) and \(android1)")

// Asignación por referencia
func forValue(x: inout String, y: inout String) -> (String, String){
    let temp = x
    x=y
    y=temp
    return (x,y)
}

var dr = "RD-D2"
var an = "C3-PO"
var (droid2, android2) = forValue(x: &dr, y: &an)
print("original values \(droid) and \(android)")
print("new values \(droid2) and \(android2)")


