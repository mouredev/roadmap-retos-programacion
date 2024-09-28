// Sitio web del lenguaje elegido : https://developer.mozilla.org/en-US/docs/Web/JavaScript 

// Comentario de 1 línea.

/* 
Comentario
multi-línea
*/

// Variables 

//var = variable global, puede actualizarse y redeclararse en cualquier lado. NO recomendada.


var saludo = "Hola, soy var"



/*let = variable no global, puede actualizarse y pero no redeclararse en cualquier lado, salvo, se lo haga en otro ámbito como por ej :

let saludar = "Hola";
    if (true) {
        let saludar = "Hola tambien";
        console.log(saludar); // "Hola tambien"
    }
    console.log(saludar); // "Hola"

Aquí si podremos modificar la variable. RECOMENDADA UTILIZAR.

*/


let saludo2 = "Hola, soy let"



//const = variable global, no puede reescribirse ni declararse nuevamente.


const saludo3 = "Hola, soy const"



let numero = 1; // Variable Number.
numero = "uno"; // Variable String.
numero = true; // Variable Boolean.
numero = false; // Variable Boolean.
numero = Symbol("unico"); // Variable Symbol (único e inmutable).
numero = 12n; // Variable BigInt.
numero = BigInt(10); // Variable BigInt ( es igual a 10n ).
numero = null; // Variable Null.
numero; // Variable Undefined.


let lenguaje = "Javascript"
console.log("!Hola, " + lenguaje + "!")