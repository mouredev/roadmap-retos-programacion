// Aritméticos
console.log(5 + 3);     
console.log(7 - 2);      
console.log(4 * 6);    
console.log(9 % 4);      

// Lógicos
let x = true;
let y = false;

console.log(x && y);    
console.log(x || y);    
console.log(!x);         

// Comparación
console.log(5 > 3);      
console.log(3 < 5);       
console.log(5 >= 3);      
console.log(3 <= 5);      
console.log(5 == 3);      
console.log(5 != 3);     
console.log(5 === 3);     
console.log(5 !== 3);     

// Asignación
let z = 0;
z += 5;              
z -= 3;              
z *= 2;              
z /= 2;                

// Identidad
console.log(z === z);     

// Pertenencia
const array = [1, 2, 3, 4, 5];
console.log(array.includes(3)); 

// Bits
console.log(5 & 3);       
console.log(5 | 3);    
console.log(~5);          

// Condicionales
if (true) {
    console.log("Esta es una condición verdadera");
} else {
    console.log("Esta es una condición falsa");
}

switch (2) {
    case 1:
        console.log("Es 1");
        break;
    case 2:
        console.log("Es 2");
        break;
    default:
        console.log("No es 1 ni 2");
}

// Iterativas
for (let i = 0; i < 5; i++) {
    console.log(i);
}

while (true) {
    console.log("Este bucle mientras sea cierto");
    break;  // Para evitar un bucle infinito
}

do {
    console.log("Este bucle se ejecuta al menos una vez");
} while (false);

// Excepciones
try {
    throw new Error("Excepción lanzada intencionalmente");
} catch (error) {
    console.error(error.message);
}

function isEven(num) {
    return num % 2 === 0;
}

function isNotMultipleOfThree(num) {
    return num % 3 !== 0;
}

function isNotSixteen(num) {
    return num !== 16;
}

for (let i = 10; i <= 55; i++) {
    if (isEven(i) && isNotMultipleOfThree(i) && isNotSixteen(i)) {
        console.log(i);
    }
}
