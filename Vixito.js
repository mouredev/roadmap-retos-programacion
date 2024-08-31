console.log("OPERADORES");


console.log("De asignación\n");

let a=2; let b=4; c=null; d=undefined; // asignación
console.log(a+=b); // asignación de adición
console.log(a-=b); // asignación de resta
console.log(a&b); // asignación AND bit a bit
console.log(a||b); // asignación OR lógico
console.log(a??=b); // asignación de anulación lógica
console.log(c, d);

console.log("\nDe comparación\n");

console.log("Igualdad: " + (a == b));
console.log("Igualdad estricta: " + (a === b));
console.log("Diferente: " + (a != b));
console.log("Mayor o igual que: " + (a >= b));
console.log("Mayor que: " + (a > b));
console.log("Menor o igual que: " + (a <= b));
console.log("Menor que: " + (a < b));

console.log("\nAritméticos\n");

const suma = a + b;
const resta = a - b;
const multiplicacion = a * b;
const division = a / b;
const potenciacion = a ** b;
const residuo = a % b;
console.log("Suma: "+suma+"\nResta: "+resta+"\nMulitplicación "+multiplicacion+"\nDivisión: "+division+"\nPotenciación: "+potenciacion+"\nResiduo: "+residuo);

console.log("\nBit a bit\n");

console.log("AND a nivel de bits: "+(a & b));
console.log("OR a nivel de bits: "+(a | b));
console.log("XOR a nivel de bits: "+(a ^ b));
console.log("NOT a nivel de bits: "+(~ a));
console.log("Desplazamiento a la izquierda: "+(a << b));
console.log("Desplazamiento a la derecha de propagación de signo: "+(a >> b));
console.log("Desplazamiento a la derecha de relleno 0: "+(a >>> b));

console.log("\nLógicos\n");

console.log("AND Lógico: "+(b && a));
console.log("OR Lógico: "+(b || a));
console.log("NOT Lógico: "+(!b));

console.log("\nDe cadena\n");

let cadena = "Ejemplo de " + "cadena"; 
console.log(cadena);
cadena += " combinada";
console.log(cadena);

console.log("\nCondicional (ternario)\n");

(a != b) ? console.log(a) : console.log(b);

console.log("\nComa\n");

let coma = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(coma);

console.log("\nUnarios\n");

console.log(typeof a);
console.log(typeof cadena);
console.log(typeof null); // xd

console.log("\nRelacionales\n");

console.log('PI' in Math); // in

// ESTRUCTURAS DE DATOS

if (cadena != null){
    console.log("\n"+(a+b)+"\n");
} else{
    console.log("\n"+(a-b)+"\n");
}

while (b>=4 && b<=10){
    console.log(`4 x ${b} = ${4*b}`);
    b++;
    // Tabla de multiplicar del 4 multiplicado por el rango del while
}

switch (typeof a === 'number') {
    case (true):
        console.log("\na es un número\n");
        break;

    default:
        console.log("\nNo lo es\n");
        break;
}

try{
    zzz("Prueba del comando zzz");
} catch(error){
    console.log(error.message);
} finally{
    console.log("Error diligenciado.\n");
}

// EJERCICIO EXTRA
for (let index = 10; index <= 55; index++) {
    if (index % 2 === 0 && index != 16 && index % 3 !== 0) {
        console.log(index);
    }
}