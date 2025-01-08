// EJERCICIO 

// Concatenación de cadenas
let name = "César";
let surname = "Carmona";

let fullname = name + " " + surname;
console.log("Nombre: ", fullname);

// Interpolación
console.log(`Soy ${name} ${surname}`);

// Acceso a caracteres específicos
let language = "JavaScript";
console.log("El lenguaje en que estás programando es: ", language[0], language[4]);
console.log("Primer caracter: ", language.charAt(0));

// Subcadena
let substring = language.substring(0, 3);
console.log("Subcadena:", substring);

// Longitud de cadena
console.log("Longitud de la cadena:", language.length);


// Repetición
let languageRepeat = language.repeat(3);
console.log("Cadena repetida:", languageRepeat);

// Recorrido 
for (let i = 0; i < language.length; i++) {
    console.log("Carácter en posición", i, ":", language[i]);
}

// Conversión a mayúsculas y minúsculas
console.log("Mayúsculas:", language.toUpperCase());
console.log("Minúsculas:", language.toLowerCase());

// Reemplazo
let newlanguage = language.replace("Java", "Python");
console.log("Reemplazo:", newlanguage);

// División
let string = "¡Hola Mundo!"
let words = string.split(" ");
console.log("División por espacio:", words);

// Unión
let newString = words.join("-");
console.log("Unión con guiones:", newString);

// Verificación
let contains = string.includes("Hola");
console.log("Contiene 'Hola': ", contains);

// Dificultad extra

function check(cadena1, cadena2) {
    function palindrome(cadena1, cadena2) {
        return cadena1.toLowerCase() === cadena2.split("").reverse().join("").toLowerCase();
    }
    console.log("Es palíndromo:", palindrome(cadena1, cadena2));

    function anagram(cadena1, cadena2) {
        return cadena1.toLowerCase().split("").sort().join("") === cadena2.toLowerCase().split("").sort().join("")
    }
    console.log("Es anagrama:", anagram(cadena1, cadena2));

    function isogram(cadena1, cadena2) {
        let caracteres = {};

        for (let i = 0; i < cadena1.length; i++) {
            if (caracteres[cadena1[i].toLowerCase()]) {
                return false;
            }
            caracteres[cadena1[i]] = true;
        }

        for (let i = 0; i < cadena2.length; i++) {
            if (caracteres[cadena2[i].toLowerCase()]) {
                return false;
            }
            caracteres[cadena2[i]] = true;
        }

        return true;
    }
    console.log("Es isograma:", isogram(cadena1, cadena2));
}


check("radar", "pythonpythonpythonpythonpython");
check("amor", "roma");