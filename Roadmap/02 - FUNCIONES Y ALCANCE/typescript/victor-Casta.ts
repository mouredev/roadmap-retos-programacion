//Funciones sin parametros y sin retorno
let myFunction = function() {
  console.log("Soy una función");
}

//Funciones con unos o varios parametros
let addNumbers = function(a:number, b:number) {
  console.log(a + b);
}
addNumbers(1, 2);

//Funciones con retorno
let multiply = function(a:number, b:number):number{
  return a * b;
}
console.log(multiply(3,4));

/*
  * -Utiliza algún ejemplo de funciones ya creadas en el lenguaje
*/

setTimeout(() => console.log('Hola despues de 2000 ms'), 2000)


/*
  * -Pon a prueba el concepto de variable LOCAL y GLOBAL.
*/

let myGlobalVariable = 'Hola' //Esta varible  se puede acceder en cualquier lugar del documento
let variables = function(){
  let myLocalVariable = 'TypeScript'//solo se puede acceder a myLocalVariable dentro de esta funcion
  return myGlobalVariable + myLocalVariable
}
console.log(variables())

/*
  * - Comprueba si puedes crear funciones dentro de funciones.
*/

let saludar = function(a:string) {
  let hablar = (b:string) => console.log(`${a} ${b}`);
  return hablar;
}
saludar("Hola")("TypeScript");

/*
 * - Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

let myPrincipalFuncion = function(a:string, b:string) {
  let contador = 0
  for (let i=1; i<=100;i++){
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(`${a} ${b}`);
    } else if(i % 3 === 0) {
      console.log(a);
    } else if(i % 5 === 0) {
      console.log(b);
    }
    else {
      contador++;
    }
  }
  return contador;
}

console.log(myPrincipalFuncion('Hola', 'TypeScript'));
