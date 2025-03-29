/* Los operadores son herramientas lógicas y matematicas que nos ayudan
 * a trabajar con los datos del sistema, haciendo asignaciones, comparaciones
 * y como su nombre mismo lo indica, operando estos datos de diferentes maneras
 * */ 

console.log("------------------------------------")

console.log("Operadores matematicos\n");
console.log(1 + 2); // -> Suma
console.log(3 - 2); // -> resta
console.log(1 * 2); // -> multiplicacion
console.log(1 / 2); // -> divicion
console.log(1 % 2); // -> Resto
console.log(1 ** 2); // -> Potenciacion

console.log("------------------------------------")

const numbers = [10, 20, 30, 40, 50, 60, 70, 80];

for (let i = 0; i < numbers.length; i++) {
    const mod = i % 2;
    console.log(numbers[i], numbers[mod], mod);
}

console.log("------------------------------------")

console.log("Operadores de Asignación.\n")
let _variable_1 : number;

_variable_1 = 1;
_variable_1 += 4;
_variable_1 -= 2;
_variable_1 *= 4;
_variable_1 /= 2;
_variable_1 **= 2;

console.log(_variable_1);

_variable_1 %= 7;

console.log("------------------------------------")

console.log("Operadores unarios\n");
console.log(++_variable_1); // Primero suma y despues muestra
console.log(_variable_1++); // Primero muestra y luego suma 
console.log(_variable_1--);
console.log(--_variable_1);

console.log("------------------------------------")

const P : boolean = false;
const Q : boolean = true;

console.log("Operadores lógicos")
console.log(!P);
console.log(!Q);
console.log(P && Q);
console.log(!P && Q);
console.log(P || Q);
console.log(!P || Q);

console.log("------------------------------------")

console.log("Operadores de igualdad")

const uno : number = 1;
const dos : number = 2;
const tres : number = 3;

console.log( uno == uno );
console.log( dos <= tres );
console.log( dos >= tres );
console.log( dos == tres );
console.log( uno < dos );
console.log( uno > dos );
console.log( uno != dos );

console.log("------------------------------------")

console.log("Nullish Coalescing")
console.log(_variable_1 ?? 3);

let q;

console.log(q ?? 3);
console.log(q)

console.log("------------------------------------")
console.log("------------------------------------")

console.log("Estructuras de control")

console.log("------------------------------------")

if ("puto el que lo lea".length > 0 )
    console.log("Ya lo leiste jssjjs");
else 
    console.log("Igual eres tremenda p***");

console.log("------------------------------------")

for(let i = 1; i < 5; i++)
    console.log(i)

console.log("------------------------------------")

do {
    console.log("Primero beso y despues pregunto");
} while (false);

console.log("------------------------------------")

while(true) {
    console.log("Primero pregunto y despues beso");
    break;
}

console.log("------------------------------------")
console.log("------------------------------------")

for(let i = 10; i <= 55; i++)
    if(i != 16 && !(i % 3 == 0) )
        console.log(i)

