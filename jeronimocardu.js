let a = 2;
let b = 3;

// OPERADORES ARITMETICOS
let suma = a + b;           // Suma
let resta = a - b;          // Resta
let multiplicacion = a * b; // Multiplicacion
let division = a / b;       // Division
let exponente = a ** b;     // Potenciacion
let residuo = b % a;        // Resiudo
// ejemplo
if((a+b) > 0){
    console.log('La suma da un numero natural')
}

// OPERADORES LOGICOS

a === b                     // Igualdad estricta
a == b                      // Igualdad pero no incluye el tipo de dato
a !== b                     // Desigualdad estricta
a != b                      // Desiguldad
a > b                       // Mayor que..
a >= b                      // Mayor o igual que..
a < b                       // Menor que..
a <= b                      // Menor o igual que..
a && b                      // AND
a || b                      // OR
!a                          // Negacion
if(a === b){
    console.log('Son iguales');
} else if(a > b){
    console.log('A mayor que B');
} else{
    console.log('B mayor que A');
}


// OPERADORES DE ASIGNACION

let variable = 'Hola mundo';
const texto = variable;
a += 1;                     // Asignacion y suma
a -= 1;                     // Asignacion y resta
for(let i=0; i<5; i++){
    console.log(variable[i]);
}

// OPERADORES DE IDENTIDAD

const objeto1 = {nombre: 'Jeronimo'};
if('nombre' in objeto1){
    console.log('LA PERSONA TIENE NOMBRE Y ES', objeto1.nombre)
}

// OPERADORES DE PERTENENCIA

const persona = {
    nombre: 'Jeronimo',
    edad: 19,
}
if(persona.edad > 17){
    console.log(persona.nombre, 'es mayor de edad')
}

// EXTRA
for(let i=10; i<55; i++){
    if(i%2 === 0 && i !== 16 && i%3 !== 0){
        console.log(i)
    }
}