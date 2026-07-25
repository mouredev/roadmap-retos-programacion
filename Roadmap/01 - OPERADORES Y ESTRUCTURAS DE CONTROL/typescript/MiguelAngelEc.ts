
// Operadores Aritmeticos
//suma
let suma:number = 1 + 1
console.log(`La Suma es ${suma}`)
//resta
let resta:number = 2 - 1
console.log(`La Resta es ${resta}`)
//multiplicacion
let multiplicacion:number = 2 * 2
console.log(`La Multiplicacion es ${multiplicacion}`)
//division
let division:number = 4 / 2
console.log(`La Division es ${division}`)
//modulo
let modulo:number = 5 % 2
console.log(`El Modulo es ${modulo}`)
//incremento
let incremento:number = 1
incremento++
console.log(`El Incremento es ${incremento}`)
//decremento
let decremento:number = 1
decremento--
console.log(`El Decremento es ${decremento}`)
//exponenciacion
let exponenciacion:number = 2 ** 3
console.log(`La Exponenciacion es ${exponenciacion}`)
let resto:number = 5 % 2
console.log(`El Resto es ${resto}`)

// Operadores Logicos
//and
let and:boolean = true && true
//or
let or:boolean = true || false
//not
let not:boolean = !true

//condicionales
function condicionales(num: number) {
    if (num >= 18) {
        console.log("Mayor de edad")
    } else if (isNaN(num)) {
        console.log("Porfavor ingrese un numero valido")
    } else {
        console.log("Menor de edad")
    }
}
let edadVar = condicionales(18)
console.log(edadVar)

while(1<2){
    console.log("while")
}

//iterativas
for (let i:number = 0; i < 10; i++) {
    console.log(i)
}

//excepciones
try {
    console.log("try")
} catch (error) {
    console.log("catch")
} finally {
    console.log("finally")
}

//DIFICULTAD EXTRA (opcional):
//Crea un programa que imprima por consola todos los números comprendidos
//entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
let i: number = 10;

while (i <= 55) {
    if (i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
    i++; 
}
