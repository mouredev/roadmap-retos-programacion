/* OPERADORES ARITMÉTICOS */
console.log('*** OPERADORES ARITMÉTICOS ***\n')

let num1 = 20
let num2 = 10

// Addition (+)
let sum = num1 + num2
console.log(`La SUMA de ${num1} y ${num2} es: ${sum}`)

// Subtraction (-)
let difference  = num1 - num2
console.log(`La RESTA de ${num1} y ${num2} es: ${difference}`)

// Multiplication (*)
let product  = num1 * num2
console.log(`La MULTIPLICACIÓN de ${num1} y ${num2} es: ${product}`)

// Division (/)
let division = num1 / num2
console.log(`La DIVISIÓN de ${num1} y ${num2} es: ${division}`)

// Modulus (%)
let modulo = num1 % num2
console.log(`El MÓDULO de ${num1} y ${num2} es: ${modulo}`)

// Increment (++)
num1++
console.log(`El valor despues del incremento es: ${num1}`)

// Decrement (--)
num2--
console.log(`El valor despues del decremento es: ${num2}`)

// Exponentiation (**)
let result = num1 ** num2
console.log(`El resultado es: ${result}`)

// Unary negation (-)
let negation = -num1
console.log(`La NEGACIÓN es: ${negation}`)

/* OPERADORES DE ASIGNACIÓN */
console.log('\n*** OPERADORES DE ASIGNACIÓN ***\n')

// Asignación básica (=)
let numAssignmentExample1  = 5
console.log(`Asignación básica (=), el valor es: ${numAssignmentExample1}`)

// Asignación con suma (+=)
let numAssignmentExample2 = 5
numAssignmentExample2 += 3
console.log(`Asignación con suma (+=), el valor es: ${numAssignmentExample2}`)

// Asignación con resta (-=)
let numAssignmentExample3 = 5
numAssignmentExample3 -= 3
console.log(`Asignación con resta (-=), el valor es: ${numAssignmentExample3}`)

// Asignación con multiplicación (*=)
let numAssignmentExample4 = 5
numAssignmentExample4 *= 3
console.log(`Asignación con multiplicación (*=), el valor es: ${numAssignmentExample4}`)

// Asignación con división (/=)
let numAssignmentExample5 = 15
numAssignmentExample5 /= 3
console.log(`Asignación con división (/=), el valor es: ${numAssignmentExample5}`)

// Asignación con módulo (%=)
let numAssignmentExample6 = 7
numAssignmentExample6 %= 3
console.log(`Asignación con módulo (%=), el valor es: ${numAssignmentExample6}`)

// Asignación con exponenciación (**=)
let numAssignmentExample7 = 5
numAssignmentExample7 **= 3
console.log(`Asignación con exponenciación (**=), el valor es: ${numAssignmentExample7}`)

/* OPERADORES DE COMPARACIÓN */
console.log('\n*** OPERADORES DE COMPARACIÓN ***\n')
// Igual a (==)
let comparisonOperator1 = 5
let comparisonOperator1y = "5"
console.log(`Igual a (==), el valor es: ${comparisonOperator1 == comparisonOperator1y}`)

// No igual a (!=)
let comparisonOperator2 = 5
let comparisonOperator2y = "5"
console.log(`No igual a (!=), el valor es: ${comparisonOperator2 != comparisonOperator2y}`)

// Estrictamente igual a (===)
let comparisonOperator3 = 5
let comparisonOperator3y = "5"
console.log(`Estrictamente igual a (===), el valor es: ${comparisonOperator3 === comparisonOperator3y}`)

// Estrictamente no igual a (!==)
let comparisonOperator4 = 5
let comparisonOperator4y = "5"
console.log(`Estrictamente no igual a (!==), el valor es: ${comparisonOperator4 !== comparisonOperator4y}`)

// Mayor que (>)
let comparisonOperator5 = 5
let comparisonOperator5y = 10
console.log(`Mayor que (>), el valor es: ${comparisonOperator5 > comparisonOperator5y}`)

// Menor que (<)
let comparisonOperator6 = 5
let comparisonOperator6y = 10
console.log(`Menor que (<), el valor es: ${comparisonOperator6 < comparisonOperator6y}`)

// Mayor o igual que (>=)
let comparisonOperator7 = 5;
let comparisonOperator7y = 10;
console.log(`Mayor o igual que (>=), el valor es: ${comparisonOperator7 >= comparisonOperator7y}`)

// Menor o igual que (<=)
let comparisonOperator8 = 5;
let comparisonOperator8y = 10;
console.log(`Menor o igual que (<=), el valor es: ${comparisonOperator8 <= comparisonOperator8y}`)


/* OPERADORES LÓGICOS */
console.log('\n*** OPERADORES LÓGICOS ***\n')

// AND (&&)
let xAnd = true
let yAnd = false
let resultAnd = xAnd && yAnd
console.log(`AND (&&), el valor es: ${resultAnd}`)

// OR (||)
let xOr = true
let yOr = false
let resultOr = xOr || yOr
console.log(`OR (||), el valor es: ${resultOr}`)

// NOT (!)
let xNot = true
let resultNot = !xNot
console.log(result)
console.log(`NOT (!), el valor es: ${resultNot}`)

/* OPERADORES DE CADENAS */
console.log('\n*** OPERADORES DE CADENAS ***\n')

// Concatenación de cadenas con el operador suma (+)
let text1 = 'Hola'
let text2 = 'Mundo'
let mensaje1 = text1 + ', ' + text2 + '!'
console.log(`${mensaje1}`)

// Concatenación de cadenas con el operador de asignación con suma (+=
let mensaje2 = '¡Felicitaciones'
console.log(`- ${mensaje2}`)
mensaje2 += ', has ganado';
console.log(`-- ${mensaje2}`)
mensaje2 += ' el primer lugar!'
console.log(`--- ${mensaje2}`)

/* OPERADORES DE INCREMENTO Y DECREMENTO */
console.log('\n*** OPERADORES DE INCREMENTO Y DECREMENTO ***\n')

// Incremento (++)
// - Incremento de prefijo (++variable)
let contador1 = 5
let resultadoIncrement1 = ++contador1
console.log(`Contador es: ${contador1}, Resultado es: ${resultadoIncrement1}`)


// Incremento (++)
// - Incremento de sufijo (variable++)
let contador2 = 5
let resultadoIncrement2 = contador2++
console.log(`Contador es: ${contador2}, Resultado es: ${resultadoIncrement2}`)

// Decremento (--)
// - Decremento de prefijo (--variable)
let contador3 = 5
let resultadoDecrement1 = --contador3
console.log(`Contador es: ${contador3}, Resultado es: ${resultadoDecrement1}`)

// Decremento (--)
// - Decremento de sufijo (variable--)

let contador4 = 5
let resultadoDecrement2 = contador4--
console.log(`Contador es: ${contador4}, Resultado es: ${resultadoDecrement2}`)

/* OPERADORES TERNARIOS  */
console.log('\n*** OPERADORES TERNARIO ***\n')
let age = 25
let finalMessage = age >= 18 ? 'Eres mayor de edad.' : 'Eres menor de edad.'
console.log(`Ternario (condicion ? expresionSiTrue : expresionSiFalse), el valor es: ${finalMessage}`)

/* OPERADORES DE TIPO  */
console.log('\n*** OPERADORES DE TIPO ***\n')

// typeof
let number = 42
console.log(`El tipo es, ${typeof number}`)

let cadena1 = 'Hola, mundo!' 
console.log(`El tipo es, ${typeof cadena1}`)

let funcion = function () {}
console.log(`El tipo es, ${typeof funcion}`)


// Conversiones de tipo explícitas (parseInt, parseFloat, String, Number, y Boolean)
let numStr = '42'
let entero = parseInt(numStr)
console.log(`El tipo es, ${typeof entero} y el valor es ${entero}`)

let cadena2 = 42 
let text = String(cadena2); 
console.log(`El tipo es, ${typeof text} y el valor es ${text}`)

/* BIT  */
console.log('\n*** BIT ***\n')

// Operador AND (&)
/*En este ejemplo, la operación AND se realiza bit a bit en los números aAnd y bAnd. El resultado es 1, ya que ambos bits en la posición 1 son 1.*/
let aAnd = 5 // binario: 0101
let bAnd = 3 // binario: 0011
let resultadoAnd = aAnd & bAnd
console.log(`Operador AND (&), el resultado es: ${resultadoAnd}`)


// Operador OR (|)
/*En este ejemplo, la operación OR se realiza bit a bit en los números aOr y bOr. El resultado es 7, ya que al menos uno de los bits en las posiciones 1 y 2 es 1.*/
let aOr = 5 // binario: 0101
let bOr = 3 // binario: 0011
let resultadoOr = aOr | bOr
console.log(`Operador OR (|), el resultado es: ${resultadoOr}`)

// Operador XOR (^)
/*En este ejemplo, la operación XOR se realiza bit a bit en los números aXor y bXor. El resultado es 6, ya que los bits en las posiciones 2 y 3 son diferentes.*/
let aXor = 5 // binario: 0101
let bXor = 3 // binario: 0011
let resultadoXor = aXor ^ bXor
console.log(`Operador XOR (^), el resultado es: ${resultadoXor}`)

// Operador NOT (~)
/*En este ejemplo, la operación NOT invierte todos los bits del número aNot. El resultado es -6. */
let aNot = 5 // binario: 0101
let resultadoNot = ~aNot
console.log(`Operador NOT (~), el resultado es: ${resultadoNot}`)

// Desplazamiento a la izquierda (<<)
/*En este ejemplo, los bits del número a se desplazan 2 posiciones a la izquierda. El resultado es 20. */
let adi = 5 // binario: 0000 0101
let resultadodi = adi << 2
console.log(`Desplazamiento a la izquierda (<<), el resultado es: ${resultadodi}`)

// Desplazamiento a la derecha (>>)
/*El resultado es 5 porque cada desplazamiento a la derecha divide el número por 2. */
let add = 20 // binario: 0001 0100
let resultadodd = add >> 2
console.log(`Desplazamiento a la derecha (>>), el resultado es: ${resultadodd}`)

// Desplazamiento a la derecha sin signo (>>>)
/*El resultado es 1073741820 porque el desplazamiento a la derecha sin signo siempre llena los bits vacíos con 0, lo que da como resultado es un número positivo. */
let xdds = -20 // 11101100 en binario (número negativo)
let resultdds = xdds >>> 2 // 00101100 en binario (desplazamiento 2 posiciones a la derecha sin signo)
console.log(`Desplazamiento a la derecha sin signo (>>>), el resultado es: ${resultdds}`)

/* ESTRUCTURAS DE CONTROL  */
console.log('\n*** ESTRUCTURAS DE CONTROL ***\n')

// If-else
let iFElse = 10
if(iFElse > 5){
    console.log(`(If-else), El valor de ${iFElse} es mayor a 5`)
} else {
    console.log(`(If-else), El valor de  ${iFElse} es menor a 5`)
}

// Switch
let nSwitch = 10
switch(nSwitch){
    case 10:
        console.log(`(Switch), El valor de ${nSwitch} es igual a 10`)
        break
    case 20:
        console.log(`(Switch), El valor de ${nSwitch} es igual a 20`)
        break
    default:
        console.log('No se cumplió ningún caso')
        break
}

// While
let iWhile = 0
while(iWhile <= 10){
    if(iWhile % 2 == 0) {
        console.log('(While), ', iWhile)
        }
    iWhile ++
}

// Do-while
let iDoWhile = 5
do {
    console.log('(Do-while), example')
    iDoWhile ++
} while(iDoWhile < 10)

// For
let forExample = 5
for (let i = 1; i <= 10; i++) {
    console.log(`${forExample} x ${i} = ${forExample * i}`);
}

// Try-catch
try{
    ejemplo()
}
catch(error){
    console.log('(Try-catch), Error: ' +  error)
}

/* EXTRA  */
console.log('\n*** EXTRA ***\n')

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}