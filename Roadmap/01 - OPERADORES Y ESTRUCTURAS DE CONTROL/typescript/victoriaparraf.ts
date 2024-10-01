//OPERADORES ARITMETICOS
//Suma (+): Adición de dos números o concatenación de cadenas.
let ahorro: number = 35000;
let salario: number = 15000;
let nombre: string = 'Victoria';
let apellido: string = 'Parra';

let montoTotal: number = ahorro + salario;
let mensajito: string = nombre + ' ' + apellido + ' tiene en total de dinero (ojala): ';
console.log(mensajito + montoTotal);

//Resta (-): Resta de dos números.
let restaComun: number = 2109 - 42342;
console.log(restaComun);

//Multiplicación (*): Multiplicación de dos números.
let multiplicacionComun: number = 8 * 8; 
console.log(multiplicacionComun);

//Módulo (%): Resto de la división de dos números.
let residuoDivision: number = 42 % 2;
console.log(residuoDivision);

//Incremento (++): Incrementa el valor de una variable en uno.
let numerito = 1;
numerito++; //2
console.log(numerito);

//Decremento (--): Decrementa el valor de una variable en uno.
let numerazo = 100;
numerazo--; //99
console.log(numerazo);

//OPERADORES DE ASIGNACION
//Asignación (=): Asigna un valor a una variable.
let variable = 'Es obvio que es de asignacion el = ';
console.log(variable);

//Asignación de suma (+=): Suma y asigna el resultado.
let sumandoAsignando: number = 15;
sumandoAsignando += 5; //20
console.log(sumandoAsignando);

//Asignación de resta (-=): Resta y asigna el resultado.
let restandoAsignando: number = 30;
restandoAsignando-= 10; //20
console.log(restandoAsignando);

//Asignación de multiplicación (*=): Multiplica y asigna el resultado.
let y = 5;
y*=5;
console.log(y);

//Asignación de división (/=): Divide y asigna el resultado.
let z = 12
z /= 3;
console.log(z);

//Asignación de módulo (%=): Calcula el resto y asigna el resultado.
let x = 10;
x %= 3; // 1
console.log(x);

//OPERADORES DE COMPARACION
//Igualdad (==): Compara si dos valores son iguales (sin comparar el tipo).
let esIgual = 5 == 5; // true
console.log(esIgual);

//Igualdad estricta (===): Compara si dos valores son iguales y del mismo tipo.
let esIgualEstricta = 5 === 5; // true
console.log(esIgualEstricta);

//Desigualdad (!=): Compara si dos valores no son iguales (sin comparar el tipo).
let esDiferente = 5 != 5; // false
console.log(esDiferente);

//Desigualdad estricta (!==): Compara si dos valores no son iguales o no son del mismo tipo.
let esDiferenteEstricta = 5 !== 5; // false
console.log(esDiferenteEstricta);

//Mayor que (>): Comprueba si el valor de la izquierda es mayor que el de la derecha.
let esMayor = 5 > 2; // true
console.log(esMayor);

//Menor que (<): Comprueba si el valor de la izquierda es menor que el de la derecha.
let esMenor = 5 < 2; // false
console.log(esMenor);

//Menor o igual que (<=): Comprueba si el valor de la izquierda es menor o igual que el de la derecha.
let esMenorIgual = 5 <= 5; // true
console.log(esMenorIgual);

//Mayor o igual que (>=): Comprueba si el valor de la izquierda es mayor o igual que el de la derecha.
let esMayorIgual = 5 >= 5; // true
console.log(esMayorIgual);

//OPERADORES LOGICOS
//AND (&&): Comprueba si ambos operandos son verdaderos.
let esVerdadero = true && false; // false
console.log(esVerdadero);

//OR (||): Comprueba si al menos uno de los operandos es verdadero.
let cual = true || false; // true
console.log(cual);

//NOT (!): Niega el valor booleano.
let noEsVerdadero = !true; // false
console.log(noEsVerdadero);

//OPERADORES BIT A BIT
//AND bit a bit (&): Realiza una operación AND bit a bit.
let andBitA = 5 & 1; // 1

//OR bit a bit (|): Realiza una operación OR bit a bit.
let orBitA = 5 | 1; // 5

//XOR bit a bit (^): Realiza una operación XOR bit a bit.
let xorBitA = 5 ^ 1; // 4

//NOT bit a bit (~): Invierte los bits.
let notBitA = ~5; // -6

//Desplazamiento a la izquierda (<<): Desplaza los bits a la izquierda.
let desplazamientoIzq = 5 << 1; // 10

//Desplazamiento a la derecha (>>): Desplaza los bits a la derecha.
let desplazamientoDer = 5 >> 1; // 2

//Desplazamiento a la derecha sin signo (>>>): Desplaza los bits a la derecha sin signo
let desplazamientoDerSinSigno = 5 >>> 1; // 2

//OPERADOR TERNARIO
//El operador ternario es una forma abreviada de un if-else.
let esMayorcito = (5 > 2) ? 'Sí' : 'No'; // 'Sí'
console.log(esMayorcito);

//OPERADOR DE CADENA
//Concatenación (+): Combina dos cadenas.
let saludo = 'Hola' + ' Mundo'; // 'Hola Mundo'
console.log(saludo);

//TIPOS DE ESTRUCTURAS DE CONTROL
//if, else if, else

let numero: number = 10;

if (numero > 0) {
    console.log("El número es positivo");
} else if (numero < 0) {
    console.log("El número es negativo");
} else {
    console.log("El número es cero");
}

//Switch
let dia: number = 3;
let nombreDia: string;

switch (dia) {
    case 0:
        nombreDia = "Domingo";
        break;
    case 1:
        nombreDia = "Lunes";
        break;
    case 2:
        nombreDia = "Martes";
        break;
    case 3:
        nombreDia = "Miércoles";
        break;
    case 4:
        nombreDia = "Jueves";
        break;
    case 5:
    nombreDia = "Viernes";
    break;
    case 6:
        nombreDia = "Sábado";
        break;
    default:
        nombreDia = "Día inválido";
}

console.log(nombreDia); // "Miércoles"

//Bucles
//for
for (let i: number = 0; i < 5; i++) {
    console.log(i);
}
// Salida: 0, 1, 2, 3, 4

//for...of Se utiliza para iterar sobre los valores de un objeto iterable (como un array).
let ListaNumeros: number[] = [1, 2, 3, 4, 5];

for (let numero of ListaNumeros) {
    console.log(numero);
}
// Salida: 1, 2, 3, 4, 5

//for...in Se utiliza para iterar sobre las propiedades enumerables de un objeto.
let usuario = {
    nombre: "Juan",
    edad: 30
};

for (let propiedad in usuario) {
    console.log(`${propiedad}: ${usuario[propiedad]}`);
}
  // Salida: 
  // nombre: Juan
  // edad: 30

//while
let contador: number = 0;

while (contador < 5) {
    console.log(contador);
    contador++;
}
  // Salida: 0, 1, 2, 3, 4

//do...while
let contadorDos: number = 0;

do {
    console.log(contadorDos);
    contadorDos++;
} while (contadorDos < 5);
// Salida: 0, 1, 2, 3, 4

//EXCEPCIONES
//try, catch, finally, throw Se utilizan para manejar errores y excepciones.
try {
    let resultado: number = 10 / 0;
    if (resultado === Infinity) {
        throw new Error("División por cero");
    }
} catch (error) {
    console.error(error.message);
} finally {
    console.log("El bloque finally siempre se ejecuta");
}
  // Salida: "División por cero"
  //         "El bloque finally siempre se ejecuta"
//*********************************************************************************//

console.log("Agarrese de esa silla que vamos con el reto:");
console.log("Todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3");

for(let contando: number = 10; contando <=55; contando++){
    if (contando == 16){
        continue;
    } else if (contando % 3 == 0){
        continue;
    } else if (contando % 2 == 0){
        console.log(contando);
    }
}