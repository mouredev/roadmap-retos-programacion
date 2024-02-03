/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 */

/**
 * ASSIGNACIÓN POR VALOR
 * Las variables primitivas de tipo: string, number, bolean, etc, se assignan por valor.
 * Esto quiere decir que el valor de la variable se guarda en un espacio de la memoria
 * del ordenador. Cada variable tiene un valor único.
 *
 * En el ejemplo siguiente vemos que la variable miFrase sigue manteniendo su valor
 * a pesar de utilizarla como parámetro en la función.
 */

let miFrase = "La canción tranquila";

function pintaFrase(frase: string) {
  frase = frase + "dentro de la función";
  console.log(frase);
}

console.log(miFrase); // La canción tranquila
pintaFrase(miFrase); // La canción tranquiladentro de la función
console.log(miFrase); // La canción tranquila

/**
 * ASSIGNACIÓN POR REFERÉNCIA
 *
 * Los objetos y funciones se assignan por referéncia. Eso quiere decir que el
 * valor de la variable sera modificada estemos fuera o dentro de una función ya que
 * ira a buscar al mismo punto de la memória donde reside el valor de la variable y
 * lo modificarà.
 *
 * En el ejemplo siguiente, vemos como el valor del atributo cambia al passar por
 * dentro de la función, así como también después.
 *
 */

let miObjeto = {
  nombre: "Guillem",
  edad: 12,
};

function cambiarObjeto(mi: any) {
  mi.nombre = "Carol";
  console.log(mi.nombre);
}

console.log(miObjeto.nombre); // Guillem
cambiarObjeto(miObjeto); // Carol
console.log(miObjeto.nombre); // Carol

/**
 *  * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

let valor1 = "Assignación por valor 1";
let valor2 = "Assignación por valor 2";

function parametrosPorValor(valor1: string, valor2: string) {
  let iniValor1 = valor1;
  valor1 = valor2;
  valor2 = iniValor1;
  return [valor1, valor2];
}

console.log(`Variable original valor1 ${valor1}`);
console.log(`Variable original valor2 ${valor2}`);
const newValores = parametrosPorValor(valor1, valor2);
console.log(`Nuevo valor 1 ${newValores[0]}`);
console.log(`Nuevo valor 2 ${newValores[1]}`);
console.log(`Variable original valor1 ${valor1}`);
console.log(`Variable original valor2 ${valor2}`);

interface Producto {
  nombre: string;
}

interface Usuario {
  nombre: string;
}

let producto: Producto = {
  nombre: "piano",
};

let usuario: Usuario = {
  nombre: "Guillem",
};

function parametrosPorReferencia(producto: Producto, usuario: Usuario) {
  const initProductoNombre = producto.nombre;
  producto.nombre = usuario.nombre;
  usuario.nombre = initProductoNombre;

  return [producto.nombre, usuario.nombre];
}

console.log(`Original producto nombre ${producto.nombre}`);
console.log(`Original usuario nombre ${usuario.nombre}`);

const nombres = parametrosPorReferencia(producto, usuario);

console.log(`Nuevo producto nombre ${nombres[0]}`);
console.log(`Nuevo usuario nombre ${nombres[1]}`);

console.log(`Original producto nombre ${producto.nombre}`);
console.log(`Original usuario nombre ${usuario.nombre}`);

/**
 * Recursos visitatdos
 *
 * https://flexiple.com/javascript/javascript-pass-by-reference-or-value
 *
 * https://es.stackoverflow.com/questions/1493/cu%C3%A1l-es-la-diferencia-entre-paso-de-variables-por-valor-y-por-referencia
 */
