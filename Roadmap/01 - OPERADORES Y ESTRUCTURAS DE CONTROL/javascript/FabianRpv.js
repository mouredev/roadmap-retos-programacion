// Tipos de operadores

// Operadores aritméticos

let a = 2;
let b = 5;

let suma = a + b; // Suma
console.log( a + " + " + b + " = " + suma);

let resta = a - b; // Resta
console.log( a + " - " + b + " = " + resta);

let multiplicacion = a * b; // Multiplicación
console.log( a + " * " + b + " = " + multiplicacion);

let division = a / b; // División
console.log( a + " / " + b + " = " + division);

let modulo = a % b; // Módulo
console.log( a + " % " + b + " = " + modulo);

let potencia = a ** b; // Potencia
console.log( a + " ** " + b + " = " + potencia);

let incremento = a; // Incremento
incremento++
console.log(a + "++ = " + incremento);

let decremento = a; // Decremento
decremento--
console.log( a + "-- = " + decremento);



// Operadores lógicos

console.log(true && true); // AND
console.log(true && false);

console.log(true || false); // OR
console.log(false || false);

console.log(!true); // NOT
console.log(!false);



// Operadores de comparacion

console.log(a == b); // es igual a
console.log(a != b); // es diferente a
console.log(a > b); // es mayor que
console.log(a >= b); // es mayor o igual que
console.log(a < b); // es menor que
console.log(a <= b); // es menor o igual que



// Operadores de asignacion

let variable = 5; // Se asigna un valor de 5 a la variable
console.log("variable = " + variable);

variable += 5; // Se suma 5 a la variable
console.log("variable más 5 = " + variable);

variable -= 5; // Se resta 5 a la variable
console.log("variable menos 5 = " + variable);

variable *= 5; // Se multiplica por 5 a la variable
console.log("variable por 5 = " + variable);

variable /= 5; // Se divide por 5 a la variable
console.log("variable entre 5 = " + variable);

variable %= 5; // Se obtiene el módulo de la variable
console.log("variable módulo 5 = " + variable);

variable **= 5; // Se obtiene la potencia de la variable
console.log("variable elevado a 5 = " + variable);



// Operadores de Identidad 

console.log(a === b); // es estrictamente igual a
console.log(a !== b); // es estrictamente diferente a



// Operadores de Pertenencia

let persona = {
    nombre: "Fabian", 
    edad: 20
};

console.log("nombre" in persona); // la propiedad existe en el objeto
console.log("apellido" in persona); // la propiedad no existe en el objeto



// Operadores de Bits

console.log(a & b); // AND
console.log(a | b); // OR
console.log(a ^ b); // XOR
console.log(~a); // NOT
console.log(a << b); // Desplazamiento a la izquierda
console.log(a >> b); // Desplazamiento a la derecha



// Operador Ternario

let edad = 20;
edad >= 18 ? console.log("Eres mayor de edad") : console.log("Eres menor de edad");



// Estructuras de control

// Condicionales (if, else, else if, switch)

let condicion = true;
let condicion2 = false;

if(condicion){

    console.log("La primera condicion se cumple");

} else if(condicion2){

    console.log("La segunda condicion se cumple");

} else {

    console.log("Ninguna condicion se cumple");

}

let dia = 3;

switch(dia){

    case 1:
        console.log("Lunes");
        break;
    case 2:
        console.log("Martes");
        break;
    case 3:
        console.log("Miercoles");
        break;

}


// Iterativas (for, while, do while, for of, for in)

for(let i = 0; i <= 5; i++){

    console.log(i);

}


let i = 5;

while(i >= 0){

    console.log(i);
    i--;

}


do {

    i++;
    console.log(i);

} while(i < 5);


let array = [1, 2, 3, 4, 5];

for (let numero of array){

    console.log(numero);

}


for(let datos in persona){

    console.log(datos + " : " + persona[datos]);

}


// Excepciones(try, catch, throw,  finally)

try {
    
    if(edad < 18){

        throw new Error("Eres menor de edad");

    }

    console.log("Eres mayor de edad");

} catch (error) {
   
    console.log(error.message);
    
} finally {

    console.log("Fin del bloque try-catch");

}


/*
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. 
*/

for(let i = 10; i <= 55; i++){

    if(i == 16){
        continue;
    }

    if(i % 2 == 0 && i % 3 != 0){

        console.log(i);

    }

}