
//* CADENAS DE CARACTERES

/*

En JavaScript, una cadena de caracteres (también conocida como "string") 
es una secuencia de caracteres Unicode. Puedes crear cadenas utilizando 
comillas simples (''), comillas dobles ("") o la sintaxis de comillas 
invertidas (``).

*/


//* OPERACIONES

//Acceso a caracteres específicos:
let cadena = "JavaScript";
let tercerCaracter = cadena[2];
console.log(tercerCaracter); // Salida: v


//Subcadenas:
let cadena2 = "JavaScript";
let subcadena = cadena2.substring(0, 4);
console.log(subcadena); // Salida: Java


//Longitud de una cadena:
let cadena3 = "Hola, mundo!";
let longitud = cadena3.length;
console.log(longitud); // Salida: 12


//Concatenación:
let str1 = "Hola";
let str2 = "Mundo";
let resultado = str1.concat(" ", str2);
console.log(resultado);          // Salida: Hola Mundo
console.log(str1 + " " + str2 ); // Salida: Hola Mundo


//Repeticion
let cadena4 = "Hola ";
let repetida = cadena4.repeat(4);
console.log(repetida); // Salida: Hola Hola Hola Hola


//Recorrido
let cadena5 = "JavaScript";
for (let i = 0; i < cadena5.length; i++) {
  console.log( cadena5[i] );
};
//Salida:
/*

"J"
"a"
"v"
"a"
"S"
"c"
"r"
"i"
"p"
"t"

*/


//Conversión a mayúsculas y minúsculas:
let cadena6 = "JavaScript";
let mayusculas = cadena6.toUpperCase();
let minusculas = cadena6.toLowerCase();
console.log(mayusculas); // Salida: JAVASCRIPT
console.log(minusculas); // Salida: javascript


//Reemplazo
let frase = "La programación es divertida";
let buscar = "divertida";
let reemplazarCon = "increíble";
let nuevaFrase = frase.replace(buscar, reemplazarCon);
console.log(nuevaFrase); // Salida: La programación es increíble


//División
let cadena7 = "Manzana,Naranja,Uva";
let frutas = cadena7.split(",");
console.log(frutas); // Salida: ["Manzana", "Naranja", "Uva"]


//Unión
let frutas2 = ["Manzana", "Naranja", "Uva"];
let cadena8 = frutas2.join(" - ");
console.log(cadena); // Salida: Manzana - Naranja - Uva


//Interpolación de Cadenas
let nombre = "Artic";
let edad = 34;
let mensaje = `Hola, soy ${nombre} y tengo ${edad} años.`;
console.log(mensaje); // Salida: Hola, soy Artic y tengo 34 años.


//Verificación de presencia
let cadena9 = "JavaScript";
let contieneJava = cadena9.includes("Java");
console.log(contieneJava); // Salida: true


//Busqueda de subcadena
var cadena10 = "Hola mundo";
var subcadena2 = "mundo";
var indice = cadena10.indexOf(subcadena2); // indice será 5


//Comparación de Cadenas
var cadenaA = "Hola";
var cadenaB = "Hola";
var comparacion = cadenaA === cadenaB; // comparacion será true



//* DIFICULTAD EXTRA:
/*

Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:

    Palíndromos
    Anagramas
    Isogramas

*/

/*

Polindromos
son aquellas que se leen igual de izquierda a derecha que de derecha a izquierda.
"oso", "reconocer", "radar" y "salas". 

Anagramas
Las palabras anagramas son aquellas que se forman mediante la reorganización de 
las letras de otra palabra, utilizando todas las letras originales exactamente 
una vez. 
"amor" y "roma" son anagramas, ya que comparten las mismas letras pero están 
dispuestas de manera diferente.

Isogramas
Las palabras isogramas son aquellas que no tienen letras repetidas. En un isograma, 
cada letra aparece una sola vez.
"murciélago", "estufa" y "celular".

*/


let analyzeWord = () => {

//Palabras que se pueden cambiar para testear
    let word1 = 'murciélago';
    let word2 = 'oso';

    console.log('---------- PALINDROMO ----------');
    let palindromo = (w) => {
        let minus = w.toLowerCase();
        let rev = minus.split('').reverse().join('');
        if( minus === rev ){
            console.log(`${w} Es Palíndromo`);
        }else{
            console.log(`${w} No es Palíndromo`);
        }
    };
    palindromo( word1 );
    palindromo( word2 );
    console.log('---------- ANAGRAMA ----------');
    let anagrama = ( w1,w2 ) =>{
        let str1 = w1.toLowerCase();
        let str2 = w2.toLowerCase();
        const arr1 = str1.split('').sort().join('');
        const arr2 = str2.split('').sort().join('');
        return arr1 === arr2;
    };
    if( anagrama(word1, word2) ){
        console.log(`${word1} y ${word2} Son Anagramas.`);
    }else{
        console.log(`${word1} y ${word2} No son Anagramas.`);
    }
    console.log('---------- ISOGRAMA ----------');
    let isograma = (w) =>{
        let minus = w.toLowerCase();
        let letras = new Set();
        for (let letra of minus) {
            // Si la letra ya está en el conjunto, no es un isograma
            if ( letras.has(letra) ) {
              console.log(`${w} No es un Isograma`);
              return;
            }else{
                letras.add(letra);
            }
          }
        //no se encontraron letras repetidas, es un isograma
        console.log(`${w} Es un Isograma`);;
    }
    isograma( word1 );
    isograma( word2 );
};


analyzeWord();

