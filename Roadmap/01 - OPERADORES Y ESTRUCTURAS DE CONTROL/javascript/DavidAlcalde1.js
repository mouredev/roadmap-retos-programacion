//Ejemplo de operadores aritméticos
let a = 10;
let b = 4;
console.log(a + b);
console.log(a / b);
console.log(a - b);
console.log(a * b);
console.log(a % b);

//Comparaciones lógicas
console.log(a < b);
console.log(a > b);
console.log(a <= b);
console.log(a >= b);
console.log(a === b);
console.log(a !== b);

//Operadores Lógicos
console.log(true && false);
console.log(true || false);
console.log(!true);

//Operadores de bits
console.log(a & b);
console.log(a | b);
console.log(a ^ b);



// --- Estructuras de control ---

//Condicional 

if (a < b) {
    console.log(`${a} es menor que ${b}`);
}else {
    console.log(`${a} es mayor que ${b}`);
}


for (let i = 0; i < a; i++){
    console.log("Este es un for");
}

while (a > b) {
    console.log("Hola");
    a--;
}

switch (a) {
    case 1: 
        console.log("a es 1");
        break;
    case 2:
        console.log("a es 2");
        break;
    default:
        console.log("a no es ni 1 ni 2");
}


//DIFICULTAD EXTRA:

for (let i =10; i <= 55 ; i++) {
    if (i % 2 === 0) {
        if (i % 3 !== 0 && i !== 16) {
            console.log(i);
        }
    }
}
