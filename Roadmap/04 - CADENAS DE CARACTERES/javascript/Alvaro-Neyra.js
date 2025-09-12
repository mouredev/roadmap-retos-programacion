// Acesso a caracteres
let string = 'Hello, World!';
let charW = string[7];
console.log(`Accediendo a un caracter en especifico del string usando []: ${charW}`);

// Subcadenas
let subCadena = string.substring(0,5);
console.log(`Conseguiendo una subcadena de la cadena principal usando el metodo .substring(): ${subCadena}`);

// Longitud
let cadenaEjemplo = "Hola, Hermoso mundo!";
let longitudDeLaCadena = cadenaEjemplo.length;
console.log(`Conseguiendo la longitud o la cantidad de caracteres de la cadena usando .length: ${longitudDeLaCadena}`);

// Repeticion
let otraCadenaEjemplo = "Querido, Mundo...";
let repetirCadena = otraCadenaEjemplo.repeat(4);
console.log(`Hemos usado el metodo .repeat(4) para repetir la cadena 4 veces: ${repetirCadena}`);

// Recorrido:
let cadenaAIterar = "Mi nombre es ...";
console.log(`Iterando la cadena....`);
for (let i = 0; i < cadenaAIterar.length; i++) {
    console.log(`${cadenaAIterar[i]}`)
}

// Conversion a Mayusculas:
let importante = "esto es importante"
let importanteDeVerdad = importante.toUpperCase();
console.log(`Con el metodo toUpperCase() transformamos la cadena a mayusculas: ${importanteDeVerdad}`);

// Conversion a Minusculas:
let noImportante = "ESTO NO DEBERIA SER IMPORTANTE";
let noImportanteDeVerdad = noImportante.toLowerCase();
console.log(`Con el metodo .toLowerCase() transformamos la cadena a mayusculas: ${noImportanteDeVerdad}`);

// Reemplazo
let sentence = "Esta maquina esta malograda!";
let reemplazo = sentence.replace("malograda", "en buen estado");
console.log(`Hemos usado el metodo .replace() para reemplazar una subcadena existente: ${reemplazo}`);

// Division
let cadenaALista = "Esta va a ser una cadena que se separara por espacios";
let divisionDeCadena = cadenaALista.split(" ");
console.log(`Hemos usado el metodo .split() para separar la cadena en subcadenas y conviertiendo cada subcadena en elementos de una lista: ${divisionDeCadena}`);

// Union
let listaDeSubCadenas = ["Hola", "Mundo", "Te", "Amo"];
let cadenaUnida = listaDeSubCadenas.join(", ");
console.log(`Hemos usado el metodo .join() en una lista de elementos para separar esos elementos y luego convertirlos en un solo string: ${listaDeSubCadenas}`);

// Interpolacion
let nombre = "Alvaro";
let saludo = `Hola, ${nombre}!`;
console.log(`Usando la interpolacion para usar los valores de las variables existentes dentro un string: ${saludo}`);

// Verificacion
let cadenaNoVerificada = "Mi lindo perro se llama Luke!";
let incluyeMiPerro = cadenaNoVerificada.includes("Luke");
console.log(`Usando el metodo .includes() para verificar si una subcadena existe dentro de la cadena principal, si existe devuelve true: ${incluyeMiPerro}`);

// Ejercicio Opcional:
function anagrama(string1, string2) {
    let normalizar = (str) => str.toLowerCase().split('').sort().join('');
    return normalizar(string1) === normalizar(string2);
}

function palindroma(string1) {
    return string1 === string1.split('').reverse().join('');
}

function isograma(string1) {
    let letras = string1.toLowerCase().split('').sort();
    for (let i = 1; i < letras.length; i++){
        if (letras[i] === letras[i - 1]) {
            return false;
        }
    }
    return true;
}

let palabra1 = "iman";
let palabra2 = "mani";

console.log(`Es ${palabra1} un palindrome?:`, palindroma(palabra1));
console.log(`Es ${palabra2} un palindrome?:`, palindroma(palabra2));

console.log(`Son ${palabra1} y ${palabra2} anagramas?`, anagrama(palabra1, palabra2));

console.log(`Es ${palabra1} un isograma?:`, isograma(palabra1));
console.log(`Es ${palabra2} un isograma?:`, isograma(palabra2));