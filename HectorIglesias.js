/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

//OPERADORES ARITMÉTICOS
let x = 5
let y = 5
let resultado = 0

//Operador de asignación  =
//Operador de suma +
resultado = x + y 
console.log(x +"+"+ y +"="+resultado)
//Operador de resta -
resultado = x - y
console.log(x +"-"+ y +"="+resultado)
//Operador de multiplicación * 
resultado = x * y
console.log(x +"*"+ y +"="+resultado)
//Operador de división (/) y del resto de la división(%)
resultado = x / y
console.log(x +"-"+ y +"="+resultado)
resultado = x % y
console.log("El resto de esta división es "+resultado)
//Operador de exponenciación
resultado = x**y
console.log(x +" elevado a "+ y +" es "+resultado)

//OPERADORES DE COMPARACIÓN

//Operadores de igualdad == != === !==
console.log(x == y)
console.log(x != y)
console.log(x === y)
console.log(x !== y)
//Operador mayor que >
console.log(x > y)
//Operador mayor o igual que >=
console.log(x >= y)
//Operador menor que <
console.log(x < y)
//Operador menor o igual que <=
console.log(x <= y)

//OPERADORES DE BITS

//Operador AND a nivel de bits &
resultado = x & y
console.log(x +"&"+ y + " a nivel de BITS es "+resultado)
//Operador OR a nivel de bits |
resultado = x | y
console.log(x +"|"+ y + " a nivel de BITS es "+resultado)
//Operador XOR a nivel de bits ^
resultado = x ^ y
console.log(x +"^"+ y + " a nivel de BITS es "+resultado)
//Operador NOT a nivel de bits ~
resultado =  ~y
console.log("~"+ y + " a nivel de BITS es "+resultado)
//Operador de desplazamiento hacia la derecha
resultado = x >> 1
console.log("Desplazamiento hacia la derecha "+resultado)
//Operador de desplazamiento hacia la derecha
resultado = x << 1
console.log("Desplazamiento hacia la izquierda "+resultado)

//OPERADORES LÓGICOS 
let bool1 = true
let bool2 = false
//AND lógico &&
console.log(bool1 && bool2)
//OR lógico ||
console.log(bool1 || bool2)
//NOT lógico !
console.log(!bool1, !bool2)

//OPERADORES DE PERTENENCIA
let array = [0, 1, 2, 3, 4, 5]
let found = 3 in array
console.log(found)
let not_found = 9 in array
console.log(not_found)


//ESCTRUCTURAS DE CONTROL

//IF-ELSE
let num = 1

if(num > 0)
    console.log("El número " +num+ " es mayor que 0")
else if (num < 0)
    console.log("El número " +num+ " es menor que 0")
else
console.log("El número es 0")

//SWITCH
switch(num){
    case 1:
        console.log("El número es 1")
    case 2:
        console.log("El número es 2")
    case 3:
        console.log("El número es 3")
    default:
        console.log("El número es distinto a 1, 2 o 3")
}

//FOR
let array2 = ["hola", " ", "mundo"]
for(let i=0; i<array2.length; i++){
    console.log(array2[i])
}

//WHILE
let num2 = 0

while(num2 < 5){
    console.log(num2)
    num2 = num2 + 1
}

//DO WHILE
let num3 = 0

do{
    console.log(num3)
    num3 = num3 + 1
}while (num3 < 5)

//EXCEPCIONES
let var3 = 5

try {
    if (var3 === 5) {
        throw new Error("El número es igual a 5")
    }
    console.log('El número es distinto de 5')
} catch (error) {
    console.log(`Se ha producido un error debido a -> ${error.message}`)
}

console.log('\nBloque try-catch-finally')
try {
    if (var3 === 5) {
        throw new Error("El número es igual a 5")
    }
    console.log("El número es distinto de 5")
} catch (error) {
    console.log("Se ha producido un error debido a "+error.message)
} finally {
    console.log("Bloque finally. Esto siempre se ejecuta haya o no excepción")
}

//DIFICULTAD EXTRA
for(let i= 10; i <= 55; i++){
    if (i % 2 == 0){
        if((i != 16) && (i % 3 != 0)){
            console.log(i)
        }
    }
    if(i == 55){
            console.log(i)
        }
}