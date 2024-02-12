// OPERADORES ARITMÉTICOS:

let a = 5;
let b = 3;

console.log (a + b); //Suma
console.log (a - b); //Resta
console.log (a * b); //Multiplicación
console.log (a / b); //División
console.log (a % b); //Módulo
console.log (a ** b); //Potencia

console.log (++a); //Incremento
console.log (--a); //Decremento

//OPERADORES DE ASIGNACIÓN:
a += 2; //Igual que a = a + 2;
a -= 2;
a *= 2;
a /= 2;
a %= 2;
a **= 2;

//OPERADORES DE COMPARACIÓN:
a > 2;
a < 2;
a >= 2;
a <= 2;

a == 5; //True. Evalúa el valor
a != 5; //False
a === 5; // Evalúa valor y tipo de dato.
a !== 5; // False

//OPERADORES LÓGICOS:
let c = true;
let d = false;
let e = true;
let f = false;

    //AND &&
console.log(c && e);// Ambos son true, devuelve true.
console.log(c && d); //Devuelve false.

    //OR ||
console.log (c || d); //Devuelve true por que al menos un valor es true.
console.log (d || f); //Devuelve false porque ambos valores son false.

    //NOT !
console.log (c, !d); //Devuelve true por que c no es igual a d.


//OPERADOR TERNARIO
//expresión ? "si es true" : "si es false";
let edad = 16;
let acceso = edad > 17 ? "Permitir acceso" : "Denegar acceso";
console.log(acceso);


//ESTRUCTURAS DE CONTROL

//If
if (edad >= 16) {
    console.log("Mayor de 16");
}

//If Else
if (edad < 17) {
    console.log("Menor de 17")
} else {
    console.log("Mayor de 17")
}

//While
let i = 0;
while (i < 10) {
    console.log(i);
    i++
}

//Do While
do {
    console.log(i);
    i++;
} while(i < 3); 

//For
for (let i = 0; i < 3; i++) {
    console.log(i);
}

//For of
let nameList = ["Marea", "León", "Roberto"];
for (let name of nameList) {
    console.log(name);
}

//For in
let user = {
    name: "Marea",
    age: 9,
    color: "blue",
};

for (let prop in user) {
    console.log(user["color"]);
    
}

// Switch
let nota = 8;
switch(nota) {
    case 10:
        calificacion = "Sobresaliente";
        break;
    case 9:
    case 8:
        calificacion = "Notable";
        break;
    case 7:
    case 6:
        calificacion = "Bien";
        break;
    case 5:
        calificacion = "Suficiente";
        break;
    case 4:
    case 3:
    case 2:
    case 1:
    case 0:
        calificacion = "Suspenso";
        break;
    default:
        calificacion = "Nota errónea";
        break;
}

console.log("He sacado un " + calificacion);

//Ejercicio Extra 

for (let i = 10; i <= 55; i++) {
    if (i % 2 == 0 && i != 16 && i % 3 !== 0);
    console.log(i);
} 