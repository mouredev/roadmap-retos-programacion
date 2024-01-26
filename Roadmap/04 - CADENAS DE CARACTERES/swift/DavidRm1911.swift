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
print("nuevo numero \(Double(numero)*4.5) \u{65}\u{20DD}")

//contar caracteres
print ("\(string1) tiene \(string1.count) caracteres")
//mostrar palabras
print(string1[string1.startIndex]) //Muestra la primera letra
print(string1[string1.index(after: string1.startIndex)])
print(string1[string1.index(string1.startIndex, offsetBy: 2)]) //Elige la letra por numero de orden desde 0

//se puede acceder a todas por:

for index in string1.indices{
    print(string1[index], terminator: "1")
}

//insertar 

var azul = "\nhola como estan"
azul.insert("A", at: azul.endIndex)
print(azul)
azul.insert(contentsOf: " cuentenme de su vida ", at: azul.index(before: azul.endIndex))
print(azul)
//remover
azul.remove(at: azul.index(before: azul.endIndex))
print(azul)
//esto es para recortar desde un punto en este caso e caso SUBSTRING
var azulrecortado = azul.firstIndex(of: "e") ?? azul.endIndex

let azulre = azul[..<azulrecortado]
let nuevoazulstring = String(azulre)
print(nuevoazulstring)


//Comparacion
if(azul != nuevoazulstring){
    print("no son iguales")
}

//uppercase
print(azul.uppercased())
//lower case
print(string1.lowercased())
var azulrepetido = String(repeating: azul, count: 3)
print (azulrepetido)

var cambiarazul = azul.replacingOccurrences(of: "hola", with: "adios")
print(cambiarazul)

let unionColores = ["rojo","amarillo","azul"]
let unioncadena = unionColores.joined(separator: ", ")
print(unioncadena)

//PALINDROMO


func palindromo(aux: String){
    var palabraaux: String = ""
    palabraaux = String(aux.reversed())
    if(aux == palabraaux){
        print("La palabra \(aux) si es un palindromo")
    }else{
        print("La palabra \(aux) no es palindromo")
    }
}

func anagrama(aux: String, aux1: String){
    var palabraaux: String = ""
    var arraypalabra:[Character] = []
    var arraypalabra2: [Character] = []
    for a in aux{
        arraypalabra.append(a)
    }
    for a in aux1{
        arraypalabra2.append(a)
    }
    if(arraypalabra.sorted() == arraypalabra2.sorted()){
        print("Si son anagramas")
    }
}

func isograma(aux: String){
    var arrayor: [Character] = []

    for a in aux{
        arrayor.append(a)
    }

    arrayor = arrayor.sorted()
    print(arrayor)
    var isograma = false
    for x in 0...arrayor.count-2{
        if(arrayor[x]==arrayor[x+1]){
            isograma = true
        }
    }
    if(isograma == true ){
        print("No es isograma")
    }
    else{
        print("Es isograma")
    }
}


var palabra = "aromma"
palindromo(aux: palabra)
var palabra2 = "maroma"
anagrama(aux: palabra, aux1: palabra2)
isograma(aux: palabra)

//