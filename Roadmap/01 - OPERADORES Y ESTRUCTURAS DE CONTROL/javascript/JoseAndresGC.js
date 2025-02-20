// Aritméticos:

let sumaA = 1;
let sumaB = 1;

console.log(sumaA + sumaB); // sumaA + sumaB = 2

let restaA = 4;
let restaB = 2;

console.log(restaA - restaB); // 4 - 2 = 2

let multiplicacionA = 5;
let multiplicacionB = 2;

console.log(multiplicacionA * multiplicacionB); // 5 * 2 = 10

let divisionA = 4;
let divisionB = 2;

console.log(divisionA / divisionB); // 4 / 2 = 2

let incremento = 0
incremento++
console.log(incremento); // 1

let decremento = 1
decremento--
console.log(decremento); // 0

// Lógicos:

let expr1 = true;
let expr2 = false;

console.log(expr1 && expr2); // AND: Si una de las dos expresiones es false se devuelve siempre false. Ambas expresiones deben ser true para devolver true

let expr_A = false;
let expr_B = false;

console.log(expr_A || expr_B); // OR: Devuelve true si al menos una de las expresiones es true, de lo contrario devuelve false

let expr_C = true;

// NOT: vuelve true al valor booleano que sea false, y vuelve false al valor que sea true. Los invierte básicamente
console.log(!expr_C); // devuelve false

// Comparación:

let comparacion1 = 100;
let comparacion2 = 10;

// mayor que
console.log(comparacion1 > comparacion2); // true
// mayor o igual que
console.log(comparacion1 >= comparacion2); // true
// menor que
console.log(comparacion1 < comparacion2); // false
// menor o igual que
console.log(comparacion1 <= comparacion2); // false
// igual
console.log(comparacion1 == comparacion2); // false
// exactamente igual
console.log(comparacion1 === comparacion2); // false
// No es igual
console.log(comparacion1 != comparacion2); // true
// Estrictamente desigual
console.log(comparacion1 !== comparacion2); // true

// ternario

let edad = 25
let acceso = edad > 17 ? 'Permitir ingreso' : 'No puede ingresar';

console.log(acceso); // 'Permitir Ingreso'

// Estructuras repetitivas:

// for:

let array = ["juan", "juanito juan", "juanito el golondrina", "amigo de los gallos", "y de las gallinas"];
let array2 = [];

for (let index = 0; index < array.length; index++) {
    console.log(array[index]);
}

for (let index = 0; index < 10; index++) {
    array2[index] = index;
    console.log(array2[index]);
}

// for in:

const objeto = {a: 1, b: 2, c: 3};


for (let propiedad in objeto) {
    console.log(`${propiedad} : ${objeto[propiedad]}`);
}

// for of:

for (let cancionLetra of array) {
    console.log(cancionLetra);
}

// while:

let cont = 0;

while (cont <= 5) {
    console.log(cont);
    cont++;
}

// do-while

let cont2 = 0;

do {
    console.log(cont2);
    cont2++;
} while (cont2 < 5);

// Condicionales:

// if:

const condicion = 10;

if (condicion > 1) {
    console.log(true);
}

// if else:

let condicion2 = 10

if (condicion2 > 100) {
    console.log(true);
} else {
    console.log(false);    
}

// switch:

let dia
let diaNum = 6
switch (diaNum) {
    case 1:
        dia = 'Lunes!';
        break;
    case 2:
        dia = 'Martes!';
        break;
    case 3:
        dia = 'Miércoles!';
        break;
    case 4:
        dia = 'Jueves!';
        break;
    case 5:
        dia = 'Viernes!';
        break;
    case 6:
        dia = 'Sábado!';
        break;
    case 7:
        dia = 'Domingo!';
        break;
    default:
        dia = "Valor indefinido"
        break;
    }
    console.log(dia);
   
// DIFICULTAD EXTRA:

for (let numero = 10; numero <= 55 ; numero++) {
    if ((numero % 2 === 0 || numero === 55) && numero !== 16 && numero % 3 !== 0) {
        console.log(numero);
    }
}