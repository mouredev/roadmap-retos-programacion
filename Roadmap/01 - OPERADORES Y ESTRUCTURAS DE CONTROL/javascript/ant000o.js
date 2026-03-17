// Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...



// Operadores de Asignación y Aritméticos
let x = 12; // Asignación simple
x += 1; // Suma
x -= 2; // Resta
x *= 2; // Multiplicación
x /= 2; // División
x %= 2; // Residuo
x **= 3 // Exponencial
x++ // Incremento
x--; // Decremento
console.log(x);

console.log('----------------------------------------------------------------------------')

// Operadores Lógicos de Asignación
x = true;
x &&= 10; // Se asigna 10 a x solo si x es truthy.
console.log(x);
x = false;
x ||= 5; // Se asigna 5 a x solo si x es falsy.
console.log(x);
x = null;
x ??= 20; // Se asigna 20 a x solo si x es null o undefined.
console.log(x);

console.log('----------------------------------------------------------------------------')

// Operadores de Comparación
let y = (x == 8); // Igual a.
console.log(y);
y = (x === '5'); // Igual valor y tipo de dato.
console.log(y);
y = (x != 8) // Distinto de.
console.log(y);
y = x !== 8; // Distinto valor o tipo de dato
console.log(y);
y = x >= 8; // Mayor o igual a
console.log(y);
y = x <= 8; // Menor o igual a
console.log(y);


console.log('----------------------------------------------------------------------------')

//  Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones...
//  Debes hacer print por consola del resultado de todos los ejemplos.

// Estructuras de Control

// Condicionales:

// if else:
let juegos = 10;
if (juegos > 10) {
    console.log("Más de 10 juegos")
} else {
    console.log("Menos de 10 juegos")
};
// if else en ternario
juegos = 20
let cantidad = juegos > 10 ? "Más" : "Menos";
console.log(cantidad);

console.log('----------------------------------------------------------------------------')

// switch
let dia = "Sábado"
switch(dia){
    case "Viernes":
        console.log('Mañana es Sábado');
        break;
    case "Domingo":
        console.log('Ayer fue Sábado');
        break;
    default:
        console.log('Hoy es ' + dia);
}

console.log('----------------------------------------------------------------------------')

// Iterativas

// for
let i;
for (i = -2 ; i < 5 ; i++){
    console.log("El número es "+ i);
};

console.log('----------------------------------------------------------------------------')

// while
while (i < 10){
    i++;
    console.log(i);
};

console.log('----------------------------------------------------------------------------')

// do while
i = 0;
do {
    i++;
    console.log(i);
} while (i < 15);

console.log('----------------------------------------------------------------------------')

// for of
for (const letra of "hola"){
    console.log(letra);
};

console.log('----------------------------------------------------------------------------')

// for in
const user = {nombre: "ant000o", edad: 21}
for (const x in user){
    console.log(x, user[x]);
}

console.log('----------------------------------------------------------------------------')

// Excepciones

// break
for (i = 0; i < 10; i++){
    if (i === 3) {break}
    console.log(i);
}

console.log('----------------------------------------------------------------------------')

// continue
for (i = 0; i < 10; i++){
    if (i === 2) continue;
    console.log(i);
}

console.log('----------------------------------------------------------------------------')

// Errores
x = 20;
try{
    x = z + 20;
}catch(error){
    console.log("Error:", error.message);
}finally{
    console.log("Siempre se ejecuta");
}

console.log('----------------------------------------------------------------------------')
console.log('----------------------------------------------------------------------------')


//  * DIFICULTAD EXTRA (opcional):
//  * Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
//  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

for (let i = 10; i <= 55; i++){
    if (i % 2 === 0 && i != 16 && i % 3 != 0){
    console.log(i);
}}