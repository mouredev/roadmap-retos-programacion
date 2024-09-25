// Ejemplos de Operadores

console.log(1 + 1) // Suma
console.log(1 - 1) // Resta
console.log(2 * 2) // Multiplicacion
console.log(2 / 2) // Division
console.log(5 % 2) // Modulo
console.log(2 ** 2) // Potenciacion

// Operaciones con enteros

console.log(3 < 2)
console.log(3 <= 2)
console.log(3 > 2)
console.log(3 >= 2)
console.log(3 == 2)
console.log(3 === 2)
console.log(3 != 2)

// Operadores logicos
console.log(3 < 2 && "hola" < "mundo")
console.log(3 < 2 || "hola" < "mundo")
console.log(!false)

// Operadores de asignacion
let myNumber = 1
console.log(myNumber)
myNumber += 1
console.log(myNumber)
myNumber -= 1
console.log(myNumber)
myNumber *= 1
console.log(myNumber)
myNumber /= 1
console.log(myNumber)
myNumber %= 1
console.log(myNumber)
myNumber **= 1
console.log(myNumber)


// Incremento
myNumber++
// Decremento
myNumber--

/*
Estructuras de control
*/
// Condicionales
let myName = "TizoG"
if (myName == "TizoG") {
    console.log("myName es 'TizoG'")
} else if(myName == "tizog"){
    console.log("myName es 'tizog'")
} else{
    console.log("miName no es 'TizoG' ni 'tizog'")
}

// Iteracion
for (let i = 0; i < 10; i++){
    console.log(`El valor actual de i es ${i}`)
}

// Manejo de excepciones
try{
    console.log("Primero se ejecutara este bloque")
}catch{
    console.log("Este bloque se ejecutara si en el bloque primero ocurre un error")
}finally{
    console.log("Finalmente se ejecutara este bloque de codigo")
}