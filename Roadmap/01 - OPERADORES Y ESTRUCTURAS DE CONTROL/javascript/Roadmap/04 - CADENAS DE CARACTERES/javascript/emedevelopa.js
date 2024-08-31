// CADENAS DE CARACTERES

// Concatenación
let str1 = "Hola";
let str2 = "qué tal estás?";
let resultado = str1 + " " + str2;
console.log(resultado);

// Longitud de cadena
let frase = "Hola me llamo Antoñita";
let longitud = frase.length;
console.log(longitud);

// Acceso a caracteres individuales
let palabra = "Machete";
let caract = palabra[0];
console.log(caract);

// Búsqueda y comparación
let frase1 = "Dale a tu cuerpo alegría macarena";
console.log(frase1.indexOf("cuerpo")); //10
console.log(frase1.lastIndexOf("tu")); //7
console.log(frase1.startsWith("Hola")); //flase
console.log(frase1.endsWith("macarena")); //true
console.log(frase1.includes("culo")); //false

// Extracción de subcadenas
let oracion = "El mundo es mío y de nadie más";
console.log(oracion.substring(2, 7));
console.log(oracion.slice(5));

// Transformación de texto
let word = "Me gusta la lasaña";
console.log(word.toUpperCase());

// Reemplazar
console.log(word.replace ("lasaña", "sopa"));

// Acceder a un caracter
let sofa = "sofa";
//console.log(sofa.charAt(2)); //f
console.log(sofa[2]); //f

// Repetición
let piano = "piano";
console.log(piano.repeat(3)); //pianopianopiano

// Recorrido
let bucle = "Esto es un bucle";
for(let i = 0; i < bucle.length; i++) {
    console.log(bucle[i]);
}

// Dividir
let str3 = "azul, verde, naranja, negro";
//let strdiv = str3.split(' ');//Por espacios
//let strdiv = str3.split(''); //por caracter
//let strdiv = str3.split(','); //por comas
let strdiv = str3.split(',', 3); //por limite
console.log(strdiv);

// Eliminar espacios en blanco
let str4 = " Me duele un pie ";
console.log(str4.trim());

// Revertir cadena
let str5 = "No quiero trabajar";
console.log(str5.split('').reverse().join(''));

//Interpolación
let msg1 = "mañana";
let msg2 = "frío";
let msg3 = "lloviendo";
let finalmsg = `Esta ${msg1} hacía ${msg2} y estaba ${msg3}`
console.log(finalmsg);

//EXTRA

function esPalindromo (palabra) {
    const palabraReversa = palabra.split('').reverse().join('');
    return palabraReversa === palabra;
}

function esAnagrama(palabra) {
    const ordenada = palabra.split('').sort().join('');
    return ordenada === palabra;
}

function esIsograma(palabra) {
    const letras = {};
    for (let letra of palabra) {
        if (letras[letra]) {
            return false;
        }
        letras[letra] = true;
    }
    return true;
}

function palabras (palabra1, palabra2) {
    let resultado = "";
    
    if (esPalindromo(palabra1) && esPalindromo(palabra2)) {
        resultado += `"${palabra1}" y "${palabra2}" son Palíndromos.`;
    } else if (esPalindromo (palabra1)) {
        resultado += `"${palabra1}" es un Palíndromo y "${palabra2}" no lo es.`;
    } else if (esPalindromo (palabra2)) {
        resultado += `"${palabra2}" es un Palíndromo y "${palabra1}" no lo es.`;
    } else {
        resultado += `Ninguna es un palíndromo`;
    }

    if (esAnagrama(palabra1) && (palabra2)) {
        resultado += `"${palabra1}" y "${palabra2}" son Anagramas.`;
    } else if (esAnagrama (palabra1)) {
        resultado += `"${palabra1}" es Anagrama y "${palabra2}" no lo es.`;
    } else if (esAnagrama (palabra2)) {
        resultado += `"${palabra2}" es Anagrama y "${palabra1}" no lo es`;
    } else {
        resultado += `Ninguna es una anagrama`;
    }

    if (esIsograma(palabra1) && (palabra2)) {
        resultado += `"${palabra1}" y "${palabra2}" son Isogramas.`;
    } else if (esIsograma(palabra1)) {
        resultado += `"${palabra1}" es Isograma y "${palabra2}" no lo es.`
    } else if (esIsograma(palabra2)) {
        resultado += `"${palabra2}" es Isograma y "${palabra1}" no lo es.`
    } else {
        resultado += `Ninguna es un isograma`;
    }
    return resultado.trim();
}

console.log(palabras("amor", "reconocer"));


