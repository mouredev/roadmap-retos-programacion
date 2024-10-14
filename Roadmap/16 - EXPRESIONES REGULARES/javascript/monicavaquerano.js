// # 16 EXPRESIONES REGULARES
// # Monica Vaquerano
// # https://monicavaquerano.dev

/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */

// Regular Expresions

// Search Method
let text = "hola, mundo!";

// with a String
let x = text.search("mundo");
console.log(x);

// with a Regular Expression 
x = text.search(/mundo/i);
console.log(x);

x ? console.log("It's a match") : console.log("Not a match");

// Replace Method
text = "Visit Berlin!";

// with a String
x = text.replace("Berlin", "Stuttgart");
console.log(x);

// with a Regular Expression
x = text.replace(/Berlin/i, "Stuttgart");
console.log(x);

// test() Method
let pattern = /e/;
x = pattern.test("The best things in life are free!");
x ? console.log("El patrón existe en la string") : console.log("El patrón NO existe en la string")

// exec() Method
const obj = /e/.exec("The best things in life are free!");
console.log(obj)
console.log(`Found ${obj[0]} in position ${obj.index} in the text: ${obj.input}`)

// toString() Method
pattern = new RegExp("Hello World", "g");
text = pattern.toString();
console.log(text)

// match() Method
const findDigits = (txt) => {
    let pattern = /\d+/g;
    let digits = txt.match(pattern);
    return digits;
}

console.log(findDigits("The r4in in 5p4in"))

// Regular Expression Modifiers: Modifiers can be used to perform case-insensitive more global searches:
// Modifier	Description
// i        Perform case-insensitive matching	
// g        Perform a global match (find all)	
// m        Perform multiline matching	
// d        Perform start and end matching (New in ES2022)

// Extra

// E-Mail
const emailCheck = (email) => {
    let pattern = /^[\w.+-]+@[\w.+-]+\.[a-zA-Z]+$/g;
    let check = pattern.test(email);
    return check;
}
console.log("example@example.com es un email válido? =>", emailCheck("example@example.com")) // true
console.log("Ex.4-mpl3@exampl3.co es un email válido? =>", emailCheck("Ex.4-mpl3@exampl3.co")) // true
console.log("exampleexample.com es un email válido? =>", emailCheck("exampleexample.com")) // false
console.log("example!@example.c0m es un email válido? =>", emailCheck("example@example.c0m")) // false

// # Número de teléfono
function telephoneCheck(str) {
    let regex = /^(1\s?)?(\(\d{3}\)|\d{3})([\-\s])?(\d{3})([\-\s])?(\d{4})$/;
    let phoneCheck = regex.test(str)
    return phoneCheck;
}

console.log("555-555-5555 es un número válido? =>", telephoneCheck("555-555-5555")); // true
console.log("1 (555) 555-5555 es un número válido? =>", telephoneCheck("1 (555) 555-5555")); // true
console.log("5555555555 es un número válido? =>", telephoneCheck("5555555555")) // true
console.log("(555)555-5555 es un número válido? =>", telephoneCheck("(555)555-5555")) // true
console.log("5555555 es un número válido? =>", telephoneCheck("5555555")) // false
console.log("123**&!!asdf# es un número válido? =>", telephoneCheck("123**&!!asdf#")) // false
console.log("11 555-555-5555 es un número válido? =>", telephoneCheck("11 555-555-5555")) // false
console.log("1 555)555-5555 es un número válido? =>", telephoneCheck("1 555)555-5555")) // false
console.log("(6054756961) es un número válido? =>", telephoneCheck("(6054756961)")) // false
console.log("27576227382 es un número válido? =>", telephoneCheck("27576227382")) // false
console.log("(275)76227382 es un número válido? =>", telephoneCheck("(275)76227382")) //false

// # URL
const urlCheck = (url) => {
    let pattern = /(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?/g;
    let urlCheck = pattern.test(url);
    return urlCheck;
}

console.log("https://google.com/ es un url válido? =>", urlCheck("https://google.com/")) // true
console.log("http://google.com es un url válido? =>", urlCheck("http://google.com")) // true
console.log("https://www.google.com es un url válido? =>", urlCheck("https://www.google.com")) // true
console.log("www.google.com es un url válido? =>", urlCheck("www.google.com")) // true
console.log("google.com es un url válido? =>", urlCheck("google.com")) // true
console.log("google.c es un url válido? =>", urlCheck("google.c")) // false
console.log("goo/gle.c es un url válido? =>", urlCheck("goo/gle.c")) // false

//     pattern = r"^(http[s]?://)?(www.)?[\w]+\.[\w]{2,}[/]?$"