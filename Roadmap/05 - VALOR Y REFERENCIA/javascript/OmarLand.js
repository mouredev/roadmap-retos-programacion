/*
    * EJERCICIO:
    * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
    *   su tipo de dato.
    * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
    *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
    * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
    *
*/

// Asignación de variables "por valor" y "por referencia", según su tipo de dato.

let numA = 10;
console.log("Variable por su valor: ", numA);
let numB = numA;
console.log("Variable por referencia: ", numB);
numB = 20;
console.log("Variable por referencia: ", numB);

let stringA = "Hola";
console.log("Variable por su valor: String", stringA);
let stringB = stringA;
console.log("Variable por su valor: String", stringB);
stringB = "Adios";
console.log("Variable por su valor: String", stringB);

/* 
  Muestra ejemplos de funciones con variables que se les pasan "por valor"   y "por referencia", y cómo se comportan en cada caso en el momento de      ser modificadas.
*/

const saludar = () =>{
  let saludo = "Hola saludo por valor!!! xD"
  return saludo;
}
console.log(">>>", saludar() )

const saludoPorReferencia = (saludo) => {
  let saludando = saludo;
  return saludando;
}

console.log(saludoPorReferencia(">>> Hola saludo por referencia!!! xD"))


/*
    * DIFICULTAD EXTRA (opcional):
    * Crea dos programas que reciban dos parámetros (cada uno) definidos como
    * variables anteriormente.
    * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
    *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
    *   se asigna a dos variables diferentes a las originales. A continuación, imprime
    *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
    *   su valor en las segundas.
    *   Comprueba también que se ha conservado el valor original en las primeras.
*/
 
// Función que intercambia dos variables por su valor:
const interChangeValues = () => {
    let valueA = "Perro"
    let valueB = "Gato"
    let temp   = "";

    console.log(`Valor original de ValueA es: ${valueA}`);
    console.log(`Valor original de ValueB es: ${valueA}`);

    temp = valueA;
    valueA = valueB;
    valueB = temp;

    console.log(`Ahora el valor de valueA es: ${valueA}`);
    console.log(`Ahora el valor de valueB es: ${valueB}`);

}

console.log( ">>> ", interChangeValues() );

// Función que intercambia dos variables por parametro:
const interChangeValuesByParam = ( valA, valB ) => {

    console.log("Valor original de valA: ", valA);
    console.log("Valor original de valB: ", valB);

    let aux = valA;
    valA = valB;
    valB = aux;

    console.log(">>> Ha cambiado el valor de valA y es: ", valA);
    console.log(">>> Ha cambiado el valor de valB y es: ", valB);

}

interChangeValues("JavasCript", "TypeScript");