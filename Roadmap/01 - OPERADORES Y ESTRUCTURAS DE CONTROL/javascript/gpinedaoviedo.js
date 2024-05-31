/*-----Operadores Aritmeticos------ */
let num1, num2;
num1 = 88;
num2 = 12;

//suma
let suma = num1 + num2;
console.log(suma);

//resta
let resta = num1 - num2;
console.log(resta);

//multiplicacion
let multi = num1 * num2;
console.log(multi);

//division
let division = num1 / num2;
console.log(division);

//modulo (resto de la division)
let restoDivision = num1 % num2;
console.log(restoDivision);

//incremento
let incremento = num2++;
console.log(incremento);

//dencremento
let dencremento = num1--;
console.log(dencremento);

//exponensiacion
let expo = num1**num2;
console.log(expo);

/*------Operadores de Asignacion-------- */

//asignacion (=)
let num3 = num2;
console.log(num3);

//asignacion de suma (+=)
console.log(num1+=num3);

//asignacion de resta (-=)
console.log(num1-=10);

//asignacion de multiplicacion (*=)
console.log(num1*=num3);

//asignacion de division (/=)
console.log(num1/num3);

//asignacion de modulo (%=)
console.log(num1%=num3);

//asignacion de exponenciacion (**=)
console.log(num1**=num3);

/*------operadores de comparacion----- */

let text1 = "Hello World!";
let text2 = "hello world!";
let text3 = "HELLO WORLD!";

//igualdad (==)
console.log(text1==text2);

//desigualdad (!=)
console.log(text1!=text2);

//estrictamente igual
console.log(text1===text2);

//estrictamente desigual
console.log(text1!==text2);

///////////////////////////
let num4 = 24;
let num5 = 20;

//mayor que
console.log(num4 > num5);

//mayor o igual que
console.log(num4 > num5);

//menor que
console.log(num4 < num5);

//menor o igual que
console.log(num4 <= num5);

/*----Operadores Logicos----- */

//AND
console.log(text1&&text2);

//OR
console.log(text1||text2);

//NOT
console.log(!text1 === text2);

/*-----Operadores de pertencia----- */

const persona = {
    "nombre" : "Alex",
    "edad" : 20
};

//in: prop in obj (devuelve verdadero si el objeto tiene la propiedad especificada)
console.log(persona.edad in(persona));

//instanceof: obj instanceof Tipo (devuelve verdadero si el objeto es una instancia del tipo especificado)
console.log(persona instanceof(Object));


/*---Estructuras de control---- */

//if, else if, else

num1 > num2 ? console.log(`${num1} es menor que ${num2}`) 
? num1 < num2 : console.log(`${num1} es mayor que ${num2}`)
: console.log('operacion no completada');

//switch
let dia = ['lunes',"martes","miercoles","jueves","viernes","sabado","domingo"];

switch (dia[1]) {
    case 'lunes':
        console.log(`Hoy es ${dia[0]}`);
        break;

    case 'martes' : 
    console.log(`Hoy es ${dia[1]}`);
    break;

    case 'martes' : 
    console.log(`Hoy es ${dia[2]}`);
    break;

    default:
        break;
}

//bucles: for

for (let i = 0; i < 8; i++) {
    if (i === 5) {
        continue;
    }  
    console.log("Iteracion numero de for: " + i);  
}

//bucles: while
let num = 0;
while (num < 5) {
    console.log("Iteracion numero de while:" + num);
    num++;
}

//bucles: do while
let n = 0;
do {
    console.log("Iteracion numero de do-while:" + n);
    n++;
} while (n <= 10);

//bucles: for...in

const listNumber = ["alex",2,3,4,5,6];
for (numero in listNumber) {
    console.log("iTERACION BUCLE FOR...in: " + numero);
}

//bucles: for...of

const listName = ["alex","kevin","marino","esteban","cesar"];
for (nombre of listName) {
    console.log("iTERACION BUCLE FOR...OF: " + nombre);
}

//exeptions try...catch

try {
    let op = dividir(10,0);
} catch (error) {
    console.log(`Se ha producido un error: ${error}`);
} finally {
    console.log("Se ejecuta siempre.");
}


/*Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

const operacion = () => {
    for (let i = 10; i <= 55 ; i++) {
        if (i !== 16 && i % 2 === 0 && i % 3 !== 0 ){
            console.log("Numero: " + i);
        } 
    }
}
operacion();
