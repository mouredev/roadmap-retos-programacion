/*
Operaciones
*/

let s1 = "Hola";
let s2 = "JavaScript";

//Concatenación
console.log(s1 + ", " + s2 + "!");

//Repeticion
console.log(s1.repeat(3));

//Indexacion
console.log(s1[0] + s1[1] + s1[2] + s1[3]);

//Longitud 
console.log(s2.length);

//Slicing (porcion)
console.log(s2.slice(3, 10));

//Busqueda
console.log(s2.includes("Java")); //true

//Remplazo
console.log(s2.replace("Java", "Type"));

//Division
console.log(s2.split("a"));

//Mayusculas y minusculas
console.log(s1.toUpperCase());
console.log(s1.toLowerCase());

//Eliminacion de especacios al inicio y al final
console.log("   Emanuel Aristizabal   ".trim());

//Busqueda al principio y al final
console.log(s2.startsWith("Java"));
console.log(s2.startsWith("Script"));
console.log(s2.endsWith("Script"));
console.log(s2.endsWith("Java"));

//Busqueda de posicion
console.log(s2.indexOf("a")); //posicion de la primera "a"
console.log(s2.lastIndexOf("a")); //posicion de la ultima "a"
console.log(s2.toUpperCase().indexOf("S"));

//Interpolacion
console.log(`Saludo: ${s1}, lenguaje: ${s2}`);

//Transformacion de cadena a arreglo
console.log(Array.from(s2));


//Transformacion de lista en cadena
let l1 = [s1, ", ", s2, "!"];
console.log(l1.join(""));

//Transformaciones numericas
let s4 = "12345";
s4 = Number(s4);
console.log(s4);

let s5 = "12345.123";
s5 = parseFloat(s5);
console.log(s5);

/*
Extra
*/

function check(word1, word2) {

    //Palindromos
    console.log(`${word1} es un palindromo?: ${word1 === word1.split("").reverse().join("")}`)
    console.log(`${word2} es un palindromo?: ${word2 === word2.split("").reverse().join("")}`)

    //Anagramas
    console.log(`${word1} es un anagrama de ${word2}?: ${word1.split("").sort().join("") === word2.split("").sort().join("")}`)

    //Isograma
    console.log(word1.length === new Set(word1).size)
    console.log(word2.length === new Set(word2).size)



}

check("radar", "python");

function esPalindromo(palabra1) {

    const palabraTransformada = palabra1.split("").reverse().join("");

    if (palabraTransformada === palabra1) {
        console.log(`La palabra ${palabra1}, si es un palindromo y es ${palabraTransformada}`);
    } else{
        console.log(`La palabra ${palabra1}, no es un palindromo`);
    }

}

esPalindromo("reconocer");

function esAnagrama(palabra2, palabra3) {

    const palabraUnificada = palabra2.split("").reverse().join("")
    const palabraUnificada1 = palabra3.split("").reverse().join("")

    if (palabraUnificada === palabraUnificada1) {
        console.log(`La palabra ${palabra2}, si es un anagrama y su anagrama es ${palabra3}`);
    } else {
        console.log(`La palabra ${palabra2} y la palabra ${palabra3}, no son anagramas`);
    }

}

esAnagrama("amar", "rama");

function esIsogram(palabra4) {

    const wordDict1 = new Map();

    for (let character of palabra4) {
        let count = wordDict1.get(character) || 0;
        wordDict1.set(character, count + 1);
    }
    const valores = Array.from(wordDict1.values());
    let isogram = true;

    for(let valor of valores){
        if(valor !== 1){
            isogram = false;
        }
    }
    console.log(`La palabra ${palabra4} es un isograma?: ${isogram}`)
};

esIsogram("amor")