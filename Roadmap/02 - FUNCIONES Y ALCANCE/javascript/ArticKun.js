

//* 1. FUNCIONES Y TIPOS DE FUNCIONES -----
/*
Las funciones en JavaScript son bloques de código reutilizable que 
realizan una tarea específica. Son fundamentales en la programación en 
JavaScript y se utilizan para organizar el código, modularizar la lógica, 
y facilitar la reutilización.
*/

//⚡⚡ Declaración de Función -----
function miFuncion() {
    console.log('Declaración de funcion');
};
miFuncion(); // Llamada a la funcion


//⚡⚡ Expresión de Función / Anónima -----
const miFuncion2 = function() {
    console.log('Expresion de Funcion');
};
miFuncion2(); // Llamada a la funcion


//⚡⚡ Funciones Anónimas -----
const miFuncion3 = function() {
    console.log('Funcion anonima / expresion de la funcion');
};
miFuncion3(); // Llamada a la funcion


//⚡⚡ Funciones que se auto ejecutan -----
//Se autoejecutan al colocar: ()
( function() {
    console.log('Funcion Auto-Ejecutable');
})();


//⚡⚡ Funciones con parametros y argumentos y retorno -----
/*
Las funciones pueden recibir parametros que son enviados como argumentos al
llamar a la funcion, son los valores o datos con los que trabajaremos dentro
de la misma, y pueden tener o no el mismo nombre

recibe = parametros
al llamarla = argumentos

*/

//           parametros
function suma( a, b ) {
    return a + b;
};

//            argumentos
console.log( suma(3,3) ); // Llamada a la funcion


//⚡⚡ Funciones con Valores predeterminados -----
//             parametro con valor predeterminado
function saludar( nombre = "Artic" ) {
    console.log( `Hola, ${nombre}!` );
};
saludar(); // Llamada a la funcion


//⚡⚡ Funcion flecha o Arrow Function o lambda -----
const miFuncion4 = () => {
    console.log('Arrow function');
};
miFuncion4(); // Llamada a la funcion

/* Las funcion de flecha tiene la facultad de poder simplificarse
u omitir parentesis, llaves y tener un retorno implícito, siempre que sea una
linea de código el cuerpo de la funcion en si mismo solo usamos el simbolo =>
*/
const miFuncion5 = nombre => `Mi nombre es ${nombre}`;
miFuncion5( 'Artic' ); //Llamada a la funcion

/* Cuando tenemos dos parametros o mas, ya no debemos quitar los ()
el cuerpo si sigue siendo una única expresion si podemos omitir las llaves y
entender el return como implícito */
const sumar = (a, b) => a + b;
sumar( 5,5 ); //Llamada a la funcion


//⚡⚡ Funciones Recursivas -----
function sumaArray(array) {
// Caso base: si el array está vacío, la suma es 0
    if ( array.length === 0 ) {
      return 0;
    } else {
// Caso recursivo: la suma es el primer elemento del array más la suma del resto de los elementos
      return array[0] + sumaArray( array.slice(1) );
    }
};
  
// Ejemplo de uso
const array = [1, 2, 3, 4, 5];
const resultado = sumaArray(array);
console.log(resultado); // Salida: 15 (1 + 2 + 3 + 4 + 5)


//⚡⚡ Funciones Anidadas dentro de otras funciones -----
//Ejemplo 1 
//La función interior solo es accesible dentro del cuerpo de la función exterior.
function exterior() {

    console.log("Función exterior");

        function interior() {
            console.log("Función interior");
        }

        interior(); // Llamada a la función interna
};
  
exterior(); // Llamada a la función exterior

//Ejemplo 2
function exterior( x ) {
// Función interna (closure)
    function interior( y ) {
      return x + y;
    }
  
    return interior;
};
  
  const closureFunc = exterior( 10 );   // El valor de x se establece en 10
  const resultado2  = closureFunc( 5 ); // Llamamos a la función interna con y = 5
  
  console.log( resultado2 );            // Salida: 15
  
/*
Cuando una función se declara dentro de otra función, la función 
interna tiene acceso a las variables de la función externa, 
incluso después de que la función externa haya completado su ejecución. 

📌 Variables capturadas: Las funciones internas dentro de otras funciones 
capturan las variables de la función externa, permitiendo el acceso a 
esas variables incluso después de que la función externa haya finalizado.

📌 Preservación del entorno léxico: El entorno léxico (conjunto de variables 
disponibles en un momento dado) se mantiene vivo en el closure, lo que 
significa que las funciones internas pueden hacer referencia a variables 
de su entorno externo.

📌 Encapsulamiento: Los closures proporcionan una forma de 
encapsular variables y lógica, permitiendo la creación de
funciones más especializadas.

Los closures son una característica fundamental en JavaScript y 
se utilizan comúnmente en patrones de diseño y programación funcional 
para lograr modularidad y reutilización de código.
*/ 

//⚡⚡ Funciones como parametros de otras funciones -----
//Tambien son conocidas como CALLBACKS
/*
En JavaScript, puedes pasar funciones como parámetros a otras funciones. 
Esto es útil para lograr mayor flexibilidad y reutilización de código.
*/

/*En JavaScript, la terminología "callback" se utiliza para describir 
una función que se pasa como argumento a otra función y que se ejecutará 
después de que la función principal haya completado su ejecución.

En resumen, un callback es simplemente una función que se pasa como 
parámetro a otra función. Esta función pasada como parámetro se ejecutará 
en algún momento futuro, generalmente después de que se complete una 
operación asíncrona o se produzca un evento.
*/

//Ejemplo 1
// Función que toma dos números y una función para realizar una operación
function operacionBinaria( a, b, operacion ) {
    return operacion( a, b );
};
  
// Funciones para realizar diferentes operaciones
function adicion( x, y ) {
    return x + y;
};
  
function resta( x, y ) {
    return x - y;
};
  
// Uso de la función operacionBinaria con diferentes operaciones
console.log( operacionBinaria( 5, 3, adicion ) );  // Salida: 8
console.log( operacionBinaria( 5, 3, resta ) );    // Salida: 2

//Ejemplo2
// Función que ejecuta otra función n veces
function ejecutarNVeces( n, funcion ) {
    for (let i = 0; i < n; i++) {
      funcion();
    }
};
  
// Función de ejemplo para ser ejecutada
function saludo() {
    console.log("Hola, mundo!");
};
  
// Llamado de la función ejecutarNVeces para ejecutar la función saludar 3 veces
ejecutarNVeces( 3, saludo );
  

//Ejemplo 3 Callback
function realizarOperacion( a, b, callback ) {
    const resultado = a + b;
    callback( resultado );
};
  
function miCallback(resultado) {
    console.log( "El resultado es: " + resultado );
};
  
realizarOperacion( 3, 4, miCallback );

//Ejemplo 4 Callback Asincrono
function hacerAlgoAsincrono( callback2 ) {
    setTimeout( function() {
      console.log( "Operación asíncrona completada" );
      callback2();
    }, 2000);
};
  
function miCallback2() {
    console.log( "Callback ejecutado" );
};
  
hacerAlgoAsincrono( miCallback2 );
  

//* 2. ALGUNAS FUNCIONES PROPIAS DE JAVASCRIPT -----

/*
La mayoria de las veces cuando veamos () es simbolo de que es una funcion
o una linea de codigo que se puede ejecutar
La documentación oficial de JavaScript es una excelente fuente para 
explorar más funciones y aprender sobre sus usos
*/

//📌 1 Console.log()
console.log("Hola, mundo!");
// Imprime "Hola, mundo!" en la consola del navegador o entorno de ejecución.
//📌 2 Alert
alert("¡Esto es una alerta!");
// Muestra una alerta en el navegador con el mensaje proporcionado.
//📌 3 Confirm
const confirmacion = confirm("¿Está seguro?");
console.log(confirmacion); 
// Devuelve true si el usuario hizo clic en "Aceptar" y false si hizo clic en "Cancelar".
//📌 4 PaseInt
const numeroEnTexto = "42";
const numero = parseInt( numeroEnTexto );
console.log( numero ); // Devuelve el número entero 42.
// Convierte una cadena de texto que representa un número en un valor numérico entero.
//📌 5 Math.Round
const numeroDecimal = 5.67;
const redondeado = Math.round( numeroDecimal );
console.log( redondeado ); // Resultado: 6
// Redondea un número al entero más cercano.
//📌 6 Push()
const arr = [1, 2, 3];
array.push(4);
console.log(arr); // Resultado: [1, 2, 3, 4]
// Añade un elemento al final de un array.


//* 3. SCOPE DE JAVASCRIPT (LOCAL / GLOBAL) -----

/*
El ámbito (scope) en JavaScript se refiere a la visibilidad 
y accesibilidad de las variables en diferentes partes del código. 
Hay dos tipos principales de ámbito: local y global.
*/

// 1 Variable Local

/*
Variable Local:
Una variable declarada dentro de una función es una variable local. 
Esto significa que su alcance está limitado a la función en la que se 
declara y no es accesible fuera de esa función.
*/

function ejemploLocal() {
// Variable local
    let x = 10;
    console.log( x ); // Se puede acceder dentro de la función
};
  
ejemploLocal();    // Imprimirá 10 ya que es el llamado propio de la funcion
// console.log(x); // Esto dará un error, ya que x no es accesible fuera de la función

// 2 Variable Global

/*
Una variable declarada fuera de cualquier función o bloque de código es una variable global. 
Está disponible en todo el código, incluidas las funciones, y se puede acceder desde 
cualquier parte del código.
*/

// Variable global
let y = 20;

function ejemploGlobal() {
  console.log( y ); // Se puede acceder dentro de la función
};

ejemploGlobal();
console.log( y );  // También se puede acceder fuera de la función


//* 4. DIFICULTAD EXTRA -----
/*
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

function extra( texto1, texto2 ) {

    let contador = 0;
  
    for ( let i = 1; i <= 100; i++ ) {

        if( i % 3 === 0 && i % 5 === 0 ){
            console.log( `Soy ${texto1} y ${texto2}` );
        }else if( i % 3 === 0 ){
            console.log( `Soy ${texto1}` );
        }else if( i % 5 === 0  ){
            console.log( `Soy ${texto2}` );
        }else{
            console.log( i );
            contador ++;
        }
    }
    return `Los numeros impresos, que NO son texto, son: ${contador}`;
};
  
let reto = extra( "multiplo de 3","multiplo de 5" );
console.log( reto );