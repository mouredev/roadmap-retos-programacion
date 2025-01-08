/* Dificultad: Fácil | Publicación: 29/01/24 | Corrección: 05/02/24
Ejercicio */

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



// ASIGNACIÓN VARIABLES "POR VALOR"

/* 
Esto aplica con tipos de datos primitivos: String, Number, Null, Boolean, Undefined (Revisar: BigInt y Symbol)

Este tipo de asignación basicamente cuando se crea una variable "a" y se le asigna valor x, depués se crea una 
variable "b" y se le asigna la variable "a", practicamente se está haciendo una copia de la variable "a", 
para asignarsela a "b".

La variable "a" está en un espacio de memoria y la variable "b" está en otro espacio de memoria, por ello es que aunque 
después se cambie el valor de la variable "a" por z, el valor que está en la variable "b" seguirá siendo el mismo que ya 
tenia asignado una copia (x). 
*/

//POR VALOR
let var1 = "México";
let var2 = "España";
console.log(var1); // México
console.log(var2); // España

let var3 = var1; //var3 ahora se le asignó una "copia" del valor de la var1 entonces var3 = "México"

console.log(var3 == var1)
/* Resultado true, porque a pesar de que están en distintos espacios de memoria, tienen el mismo valor con el mismo 
tipo de dato. Ya que los datos primitivos se asignan "por valor".
*/
var3 = "Francia"; //var3 ahora se le asignó un nuevo valor, ahora var3 = "Francia"
console.log(var3);
console.log(var1); //var1 sigue valiendo "México".



//ASIGNACIÓN DE VARIABLES "POR REFERENCIA"

/* 
Esto aplica con tipos de datos compuestos: Object (Objects, Functions, Arrays, Set, Etc...)

Basicamente cuando se crea un arreglo o un objeto con ciertos valores como nombre: Daniel y edad: 27 y se asigna a 
una variable.

Por ejemplo obj1, como tal obj1 no tiene asignados lo valores nombre y edad, lo que tienen asignado literalmente es la
dirección en memoria donde se encuentran esos datos.
Ahora si se crea otra variable como obj2, a la cual se le asigna la variable obj1 (let obj2 = obj1), entonces en este caso 
no se hace una copia de los valores dentro del objeto, se hace una copia de la dirección en memoria donde se encuentran
los valores. Así que en dado caso en el que se cambie algun valor del objeto obj1, este tambien se verá reflejado en obj2.

Esto es porque no se copia directamente el valor sino la dirección en memoria donde se encuentran los valores.
*/

//EJEMPLO
let arr = ["Daniel", "Gustavo", "Jannet"];
let arr2 = arr;

arr2.push("Daneri");

console.log(arr);
console.log(arr2);

let arr3 = arr2;
arr3.push("Zulema")

console.log("arr3");
console.log(arr3);

console.log("arr");
console.log(arr);

console.log("arr2");
console.log(arr2);

//EJEMPLO
let obj1 = {
    nombre: "Daniel",
    edad: 27
}
console.log(obj1);

let obj3 = obj1;
console.log(obj3);

obj3.nombre = "Alejandra";
console.log(obj3);
console.log(obj1);
console.log(obj1 == obj3);
//Resultado true, porque las dos variables apuntan a la misma dirección en memoria (espacio en memoria).


let obj2 = {
    nombre: "Daniel",
    edad: 27
}
console.log(obj2 == obj1);
/* Resultado false, porque a pesar de tener los mismos valores, estos están en distintas direcciones en memoria 
(espacios de memoria).

Los objetos compuestos se asignan "por referencia", unicamente son iguales cuando se encuentran en el mismo 
espacio de memoria ya que comparten los mismo valores
*/




//FUNCIONES CON ASIGNACIÓN POR VALOR Y POR REFERENCIA.

//FUNCION POR VALOR

/* 
Cuando pasamos valores primitivos a una función, ésta copia los valores en sus parámetros. 
Es efectivamente lo mismo que usar =

Todas las operaciones que se realizan dentro de la función con las copias de los valores de esas variables
no afecta en nada los valores que se encuentran fuera de la función.
*/

let num1 = 50, num2 = 34;

function sumar(x, y) {
    console.log("Suma de los parametros antes de cambiar su valor dentro de la función " + (x + y)); //84
    x = 20;
    y = 30;
    return x + y;
}
console.log(`Suma de los parametros dentro de la función ${sumar(num1, num2)}`); //50
console.log(`Suma de variable fuera de la función ${num1 + num2}`); //84

/* Como se ve en el ejemplo, la variables fuera de la función no se ven afectadas ya que x & y hacen una copia de los valores
que tienen num1 y num2. */



// FUNCION REFERENCIA

/* 
Cuando pasamos valores compuestos a una función, de la misma forma solo se hace una copia de la dirección en memoria de
donde se encuentran los valores reales.

Todas las operaciones que se realizan dentro de la función con las variables o parametros que contengan 
las copias de la dirección de referencia, se veran afectadas dentro y fuera de la función. 

Esto se puede evitar realizando cierta operación para evitar que los objetos modificados dentro de la función
no afecten a los objetos fuera de esta. Y esto se logra haciendo una copia legitima del objeto en cuestion.
*/

//FUNCION REFERENCIA NORMAL
let array = ["Daniel", "Gustavo", "Jannet"];
function reff() {
    let array2 = array;
    array2.push("Rosalí");
    return array2;
}
console.log(reff()); //[ 'Daniel', 'Gustavo', 'Jannet', 'Rosalí' ]
console.log(array); //[ 'Daniel', 'Gustavo', 'Jannet', 'Rosalí' ]


//Ejemplo por referencia
function cambiaLaEdadYLaReferencia(persona) {
    persona.edad = 25;
    persona = {
        nombre: 'John',
        edad: 50
    };
    return persona;
}
let persona1 = {
    nombre: 'Claudia',
    edad: 31
};
let persona2 = cambiaLaEdadYLaReferencia(persona1);
console.log(persona1); // -> ?  
console.log(persona2); // -> ?


//Ejemplo copia de objeto:
let arreglo = ["HTML", "CSS", "JAVASCRIPT"];
function lenguaje(dev) {
    //Convertimos el objeto en cadena y despues en objeto nuevamente para hacer una copia del objeto completo
    let nuevaPersona = JSON.parse(JSON.stringify(dev));
    nuevaPersona.push("PHP");
    console.log(nuevaPersona);
    //De esta forma cuando se modifica el nuevo objeto dentro de la función, no afecta al objeto fuera de la misma
}
lenguaje(arreglo); //[ 'HTML', 'CSS', 'JAVASCRIPT', 'PHP' ]
console.log(arreglo);//[ 'HTML', 'CSS', 'JAVASCRIPT'

/* 
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   
 * 
 * Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

let nombre = "Daniel";
let apellido = "Martínez";

function progValor(nombre, apellido) {
    let extra = nombre
    nombre = apellido
    apellido = extra
    return nombre + " " + apellido;
}
console.log(progValor(nombre, apellido));
console.log(nombre, apellido);

/* 
NOTA: El concepto de paso por referencia en JavaScript es consistente tanto dentro como fuera de las funciones. 
Siempre se manejan referencias a objetos, no copias de los objetos en sí. Las asignaciones dentro de una 
función solo afectan a las variables locales a menos que se modifiquen directamente los objetos referenciados 
(como agregar elementos a un array, por ejemplo).
*/


let listaNombre = ["Jim", "Pam", "Dwigth"];
let listName = ["Manuel", "Fidencio", "Jose"];

function progReferencia(listaNombre, listaName) {
    let extra = listaNombre;
    listaNombre = listName;
    listaName = extra;
    return [listaNombre, listaName];
}
console.log(progReferencia(listaNombre, listName));
console.log(listaNombre, listName);























