/*
 DIFICULTAD EXTRA (opcional):
 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

 Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
*/
 //EJERCICIO:
 /* - Crea ejemplos de funciones básicas que representen las diferentes
   posibilidades del lenguaje:
   Sin parámetros ni retorno, con uno o varios parámetros, con retorno... */

//funcion sin parametros
 function functionWithoutParamsAndReturns(){

 }
//funcion con parametros
 function functionWithParams(name:string ='soy un parametro'){
 }
//funcion con retorno
 function functionWithReturn(x:number){
  x = 1;
return x;
 }
//funciones dentro de funciones
 function getIntegerRandom(min:number=1, max:number=5):number {
//funciones ya definidas por el lenguaje -> random()
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
//funciones flecha
const functionWordUpperCase = (word:string='pronto sere grande') => word.toUpperCase();
// - Pon a prueba el concepto de variable LOCAL y GLOBAL.
const enum GlobalVars {Global='estoy en todo!'};
function testGlobalScope(){
GlobalVars.Global // access to global
function testToLocalScoope(){
  let local = 'this is a local var!'
}
return{local:this.local,global:GlobalVars.Global}; //test fail dont exist local in this scoope
}
async function getData(){//funciones asincronas
 const data = await fetch('https://dragonball-api.com/api/characters/1')
return await data.json()
}
const consoles:{[key:string]:any} = {
'funciones vacias': functionWithoutParamsAndReturns,
'funciones con parametros': functionWithParams,
'funciones con retorno': functionWithReturn,
'funciones dentro de funciones y ya definidas por el lenguaje': getIntegerRandom,
'funciones flecha': functionWordUpperCase,
'funcion de scoope global y local':testGlobalScope,
'funcion asincrona':getData
}
for (const result in consoles){
console.log(consoles[result](),'->',result,'\n')
}
// DIFICULTAD EXTRA (opcional):
//  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
(function twoParamStringToNumber(one:string='fizz',two:string='buzz'){

  let start:number = 1;
  let stop:number = 100;
  let total:number = 0;
//  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
  while(start<=stop){
    let response:string = '';
//    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    if(start%3==0 && start%5==0)
      response =one+two
//    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    if(start%3==0 && !response)
      response = one
//    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    if(start%5==0 && !response)
      response= two
//    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
    !response ? total++ : ''
    console.log(!response? start:response,'\n')
    start++;
  }
  return total
})()
