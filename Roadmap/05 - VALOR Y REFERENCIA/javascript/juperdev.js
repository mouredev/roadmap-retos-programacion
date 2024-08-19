/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
*/

/*

- - - - - - Solución - - - - - -

*/


// por value

// Por valor es para los tipos de datos primitivos ya que estos contienen el dato en si
let a = 10;
let b = a;
// Por referencia es cuando se almacena dentro de un espacio de memoria destinado para eso.
const persona = {
    name: "Fabian",
    age: 18
};

// Por ejemplo si yo le entrego mi variable con dato primitivo a una funcion esta no sera modificada ya que se esta creando una copia para trabajar
function suma(a, b){
    // ahora a la variable 'a' le cambiare el valor dentro de la función
    a = 5;
    // pero como a y b no tienen ninguna relación entre si b no cambiara su valor que es de 10
    console.log(`el valor de a es: ${a}`);
    console.log(`el valor de b es: ${b}`);
    let resultado = a + b;
    console.log(resultado);
}

suma(a, b);
console.log(`Entonces la variable a: ${a} nunca fue modificada, como es tipo de dato primitivo esta solo crea una copia para trabajar con ella`);

// por Referencia

// Cuando por ejemplo se almacena un objeto este se guarda en un espacio en memoria y se le asigna una localizacion por referencia
// Ejemplo el objeto fabian se le asigno el espacio en memoria AFR123
// Por mas que nosotros utilicemos el nombre de la variable con la que fue creado el objeto este apuntara al espacio de memoria asignado y trabajara sobre el
// Es como si dijecemos function procesarDatos(AFR123){}
// se modificara en todos los lugares donde estemos haciendo la referencia.

const persona2 = persona;

function procesarDatos(persona){
    persona.name = 'Arnold';
}
console.log(`Objeto persona antes de ser procesado ${persona.name}`);
procesarDatos(persona);
console.log(`Objeto persona luego de ser procesado ${persona.name}`);
console.log(`Copia persona2 -> ${persona2.name}`); // También fue modificado.

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
*/

const num = 1;
const string = 'Juan';

let auto = {
    marca: 'honda'
}
let moto = {
    marca: 'suzuki'
}

function porValor(param1, param2){
    let temp = param1;
    param1 = param2;
    param2 = temp;
    
    return [param1, param2];
}

function porReferencia(param1, param2){
    let auxiliar = param1;
    param1 = param2;
    param2 = auxiliar;
    return [param1, param2]
}
console.log(`valor de num: ${num} valor de string: ${string}`);
let resultado = porValor(num, string);
console.log(`Luego de aplicar la función y invertir las variables num: ${resultado[0]} y string: ${resultado[1]}`)
console.log(`22222 valor de num: ${num} valor de string: ${string}`);

console.log(`valor antes de invertir auto: ${auto.marca} y valor de moto: ${moto.marca}`);
let refResultados = porReferencia(auto, moto);
console.log(`Luego de invertir auto: ${refResultados[0].marca} y moto: ${refResultados[1].marca}`);
console.log(`22222 valor antes de invertir auto: ${auto.marca} y valor de moto: ${moto.marca}`);