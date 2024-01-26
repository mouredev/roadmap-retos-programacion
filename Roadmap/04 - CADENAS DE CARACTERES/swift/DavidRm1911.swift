import Foundation

//String literal:
var StringLiteral = "Soy un string"

//multiline: y unicode
var multiString = """

soy un multistring \u{1F496}
    2 lineas

""" 

//extender linea

var extenderlinea = #"""
hola\n\n\n\
"""#

print(StringLiteral,multiString, extenderlinea)

//Mutability

var string1 = "Hola"
string1 += " Mundo"

print(string1)


//iteracion por caracteeres
for a in string1{
    print(a)
}

var arraycaracteres: [Character] = ["H","o","l","a"]
let arraystring = String(arraycaracteres)
print(arraystring)

//con numeros
let numero = 3
print("nuevo numero \(Double(numero)*4.5)")
