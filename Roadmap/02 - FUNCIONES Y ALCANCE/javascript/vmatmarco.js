/* FUNCIONES BASICAS EN JAVASCRIPT */

// <--- Funciones por declaración --->

function funcionPorDeclaracion () {
    console.log('Esto es una funcion por declaración');
}

funcionPorDeclaracion();


// Pueden recibir parametro dentro del paréntesis

function funcionConParametros(numero) {
    console.log(numero);
}

funcionConParametros(10); // Llamamos a la funcíon con valor 10, que se imprimira por pantalla.


// Devolución de valores

function sumarNumeros(num1, num2) {
    return num1 + num2;
}

let suma = sumarNumeros(5, 5);
console.log('El total es: ', suma);


// <--- Funciones dentro de funciones y variables LOCALES Y GLOBALES --->

const NUMERO_PI = 3.1415; // Variable global. Puede ser accesible desde cualquier parte del codigo
                          // Tanto dentro como fuera de las funciones.  

function calcularAreaCiruculo(r) {
    function radioAlCuadrado(rPor2){
      return rPor2 **= 2;
    }
    let cuadrado = radioAlCuadrado(r); // 'cuadrado' es una variable local. Solo es accesible dentro de esta función.
    return cuadrado * NUMERO_PI;
  }
  
  const areaCirculo = calcularAreaCiruculo(5);
  console.log(areaCirculo);


// <--- Funciones creadas por el lenguaje --->

// La funcion 'length()' devuelve la longitud de un string

let longitudPalabra = "JavaScript";
console.log("JavaScript tiene " + longitudPalabra.length + " carácteres.");


/* DIFICULTAD EXTRA */

function imprimeMultiplos (texto1, texto2) {
    let contador = 0;
    for(let i = 1; i <= 100; i++){
        if(i%3 === 0 && i%5 === 0){
            console.log(texto1+texto2);
        } else if (i%3 === 0) {
            console.log(texto1);
        } else if (i%5 === 0){
            console.log(texto2);
        } else {
            console.log(i);
            contador ++;
        }
    }
    return contador;
}

const TOTAL = imprimeMultiplos('Hola', 'Mundo');
console.log("Entre 1 y 100 hay " + TOTAL + " numeros que no son multiplos de 3 ni de 5");

