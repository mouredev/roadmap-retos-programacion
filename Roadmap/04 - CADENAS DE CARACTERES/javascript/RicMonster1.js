/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 */

//-Concatenacion-
let miString1 = "Hola";
let miString2 = "JavaScript";
console.log(miString1 + " " + miString2);
console.log(miString1, miString2);
console.log(miString1.concat(" ", miString2));

//-Repeticion-
let miNombre = "Ric ";
console.log(miNombre.repeat(5));

//-Indexacion-
let alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
console.log(alphabet[17] + alphabet[8] + alphabet[2]);

//-Busqueda por posicion-
const miNombreChart1 = alphabet.charAt(17);
const miNombreChart2 = alphabet.charAt(8);
const miNombreChart3 = alphabet.charAt(2);
console.log(miNombreChart1, miNombreChart2, miNombreChart3);
console.log(alphabet.at(17), alphabet.at(8), alphabet.at(2));

//-Busqueda de posicion-
const h = alphabet.indexOf("H");
console.log(`La letra H es la  numero ${h + 1} de nuestro alfabeto`);

//-Longitud-
let miString3 = "Papas fritas";
console.log(miString3.length);

//-Slicing (porcion)-
let fritas = miString3.slice(6);
console.log(fritas);

let miString4 = "Batman le gana a Superman";
let BatmanStr = miString4.substring(0, 6);
let SupermanStr = miString4.substring(17, miString4.length);
console.log(BatmanStr);
console.log(SupermanStr);

//-Iteracion-
for (let i = 0; i < BatmanStr.length; i++) {
    console.log(BatmanStr[i]);
}

//-Busqueda-
let companies = "Google, Telegram, Facebook, YouTube";
console.log(companies.includes("Google"));
console.log(companies.includes("Microsoft"));

//-Reemplazo-
let messageMusicPlayer =
    'Music Player says: \n Now playing "The Pretender - Foo Fighters"';
console.log(messageMusicPlayer);
let latestSong = '"The Pretender - Foo Fighters"';
let currentSong = '"Monster - Skillet"';
console.log(messageMusicPlayer.replace(latestSong, currentSong));

//-Division-
let companiesArray = companies.split(", ");
console.log(companiesArray);
let colores = "amarillo, rojo, verde, marron";
console.log(colores.split("r"));

//-Union-
let companiesNuevaStr = companiesArray.join(", ");
console.log(companiesNuevaStr);

//-Mayusculas, minusculas y letras en mayusculas-
let miString5 = "CamellOs y cabAlloS";
let minusculas = miString5.toLowerCase();
let mayusculas = miString5.toUpperCase();
console.log(minusculas);
console.log(mayusculas);

//-Eliminación de espacios al principio y al final-
let miString6 = " Frase con espacios antes y despues ";
console.log("***" + miString6 + "***");
console.log("***" + miString6.trim() + "***");
console.log("***" + miString6.trimStart() + "***");
console.log("***" + miString6.trimEnd() + "***");

//-Inerpolacion-
let num1 = 23;
let num2 = 12;
console.log(`${num1} y ${num2} suman ${num1 + num2}`);

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * Se puede leer en ambos sentidos
 * - Anagramas
 * Palabras que comparten las mismas letras pero en diferente orden
 * - Isogramas
 * Palabras sin letras repetidas
 */
const analizaEstasPalabras = (a = 'Roma', b = 'Amor') => {
    console.log('------PALINDROMA------');
    function palindromo(palabra) {
        let palabraInvertida = palabra.toLowerCase().split("").reverse().join("");
        if (palabra.toLowerCase() === palabraInvertida) {
            console.log(`${palabra} es palindroma`);
        } else {
            console.log(`${palabra} no es palindorma`);
        }
    }
    palindromo(a);
    palindromo(b);

    console.log('------ANAGRAMA------');
    function anagrama(palabra1, palabra2) {
        const arr1 = palabra1.toLowerCase().split('').sort().join('');
        const arr2 = palabra2.toLowerCase().split('').sort().join('');
        if (arr1 === arr2) {
            console.log(`${palabra1} es un anagrama de ${palabra2}`);
        } else {
            console.log(`${palabra1} no es un anagrama de ${palabra2}`);
        }
    };

    anagrama(a, b);

    console.log('------ISOGRAMA------');
    function isograma(palabra) {
        const array = palabra.toLowerCase().split('');
        const set = new Set(array);
        if (array.length === set.size) {
            console.log(`${palabra} es un isograma`);
        } else {
            console.log(`${palabra} no es un isograma`);
        }
    };

    isograma(a);
    isograma(b);
};

analizaEstasPalabras();
analizaEstasPalabras('Radar', 'Paloma');
