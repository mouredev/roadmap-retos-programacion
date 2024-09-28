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

//Operadores aritméticos
    //Suma 
    let suma = 1 + 2
    //Resta 
    let resta = 7 - 8
    //Multiplicación
    let multiplicacion = 2 * 2
    //División
    let division = 10 / 2
    //Módulo (es el resto de la división)
    let modulo = 9 % 2
    //Exponente 
    let exponente = 3**3
    // Incremento (el resultado es 1 + la variable )
    let incremento = 6 
    incremento++
    // Decremento (el resultado es la variable - 1)
    let decremento = 8
    decremento--

// Operadores lógicos (vamos a declarar constantes para este apartado)
    const valorTrue = true
    const valorFalse = false
    //Operación AND (la salida será True cuando todas las variables sean true)
    let AND = valorFalse && valorTrue
    //Operación OR (la salida será True cuando alguna variable sea true)
    let OR = valorFalse || valorTrue
    //Devuelve false si su único operando es true, de lo contrario devuelve true
    let NOT = !valorTrue

//Operadores de comparación
    //Igualdad 
    let igualdad = 3==3
    //No igualdad
    let noIgualdad = 4 !=56
    //Estrictamente igual (a diferencia del de igualdad este tambien compara el tipo de dato
    let estrictamenteIgual = 2===2
    //Desigualdad estricta (devulve true cuando los valores son iguales pero no del mismo tipo de dato)
    let desigualdadEstricta = 3 !== '3' // en este caso comparamos un número con una cadena de texto
    //Mayor que 
    let mayorQue = 23 > 18
    //Menor que
    let menorQue = 12 < 34
    //Mayor o igual que 
    let mayorOIgual = 33 >= 33
    //Menor o igual que 
    let menorOIgual = 12 <= 13

//Operadores de asignación
    let numero1 = 3
    let numero2 = 5
    //Operador suma
    numero1 += numero2 // numero1 = numero1 + numero 2
    //Operador resta 
    numero2 -= numero1 //numero2 = numero2 - numero1
    //Operador multiplicación
    numero1 *= numero2 // numero1 = numero1 * numero2
    //Operador división
    numero1 /= numero2 // numero1 = numero1 / numero2
    //Operador módulo
    numero2 %= numero1 // numero2 = resto de la división entre numero 2 y numero 1
    //Operador exponente 
    numero1 **= numero2 //numero1 = numero1 ** numero2

//Operadores de identidad
    let numero3 = 7
    let numero4 = 9
    //Operador de igualdad esctricta
    numero3 === numero4 //En caso de que sean estrictamente iguales el terminal devolverá true
    //Operador de desigualdad estricta
    numero3 !== numero4 //Si son desiguales en algo el ternimal devuelve true

//Operadores de pertenencia
    let myArray = [1,2,3,4,5,6]
    const pertTrue = 3 in myArray //Devuelve true
    const pertFalse = 33 in myArray //Devuelve false

//Operadores bit a bit (Los números se convierten a numeros binarios y se hacen las operaciones lógicas correspondientes bit a bit)
    let numero5 = 15
    let numero6 = 9
    //AND a nivel de bits (Devuelve un uno en cada posición del bit para los que los bits correspondientes de ambos operandos son unos)
    let bitAnd = numero5 & numero6 // 1111 (15) & 1001 (9)= 1001, la operación AND devuelve 1 cuando ambos bits sean 1 y 0 para el resto de los casos
    //OR a nivel de bits (Devuelve un uno en cada posición del bit para los que los bits correspondientes de ambos operandos no sean 0)
    let bitOr = numero5 | numero6 // 1111 (15) & 1001 (9)= 1111, la operación OR devuelve 1 cuando ambos bits sean 1 o 0 y 0 para el resto de los casos
    //XOR a nivel de bits
    let bitXor = numero5 ^ numero6 // 1111 (15) & 1001 (9)= 0110, la operación XOR devuelve 1 cuando ambos bits sean distintosy 0 para cuando sean iguales
    //NOT a nivel de bits
    let bitNot = ~numero5 //Convierte los bits los que son 1 pasan a 0 y vicerversa 
    //Desplazamiento a la izquierda
    let bitIzq = numero6<< 3 // 9<<3 desplaza el numero6 3 ceros a la izquierda y da resultado 1001000
    //Desplazamiento a la derecha 
    let bitDcha = numero6 >> 3// 9>>3 desplaza el numero6 3 ceros a la derecha y da resultado 1

//Estructuras de control

    //Sentencia IF si se cumple la condición se ejecuta el bloque de código que hay dentro de la sentencia, en caso contrario se ejecuta otro código
    console.log("Resultado Sentencia IF:")
    if (numero1 < numero2){

        console.log("Número 1 es mayor que número 2")
    
    }
    else {

        console.log("Número 2 es mayor que número 1")
    }
    
    //Sentencia SWITCH ejecuta un bloque de código en función de un valor predeterminado
    console.log("Resultado Sentencia SWITCH:")
    const prompt = require('prompt-sync')()
    let nuevoNumero = parseInt(prompt('Escribe un número del 1 al 3:'))
    switch(nuevoNumero){
        case 1:
            console.log("Has escogido el número 1")
            break
        case 2:
            console.log("Has escogido el número 2")
            break
        case 3:
            console.log("Has escogido el número 3") 
            break
        default:
            console.log("No has escogido ningún número")
            break
    }

    // Bucle WHILE la acción se ejecuta hasta que la condición deja de cumplirse (ideal para cuando no sabemos el número de iteraciones del bucle)
    console.log("Resultado Bucle WHILE:")
        let numero7 = 1
        while (numero7 <= 9){
            console.log(numero7)
            numero7++
            
        }
    
    // Bucle FOR la acción se ejecuta hasta que se cumple con el número máximo de iteraciones
    console.log("Resultado Bucle FOR:")
        for(let i = 0; i < 5; i++){
            console.log("Es mi primer bucle for en JavaScript")
        }
    
    //Bucle DO WHILE  a diferencia del bucle while este se ejecuta una vez al menos, despues se comprueba si la condición es true
    console.log("Resultado Bucle DO WHILE:")
        let numero10= 3
        do {
            console.log("Este es mi primer bucle Do en JavaScript")
            numero10++
        }
        while (numero10 < 5)

//DIFICULTAD EXTRA 
console.log("Resultado Dificultad EXTRA:")
for (let numero = 10;numero<=55;numero++){
    if (numero % 2 === 0 && numero !== 16 && numero % 3 !== 0){  
        console.log(numero)
    }
    
}
/* en la primera condición filtramos para que los números sean pares , en la segunda quitamos el 16
y en la tercera quitamos los multiplos de 3 */



    