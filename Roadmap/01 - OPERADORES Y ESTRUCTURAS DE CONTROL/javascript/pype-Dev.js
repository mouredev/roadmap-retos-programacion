/**
 * OPERADORES:
 * Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 * Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 */

// ARITHMETIC OPERATORS
let a = 10;
let b = 3;

console.log(`Suma: ${a} + ${b} = ${a + b}`);
console.log(`Resta: ${a} - ${b} = ${a - b}`);
console.log(`Producto: ${a} * ${b} = ${a * b}`);
console.log(`División: ${a} / ${b} = ${a / b}`);
console.log(`Módulo: ${a} % ${b} = ${a % b}`);
console.log(`Potenciación: ${a} ** ${b} = ${a ** b}`);

/* incremento y decremento */
let incremento = 10;
incremento++;
++incremento;
console.log(`Incremento: (10++) y (++10) es: ${incremento}`)

let decremento = 10;
decremento--;
--decremento;
console.log(`Decremento: (10--) y (--10) es: ${decremento}`)

// LOGICAL OPERATORS
console.log(`AND (&&): 10 + 5 == 15 and 8 - 3 == 5 es: ${10 + 5 == 15 && 8 - 3 == 5}`);
console.log(`OR (||): 10 + 5 == 16 or 8 - 3 == 5 es: ${10 +5 == 16 || 8 - 3 == 5}`);
console.log(`NOT (!): 10 + 5 == 15 es: ${!(10 + 5 == 15)}`);

/* Nullish Coalescing: Devuelve el valor derecho solo si el izquierdo es null o undefined */
let puntaje = 0;
console.log(`Nullish (??): puntaje ?? 10 es: ${puntaje ?? 10}`)

// COMPARISION OPERATORS
console.log(`Igualdad débil: 5 == '5' es: ${5 == '5'}`);
console.log(`Igualdad estricta: 5 === '5' es: ${5 === '5'}`);
console.log(`Desigualdad débil: 4 != '3' es: ${4 != '3'}`);
console.log(`Desigualdad estricta: 8 !== '7' es: ${8 !== '7'}`);
console.log(`Mayor qué: 15 > 10 es: ${15 > 10}`);
console.log(`Mayor o igual qué: 2 >= 2 es: ${2 >= 2}`);
console.log(`Menor qué: 7 < 13 es: ${7 < 13}`);
console.log(`Menor o igual qué: 4 <= 2 es: ${4 <= 2}`);

// ASSIGNMENT OPERATORS
let c = 20; //asignación
console.log(c);

c += 10; //asignación de suna
console.log(c);

c -= 10; //asignación de resta
console.log(c);

c *= 10; //asignación de multiplicación
console.log(c);

c /= 4; //asignación de división
console.log(c);

c %= 4; //asiganción de módulo
console.log(c);

c **= 4; //asignación de exponenciación
console.log(c)

c <<= 2; //asignación de desplazamiento a la izquierda
console.log(c); //(16 = 00010000) (64 = 01000000)

c >>= 2; //asignación de desplazamiento a la derecha
console.log(c); //(64 = 01000000) (16 = 00010000)

/* bitwise and, xor y or assignment */
let bit1 = 12;              //1100
bit1 &= 5;                  //0101 and
console.log(bit1);          //0100

let bit2 = 10;              //1010
bit2 ^= 6;                  //0110 xor
console.log(bit2);          //1100

let bit3 = 8;               //1000
bit3 |= 3;                  //0011 or
console.log(bit3)           //1011

// BITWISE OPERATORS
let x = 5;                  //00000000000000000000000000000101
let y = 3;                  //00000000000000000000000000000011

console.log(`Bitwise And(&): ${x} & ${y} es: ${x & y}`);        //00000000000000000000000000000001
console.log(`Bitwise Or(|): ${x} | ${y} es: ${x | y}`);         //00000000000000000000000000000111
console.log(`Bitwise Xor(^): ${x} ^ ${y} es: ${x ^ y}`);        //00000000000000000000000000000110
console.log(`Bitwise Not(~): ~${x} es: ${~x}`);                 //11111111111111111111111111111010
console.log(`Left shift(<<): ${x} << 2 es: ${x << 2}`);         //00000000000000000000000000010100
console.log(`Right shift(>>): ${x} >> 2 es: ${x >> 2}`);        //00000000000000000000000000000001

// STRING OPERATORS
let myString = "Hello";
myString += " World!";
console.log(myString)

// BIGINT OPERATORS
const myBigInt = 9007199254740991n;
typeof myBigInt;

let num = 10;
let big = 20n;
console.log(BigInt(num) + big);

//CONDITIONAL (TERNARY) OPERATOR
let age = 20;
const validacion = (age >= 18) ? "Es mayor de edad" : "Es menor de edad";

console.log(validacion);

//RELATIONAL OPERATORS
/* Operador relacional en Objetos */
const vehiculo = {
    marca : "Kawasaki",
    referencia : "Ninja",
    cilindraje : 500,
    modelo : 2026,
};

console.log("marca" in vehiculo); //true
console.log("motor" in vehiculo); //false

/* Operador relacional en Arrays */
const estudiantes = ["Juan", "Karen", "Alejandra", "Sandra", "Monica"];

console.log(3 in estudiantes); //true
console.log(5 in estudiantes); //false
console.log("Karen" in estudiantes); //false


/**
 * ESTRUCTURAS DE CONTROL:
 * Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existanen tu lenguaje:
 * Condicionales, iterativas, excepciones...
 */
//IF...ELSE
const edad = Number(prompt("Por favor ingresa tu edad:")); //Number() convierte el string en number
const clienteVIP = prompt("¿Tienes membresía de cliente VIP?:)");
const valorEntrada = 15000;

if(edad < 12){
    console.log("El precio de la entrada es de $8000 cop");
} else if(edad > 65){
    console.log("El precio de la entrada es de $10000 cop");
} else if(edad >= 12 && edad <= 65 && clienteVIP == "true"){
    const descuento = (valorEntrada * 0.2);
    console.log(`Tienes un 20% de descuento en el valor de tu entrada. El precio final es de $${valorEntrada - descuento} cop`)
} else{
    console.log("El precio de la entrada es de $15.000 cop")
}

//SWITCH
const num1 = 100;
const num2 = 25;
let operacion = "División"

switch (operacion){
    case "Suma":
        console.log(`El resultado de la suma es: ${num1 + num2}`);
        break;
    case "Resta":
        console.log(`El resultado de la resta es: ${num1 - num2}`);
        break;
    case "Multiplicación":
        console.log(`El resultado de la multiplicación es: ${num1 * num2}`);
        break;
    case "División":
        if(num2 == 0){
            console.log("Ningun número se puede dividir por 0. ERROR")
        } else{
            console.log(`El resultado de la división es: ${num1 / num2}`);
        }
        break;
    default:
        console.log("La operación ingresada no es reconocida");
}

//FOR
const tablaMultiplicar = 5;

for(let i = 1; i <= 10; i++){
    let producto = tablaMultiplicar * i;
    let paridad = (producto % 2 == 0) ? "PAR" : "IMPAR";
    console.log(`El resultado ${producto} es ${paridad}.`)
}

//FOR...OF
const precios = [100, 450, 200, 600, 80, 500];
let totalOfertas = 0;

for(const valor of precios){
    if(valor < 300){
        totalOfertas += valor;
    }
}

console.log(`El total de los productos en oferta es: $${totalOfertas}`)

//FOR...IN
const stats = {
    fuerza: 80,
    agilidad: 40,
    magia: 95,
    defensa: 60,
}

for(const habilidad in stats){
    if(stats[habilidad] >= 90){
        console.log(`¡Habilidad Maestra descubierta: ${habilidad}!`);
    } else{
        console.log(`Entrenando la habilidad: ${habilidad}`)
    }
}

//WHILE
let ahorro = 0;
const meta = 100;

while(ahorro < meta){
    ahorro += 25;
    console.log(`Ahorro actual: ${ahorro}`);

    if(ahorro == 50){
        console.log("¡Ya vas a la mitad!");
    }
}

console.log(`¡Meta alcanzada! Tienes $${ahorro} ahorrados.`);

//DO WHILE
let dado;
let intentos = 0;

do{
    dado = Math.floor(Math.random() * 6) + 1;
    intentos++;
    console.log(`Lanzamiento ${intentos}: Salio un ${dado}`)
} while(dado != 6);

console.log(`¡Por fin! Tardaste ${intentos} lanzamientos en sacar un 6`);

//TRY...CATCH
let presupuestoTotal = 1000;
let numeroProyectos = 0;

try{
    if(numeroProyectos == 0){
        throw new Error("No puedes dividir el presupuesto entre cero proyectos.");
    } else{
        let resultado = presupuestoTotal / numeroProyectos;
        console.log(`A cada proyecto le corresponden $${resultado} dólares`);
    }
} catch(e){
    console.error("Error de registro: " + e.message)
} finally{
    console.log("Proceso de cálculo finalizado.")
}

/*
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/
for(let i = 10; i <= 55; i++){
    if(i % 2 == 0 && i !== 16 && i % 3 !== 0){
        console.log(i);
    };
};
