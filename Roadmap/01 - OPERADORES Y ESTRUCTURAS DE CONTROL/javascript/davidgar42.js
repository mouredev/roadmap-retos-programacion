/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * 
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
let num1 = 3
let num2 = 6
let resultado

//Operadores Aritmeticos
console.log("Operadores Aritmeticos")
console.log(num1 + num2)
console.log(num1 - num2)
console.log(num1 * num2)
console.log(num2 / num1)
console.log(num2 % num1)
console.log(num1 ** num2)
num1++
console.log(num1)
num1--
console.log(num1)

//Operadores Lógicos
console.log("Operadores Logicos")

console.log(num1 > 0 && num2 > 0)
console.log(num1 > 0 || num2 < 5)
console.log(!(num1 > 0) || num2 < 0)

//Operadores de comparación
console.info("Operadores de comparación")
console.log(num1)
console.log(num1 == "3")
console.log(num1 === num2)
console.log(num1 != num2)
console.log(num1 !== num2)
console.log(num1 > num2)
console.log(num1 < num2)
console.log(num1 >= num2)
console.log(num1 <= num2)

//Operadores de asignación
console.info("Operadores de asignación")

console.log(num1 = num2)
console.log(num1 += 2)
console.log(num1 -= 3)
console.log(num1 *= 4)
console.log(num1 /= 4)
console.log(num1 %= 4)
console.log(num1 **= 4)

//Pertenencia
console.info("Operadores de Pertenencia")

let cadena = "Hola mundo"
console.log(cadena.includes("Hola"))
console.log(cadena.includes("hola"))

//Condicionales, iterativas, excepciones...

if ( 5 > 4){
    console.log("5 es mayor que 4")
}else if (6 > 5){
    console.log("seis es mayor que cinco")
}else{
    console.log("todos los demas casos")
}

for(let j = 0; j < 10; j++){
    console.log(j)
}

let myArray = [1,"lunes",3,true,8]

for (let i of myArray){
    console.log(i)
}

let myObjet = {
    name: "David",
    surname: "Garcia",
    age: 38,
    city: "Madrid",
}
for (let a in myObjet){
    console.log(a +  ": "+ myObjet[a])
}

//While
let contador = 0
while(contador < 10){
    contador++
    console.log(contador)
}

//Do-While

contador = 0
console.log("Do - While")
do{
    console.log(contador)
    contador++
}while(contador < 10)

//Excepciones
console.log("Probando Excepciones")
try{
    console.log(5/a);
}
catch(error){
    console.log(`El tipo de Error es: ${error}`);
}
finally{
    console.log("Esto se ejecuta siempre pase lo que pase")
}

/*DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

for (let numero = 10; numero < 56; numero+=2){
    if (numero != 16 && numero % 3 != 0){
        console.log(numero)
    }
}