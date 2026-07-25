// Operaciones con cadenas de caracteres

let myString:string = 'Hola ' + 'mundo'; //Concatenar.
let saludo=`Sharah: ${myString}!`; // Interpolación.

console.log(saludo.length); //Longitud (número de caracteres incluyendo espacios, símbolos, etc.).

console.log(saludo.toUpperCase); //Conversión a mayúsculas.
console.log(saludo.toLowerCase); //Conversión a minúsculas.

console.log(saludo.charAt(2)); //Acceder a caracteres específicos.
console.log(saludo[1]); //Acceder con [].

//subcadenas
console.log(saludo.slice(8, 11)); // Extraer partes de una cadena con slice(start, end)/ desde 'start' hasta el caracter antes de 'end'.
console.log(saludo.slice(-6,-1)); //slice con negativos
console.log(saludo.substring(0,6)); //Extraer con substring(start, end): similar a slice, pero este no permite índices negativos.

console.log(saludo.indexOf('mundo')); //Obetener la primera posición de una subcadena. 
console.log(saludo.lastIndexOf('a')); // Obtiene la última posición de una subcadena.

//verificación.
console.log(saludo.includes('Hola')); // Validar si la subcadena existe.
console.log(saludo.startsWith('Sharah')); // Validar si la cadena empieza con la subcadena.
console.log(saludo.endsWith('mundo.')); // Validar si la cadena termina con la subcadena.

console.log(saludo.replace('Hola mundo', 'Hello World')); // Reemplazar la primera cadena que coincida.
saludo = 'Hola mundo desde javascript. Es divertido aprender javascript.'
saludo = saludo.replaceAll('javascript', 'typescript'); //Reemplazar todas las apariciones en la cadena de la primera subcadena dada con la segunda.

//División de cadenas: se divide una cadena según el separador establecido (' ' | ',' | '.') convirtiendola en un array.
console.log(saludo.split(' ')); // ['Hola', 'mundo', 'desde', 'typescript.', 'Es', 'divertido', 'aprender', 'typescript.']

//Unión de cadenas: permite unir un array de cadenas en una sola.
let holaMundo = ['Hola', 'mundo', 'desde', 'typescript'];
console.log(holaMundo.join(' '));

let numeros = ['10', '20', '30', '40'];
console.log(numeros.join('-'));

numeros.reverse();
console.log(numeros); //reverse

saludo = 'Hola mundo!';
console.log(saludo.repeat(3)); //repetición

// Recorrido
let palabra = 'palabra'; 

for(let i=0; i<palabra.length; i++){
    console.log(`Índice: ${i}, letra: ${palabra[i]}`);
}

for(let letra of palabra){
    console.log(letra);
}


let eliminarEspacios = '   eliminar espacios en una cadena      ';
console.log(eliminarEspacios.trim()); //Eliminar espacios al inicio y final
console.log(eliminarEspacios.trimStart()); //Eliminar espacios al inicio
console.log(eliminarEspacios.trimEnd()); //Eliminar espacios al final


let numeros2 = '1234.4566';
console.log(parseInt(numeros2)); //Convertir en número entero. 
console.log(parseFloat(numeros2)); //Convertir en número decimal.
console.log(Number(numeros2)); // Convertir en su tipo numérico correspondiente.

//Extra 
const readline = require("readline");
    
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function compararPalabras(){
    rl.question('Ingrese la primera palabra: ', (laPalabra1)=>{
        rl.question('Ingrese la segunda palabra: ',(laPalabra2)=>{
            let palabra1 = laPalabra1.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
            let palabra2 = laPalabra2.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
            
            //palíndromos
            if(palabra1 == palabra1.split('').reverse().join('')){
                console.log(`"${laPalabra1}" es un palíndromo.`);
            }else{console.log(`"${laPalabra1}" no es un palíndromo.`);}

            if(palabra2 == palabra2.split('').reverse().join('')){
                console.log(`"${laPalabra2}" es un palíndromo.`);
            }else{console.log(`"${laPalabra2}" no es un palíndromo.`);}

            //Anagramas
            let newPalabra1 = palabra1.split('').sort().join('');
            let newPalabra2 = palabra2.split('').sort().join('');
            
            if(newPalabra1 == newPalabra2){
                console.log(`"${laPalabra1}" es anagrama de "${laPalabra2}"`);
            }else{console.log(`"${laPalabra1}" no es anagrama de "${laPalabra2}"`);}

            //Isogramas
            let setPalabra1 = new Set(palabra1.split(''));
            let arrayPalabra1 = [... setPalabra1];

            if(arrayPalabra1.join('').length == palabra1.length){
                console.log(`"${laPalabra1}" es isograma.`);
            }else{console.log(`"${laPalabra1}" no es isograma.`)}

            let setPalabra2 = new Set(palabra2.split(''));
            let arrayPalabra2 = [... setPalabra2];
            
            if(arrayPalabra2.join('').length == palabra2.length){
                console.log(`"${laPalabra2}" es isograma.`);
            }else{console.log(`"${laPalabra2}" no es isograma.`);}

            rl.close();
        });
    });
}
compararPalabras();