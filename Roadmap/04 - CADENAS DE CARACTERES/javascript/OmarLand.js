/*
    * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
    * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
    * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
    *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
    *   interpolación, verificación...
*/

// Inicializo una cadena de caracteres:
let firstString = "Saludos desde Javascript"
console.log(`Esta es una cadena: ${firstString}`);

// Ver la longitud de una cadena:
console.log(`Usamos la funcion .length en la variable firstString: ${firstString.length} es su longitud`);

//Accediendo a un valor especifico de la cadena:
console.log(`Usamos nombre de la variable con corchetes ej. var[i] para acceder a un valor concreto: ${firstString[2]}`);

//Obtener el ultimo valor de una cadena:
console.log( `EL ultimo valor de la cadena usamos .length - 1: ${firstString[firstString.length - 1]}` );

// Concateniación de dos cadenas:
let str1 = "Hola saludos"
let str2 = "soy javascript, dos cadenas concatenadas"
console.log( 'Concatenamos dos cadenas así: ', str1 +' '+ str2 ); 

//Repetición de cadena:
let repeatible = "I feel good!!!";
console.log( repeatible.repeat(3) );

// Recorrido de una cadena:
for(let i = 1; i <= firstString.length; i++){
    let caracter = firstString[i - 1];
    console.log(`Position: ${i} >>> `, caracter);
}

// Convertir de mayusculas a minisculas y minusculas a mayusculas:
console.log('A Mayusculas: >>>', firstString.toUpperCase() );
console.log('A Minusculas: >>>', firstString.toLowerCase() );

// Uso del replace:
let str3 = 'I love the Streetfood for a lifetime';
let replaced = str3.replace('Streetfood', 'programming');
console.log('Original: >>>', str3);
console.log('Reemplazado: >>>', replaced);

let replacedAllChar = str3.replaceAll('o', '4')
console.log('>>> ', replacedAllChar);

// Dividiendo / Uso del SPLIT
const splited = firstString.split(' ');
console.log('Dividido split: >>>', splited );

// Union
const joined = splited.join(' ');
console.log("Joined by ' ' >>>: ", joined);

//Interpolación:
console.log(`Esta es una cadena interpolada: ${str1 + ' ' + str2}  `);

// Verificación de una cadena:
const verificando = firstString.includes('Javascript');
console.log("Contiene Javascript: >>>", verificando);


/*
    * DIFICULTAD EXTRA (opcional):
    * Crea un programa que analice dos palabras diferentes y realice comprobaciones
    * para descubrir si son:
    * - ✔️ Palíndromos
    * - ✔️ Anagramas
    * - Isogramas
*/

// Compruebo si dos palabras son Palíndromos:
let str4 = 'Reconocer';
let check0 = str4.toLowerCase().split('').join();
let check1 = str4.toLowerCase().split('').reverse().join();

if( check0 === check1 ){
    console.log('>>> Se trata de un Palíndromo...');
} else {
    console.log('>>> No se trata de un Palíndromo...');
}

// Compruebo si la palabra es un anagrama:
const isAnagrama = (palabra, posibleAnagrama) => {
    let check = palabra.toLowerCase().split("").sort().join();
    let check1 = posibleAnagrama.toLowerCase().split("").sort().join();
  
    if (check === check1) {
      console.log(">>> Se trata de un Anagrama...");
    } else {
      console.log(">>> No se trata de un anagrama");
    }
    return "Proceso completado.";
  };
  
  console.log(isAnagrama("Omar", "roma"));
  
// Compruebo si una palabra es Isograma:
console.log("\n##### Comprobando si un String es Isograma #####");
const isIsograma = (string) => {
  
  const word = string.toLowerCase();

  const wordArray = word.split("");
  const wordSet = new Set(wordArray);
  if (wordArray.length === wordSet.size){
    console.log(">>> Se trata de un Isograma...");
  } else {
    console.log(">>> No se trata de un Isograma...");
  }

  return "Proceso completado.";;

};

console.log( isIsograma("Hola") );
