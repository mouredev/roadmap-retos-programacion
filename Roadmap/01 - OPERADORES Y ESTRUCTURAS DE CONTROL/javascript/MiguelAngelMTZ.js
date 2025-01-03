// Operadores Aritmeticos - JavaScript
console.info("------(◉◉∖____/◉◉)------ Operadores Aritméticas (+, -, *, /, %, ++, --) ------(OO∖____/OO)------")
let Numero = 17 // Dividiendo
let numero = 5 // Divisor
// Suma
console.log(`Sumando: ${Numero} + ${numero}, da como resultado:`, Numero + numero)
// Resta
console.log("Restando:", Numero, "-", numero, ", da como resultado:",   Numero - numero)
// Multiplicación
console.log(`Multiplicando: ${Numero} x ${numero}, da como resultado: ` + Numero * numero)
// Division
console.log(`Dividiendo: ${Numero} / ${numero}, da como resultado:`, Numero / numero)
// Modulo
console.log(`Modulo: ${Numero} % ${numero}, da como resultado:`, Numero % numero + `. 
    Porque dividiendo ${Numero} entre ${numero} obtenemos ${Math.floor(Numero/numero)} como cociente (porque ${numero} * ${Math.floor(Numero/numero)} = ${numero * Math.floor(Numero/numero)}) y un residuo de:`, Numero % numero)
/////////////////////////////////////
console.log(`Modulo: ${24} % ${2}, da como resultado: ${24 % 2}. 
    Porque dividiendo ${24} entre ${2} obtenemos ${Math.floor(24/2)} como cociente (porque ${2} * ${Math.floor(24/2)} = ${2 * Math.floor(24/2)}) y un residuo de: ${24 % 2}`)
// Incremento ++
console.log("Incremento:", "++" + numero, "=", ++numero)
// Descremento --
console.log(`Descremento: --${Numero} =`, --Numero)
// Exponente

// Operadores de asignación - JavaScript
console.log("------(◉◉∖____/◉◉)------ Operadores de Asignación (=, +=, -=, *=, /=, **=/ %=) ------(OO∖____/OO)------")
let variableNum = 10
console.log(`Asignar valor a (variableNum =):`, variableNum)
console.log(`Suma con asignación: variableNum (${variableNum}) += 35:`, variableNum += 35)
console.log(`Resta con asignación: variableNum (${variableNum}) -= 5:`, variableNum -= 5)
console.log(`Multiplicación con asignación: variableNum (${variableNum}) *= 12:`, variableNum *= 12)
console.log(`División con asignación: variableNum (${variableNum}) /= 2:`, variableNum /= 2)
console.log(`Exponente con asignación: variableNum (${variableNum}) **= 2:`, variableNum **= 2)
console.log("---------------------------------------------------------------------")
console.log(`${variableNum} % ${42}: ${(variableNum % 42)}
    Dividiendo ${variableNum} entre ${42} obtenemos ${Math.floor(variableNum/42)} como cociente, (porque ${Math.floor(variableNum/42)} * ${42} = ${42 * Math.floor(variableNum/42)}) y un residuo de: ${variableNum % 42}.
    (${variableNum % 42}) más (${42 * Math.floor(variableNum/42)}) da como resultado: ${(variableNum % 42) + (42 * Math.floor(variableNum/42))}`)
console.log("---------------------------------------------------------------------")
console.log(`Módulo con asignación: variableNum (${variableNum}) %= 42:`, variableNum %= 42)

// Operadores de Comparación - JavaScript
console.log("------(◉◉∖____/◉◉)------ Operadores de Comparación (>, >=, <, <=, == , ===, !=, !==) ------(OO∖____/OO)------")
console.log("Operador Lógico (Mayor que), 4 > 2:", 4 > 2)
console.log("Operador Lógico (Mayor que), 4 > 8:", 4 > 8)
console.log("Operador Lógico (Mayor o igual que), 4 >= 8:", 4 >= 8)
console.log("Operador Lógico (Mayor o igual que), 4 >= 4:", 4 >= 4)
console.log("Operador Lógico (Mayor o igual que), 4 >= 3:", 4 >= 3)

console.log("---------------------------------------------------------------------")
console.log("Operador Lógico (Menor que), 4 < 50:", 4 < 50)
console.log("Operador Lógico (Menor que), 50 < 50:", 50 < 50)
console.log("Operador Lógico (Menor o igual que), 51 <= 50:", 51 <= 50)
console.log("Operador Lógico (Menor o igual que), 50 <= 50:", 50 <= 50)
console.log("Operador Lógico (Menor o igual que), 49 <= 50:", 49 <= 50)

console.log("---------------------------------------------------------------------")
let VeintiCuatro = 24
console.log("Operador Lógico (Igual a), VeintiCuatro == 24:", VeintiCuatro == 24) // Igualdad por valor
console.log("Operador Lógico (Igual a), 24 == 24:", 24 == 24) // Igualdad por valor
console.log(`Operador Lógico (Igual a), 24 == "24":`, 24 == `24`) // Igualdad por valor
console.log("Operador Lógico (Igual a), 24 == 25:", 24 == 25) // Igualdad por valor
console.log("Operador Lógico (Igual a), 24 == '25':", 24 == "25") // Igualdad por valor
console.log("Operador Lógico (Igual a), true == true:", true == true) // Igualdad por valor
console.log("Operador Lógico (Igual a), true == !true:", true == !true) // Igualdad por valor
console.log("Operador Lógico (Igual a), false == false:", false == false) // Igualdad por valor
console.log("Operador Lógico (Igual a), false == !false:", false == !false) // Igualdad por valor
console.log("Operador Lógico (Igual a), 0 == true:", 0 == true) // Igualdad por valor
console.log("Operador Lógico (Igual a), 0 == false:", 0 == false) // Igualdad por valor
console.log("Operador Lógico (Igual a), 0 == ' ':", 0 == "") // Igualdad por valor
console.log("Operador Lógico (Igual a), null == null:", null == null) // Igualdad por valor
console.log("Operador Lógico (Igual a), 0 == null:", 0 == null) // Igualdad por valor
console.log("Operador Lógico (Igual a), 0 == !null:", 0 == !null) // Igualdad por valor
console.log("Operador Lógico (Igual a), 0 == !!null:", 0 == !!null) // Igualdad por valor
console.log("Operador Lógico (Igual a), undefined == undefined:", undefined == undefined) // Igualdad por valor
console.log("Operador Lógico (Igual a), 0 == undefined:", 0 == undefined) // Igualdad por valor
console.log("Operador Lógico (Igual a), 0 == !undefined:", 0 == !undefined) // Igualdad por valor
console.log("Operador Lógico (Igual a), 0 == !!undefined:", 0 == !!undefined) // Igualdad por valor
console.log("Operador Lógico (Igual a), 0 == 'Hola':", 0 == "Hola") // Igualdad por valor
console.log("Operador Lógico (Igual a), 'HOla' == 'Hola':", "HOla" == "Hola") // Igualdad por valor
console.log("Operador Lógico (Igual a), 'Hola' == 'Hola':", "Hola" == "Hola") // Igualdad por valor
console.log("Operador Lógico (Igual a), 'Hola' == 'McLaren':", "Hola" == "McLaren") // Igualdad por valor
console.log("Operador Lógico (Igual a), object == object:", Object == Object) // Igualdad por valor

console.log("---------------------------------------------------------------------")
let cinco = 5
console.log("Operador Lógico (Estrictamente igual), cinco === 5:", cinco === 5) // Igualdad por identidad (por tipo y valor) o igualdad estricta
console.log("Operador Lógico (Estrictamente igual), 5 === 5:", 5 === 5) // Igualdad por identidad (por tipo y valor) o igualdad estricta
console.log("Operador Lógico (Estrictamente igual), '5' === 5:", "5" === 5) // Igualdad por identidad (por tipo y valor) o igualdad estricta
console.log("Operador Lógico (Estrictamente igual), 1 === 10:", 1 === 10) // Igualdad por identidad (por tipo y valor) o igualdad estricta
console.log("Operador Lógico (Estrictamente igual), -10 === 10:", -10 === 10) // Igualdad por identidad (por tipo y valor) o igualdad estricta
console.log("Operador Lógico (Estrictamente igual), 'Porsche' === 'PorschE':", "Porsche" === "PorschE") // Igualdad por identidad (por tipo y valor) o igualdad estricta
console.log("Operador Lógico (Estrictamente igual), null === null:", null === null) // Igualdad por identidad (por tipo y valor) o igualdad estricta
console.log("Operador Lógico (Estrictamente igual), ' ' === 0:", " " === 0) // Igualdad por identidad (por tipo y valor) o igualdad estricta
console.log("---------------------------------------------------------------------")
console.log("Operador Lógico (No igual a), 24 != 24:", 24 != 24) // Desigualdad por valor
console.log("Operador Lógico (No igual a), '24' != 24:", "24" != 24) // Desigualdad por valor
console.log("Operador Lógico (No igual a), '24' != '24':", "24" != "24") // Desigualdad por valor
console.log("Operador Lógico (No igual a), 25 != 24:", 25 != 24) // Desigualdad por valor
console.log("Operador Lógico (No igual a), 24 != '25':", 24 != "25") // Desigualdad por valor
console.log("Operador Lógico (No igual a), 25 != 'Volkswagen':", 25 != "Volkswagen") // Desigualdad por valor
console.log("Operador Lógico (No igual a), true != true:", true != true) // Desigualdad por valor
console.log("Operador Lógico (No igual a), true != false:", true != false) // Desigualdad por valor

console.log("---------------------------------------------------------------------")
console.log("Operador Lógico (Estrictamente no igual), 12 !== '13':", 12 !== '13') // Desigualdad por identidad (por tipo y por valor) o desigualdad estricta
console.log("Operador Lógico (Estrictamente no igual), 12 !== '12':", 12 !== '12') // Desigualdad por identidad (por tipo y por valor) o desigualdad estricta
console.log("Operador Lógico (Estrictamente no igual), 12 !== 12:", 12 !== 12) // Desigualdad por identidad (por tipo y por valor) o desigualdad estricta
console.log("Operador Lógico (Estrictamente no igual), '11' !== '11':", 11 !== 11) // Desigualdad por identidad (por tipo y por valor) o desigualdad estricta
console.log("Operador Lógico (Estrictamente no igual), 'Doce' !== 12:", "Doce" !== 12) // Desigualdad por identidad (por tipo y por valor) o desigualdad estricta
console.log("Operador Lógico (Estrictamente no igual), 'Doce' !== 'Doce':", "Doce" !== "Doce") // Desigualdad por identidad (por tipo y por valor) o desigualdad estricta

// Operadores Logicos - JavaScript
console.log("------(◉◉∖____/◉◉)------ Operadores Lógicos (&&, ||, !) ------(OO∖____/OO)------")
console.log("----------------------------------- (y && ADD) ----------------------------------")
console.log("24 > 24 && 24 > 24:", 24 > 24 && 24 > 24)
console.log("24 > 0 && 24 > 23:", 24 > 0 && 24 > 23)
console.log("23 > 24 && 24 > 23:", 23 > 24 && 24 > 23)
console.log("23 < 24 && 24 > 23:", 23 < 24 && 24 > 23)
console.log("23 < 24 && 23 > 24:", 23 < 24 && 23 > 24)
console.log("'Ford GT' != 40 && 5 !== '5':", 'Ford GT' != 40 && 5 !== '5')

console.log("----------------------------------- (o || OR) ----------------------------------")
console.log("23 >= 23 || McLaren == McLaren:", 23 >= 23 || "McLaren" == "McLaren")
console.log("23 < 100 || McLaren == McLaren:", 23 < 100 || "McLaren" == "McLaren")
console.log("Lamborghini == McLaren || 512 < 100:", "Lamborghini" == "McLaren" || 512 < 100 )
console.log("'Ford GT' != 40 || 5 !== '5':", 'Ford GT' != 40 || 5 !== '5')

console.log("----------------------------------- (no ! NOT) ----------------------------------")
console.log("!true:", !true)
console.log("!false:", !false)
console.log("!null:", !null)
console.log("null:", null)
console.log("!undefined:", !undefined)
console.log("undefined:", undefined)
console.log("!(100 < 50) && 'Nissan' == 45:", !(100 < 50) && "Nissan" == 45)
console.log("!(100 < 50) && 'Nissan' != 45:", !(100 < 50) && "Nissan" != 45)
console.log("!(100 < 50) && '45' !== '45':", !(100 < 50) && "45" !== "45")
console.log("!(100 < 50) && 45 !== '45':", !(100 < 50) && 45 !== "45")

// Operadores de bit - JavaScript
console.log("------(◉◉∖____/◉◉)------ Operadores de Bit (&, |, ^, ~, ~~, <<, >>, >>>) ------(OO∖____/OO)------")
console.log("Operador AND, 1 & 0:", 1 & 0) // Devuelve 1 si ambos operados son 1.
console.log("Operador AND, 1 & 1:", 1 & 1) // Devuelve 1 si ambos operados son 1.
console.log("Operador OR, 0 | 1:", 0 | 1) // Devuelve 1 si al menos un operador es 1.
console.log("Operador OR, 1 | 1:", 1 | 1) // Devuelve 1 si al menos un operador es 1.
console.log("Operador OR, 0 | 0:", 0 | 0) // Devuelve 1 si al menos un operador es 1.
console.log("Operador XOR (OR exclusivo), 1 ^ 1:", 1 ^ 1) // Devuelve 1 si ambos operadores son diferentes
console.log("Operador XOR (OR exclusivo), 0 ^ 1:", 0 ^ 1) // Devuelve 1 si ambos operadores son diferentes
console.log("Operador NOT (unario), ~0:", ~0) // Invierte los bits del operador. Trunca a 32 bits.
console.log("Operador NOT (unario), ~1:", ~1) // Invierte los bits del operador. Trunca a 32 bits.
console.log("Operador NOT (unario), ~9:", ~9) // Invierte los bits del operador. Trunca a 32 bits.
console.log("Operador NOT (unario), ~-9:", ~-9) // Invierte los bits del operador. Trunca a 32 bits.
console.log("Operador double NOT (unario), ~~0:", ~~0) // Trunca los decimales del numero, convirtiendolo en entero. Solo 32 bits.
console.log("Operador double NOT (unario), ~~1:", ~~1) // Trunca los decimales del numero, convirtiendolo en entero. Solo 32 bits.
console.log("Operador double NOT (unario), ~~1.52:", ~~1.52) // Trunca los decimales del numero, convirtiendolo en entero. Solo 32 bits.
console.log("Operador double NOT (unario), ~~5.68:", ~~5.68) // Trunca los decimales del numero, convirtiendolo en entero. Solo 32 bits.
console.log("Operador double NOT (unario), ~~-5.68:", ~~-5.68) // Trunca los decimales del numero, convirtiendolo en entero. Solo 32 bits.
console.log("Operador LEFT SHIFT, 9 << 2:", 9 << 2) // Desplazamiento de bits hacia la izquierda
console.log("Operador RIGHT SHIFT, 9 >> 2:", 9 >> 2) // Desplazamiento de bits hacia la derecha
console.log("Operador  RIGHT SHIFT sin signo, 19 >>> 2:", 19 >>> 2) // Desplazamiento de bits hacia la derecha, como un operador sin signo

// Condicionales - JavaScript
console.log("------(◉◉∖____/◉◉)------ Condicionales-JavaScript ------(OO∖____/OO)------")
console.log("----------------------------------- (if, else if, else) ----------------------------------")
let dividiendo = 24
let divisor = 2
if (dividiendo == 0 && divisor == 0) {
    console.log(`No se puede hacer la división, porque: ${dividiendo} / ${divisor} es 0.`)
} else if (dividiendo == 0) {
    console.log("No se puede dividir entre: " + dividiendo + "/" + divisor)
} else if (divisor == 0){
} else {
    console.log(`El resultado de la división: ${dividiendo}/${divisor} = ${dividiendo/divisor}`)
}

console.log("----------------------------------- (switch) ----------------------------------")
// Switch
const a = 12
const b = 10
let operación = "Suma"

switch (operación) {
    case "Suma":
        console.log(`Sumando ${a} + ${b}:`, a+b)
        break
    case "Resta":
        console.log(`Restando ${a} - ${b}:`, a-b)
        break
    case "Multiplicación":
        console.log(`Multiplicando ${a} x ${b}:`, a*b)
        break
    case "Modulo":
        console.log(`Modulo ${a} % ${b}:`, a%b)
        break
    case "Exponente":
        console.log(`Exponente ${a}**${b}:`, a**b)
        break
    default:
        console.log("default")
        break
}

// Iterativas - JavaScript
console.log("------(◉◉∖____/◉◉)------ Iterativas-JavaScript ------(OO∖____/OO)------")
console.log("----------------------------------- (Ciclo For) ----------------------------------")
let i
for (let i = 1; i <= 10; i++) {
    console.log("-. " + i)
}
console.log("----------------------------------- (For Of) ----------------------------------")
const animales = ["🦉", "🐧", "🦆", "🐓", "🐌", "🦔", "🐿", "🐠", "🐕‍🦺", "🐈"]
for (const value of animales) {
    console.log(value)
}
let numeros = [1, 3, 5, 7, 9]
for (let value of numeros) {
    value += 1
    console.log(value)
}

console.log("----------------------------------- (Ciclo while) ----------------------------------")
let num = 1
while (num <= 10) {
    console.log("Número: " + num)
    num ++
}

console.log("----------------------------------- (Ciclo do-while) ----------------------------------")
let contador = 1
do {
    console.log("Nº: " + contador);
    contador ++
} while (contador <= 10);

console.log("------(◉◉∖____/◉◉)------ Excepciones-JavaScript ------(OO∖____/OO)------")
console.log("----------------------------------- (Excepción try-catch, finally) ----------------------------------")
let VarUndefined
try {
    console.log(VarUndefined.Hola_Yo_No_Estoy_Definido)
} catch (error) {
    console.log("Se ha producido un error dentro del catch:", error.message)
} finally {
    console.log("Este código se ejecuta siempre")
}

console.log("------(◉◉∖____/◉◉)------ Ejercio extra - JavaScript ------(OO∖____/OO)------")
console.log(`Creando un programa que imprima por consola todos los números empezando
del 10 al 55, pares, que no imprima el 16 ni múltiplos de 3.`)
function ejercicio() {
    for (let i = 10; i <= 55; i++) {
        if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
            console.log(`N° ${i}`);
        }
    }
}
ejercicio();


