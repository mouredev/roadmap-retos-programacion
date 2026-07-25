//OPERADORES


//Operadores Aritmeticos
console.log(`Suma: ${7 + 5}`) //Suma
console.log(`Resta: ${7 - 5}`) //Resta
console.log(`Multiplicación: ${7 * 5}`) //Multiplicación
console.log(`División: ${7 / 5}`) //División
console.log(`División: ${7 / 5}`) //División
console.log(`Módulo: ${7 % 5}`) //Resto de Division
console.log(`Exponenciación: ${7 ** 5}`) //Potencia

//Operadores de comparacion
console.log(`Mayor que: ${7 > 5}`)
console.log(`Menor que: ${5 < 7}`)
console.log(`Igual que: ${7 === 7}`)
console.log(`Distinto que: ${5 !== 7}`)
console.log(`Mayor o igual que: ${5 >= 5}`)
console.log(`Menor o igual que: ${7 <= 7}`)

//Operadores Lógicos
let a = true
let b = false

console.log("a AND b", a && b)
console.log("a OR b", a || b)
console.log("NOT a", !a )

//Operadores de Assignación

let c = 4   // Asignacion
c += 5      // Suma y Asignacion
c -= 5      // Resta y Asignacion
c *= 5      // Multiplicacion y Asignacion
c /= 5      // Division y Asignacion
c %= 5      // Resto y Asignacion
c **= 5     // Potencia y Asignacion


//Operadores de bits
console.log(`5 AND 3: ${5 & 3}`) // 0101 & 0011 =  0001
console.log(`5 OR 3: ${5 | 3}`) // 0101 | 0011 =  0111
console.log(`5 XOR 3: ${5 ^ 3}`) // 0101 ^ 0011 =  0110
console.log(`5 shift left 1: ${5 << 1}`) // 0101  =  1010
console.log(`5 shift rigth 1: ${5 >> 1}`) // 0101 =  0010

//ESTRUCTURAS DE CONTROL
let edad =18

//Condicional: if-else
if (edad >= 18) {
    console.log("Eres Mayor de edad")
}else if (edad <=3){
    console.log("Eres un bebe")
}else{
    console.log("Eres menor de edad")
}

//Condicional: Switch
let fruta ="kiwi"

switch (fruta) {
    case "kiwi" :
        console.log("Es un kiwi")
        break;
    case "naranja" :
        console.log("Eres una naranja")
        break;
    case "piña" :
        console.log("Eres una piña")
        break;
    default:
        console.log("No se que fruta eres")
}

//Bucle for
for (let i = 1; i <= 10; i++) {
    console.log("Numero: ", i)
}

//Bucle while
let cont = 10
while (cont >= 1) {
    console.log("Numero: ", cont)
    cont --;
}

//Manejo de excepciones try-catch
try {
    let resultado = 10/0 // Error Logico
    console.log("Resultado: ", resultado)
}catch(error){
    console.log("¡Error atrapado! " , error.message)
}

//DIFICULTAD EXTRA:números entre 10 y 55 , pares, ni 16 ni múltiplos de 3.
console.log("=== DIFICULTAD EXTRA ===")
for (let i = 10; i <= 55; i++) {
    if(i % 2 === 0 && i !== 16 && i % 3 !==0) {
        console.log("Numero: ", i)
    }
}