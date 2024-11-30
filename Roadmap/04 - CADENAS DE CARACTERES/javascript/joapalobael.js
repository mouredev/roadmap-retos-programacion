
let my_quote = "Maybe I don't really want to know how your garden grows, 'Cause I just want to fly."
//Cantidad de caracteres (incluye espacios)
console.log("-------- Length→ Cantidad de caracteres --------");
console.log(my_quote.length - 1);
// Un caracter individual
console.log("-------- charAt→ Posición de un caracter en particular --------");
console.log(my_quote.charAt(71));
// Subcadena dentro de cadena
console.log("-------- indexOf→ Encuentra una subcadena dentro de una cadena --------");
let a = "know";
if (my_quote.toLocaleLowerCase().indexOf(a) !== -1) {
    console.log(`Si, encontré la palabra: ${a}`)
} else {
    console.log('no se encuentra la palabra');
}
console.log("-------- Slice→ Extrae una subcadena dentro de una cadena, conociendo el inicio --------");
// Extraer una subcadena dentro de una cadena, conociendo el inicio
console.log(my_quote.slice(71, 75));
// Actualizar parte de una cadena
console.log("-------- Replace→ Actualiza parte de una cadena --------");
console.log(my_quote.replace("fly", "swim"));
//Concatenación
console.log("-------- Concatenación→ Suma cadena de textos --------");
let part1 = "Latlely, did you ever feel the pain?"
let part2 = "in the morning rain, as it soaks you to the bone."
console.log(part1 + " " + part2);
console.log(part1.concat(" ", part2));
console.log("-------- Interpolación→ template literals --------");
console.log(`${part1} ${part2}`)
//Busqueda de ocurrencias
console.log("-------- split+reduce → Busqueda de ocurrencias --------");
let part1ToArray = part1.split('');
let counter = part1ToArray.reduce((objetoAcumulador, letra) => {
    // console.log(`Acumulador: ${JSON.stringify(objetoAcumulador)}`);
    // console.log(`Elemento Actual: ${letra}`);
    objetoAcumulador[letra] = (objetoAcumulador[letra] || 0) + 1;
    return objetoAcumulador;

}, {});
console.log(`El resultado final es: ${JSON.stringify(counter)}`);

// Join
console.log("-------- Join → Metodo para concatenar elementos de un array --------");
console.log(part1ToArray.join(""));

console.log("-------- Transformaciones numericas --------");
const num1 = "100793"
console.log(parseInt(num1));
const num2 = "21.09"
console.log(parseFloat(num2));

console.log("-------- Validar si es alpha o alphanumerico --------");
// En JS no existe las funciones como en phyton, pero se pueden crear con arrow functions

const isAlpha = (str) => /^[A-Za-z\s.,?!]+$/.test(str);
const isAlnum = (str) => /^[A-Za-z0-9\s.,?!]+$/.test(str);

console.log(isAlnum(part2));
console.log(isAlpha(num2));

/*---- Ejercicio Extra ----*/
//instale npm install prompt-sync
const prompt = require("prompt-sync")({ sigint: true });

// Palindromo
function palindromoCheck() {
    let esPalindromo = prompt('Ingrese una palabra para chequear si es Palindromo:');
    // Cualquier caracter que NO sea A-Z o a-z o un espacio, se reemplazara con ''. /g significa global, no solo la primer coincidencia. 
    let palindromoNormalizado = esPalindromo.replace(/[^A-Za-z]/g, '').toLocaleLowerCase();
    let palindromoInvertido = palindromoNormalizado.split('').reverse().join('');
    if (palindromoNormalizado === palindromoInvertido) {
        console.log(`Efectivamente, ${palindromoNormalizado} es un palíndromo`)
    } else {
        console.log(`No, ${palindromoNormalizado} no es un palindromo. El inverso es ${palindromoInvertido}`);
    }
}
palindromoCheck();

//Anagrama
function anagramaCheck() {
    let esAnagrama1 = prompt('Vamos a chequear si dos palabras son anagramas entre sí. Ingrese la primer palabra: ');
    let esAnagrama2 = prompt('Ingrese la segunda palabra palabra: ');

    let anagramaNormalizado1 = esAnagrama1.replace(/[^A-Za-z]/g, '').toLocaleLowerCase().split('').sort().join('');
    let anagramaNormalizado2 = esAnagrama2.replace(/[^A-Za-z]/g, '').toLocaleLowerCase().split('').sort().join('');

    if (anagramaNormalizado1 === anagramaNormalizado2) {
        console.log(`Efectivamente, ${esAnagrama1} es un anagrama de ${esAnagrama2} porque utilizan las mismas letras: ${anagramaNormalizado1}`);
    } else {
        console.log(`No, ${esAnagrama1} no es un anagrama de ${esAnagrama2}`);
    }

}
anagramaCheck();

//Isograma
function isogramaCheck() {
    let esIsograma = prompt('Ingrese una palabra para validar si es un isograma: ');
    let isogramaToArray = esIsograma.replace(/[^A-Za-z]/g, '').toLocaleLowerCase().split('');
    let isoCounter = isogramaToArray.reduce((objetoAcumulador, letra) => {
        // console.log(`Acumulador: ${JSON.stringify(objetoAcumulador)}`);
        // console.log(`Elemento Actual: ${letra}`);
        objetoAcumulador[letra] = (objetoAcumulador[letra] || 0) + 1;
        return objetoAcumulador;

    }, {});
    let check = true;
    for (const letra in isoCounter) {
        if (isoCounter[letra] > 1) {
            check = false;
            break;
        }
    }

    if (check) {
        console.log(`¡Buenísimo! ${esIsograma} es un isograma.`);
    } else {
        console.log(`${esIsograma} no es un isograma. Se repiten algunas letras.`);
    }
}
isogramaCheck();