/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

// operadores
let numeroUno = 10;
let  numeroDos = 25;
let suma =  `Resultado Suma: ${numeroUno + numeroDos}`;
console.log(suma); 

console.log();

let restarNumero = 25;
let restarnumeroDos = 21;
let resultadoResta = `Resultado resta: ${restarNumero - restarnumeroDos}`;
console.log(resultadoResta);

console.log();

let multiplicarNumero = 5;
let multiplcarNumeroDos = 10;
let resultadoMultiplicacion = `Resultado Multiplicacion: ${multiplicarNumero * multiplcarNumeroDos}`;
console.log(resultadoMultiplicacion);

console.log();

let dividirNumero = 5;
let dividirNumeroDos = 10;
let resultadodivicion = `Resultado Division: ${dividirNumero / dividirNumeroDos}`;
console.log(resultadodivicion);

console.log();

let moduloUno = 20;
let moduloDs = 10;
let resultadoModulo = `Resultado Modulo: ${moduloUno % moduloDs}`;
console.log(resultadoModulo);

console.log();
console.log(`Exponente 10**3: ${10**3}`)

// Operadores de comparacion
console.log();
console.log(`Igualdad: 10 es igual a 2 ${20===2}`);
console.log(`Desigualdad: 10 es distinto de 5 ${10 != 5}`);
console.log(`Mayor: 20 mayor a 10 ${20 > 10}`);
console.log(`Menor: 25 menor a 21 ${25 < 21}`);
console.log(`Mayor o igual: 25 mayor o igual a 21: ${25 >=21}`);
console.log(`Menor o igual: 25 menor o igual a 21: ${25 >= 21}`);

// Operadores logicos
console.log();
console.log(`AND &&: 10 + 10 == 20 and 5 + 5 == 10 es: ${10 + 10 == 20 && 5 + 5 == 10}`); // ambos condiciones deben ser verdadera para que sea true
console.log(`or ||: 10 + 10 || 20 and 5 + 5 == 10 es: ${10 + 10 == 22 || 5 + 5 == 11}`); // por lo menos una condicion debe ser verdadera para que sea true
console.log(`NOT !: not 10 + 10 == 20 es: ${!10 + 10 == 20}`); // negacion

// operadores de asignacion
console.log();
let number = 14; // asiganacion
console.log(`Asignacion: ${number}`);

number +=5; // suma y asignacion
console.log(`suma y asigancion: ${number}`);

number -= 2; // resta y asignacion
console.log(`Resta y asigancion: ${number}`);

number *= 5; // multiplicacion y asignacion
console.log(`Multiplicacion y asignacion: ${number}`);

number %= 6; // modulo y asignacion
console.log(`Modulo y asignacion: ${number}`);

number /= 2; //Division y asignacion
console.log(`Division y asignacion: ${number}`); 

/*
estructuras de control
*/

// condicionales 
let edad = 10;
if(edad >= 18)
    console.log("puede votar");
else{
    console.log("No puede votar");
}

var myName = "Esdras";
if(myName == "Esdras"){
    console.log(`Hola mi nombre es ${myName}`);
}
else{
    console,log(`Mi nombre no es ${myName}`);
}

// Iterativas

for(let i = 10; i<=55; i++){
    if(i % 2 == 0 && i % 3 != 0 && i !=16){
        console.log(i)
    }
}

// manejos de errores
try{
    let resultado = 10/0;
    if(!isFinite(resultado)){

        throw new Error("no se puede dividir por cero")
    }
    console.log(resultado);

} catch(error){
    console.error("Ocurrio un error " + error.message);
}




 


