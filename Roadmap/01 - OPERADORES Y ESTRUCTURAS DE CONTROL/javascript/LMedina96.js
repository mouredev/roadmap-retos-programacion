/*
# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
> #### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

## Ejercicio

```
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

const number1 = 20
const number2 = 4
let result
let booleanResult
let asignationResult

//Operadores aritmeticos
console.log('OPERADORES ARITMETICOS:')
const operadoresAritmeticos = [
    {operador: 'Suma', simbolo: '+'},
    {operador: 'Resta', simbolo: '-'},
    {operador: 'Multiplicacion', simbolo: '*'},
    {operador: 'Division', simbolo: '/'},
    {operador: 'Resto', simbolo: '%'},
    {operador: 'Exponencial', simbolo: '**'},
]

for (const operador of operadoresAritmeticos) {
    result = eval(`${number1} ${operador.simbolo} ${number2}`)
    console.log(`Resultado del operador aritmetico ${operador.operador}: ${number1} ${operador.simbolo} ${number2} = ${result}`)
}
console.log('')
console.log('OPERADORES DE COMPARACIÓN:')
//Operadores de comparación
const operadoresComparacion = [
    {operador: 'Mayor que', simbolo: '>'},
    {operador: 'Menor que', simbolo: '<'},
    {operador: 'Mayor o igual que', simbolo: '>='},
    {operador: 'Menor o igual que', simbolo: '<='},
    {operador: 'Igualdad', simbolo: '=='},
    {operador: 'Igualdad Estricta', simbolo: '==='},
    {operador: 'Desigualdad', simbolo: '!='},
    {operador: 'Desigualdad Estricta', simbolo: '!=='},
]

for (const operador of operadoresComparacion) {
    booleanResult = eval(`${number1} ${operador.simbolo} ${number2}`)
    console.log(`Resultado del operador de comparación ${operador.operador}: ¿${number1} ${operador.simbolo} ${number2}? ${booleanResult}`)
}

let asign1 = 20;
let asign2 = 40;

console.log('')
console.log('OPERADORES DE ASIGNACIÓN:')
// Operadores de asignación
const operadoresAsignacion = [
    { operador: 'Asignacion', simbolo: '=' },
    { operador: 'Asignacion de adicion', simbolo: '+=' },
    { operador: 'Asignacion de resta', simbolo: '-=' },
    { operador: 'Asignacion de multiplicacion', simbolo: '*=' },
    { operador: 'Asignacion de division', simbolo: '/=' },
    { operador: 'Asignacion de exponenciacion', simbolo: '**=' },
];

for (const operador of operadoresAsignacion) {
    let newAsign1 = asign1
    let result;

    switch (operador.simbolo) {
        case '=':
            newAsign1 = asign2;
            result = newAsign1
            console.log(`${operador.operador}: (${asign1} ${operador.simbolo} ${asign2}) = ${result}`)
            break;
        case '+=':
            result = newAsign1 += asign2;
            console.log(`${operador.operador}: (${asign1} ${operador.simbolo} ${asign2}) = ${result}`)
            break;
        case '-=':
            result = newAsign1 -= asign2;
            console.log(`${operador.operador}: (${asign1} ${operador.simbolo} ${asign2}) = ${result}`)
            break;
        case '*=':
            result = newAsign1 *= asign2;
            console.log(`${operador.operador}: (${asign1} ${operador.simbolo} ${asign2}) = ${result}`)
            break;
        case '/=':
            result = newAsign1 /= asign2;
            console.log(`${operador.operador}: (${asign1} ${operador.simbolo} ${asign2}) = ${result}`)
            break;
        case '**=':
            result = newAsign1 **= asign2;
            console.log(`${operador.operador}: (${asign1} ${operador.simbolo} ${asign2}) = ${result}`)
            break;
        default:
            result = 'Operador no reconocido';
    }
}

//Tipos de condicionales
const cond1 = 10
const cond2 = 20
const cond3 = 30

console.log('')
console.log('CONDICIONALES:')

//Condicional IF...ELSE
console.log(`Condición 1: ${cond1}`)
console.log(`Condición 2: ${cond2}`)
console.log(`Condición 3: ${cond3}`)

console.log("CONDICIÓN IF:")
console.log('Chequeamos si la condición 2 es mayor a la condición 1')

if (cond2 > cond1) {
    console.log(`¿${cond2} > ${cond1}?`, cond2 > cond1)
}

console.log('CONDICION IF...ELSE')
console.log('Chequeamos si la condición 2 es menor a la condición 1')

if (cond2 < cond1) {
    console.log(`¿${cond2} > ${cond1}?`, cond2 > cond1)
} else {
    console.log('La condición no se cumple')
}

console.log('CONDICION IF...ELSE IF...ELSE')
console.log('Chequeamos si la condición 2 es menor a la condición 1, en caso de no cumplirse chequeamos si la condición 3 es mayor a la condición 2')

if (cond2 < cond1) {
    console.log(`¿${cond2} > ${cond1}?`, cond2 > cond1)
} else if (cond3 > cond2) {
    console.log(`¿${cond3} > ${cond2}?`, cond3 > cond2)
}
else {
    console.log('No se cumple ninguna condición')
}

//Condicional Switch

console.log('')
console.log('CONDICION SWITCH:')

let diaDeLaSemana = "Lunes";

console.log("Condicional Switch en caso de mandarle un día de semana correcto")

switch (diaDeLaSemana) {
    case "Lunes":
        console.log("Hoy es lunes.");
        break;
    case "Martes":
        console.log("Hoy es martes.");
        break;
    case "Miércoles":
        console.log("Hoy es miércoles.");
        break;
    case "Jueves":
        console.log("Hoy es jueves.");
        break;
    case "Viernes":
        console.log("Hoy es viernes.");
        break;
    case "Sábado":
    case "Domingo":
        console.log("¡Es fin de semana!");
        break;
    default:
        console.log("Día no reconocido. ¿Estamos en una dimensión diferente?");
}

console.log("Condicional Switch en caso de mandarle un día de semana INcorrecto, en este caso el día 'PEPE'")

let diaDeLaSemanaIncorrecto = "Pepe"

switch (diaDeLaSemanaIncorrecto) {
    case "Lunes":
        console.log("Hoy es lunes.");
        break;
    case "Martes":
        console.log("Hoy es martes.");
        break;
    case "Miércoles":
        console.log("Hoy es miércoles.");
        break;
    case "Jueves":
        console.log("Hoy es jueves.");
        break;
    case "Viernes":
        console.log("Hoy es viernes.");
        break;
    case "Sábado":
    case "Domingo":
        console.log("¡Es fin de semana!");
        break;
    default:
        console.log(`El dia de la semana '${diaDeLaSemanaIncorrecto}' no es reocnocido en nuestro calendario`);
}

//Operaciones Iterativas

console.log('')
console.log('OPERACIONES ITERATIVAS:')

//Do...While

let i = 0
let max = 5

console.log('Ciclo Do...While:')

do {
    i++
    console.log(`Valor de i: ${i}`)
} while(i < max)

//While
console.log('Ciclo While:')

let j = 0
while (j < max) {
    j++
    console.log(`Valor de i: ${j}`)
}

//FOR
console.log('Ciclo FOR:')

for(let i = 0; i < max; i++) {
    console.log(`Valor de i: ${i}`)
}

let marcasDeAutos = ['Ford', 'Porche', 'Audi', 'Bmw']
console.log('Array a analizar: ', marcasDeAutos)
//For...in

console.log('Ciclo For...in')


for (const marca in marcasDeAutos) {
    console.log(`Conteo de marcas de autos: ${marca}`)
}

//For...of
console.log('Ciclo For...of')

for (const marca of marcasDeAutos) {
    console.log(`Marca de auto: ${marca}`)
}

//DIFICULTAD EXTRA:

console.log('')
console.log('EJERCICIO EXTRA:')

let nMin = 10
let nMax = 55
let conteo = []

for (nMin; nMin <= nMax; nMin++) {
    if (nMin % 2 === 0) {
        if (nMin !== 16) {
            if (nMin % 3 !== 0) {
                conteo.push(nMin)
            }
        }
    }
}
console.log(conteo)