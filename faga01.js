//#01 OPERADORES Y ESTRUCTURAS DE CONTROL

//Punto 1
//Operador de asignacion
let a = 8;
let b = 3;
// Operadores Aritméticos
//Operador de suma
let suma = a + b;
//Operador de resta
let resta = a - b;
//Operador de multiplicación
let multiplicacion = a * b;
//Operador de división
let division = a / b;
//Operador de exponenciación
let exponenciacion = a ** 3;
//Operador de resto de la división
let modulo = a % b;
//Operador de incremento
let incremento = ++a;
//Operador de decremento
let decremento = --b;

//Operadores de Asignación
num = 5;
asigSuma = 10; 
asigSuma += num;
asigSuma -= num;
asigSuma *= num;
asigSuma /= num;
asigSuma %= num;
asigSuma **= num;

//Operadores de comparación. Se utilizan para comprobar TRUE(verdadero) o FALSE(falso)

let x = 20;
let y = "20";
// Operador igual
let comp1 = x == y;
// Operador igual valor igual tipo
let comp2 = x === y;
// Operador no igual o diferente
let comp3 = x != y;
// Operador no igual valor y tipo o diferente tipo y valor
let comp4 = x !== y;
// Operador mayor que
let comp5 = x > y;
// Operador menor que
let comp6 = x < y;
// Operador mayor o igual que
let comp7 = x >= y;
// Operador menor que
let comp8 = x <= y;


//Operadores de cadena
let palabra1 = "nombre1";
let palabra2 = "nombre2";

let cadena1 = palabra1 == palabra2;
let cadena2 = palabra1 > palabra2;
let cadena3 = palabra1 >= palabra2;

let cadena4 = palabra1 + palabra2;
let cadena5 = palabra1 + " " + palabra2;
let cadena6 = palabra1 + " " + 10;


//Operadores lógicos. Se utliza para determinar la logica entre variables o valores
let c = 30;
let d = 20;

// && Relación de lógica que se deben cumplir todas las operaciones para TRUE de lo contrario FALSE
let rta1 = (c > 10) && (d < 25);
let rta2 = (c > 10) && (d < 25);

// || Relación de lógica que se deben cumplir tan solo una de las operaciones para TRUE de lo contrario FALSE
let rta3 = (c == 10) || (d < 25);
let rta4 = (c > 40) || (d == 25);

// Negacion de la operacion
let rta5 = !(c == 10)
let rta6 = !(d == 20)


//Punto 2
// Estructuras de Control
// Condicional if. Ejecuta el bloque de código si la respuesta de la condicioón es verdadera
let hora = 2;

if (hora < 12 ) {
    console.log("Buenos días");
}

if (hora >= 12 && hora < 19 ) {
    console.log("Buenas tardes");
}

if (hora >= 19 ) {
    console.log("Buenas noches");
}

/* Condicional else if. Ejecuta el bloque de código si la respuesta de la condicioón es verdadera. 
Hay varios bloques, si no se genera un bloque pasa al otro hasta que se ejecuta alguno.*/

let hora2 = 12;

if(hora2 < 12){
    console.log("Buenos días");
} else if (hora2 >= 12 && hora2 < 19 ) {
    console.log("Buenas tardes");
} else {
    console.log("Buenas noches");
}

/* Condicional switch. Ejecuta el bloque de código si la respuesta de la condicioón es verdadera. 
Hay varios bloques, si no se genera un bloque pasa al otro hasta que se ejecuta alguno.*/
let jornada = "tarde";

switch(jornada) {
    case "mañana":        
        console.log("Buenos días");
    break;
    case "tarde":    
        console.log("Buenas tardes");
    break;
    default:        
        console.log("Buenas noches");        
}


// Blucle for. Es útil para ejecutar el mismo código varias veces
let conteo = "";

for (let i = 5; i > 0; i--) {
    conteo = "conteo regresivo en" + " " + i + " "+"segundos";
    console.log();
}

// Blucle for in. Recorre las propiedades de un objeto o podría tambien de una matriz

const semana = {1 : "Lunes", 2: "Martes", 3: "Miercoles", 4: "Jueves", 5: "Viernes", 6: "Sabado", 7 : "Domingo"}

let dia = "";
for (let x in semana) {
    dia = "Día" + " "+ x + " " + semana[x];
    console.log(dia);
}

const numeros = [77, 53, 62, 9, 1, 20, 40];

let enteros = "";
for (let x in numeros) {
    enteros = numeros[x]
    console.log(enteros);
}


// Blucle for of. Recorre las valores de un iterable como arrays o matrices, strings, maps, etc..

const motos = ["Yamaha", "Suzuki", "Honda", "Kawasaki", "Bmw"];

let moto = "";
for (let x of motos) {
    moto = x;
    console.log(moto);
}


// Bucle While. Ejecutan un bloque de código siempre que una condición especificada sea verdadera

let increment= "";
let i = 1;

while (i <= 5) {
    increment = "Número incrementando en" + " " + i;
    console.log(increment);
    i++;
}

console.log("\n");


/* Bucle do While. Ejecutará el bloque de código una vez, antes de verificar si la condición es verdadera,
 luego repetirá el bucle mientras la condición sea verdadera. Se ejecuta el código al menos 1 vez*/
let decrement = "";
let j = 5;

do {    
     
    decrement = "Número decrementa en" + " " + j; 
    console.log(decrement);
    j--;
       
} 
while (j >= 1);

// for each. El método forEach llama a una función para cada elemento de un arrary o arreglo.

let frutero = "";

const frutas = ["pera", "manzana", "banano", "uva"];

//frutas.forEach((myFunction) => console.log(myFunction));

frutas.forEach(myFunction);

function myFunction(item, i) {
    frutero +=  console.log(i +  "." + item + " ");
}

//console.log(frutero);



