// Todos los tipos de operadores de JavaScript

// Aritméticos
console.log("Suma: ", 2 + 2);
console.log("Resta: ", 3 - 1);
console.log("Multiplicación: ", 6 * 6);
console.log("División: ", 4 / 2);
console.log("Módulo: ", 6 % 3);

// De comparación
console.log("Igualdad: ", 5 == '5');
console.log("Desigualdad: ", 2 != 8);
console.log("Mayor que: ", 5 > 4);
console.log("Menor que: ", 2 < 6);
console.log("Menor o igual: ", 2 <= 4);
console.log("Mayor o igual: ", 3 >= 2);

// De asignación
let asignacion = 2
console.log("Asignación: ", asignacion);
console.log("Asignación con suma: ", asignacion += 1);
console.log("Asignación con resta: ", asignacion -=1);
console.log("Asignación con multiplicación: ", asignacion *= 2);
console.log("Asignación con división: ", asignacion /= 2);
console.log("Asignación con módulo: ", asignacion %= 2);
console.log("Asignación con exponente: ", asignacion **= 2);

// De identidad
console.log("Es idéntico: ", 5 === 5);
console.log("No es idéntico: ", 5 !== '5');

// De pertenencia
console.log("Pertenencia: ", 2 in [2,3,4,5,6]);
console.log("No pertenencia: ", !(7 in [2,3,4,5,6]));

// De bits
console.log("AND bit a bit: ", 5 & 5);
console.log("OR bit a bit: ", 4 | 4);
console.log("XOR bit a bit: ", 6 ^ 6);
console.log("NOT bit a bit: ", ~2);
console.log("Desplazamiento a la izquierda: ", 10 << 7);
console.log("Desplazamiento a la derecha: ", -7 >> 7);
console.log("Desplazamiento a la derecha sin signo: ", -9 >>> 9);

// Estructuras de control con operadores lógicos

// Condicional if else
let condicion = 1
let condicion2 = 2

if(condicion == 1 && condicion2 == 2)
{

    console.log(true);
}
else
{

    console.log(false);
}

// Condicional switch case
let animal = "Perro"
switch (animal) {
    case "Gato": 
        console.log("Es un gato");
        break;

    case "Perro": 
        console.log("Es un perro");
        break;

    default:
        console.log("No es un animal");
        break;
}

// Iterativas 
// Loop for
for(let i = 0; i<= 5; i++)
{

   console.log(i); 
}

// Iterar en un array
let array = [0,1,2,3,4,5]
for(a of array)
{

    console.log(a); 
}

// Iterar en un objeto
let objeto = {nombre: 'Juan', edad: 30, ciudad: 'Madrid'}

for(o in objeto)
{

    console.log(`${o}: ${objeto[o]}`); 
}

// Loop while
let condicion3 = 1
let condicion4 = 15

while(condicion3 < 5|| condicion4 > 10 )
{

    console.log(condicion3);
    console.log(condicion4);
    condicion3++
    condicion4--
}

// Loop do while
let condicion5 = false
let contador = 0

do{

    console.log(contador);

    if(contador >= 5)
    {

        condicion5 = true
    }

    contador++
} while(!condicion5)

// Excepciones 
try{

    let x
    x = 5 + 5
    console.log(x);
} catch(error){

    console.error("Se produjo un error: ", error);
} finally{

    console.log("Este mensaje se muestra alla error o no");
}


// DIFICULTAD EXTRA
for(let i=10; i<=55; i++)
{

    if(i%2 == 0 && i!=16 && i%3 !=0)
    {

        console.log(i);
    }
}