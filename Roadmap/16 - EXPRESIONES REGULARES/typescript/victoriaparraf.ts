/*se definen utilizando dos barras inclinadas (/pattern/) o el constructor RegExp. */
let regex = /abc/;
const regexConstructor = new RegExp('abc');

//Busqueda en una cadena
const regular = /hello/;
let str = "hello world";
console.log(regular.test(str)); // true

//Busqueda con más opciones
const exp = /h.llo/;
const cadena = "hello world";
console.log(exp.test(cadena)); // true (coincide con "hello" y "hallo")

//Reemplazo de una cadena
regex = /world/;
str = "hello world";
const newStr = str.replace(regex, "TypeScript");
console.log(newStr); // hello TypeScript

//Extraccion de coincidencias
regex = /\d+/;
str = "There are 123 apples";
const match = str.match(regex);
console.log(match); // ["123"]

//division de una cadena
regex = /\s+/;
str = "Split this string into words";
const words = str.split(regex);
console.log(words); // ["Split", "this", "string", "into", "words"]

//buscar y extraer numeros de una cadena
const text = "En el año 2024, hubo 300 eventos importantes y 12 conferencias.";
const numberRegex = /\d+/g;
const numbers = text.match(numberRegex);

if (numbers) {
    console.log(numbers); // ["2024", "300", "12"]
} else {
    console.log("No se encontraron números.");
}

/*EXTRAAAAAAA*/

const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
const email = "test@example.com";
console.log(emailRegex.test(email)); // true

const urlRegex = /^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*\/?$/;
const url = "https://www.example.com";
console.log(urlRegex.test(url)); // true

const phoneRegex = /^\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$/;
const phoneNumber = "+1-800-555-1234";
console.log(phoneRegex.test(phoneNumber)); // true


