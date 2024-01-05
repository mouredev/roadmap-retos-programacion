import Foundation

/*Tipos de Operadores*/


//Operador de asignación (=)
let b:Int = 10
var a:Int = 5
a = b

//Operadores Aritmeticos *Un solo ejemplo

var c: String = "Hola, " + "Me llamo David"

//Operador de residuo

var d: Int = 10 % 4 // debe de salir 2



//Operador Unario de Resta

var e: Int =  -d // debe de ser -2

//Operador Unario de Suma

var f: Int = +e //sigue siendo -2


//Operador de asignacion compuesta

var g: Int = 2
g += 2 //4
print (a,c, d, e, g)

//Operador de comparación 

if g > e {
    print("Hola Mundo")
} else {
    print("Hola :p")
}

//Operador Condicional Ternario
 
var pregunta: Bool = true

pregunta ? print("Es verdad") : print("Es falso") 

//Operador Nil-coalescing

var NombrePredeterminado: String = "David"

var NombreAElegir: String?


var NormaCoalescing = NombreAElegir ?? NombrePredeterminado

print(NormaCoalescing)

//Operador de Rango
//Operador de rango cerrado
print("Operador de rango cerrado")
for g in 1...5{
    print(g)
}

//Operador de rango semiabierto
print("Operador de rango semiabierto")
var Nombres = ["David", "Daniela", "Daniel", "Oscar"]

var conteo = Nombres.count //Para que cuente la cantidad de nombres en este caso

for i in 0..<conteo{
    print(Nombres[i])
}

//Operador de Rango unilateral
print("Rango Unilateral")
for nombre in Nombres[1...]{
    print(nombre)
}


for nombre in Nombres[...2]{
    
    print(nombre)
}

//Operadores Logicos
print("Operador Logico")
if g>1 && a>1 {
    print("son mayores a 1")
} else {
    print("Son menores a 1")
}

//Bit NOT operator
print("Bit NOT Operator")

var bitnormal:UInt8 = 0b00001011 //11
var bitinvertido:UInt8 = ~bitnormal //244

print("Bit Normal: ", bitnormal, "Bit Invertido: ", bitinvertido)

//BIT AND Operator
print("Bit AND Operador")
var bit2:UInt8 = 0b00001000
var bitigualados = bitnormal & bit2
print ("BIT AND : ", bitigualados)

//Bit OR Operator
print("Bit or Operator")
var bitOR = bitigualados | bitinvertido
print("Bit OR: ", bitOR)

//Bit XOR Operator
print("Bit XOr Operator")
var bitXOR:UInt8 = bitinvertido ^ bitOR
print("BIT XOR: ", bitXOR)

//TIPOS DE ESTRUCTURA, arriba ya se uso los condicionales de IF,

switch g {
    case 1:
    print("es 1")
    default:
    print("No es 1, es: ",g)
}

//Un uso de FOR IN,

var persona = ["David":8,"Daniela":19,"Ivan":61]
for (usuario,edad) in persona {
    print("La persona se llama \(usuario) y su edad es \(edad)")
}

/*var intermedio = 10
var minutos = 100

for tiempo in stride(from: 0, through: minutos, by: intermedio){
    print(tiempo)
}*/

while g < 7 {
    g += 1
    print ("hola")
}




//DIFICULTAD EXTRA:

var numero: Int

print("Dificultad extra")

for numero in 10...55{
    if numero % 2 == 0 && numero != 16 && numero % 3 != 0 {
        print(numero)
    }
}