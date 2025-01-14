// operaciones que se pueden realizar con cadenas de caracteres

let string = "La vida es un viaje de autodescubrimiento, atrévete a explorar."

console.log(string.charAt(3)); //Acceso a caracteres específicos
console.log(string[3]); // Acceso a caracteres específicos
console.log(string.substring(3, 9)); // Subcadena que imprime una parte de la cadena
console.log(string.substring(3)); // Subcadena que imprime desde el indice indicado en adelante
console.log(string.slice(-9, -1)); // Subcadena que imprime una parte de la cadena, permite valores negativos para acceder a los caracteres del final del string
console.log(string.slice(-9)); // Subcadena que imprime desde el indice indicado en adelante, permite valores negativos para acceder a los caracteres del final del string
console.log(string.length); // Conocer la longitud
console.log(string + " Anaïs Nin"); // Concatenación
console.log(string, " Anaïs Nin"); // Concatenación
console.log(`${string} Anaïs Nin`); // Concatenación
console.log(string.concat(" ", "Anaïs Nin")); // Concatenación
console.log(string.repeat(3)); //Repetición
console.log(string.toUpperCase()); // Conversión a mayúscula
console.log(string.toLowerCase()); // conversión a minúsculas
console.log(string.replace("autodescubrimiento", "descubrimiento")); // Reemplazo
let division = string.split(" ") // División
console.log(division); 
console.log(division.join(" ")); // Union
console.log(string.includes("vida")); // Buscar cadenas
console.log(string.search("vida")); // Buscar en que indice esta la palabra
console.log(string.indexOf("v")); // Buscar indice de un caracter
console.log(string.startsWith("La")); // Buscar el inicio de una cadena
console.log(string.endsWith("explorar.")); // Buscar el final de una cadena
console.log(string.endsWith("explorar.")); // Buscar el final de una cadena
console.log(typeof(string)); // Saber el tipo de dato


// DIFICULTAD EXTRA
function palindromos(palindromo)
{
    let arraypalindromo = palindromo.split("")
    let arrayReverso = arraypalindromo.reverse()
    let palindromoReverso = arrayReverso.join("")
    if(palindromoReverso.toLocaleLowerCase() == palindromo.toLocaleLowerCase())
    {
        console.log("Esta palabra es un palíndromo");
    }
    else
    {
        console.log("Esta palabra no es un palíndromo");
    }
}
palindromos("radar")

function anagramas(palabra1, palabra2)
{
    console.log(palabra1.toLowerCase().split("").sort().join(""));
    console.log(palabra2.toLowerCase().split("").sort().join(""));
    if(palabra1.toLowerCase().split("").sort().join("") == palabra2.toLowerCase().split("").sort().join(""))
    {
        console.log("Esto es un anagrama");
    }
    else
    {
        console.log("Esto no es un anagrama");
    }
}
anagramas("amor", "roma")

function isogramas(isograma)
{
    let noIsograma = true
    let conteoPalabra = {}

    for (let i of isograma.toLowerCase()) {
    
        if(!(Object.keys(conteoPalabra).includes(i)))
        {
            conteoPalabra[i] = 0
        }

        conteoPalabra[i] += 1
    }

    let claves = Object.keys(conteoPalabra)
 
    for(let c in conteoPalabra)
    {
        if(conteoPalabra[claves[0]] != conteoPalabra[c])
        {
            noIsograma = false
        }
    }

    return noIsograma
}

console.log(isogramas("palopalopalo") ? "Es un isograma" : "No es un isograma");