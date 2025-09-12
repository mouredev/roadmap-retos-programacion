/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

console.log("asignacion por valor");
let numero1 = 66;
let numero2 = numero1;
console.log(numero1);
console.log(numero2);

console.log(" ");

console.log("asinacion por referencia");
let usuario1 = {
    nombre: "jaxi",
    edad :33,
    correo : "jaxijax86@gmail.com",
}
let usuario2 = usuario1;
console.log(usuario1);
console.log(usuario2);

console.log(" ");

console.log("funciones con variables que se les pasan por valor y por referencia");
let valor = 11;
let referencia = {
    nombre:"george",
    edad : 21,
}
console.log(valor);
console.log(referencia);

function funVariable (numero, persona) {
    numero *=2;
    console.log(numero);//aqui se imprime el valor de numero que ahora es 11 x 2 = 22
    console.log(valor);//aqui imprime valor que como ya sabemos sigue siendo 11 porque el unico que cambio de valor es numero y la variable valor se queda como estaba
    persona.nombre = "jhon";//por en cambio aqui le cambio el valor a una propiedad de referencia que tambien se llama persona y se cambia el valor de esa propiedad en persona y referencia (porque los objetos al igual que los array son datos de tipo de referencia o compuesto) como se ve a continuacion 
    console.log(persona);
    console.log(referencia);

}
funVariable(valor, referencia)

console.log(" ");

console.log("DIFICULTAD EXTRA");
let color1 = "rojo";
let color2 = "azul";
function intervalor (param1, param2) {
    param1 = color2;
    param2 = color1;
    let color3 = param1;
    let color4 = param2;
    return {color3, color4};
}
let resultado = intervalor(color1, color2);
console.log(resultado, color1, color2);//aqui se imprime las nuevas variables y las originales

let persona = {nombre: 'jaxi', edad : 25,};
let compras = ['leche', 'pollo', 'queso'];
function inter_refe (param1, param2) {
    param1 = compras;
    param2 = persona;
    let erapersona = param1;
    let eracompras = param2;
    return {erapersona, eracompras};
}
let resultado2 = inter_refe(persona, compras);
console.log(resultado2);//aqui imprimo las variables nuevas
console.log(persona, compras);//aqui imprimo las variavles originales
