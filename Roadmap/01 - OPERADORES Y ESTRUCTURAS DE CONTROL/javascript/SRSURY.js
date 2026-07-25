//ejemplos tipos de operadores en javascript
// Operadores aritméticos
let sum  = 5 + 3;
let res = 5 - 3;
let mul = 5 * 3;
let div  = 5 / 3;
let mod = 5 % 3;
let exp = 5 ** 3; // Exponente (5 elevado a la potencia de 3)
//ejemplos
let suma = 10 + 5; // Suma
console.log(suma); // 15
let resta = 10 - 5; // Resta
console.log(resta); // 5
let multiplicacion = 10 * 5; // Multiplicación
console.log(multiplicacion); // 50

// Operados logicos
let and = true && false;
let or = true || false;
let not = !true;
//ejemplos 
let andLogico = true && false; // AND lógico
console.log(andLogico); // false
let orLogico = true || false; // OR lógico
console.log(orLogico); // true
let notLogico = !true; // NOT lógico
console.log(notLogico); // false

// Operadores de comparación
let igualdad = 5 == 5; // Igualdad (valor)
let igualdadEstricta = 5 === 5; // Igualdad estricta (valor y tipo)
let desigualdad = 5 != 3; // Desigualdad (valor)
let desigualdadEstricta = 5 !== "5"; // Desigualdad estricta (valor y tipo)
let mayorQue = 5 > 3; // Mayor que
let menorQue = 5 < 3; // Menor que
let mayorIgualQue = 5 >= 3; // Mayor o igual que
let menorIgualQue = 5 <= 3; // Menor o igual que
//ejemplos 
let igualdadValor = 5 == 5; // Igualdad (valor)
console.log(igualdadValor); // true
let igualdadEstrictaValor = 5 === 5; // Igualdad estricta (valor y tipo)
console.log(igualdadEstrictaValor); // true
let desigualdadValor = 5 != 3; // Desigualdad (valor)
console.log(desigualdadValor); // true



// Operadores de asignación
let asignacion = 5;
let asignacionSuma = 5; // Asignación simple
asignacionSuma += 3; // Asignación con suma
let asignacionResta = 5; // Asignación con resta
asignacionResta -= 3; // Asignación con resta
let asignacionMulti = 5; // Asignación con multiplicación
asignacionMulti *= 3; // Asignación con multiplicación
let asignacionDiv = 5; // Asignación con división
asignacionDiv /= 3; // Asignación con división
let asignacionMod = 5; // Asignación con módulo
asignacionMod %= 3; // Asignación con módulo
let asignacionExp = 5; // Asignación con exponente
asignacionExp **= 3; // Asignación con exponente
//ejemplos 
let asignacionSimple = 10; // Asignación simple
asignacionSimple += 5; // Asignación con suma
console.log(asignacionSimple); // 15
let asignacionRestaSimple = 10; // Asignación con resta
asignacionRestaSimple -= 5; // Asignación con resta
console.log(asignacionRestaSimple); // 5


// Operadores de bits
let andBit = 5 & 3; // AND bit a bit
let orBit = 5 | 3; // OR bit a bit
let xorBit = 5 ^ 3; // XOR bit a bit
let notBit = ~5; // NOT bit a bit
let desplazamientoIzq = 5 << 1; // Desplazamiento a la izquierda
let desplazamientoDer = 5 >> 1; // Desplazamiento a la derecha
let desplazamientoSinSigno = 5 >>> 1; // Desplazamiento a la derecha sin signo
//ejemplos
let andBitwise = 5 & 3; // AND bit a bit
console.log(andBitwise); // 1 (0101 & 0011 = 0001)


// Operadores de cadena
let concaten = "Hola" + " " + "Mundo"; // Concatenación de cadenas
let concatAsignacion = "Hola"; // Asignación de cadena
concatAsignacion += " Mundo"; // Concatenación con asignación
//ejemplos
let concatenacion = "Hola" + " " + "Mundo"; // Concatenación de cadenas
console.log(concatenacion); // "Hola Mundo"
let concaten2 = "Hola";
concaten2 +=  " Mouredev";
console.log(concaten2); // "Hola Mouredev"



// Operadores de tipo

let tipoNumero = typeof 5; // Tipo de dato número
let tipoCadena = typeof "Hola"; // Tipo de dato cadena
let instancia = 5 instanceof Number; // Verifica si es una instancia de Number
let instanciaCadena = "Hola" instanceof String; // Verifica si es una instancia de String
//ejemplos
let tipoDatoNumero = typeof 5; // Tipo de dato número
console.log(tipoDatoNumero); // "number"

// Operadores de incremento y decremento

let incremento = 5; // Incremento
incremento++; // Incremento en 1
let decremento = 5; // Decremento
decremento--; // Decremento en 1
let preIncremento = ++incremento; // Incremento antes de usar el valor
let preDecremento = --decremento; // Decremento antes de usar el valor
//ejemplos
let incrementoSimple = 5; // Incremento
incrementoSimple++; // Incremento en 1
console.log(incrementoSimple); // 6

// Operadores condicionales (ternarios)
let condicion = true;
let resultado = condicion ? "Es verdadero" : "Es falso"; // Operador ternario
//ejemplos
let condicionTernaria = true;
let resultadoTernario = condicionTernaria ? "Es verdadero" : "Es falso"; // Operador ternario
console.log(resultadoTernario); // "Es verdadero"


//Operadores de control
if (true) {
    console.log("Es verdadero");
} else {
    console.log("Es falso");
}
// Operadores de control de flujo
let numero = 5;
if (numero > 0) {
    console.log("El número es positivo");
}
// Operadores de control de flujo con switch
let dia = 3;
switch (dia) {
    case 1:
        console.log("Lunes");
        break;
    case 2:
        console.log("Martes");
        break;
    case 3:
        console.log("Miércoles");
        break;
    default:
        console.log("Otro día");
}
//bucle for
for (let i = 0; i < 5; i++) {
    console.log("Iteración: " + i);
}
// Bucle while
let contador = 0;
while (contador < 5) {
    console.log("Contador: " + contador);
    contador++;
}
// Bucle for...of
let arreglo = [1, 2, 3, 4, 5];
for (let numero of arreglo) {
    console.log("Número: " + numero);
}
// Bucle for...in
let objeto = { a: 1, b: 2, c: 3 };
for (let clave in objeto) {
    console.log("Clave: " + clave + ", Valor: " + objeto[clave]);
}

// Bucle do-while
let contadorDoWhile = 0;
do {
    console.log("Contador do-while: " + contadorDoWhile);
    contadorDoWhile++;
} while (contadorDoWhile < 5);

//excepciones
try {
    // Código que puede generar una excepción
    let resultado = 10 / 0; // División por cero
}
catch (error) {
    // Manejo de la excepción
    console.error("Se ha producido un error: " + error.message);
}


// Reto extra Numeros compredidos desde 10 hasta 55 pares, ni que son el 16 ni multiplos de 3
let numeros = [];
for (let i = 10; i<=55; i++){
    if(i % 2 === 0 && i !== 16 && i % 3 !== 0){
        numeros.push(i);
    }
}
console.log(numeros); // Imprime los números pares comprendidos entre 10 y 55, excluyendo el 16 y los múltiplos de 3

