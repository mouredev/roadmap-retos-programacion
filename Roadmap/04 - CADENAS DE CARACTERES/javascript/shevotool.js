// #04 CADENAS DE CARACTERES

/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 */

// length
const lenguaje = "javaScript";
const longitudCadena = lenguaje.length;
console.log(longitudCadena);

//concatenar
const nombre = "Erick";
const apellido = "Alphonse";
console.log(nombre + " " + apellido);

//indexOf()
const secondIndex = apellido.indexOf("l", 0);
console.log(secondIndex);

//substring()
const textoRandom =
  "Vive la vida y no que la vida te viva es lo que dice mi jefe";
const extraerFrase = textoRandom.substring(0, 37);
console.log(extraerFrase);

// cadenas primitivas
const string1 = "Houston tenemos un problema";
console.log(string1);

const string2 = `Confirmado, cambio`;
console.log(string2);

const string3 = new String("Hasta la vista baby");
console.log(string3);

// interpolación
const cualidad = "inteligente";
console.log(`Mi perro lulu es muy ${cualidad}!`);

// Acceder a un caracter, existen dos formas

// charAt()
const gato = "cat";
console.log(gato.charAt(1));

//  tratar a la cadena como un objeto similar a un arreglo
console.log(gato[1]);

// Comparar cadenas con los operadores menor que y mayor que:
const numero1 = 20;
const numero2 = 10;

if (numero1 > numero2) {
  console.log(`${numero1} es mayor que ${numero2}`);
} else if (numero1 < numero2) {
  console.log(`${numero2} es mayor que ${numero1}`);
} else {
  console.log(`${numero1} y ${numero2} son iguales`);
}

// localeCompare()
console.log("a".localeCompare("c"));
console.log("check".localeCompare("against"));
console.log("look".localeCompare("foward"));
console.log("2".localeCompare("10"));

//Ordenar un arreglo con localeCompare()
let items = ["réservé", "Premier", "Cliché", "communiqué", "café", "Adieu"];
items.sort((a, b) => a.localeCompare(b, "fr", { ignorePunctuation: true }));
console.log(items);

// comparar
function isEqual(a, b) {
  return a.toUpperCase() === b.toUpperCase();
}
console.log(isEqual("PerRo", "perro"));

// JavaScript automáticamente convierte las primitivas en objetos String
let s_prim = "foo";
let s_obj = new String(s_prim);
console.log(typeof s_prim);
console.log(typeof s_obj);

// eval()
let s1 = "2 + 2";
let s2 = new String("2 + 2");
console.log(eval(s1));
console.log(eval(s2));

// valueOf()
console.log(s1.valueOf());
console.log(s2.valueOf());

// agregar varias cadenas juntas
let longString =
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit." +
  " Ut enim ad minim veniam, quis nostrud exercitation." +
  " Duis aute irure dolor in reprehenderit in voluptate.";
console.log(longString);

let longString2 =
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
   Ut enim ad minim veniam, quis nostrud exercitation.Duis\
    aute irure dolor in reprehenderit in voluptate.";
console.log(longString2);

// String() constructor

//String constructor and String function
//String function and String constructor produce different results:

const a = new String("Hello world"); // a === "Hello world" is false
const b = String("Hello world"); // b === "Hello world" is true
console.log(a instanceof String);
console.log(b instanceof String);
console.log(typeof a);
console.log(typeof b);

// Métodos estáticos

// String.fromCharCode()
console.log(String.fromCharCode(65, 66, 67, 68));

// String.fromCodePoint()
console.log(String.fromCodePoint(42));
//console.log(String.fromCodePoint(NaN));

// String.raw()
console.log("с:\u005c.js");
console.log(String.raw`с:\u.js`);

// Propiedades de la instancia

//String.length;
let lenguaje2 = "Python";
console.log(lenguaje2.length);

// charAt()
const lenguaje3 = "Rust";
console.log(lenguaje3.charAt(3));

// charCodeAt()
const lenguaje4 = "Java";
console.log(lenguaje4.charCodeAt(1));

// codePointAt()
const lenguaje5 = "Kobol";
console.log(lenguaje4.codePointAt(1));

// concat();
const saludar = "Hola ";
const individuo = "forastero";
console.log(saludar.concat(individuo));

// endsWith()
const texto2 = "vive la vida loca";
console.log(texto2.endsWith("loca"));

// includes()
const texto3 = "vive la vida loca";
console.log(texto3.includes("la"));

// indexOf()
console.log("Blue Whale".indexOf("Whale", 5));

// lastIndexOf()
const parrafo = "I think Ruth's dog is cuter than your dog!";
const mascota = "dog";

console.log(`Index of the last ${mascota} is ${parrafo.lastIndexOf(mascota)}`);

// localeCompare()
const a1 = "réservé";
const b2 = "RESERVE";
console.log(a1.localeCompare(b2));

// match()
const parrafo2 = "The quick brown fox jumps over the lazy dog. It barked.";
const regex = /[A-Z]/g;
const encontrado = parrafo2.match(regex);
console.log(encontrado);

// matchAll();
const regexexp = /t(e)(st(\d?))/g;
const str = "test1test2";
const array = [...str.matchAll(regexexp)];
console.log(array[0]);
console.log(array[1]);

// padEnd()
const str3 = "Hola";
console.log(str3.padEnd(25, "."));

// padStart()
const str4 = "Hola";
console.log(str4.padStart(25, "."));

// repeat()
const saludo = "Hola! ";
console.log(saludo.repeat(3));

// replace();
const parrafo1 =
  "¡Creo que el perro de Ruth es más bonito que el perro de Jose!";
console.log(parrafo1.replace(/Ruth/gi, "Pedro"));

// replaceAll();
const parrafo3 =
  "¡Creo que el perro de Ruth es más bonito que el perro de Jose!";
console.log(parrafo3.replaceAll(/perro/gi, "conejo"));

// search();
const parrafo4 =
  "¡Creo que el perro de Ruth es más bonito que el perro de Jose!";
const regex3 = /[^\w\s']/g;
console.log(parrafo4.search(regex3));
console.log(parrafo4[parrafo4.search(regex)]);

// slice();
const str5 = "El rápido zorro marrón salta sobre el perro perezoso.";
console.log(str5.slice(44));
console.log(str5.slice(10, 22));

// split();
const str6 = "El rápido zorro marrón salta sobre el perro perezoso.";
const palabras = str6.split(" ");
console.log(palabras[2]);

// startsWith();
const str7 = "Planes de sabado por la noche";
console.log(str7.startsWith("Pla"));

// substring()
const str8 = "Mozilla";
console.log(str8.substring(2, 7));

// toLowerCase()
const str9 = "Planes de sabado por la noche con Dios";
console.log(str9.toLowerCase());

// toString()
const strObj = new String("foo");
console.log(typeof strObj);
console.log(strObj.toString());

// toUpperCase()
const str10 = "Planes de sabado por la noche con Dios";
console.log(str10.toUpperCase());

// trim()

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

const palabra1 = "Pensar";
const palabra2 = "Correr";
const palabra3 = "radar";
const palabra4 = "amor";
const palabra5 = "Roma";

function palindromo(palabra1, palabra2) {
  return (
    palabra1.toLowerCase().split("").reverse().join("") ===
    palabra2.toLowerCase()
  );
}

console.log(palindromo(palabra3, palabra3));
console.log(palindromo(palabra1, palabra2));

function anagrama(palabra1, palabra2) {
  return (
    palabra1.toLowerCase().split("").sort().join("") ===
    palabra2.toLowerCase().split("").sort().join("")
  );
}

console.log(anagrama(palabra4, palabra5));

function isogramas(palabra1) {
  let palabra = [];
  for (let i = 0; i < palabra1.length; i++) {
    if (palabra.includes(palabra1[i])) {
      return true;
    } else {
      palabra.push(palabra1[i]);
    }
  }
  return false;
}

console.log(isogramas(palabra1));
console.log(isogramas(palabra2));
