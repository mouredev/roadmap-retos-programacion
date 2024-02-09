/* 01 - OPERADORES Y ESTRUCTURAS DE CONTROL
Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación asignación, identidad, pertenencia, bits...(Ten en cuenta que cada lenguaje puede poseer unos diferentes).
Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones...
Debes hacer print por consola del resultado de todos los ejemplos.
 
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

//------------> OPERADORES ARITMETICOS 

let suma = 5 + 5;               // SUMA
let resta = 3 - 1;              // RESTA
let multiplicación = 2 * 2;     // MULTIPLICACION
let division = 2 / 2;           // DIVISION
let resto = 7 % 2;              // RESTO
let potencia = 1 ** 5;          // POTENCIA
i++;                            // SUMA 1 AL VALOR DE i Y RETORNA i
i--;                            // RESTA 1 AL VALOR DE i Y RETORNA i
++i;                            // SUMA 1 AL VALOR DE i RETORNA EL RESULTADO DE LA OPERACION POSTERIOR
--i;                            // RESTA 1 A AL VALOR DE i Y RETORNA EL RESULTADO DE LA OPERACION POSTERIOR


//------------> OPERADORES LOGICOS
let valorFalse = false;
let valorTrue = true;

//---> AND 
// DEBE CUMPLIR AMBAS CONDICIONES
let andA = valorTrue && valorTrue;      // DEVUELVE TRUE
let andB = valorTrue && valorFalse;     // DEVUELVE FALSE
let andC = valorFalse && valorTrue;     // DEVUELVE FALSE
let andD = valorFalse && valorFalse;    // DEVUELVE FALSE

//---> OR 
// DEBE CUMPLIR AL MENOS UNA DE LAS CONDICIONES 
let orA valorTrue || valorTrue;         // DEVUELVE TRUE
let orB valorTrue || valorFalse;        // DEVUELVE TRUE
let orC valorFalse || valorTrue;        // DEVUELVE TRUE
let orD valorFalse || valorFalse;       // DEVUELVE FALSE

//---> !(NOT)
// INVIERTE EL VALOR
let notA = !valorTrue;                  // DEVUELVE FALSE
let notB = !valorFalse;                 // DEVUELVE TRUE


//------------> OPERADORES DE COMPARACION E IDENTIDAD
let A = 1
let B = 2

let comparacionA = A == B;      // ES "false", DEVUELVE "true" SI LOS VALORES SON IGUALES
let comparacionB = A != B;      // ES "true",  DUEVELVE "true" SI LOS VALORES SON DIFERENTES
let comparacionC = A === B;     // ES "false", DEVUELVE "true" SI LOS VALORES SON IGUALES Y DEL MISMO TIPO
let comparacionD = A !== B;     // ES "true",  DEVUELVE "true" SI LOS VALORES SON DIFERENTES Y DEL MISMO TIPO
let comparacionE = A > B;       // ES "false", DEVUELTE "true" SI EL VALOR DE A ES MAYOR QUE EL DE B
let comparacionF = A >= B;      // ES "false", DEVUELVE "true" SI EL VALOR DE A ES MAYOR O IGUAL QUE EL DE B
let comparacionG = A < B;       // ES "true",  DEVUELVE "true" SI EL VALOR DE A ES MENOR QUE EL DE B
let comparacionH = A <= B;      // ES "true",  DEVUELVE "true" SI EL VALOR DE A ES MENOR O IGUAL QUE EL DE B


//------------> OPERADORES DE ASIGNACION
let x = 2;
let y = 6;

let asignaciónA = x += y;     // ES IGUAL A X = X + Y
let asignacionB = x -= y;     // ES IGUAL A X = X - Y
let asignacionC = x *= y;     // ES IGUAL A X = X * Y
let asignacionD = x /= y;     // ES IGUAL A X = X / y
let asignacionE = x %= y;     // ES IGUAL A X = X % Y
let asignacionF = x **= y;    // ES IGUAL A X = X ** Y
let asignacionG = x &&= y;    // ES IGUAL A X = X && Y
let asignacionH = x ||= y;    // ES IGUAL A X = X || Y


//------------> OPERADORES DE PERTENECIA
let arr = [0,1,2];

const resA = 1 in arr;      // DEVUELVE "true" EL VALOR DE 1 ESTA EN EL ARRAY
const resB = 5 in arr;      // DEVUELVE "fasle" EL VALOR DE 5 NO ESTA EN ARRAY


//------------> OPERADORES DE TIPO DE DATO
//USANDO typeof DEVUELVE EL TIPO DE DATO QUE SE ESTA EVALUANDO
let datoA = 5;
let datoB = "hola";
let datoC = true;
let datoD = undefined;

let tipoDatoA = typeof(datoA); //DEVUELVE "number"
let tipoDatoB = typeof(datoB); //DEVUELVE "string"
let tipoDatoC = typeof(datoC); //DEVUELVE "boolean"
let tipoDatoD = typeof(datoD); //DEVUELVE "undefined"


//------------> OPERADOR CONCATENACION
let textoA = "Hola ";
let textoB = "MUNTO!";

let textoCompleto = (textoA + textoB);


//HAY VARIOS MAS, PERO ESTOS SON LOS PRINCIPALES


//--------------------> ESTRUCTURA DE CONTROL
//IF - ELSE    

let edad = 17;

if (edad < 16 ){
    console.log("La entrada solo esta permitida a mayores de 16 años");
} else if (edad >= 16 && edad < 18) {
    console.log("Puede entrar pero no consumir bebidas alcoholicas");
} else {
    console.log("Puede pasar")
}


// SWITCH

let mesDelAño = 7;

switch(mesDelAño){
    case 1:
        console.log('Enero');
        break;    

    case 2:
        console.log('Febrero');
        break;

    case 3:
        console.log('Marzo');
        break;

    case 4:
        console.log('Abril');
        break;
    
    case 5:
        console.log('Mayo');
        break;

    case 6:
        console.log('Junio');
        break;

    case 7:
        console.log('Julio');
        break;

    case 8: 
        console.log('Agosto');
        break;
    
    case 9:
        console.log('Septiembre');
        break;
    
    case 10:
        console.log('Octubre');
        break;

    case 11:
        console.log('Noviembre');
        break;
    
    case 12:
        console.log('Diciembre');
        break;
    
    default
        console.log('Debe indicar un numero entre el 1 y el 12');

}

// FOR

for(let i = 0; i < 5; i++){
    console.log(i);
}


//FOREACH 

let animales = ['perro', 'gato', 'tigre', 'elefante', 'leon', 'mono'];

animales.forEach(animal => console.log(animal));


//FOR OF

let animales = ['perro', 'gato' , 'tigre'];

for (let animal of animales){
    console.log(animal);
}


//FOR IN

let user = {
    id: 1;
    nombre: 'uno';
}

for(let valor in user){
    console.log(valor);
}


//WHILE

let i = 0;

while(i < 5){
    i++
    console.log(i);
}


//DO WHILE

let i = 0

do {
    console.log(i);
    i++;
} while (i < 5);


/*
    DIFICULTAD EXTRA:
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
*/

for (let i = 10; i <= 55, i++){
    if(i % 2 === 0 && i !== 16){
        if(i % 3 !== 0){
            console.log(i);
        }
    }
        
}























