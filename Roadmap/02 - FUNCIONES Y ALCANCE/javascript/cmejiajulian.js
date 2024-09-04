//*#02 FUNCIONES Y ALCANCE

/*
EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 */

// Funciones definidas por el usuario 

function greet (){
    console.log('Hola JavaScript');
}

greet();

// Con Retorno 

function returnGreet(){
    return 'Hola JavaScript';
}

console.log(returnGreet())

//Con Argumento 

function argGreet(greet, name){
    console.log( greet+' '+ name );
}

argGreet('Hi','Julius Batista para ti ');

//Con argumentos predeterminado

function defaultArgGreet(greet, name = 'Julini'){
    console.log( greet+' '+ name );
}

defaultArgGreet('Hi');

//Con Argumento de posición 

//en este caso en JavaScript es necesario ponerlo como objetos para que independientemente del orden pueda funcionar.

function argGreetPosition({saludo, nombre}){
    console.log( saludo+' '+ nombre );
}

argGreetPosition({nombre:'Julius Batista para ti', saludo :'hola'});

//Con Argumentos y retorno 

function returnArgsGreet (greet,name){
    return [greet,name];
}

console.log(returnArgsGreet('hola','julian'))

//Con retorno de varios Valores

function multipleReturnGreet() {
    return ['Hola', 'Mundo'];
}

const [saludo, nombre] = multipleReturnGreet();

console.log(multipleReturnGreet()); // Mostrar la referencia de la función


 // Con un numero variable de argumentos 

 function variableArgGreet(...nombres){
  for (let nombre of nombres){
    console.log('hola',nombre)
  }
 }

 variableArgGreet('julian','Phelps','Ilia')

 // con un numero variable de argumentos con palabra clave 


 function variableKeyArgGreet(nombres){
    for(let [param,key] of Object.entries (nombres))
        {console.log(`${param}:${key}`)};
 }

 /*
*   En este ejemplo:

*   La función variableArgGreet acepta un objeto nombres.
*   Object.entries(nombres) convierte el objeto en un array de pares clave-valor.
*   Usamos un bucle for...of para iterar sobre los pares clave-valor y colocar los parametros a cada uno.
  */

 variableKeyArgGreet({nombre:'Julian', edad:'205', profesion:'programador'});


// Forma de expresar las funciones 

//Funcion expresada 

let sum = function (a,b){
    return (a+b);
}

console.log(sum(3,5));

//Funcion de flecha 

let rest = (x,y) => {
    return (x-y)
}
console.log(rest(3,5));

//* tambien se podria expresar asi 

let div = (x,y) => x/y 

console.log(div(4,2));

/*
* Comprueba si puedes crear funciones dentro de funciones.
 */

let funcionExterna = ( a,b ) =>{
    
    let funcionInterna = (x) => x*x;

         return  funcionInterna(a) + funcionInterna(b);

}
console.log(funcionExterna(2,8));


 /*en este caso la funcion interna hace el siguiente trabajo

  1) al dar un valor de 2 a (a) y de 8 a (b) y al decir que la funcion interna es x*x
  entonces diriamos que (2*2) = 4  y (8*8) = 64 

  2) como estos valores se suman diriamos que 4 + 64 es igual a 68 

  3) por consiguiente al imprimirlo y llamar a la funcion externa el valor o resultado final es 68 

 */


  /*
  * Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
  */

console.log(Math.max(1,3,2));  // esta funcion elige el numero mayor de los expuestos en una lista

console.log(Math.random(10,12)); // la funcion Math.random elige un numero aleatorio entre los valores expuestos;


//Funcion del objeto Date

let momento = new Date ();
console.log(momento);

// Funciones del Objeto String

console.log( 'texto'.length); 

 /* 
 * Pon a prueba el concepto de variable LOCAL y GLOBAL.
 */

 //Variables locales y Globales 

 //Variables Globales
 //se puede acceder a ella asi este en fuera de la funcion


 let globalVar = ('soy una variable global');

 let seeGlobal =()=>{
    console.log(globalVar);
 }

 seeGlobal();
 console.log(globalVar);

 //Variables locales
//Solo se puede acceder a ellar cuando se declaran dentro de la funcion si estan por fuera no 

 let localVar = (mult)=> {
    let mult1 = mult*2
    console.log(mult1)
 }

 localVar(2);
//  console.log(mult1);

  /*
  DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
  */

  let funTwo = (num1, num2) => {
    let n1 = parseFloat(num1);
    let n2 = parseFloat(num2);
    let contador = 0
    for (let i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            console.log(num1+' '+ num2);
        } else if (i % 3 == 0) {
            console.log(num1);
        } else if (i % 5 == 0) {
            console.log(num2);
        } else {
            console.log(i);
            contador++
        }
    }
    return contador
}
console.log(funTwo('num1','num2'));