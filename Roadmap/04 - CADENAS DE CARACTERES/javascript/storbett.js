// Operaciones

let s1 = "hola";
let s2 = "javascript";

// Concatenación
console.log(s1 + ", " + s2 + "!");

// Repetición
console.log(s1.repeat(3));

// Indexación
console.log(s1[0] + s1[1] + s1[2] + s1[3]);

// Longitud
console.log(s1.length + s2.length);

// Slicing (porción)
console.log(s2.slice(2, 5));
console.log(s2.slice(2));
console.log(s2.slice(0, 2));
console.log(s2.slice(0, 2));

// Búsqueda
console.log(s1.includes("a"));

// Reemplazo
console.log(s1.replace("o", "a"));

// División
console.log(s2.split("t"));

// Mayúsculas y minúsculas
console.log(s2.toUpperCase());
console.log(s2.toLowerCase());
console.log("simon torbett".split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' '));
console.log("simon torbett".charAt(0).toUpperCase() + "simon torbett".slice(1));

// Eliminación del espacio al principio y al final
console.log(" simon torbett ".trim() + " lo lograrás");

// Búsqueda al principio y al final
console.log(s1.startsWith("ho"));
console.log(s1.startsWith("ja"));

let s3 = "simon torbett";
// Búsqueda de posición
console.log("simon torbett @storbett".indexOf("torbett"));

// Búsqueda de ocurrencias
console.log((s3.match(/t/g) || []).length);

// Formateo
console.log(`saludo: ${s1}, lenguaje: ${s2}!`);

// Transformación en lista de caracteres
console.log(s3.split(''));

// Transformación en lista en cadena
let l1 = [s1, ", ", s2, "!"];
console.log(l1.join(''));

// Transformación numérica
let s4 = "1234";
s4 = parseInt(s4);
console.log(s4);

let s5 = "1234.123";
s5 = parseFloat(s5);
console.log(s5);

// Comparaciones varias
s4 = 1234;
console.log(/^\w+$/.test(s1)); // isalnum
console.log(/^[A-Za-z]+$/.test(s1)); // isalpha

// Extra

function check(palabra1, palabra2) {
    // Palíndromos
    console.log(`${palabra1} es un palíndromo?: ${palabra1 === palabra1.split('').reverse().join('')}`); 
    console.log(`${palabra2} es un palíndromo?: ${palabra2 === palabra2.split('').reverse().join('')}`); 

    // Anagramas
    console.log(`${palabra1} es un anagrama de ${palabra2}?: ${palabra1.split('').sort().join('') === palabra2.split('').sort().join('')}`); 

    // Isogramas
    console.log(`${palabra1} es un isograma?: ${new Set(palabra1).size === palabra1.length}`); 
    console.log(`${palabra2} es un isograma?: ${new Set(palabra2).size === palabra2.length}`); 

    let palabraDict = {};
    for (let char of palabra1) {
        palabraDict[char] = (palabraDict[char] || 0) + 1;
    }

    let isograma = true;
    let values = Object.values(palabraDict);
    let isogramaLen = values[0];
    for (let value of values) {
        if (value !== isogramaLen) {
            isograma = false;
            break;
        }
    }

    console.log(isograma);
    console.log(palabraDict);
}

check("radar", "javascript");
// check("amor", "roma");
