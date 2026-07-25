
// Operadores aritméticos
console.log(1+1); // Suma
console.log(2-1); // Resta
console.log(2*2); //Multiplicación
console.log(4/2); // División
console.log(4%2); // Módulo
console.log(4**2); // Potencia

// Operadores de asignación
let a = 10;
a += 2;  // es igual a a = a + 2
console.log(a);  // 12

let b = 10;
b -= 2;  // es igual a b = b - 2
console.log(b);  // 8

let c = 10;
c *= 2;  // es igual a c = c * 2
console.log(c);  // 20

let d = 10;
d /= 2;  // es igual a d = d / 2
console.log(d);  // 5


// Operadores de comparación
console.log(1 == 1); // Igualdad
console.log(1 === 1); // Identidad
console.log(1 != 1); // Diferente
console.log(1 !== 1); // No identico
console.log(1 > 1); // Mayor que
console.log(1 < 1); // Menor que
console.log(1 >= 1); // Mayor o igual que
console.log(1 <= 1); // Menor o igual que

// Operadores lógicos
console.log(true && true); // AND
console.log(true || false); // OR
console.log(!true); // NOT

// Operadores de bits
let a = 5; // en binario 0101
let b = 3; // en binario 0011

console.log(a & b);   // 1, en binario 0001
console.log(a | b);   // 7, en binario 0111
console.log(a ^ b);   // 6, en binario 0110
console.log(~a);      // -6, es el complemento a dos
console.log(a << 1);  // 10, se desplaza a la izquierda 1 bit
console.log(a >> 1);  // 2, se desplaza a la derecha 1 bit

// Operador ternario
let a = 10;
let b = 2;

let mayor = (a > b) ? a : b;
console.log(mayor);  // 10

// Operador typeof
let a = 10;

console.log(typeof a);  // "number"

// Operador instanceof
class MiClase {
}

let obj = new MiClase();

console.log(obj instanceof MiClase);  // true



//Operadores acceso de popiedades
let obj = {
    propiedad: 'valor'
  };
  
  console.log(obj.propiedad);  // 'valor'
  console.log(obj['propiedad']);  // 'valor'
  
// Operador de nueva instancia
class MiClase {
}

let obj = new MiClase();

//Operador llamada de función
function miFuncion() {
    console.log('¡Hola Mundo!');
  }
  
  miFuncion();  // '¡Hola Mundo!'
  



// Estructuras de control
let c = 1;
if (c == 1) {
    console.log('Es uno');
} else {
    console.log('No es uno');
}

let d = 2;
switch (d) {
    case 1:
        console.log('Es uno');
        break;
    case 2:
        console.log('Es dos');
        break;
    default:
        console.log('No es uno ni dos');
}

let e = 3;
while (e > 0) {
    console.log(e);
    e--;
}

let f = 3;
do {
    console.log(f);
    f--;
} while (f > 0);

for (let g = 0; g < 3; g++) {
    console.log(g);
}

// Excepciones
try {
    throw new Error('Error');
}
catch (error) {
    console.log(error);
}

// Funciones
function h() {
    console.log('Hola');
}

h();

function i(j: string) {
    console.log(j);
}

i('Hola');

function k(l: number, m: number) {
    return l + m;
}


//Extra
for (let i = 10; i <= 55; i++) {
     
    if (i == 16) {
        continue;
    }
    let div = i % 3;
    if (div == 0) {
        continue;
    }
    let par = i % 2;
        if (par == 0) {
            console.log(i);
    }
    
}
