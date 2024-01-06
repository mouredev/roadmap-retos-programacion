// OPERADORES ARITMÉTICOS
console.log("Suma: " + ( 3 + 4 )) // Suma -> 7
console.log("Resta: " + ( 3 - 4 )) // Resta -> -1
console.log("División: " + ( 3 / 4 )) // División -> 0.75
console.log("Multiplicación: " + ( 3 * 4 )) // Multiplicación -> 12
console.log("Módulo: " + ( 3 % 4 )) // Módulo -> 3
console.log("Potencia: " + ( 3 ** 4 )) // Potencia -> 81

// OPERADORES LÓGICOS
let and = true && true // Devuelve true ya que ambas son verdaderas
let or = true || false // Devuelve true porque UNA es verdadera
let not = !true // Devuelve false

console.log("AND: " + and)
console.log("OR: " + or)
console.log("NOT: " + not)

// OPERADORES DE COMPARACIÓN
let mayorQue = 5>2
let menorQue = 3<8
let mayorIgualQue = 6>=4
let menorIgualQue = 1<=12
/* No es lo mismo == que ===, doble igual comprueba si el valor es el mismo 
y el triple igual comprueba si el valor y el tipo son lo mismo
 Ejemplo:

 let x = 5
 let y = "5"
 console.log(x == y) //Es true porque al convertirse la variable 'y' de texto a numero es 5

 console.log(x === y) //Es false porque la variable 'y' es tipo texto
 */

let igualQue = 2===2
let noEsIgual = 2!=3

// OPERADORES DE ASIGNACIÓN

let asignacionAdicion = 5
asignacionAdicion += 3
console.log("Adicion: " + asignacionAdicion)

let asignacionResta = 12
asignacionResta -= 4
console.log("Resta: " + asignacionResta)

let asignacionMultiplicacion = 7
asignacionMultiplicacion *= 2
console.log("Multiplicación: " + asignacionMultiplicacion)

let asignacionDivision = 7
asignacionDivision /= 2
console.log("División: " + asignacionDivision)

let asignacionModulo = 7
asignacionModulo %= 2
console.log("Modulo: " + asignacionModulo)

let asignacionExponencial = 2
asignacionExponencial **= 3
console.log("Exponencial: " + asignacionExponencial)

let asignacionDesplazamientoIzquierda = 5
asignacionDesplazamientoIzquierda <<= 1
console.log("Desplazamiento a la izquierda: " + asignacionDesplazamientoIzquierda)

let asignacionDesplazamientoDerecha = 5
asignacionDesplazamientoDerecha >>= 1
console.log("Desplazamiento a la derecha: " + asignacionDesplazamientoDerecha)

let asignacionDesplazamientoDerechaSinSigno = -5
asignacionDesplazamientoDerechaSinSigno >>>= 1
console.log("Desplazamiento a la derecha sin signo: " + asignacionDesplazamientoDerechaSinSigno)

let asignacionAndBit = 5
asignacionAndBit &= 3
console.log("AND bit a bit: " + asignacionAndBit)

let asignacionXorBit = 5
asignacionXorBit ^= 1
console.log("XOR bit a bit: " + asignacionXorBit)

let asignacionOrBit = 5
asignacionOrBit |= 2
console.log("OR bit a bit: " + asignacionOrBit)

// OPERADORES DE IDENTIDAD
let identidadEstricta = 5 === "5"
let desigualdadEstricta = 5 !== "5"
console.log("Identidad estricta: " + identidadEstricta)
console.log("Desigualdad estricta: " + desigualdadEstricta)

// OPERADORES DE PERTENENCIA ARRAY
let array = [1, 2, 3, 4, 5]
let prueba1 = 3 in array
let prueba2 = 6 in array
console.log("Pertenencia: " + prueba1)
console.log("No pertenencia: " + prueba2)

// OPERADORES DE BITS
let bitAnd = 5 & 3
let bitOr = 5 | 3
let bitXor = 5 ^ 3
let bitNot = ~5
let bitDesplazamientoIzquierda = 5 << 1
let bitDesplazamientoDerecha = 5 >> 1
let bitDesplazamientoDerechaSinSigno = -5 >>> 1

console.log("AND bit a bit: " + bitAnd)
console.log("OR bit a bit: " + bitOr)
console.log("XOR bit a bit: " + bitXor)
console.log("NOT bit a bit: " + bitNot)
console.log("Desplazamiento a la izquierda: " + bitDesplazamientoIzquierda)
console.log("Desplazamiento a la derecha: " + bitDesplazamientoDerecha)
console.log("Desplazamiento a la derecha sin signo: " + bitDesplazamientoDerechaSinSigno)

// ESTUCTURAS DE CONTROL

// IF-ELSE
if (5 > 3) {
    console.log("5 es mayor que 3")
} else {
    console.log("5 no es mayor que 3")
}

// SWITCH
let opt = 2
switch (opt) {
    case 1:
        console.log("Se ha seleccionado la opcion 1")
        break
    case 2:
        console.log("Se ha seleccionado la opcion 2")
        break
    case 3:
        console.log("Se ha seleccionado la opcion 3")
        break
    case 4:
        console.log("Se ha seleccionado la opcion 4")
        break
    case 5:
        console.log("Se ha seleccionado la opcion 5")
        break
    default:
        console.log("No es ninguno de los anteriores")
}

// WHILE
let i = 0
while (i < 5) {
    console.log("While: "+i)
    i++
}

// DO-WHILE
let j = 0
do {
    console.log("DO-WHILE: "+j)
    j++
}while (j < 5)

// FOR
for (let k = 0; k < 5; k++) {
    console.log("FOR: "+k)
}

// FOR-IN
const automovil = {
    marca: 'Toyota',
    modelo: 'GR YARIS',
    anio: 2021,
    color: 'Blanco'
};

for (const propiedad in automovil) {
    console.log(propiedad + ": " + automovil[propiedad]);
}

// FOR-OF
const colores = ['Rojo', 'Azul', 'Verde', 'Amarillo'];

for (const color of colores) {
    console.log(color);
}

// TRY-CATCH-FINALLY
try {
    if(5>3){
        throw new Error("Esto es una excepción")
    }
    console.log("No se ha lanzado la excepción") // Si se lanza la excepción, esta parte no se ejecutará.
}catch (error) {
    console.log(error.message)
}finally { // Esta parte se puede omitir, el finally no es obligatorio. Aqui se puede poner codigo que se ejecutara siempre haya o no excepción
    console.log("Fin del bloque try-catch-finally. Esto se ejecuta siempre")
}

// EJERCICIO EXTRA
for(let i = 10; i<55; i++){
    if(i % 2 == 0 && i != 16 && i % 3 != 0){
        console.log(i)
    }
}