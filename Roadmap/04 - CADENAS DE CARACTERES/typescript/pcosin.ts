// Operaciones a realizar con cadena de caracteres

// Concatenación:

const str1: string = "Hola";
const str2: string = "mundo";

const concatenado: string = str1 + " " + str2;

const cantenadoConcat: string = str1.concat(" ", str2);

console.log(concatenado, cantenadoConcat);

// Longitud de la cadena

const lengthStr: number = str1.length;

console.log(lengthStr);

// Acceso a la cadena con corchetes

const primerCaracter: string = str1[0];

console.log(primerCaracter);

// Subcadenas

const subCadena: string = str1.substring(0, 2);

console.log(subCadena);

// Búsqueda de subcadenas con indexOf e includes

const indexCadena: number = str2.indexOf("m");
const includesInCadena: boolean = str2.includes("l");

console.log(indexCadena, includesInCadena);

// Recorta una parte del string

const parte = str2.slice(-1);

console.log(parte)

//Mayúsculas y minúsculas

const mayusculas = str1.toUpperCase();
const minusculas = str2.toLowerCase();

console.log(mayusculas, minusculas);

// Reemplazo

const reemplazo: string = str1.replace("H", "P");

console.log(reemplazo);

// Dividir una cadena

const cadenas: string = "Holas mundos";

const dividirCadena: string[] = cadenas.split(" ");

console.log(dividirCadena);

//Unir cadenas

const unir: string = dividirCadena.join(" ");

console.log(unir);

// Fin y principio de cadena

const terminaCon: boolean = str1.endsWith("K");
const empiezaCon: boolean = str1.startsWith("H");

console.log(terminaCon);
console.log(empiezaCon);



// Extra

import * as readlineSync from "readline-sync";

function esUnPalindromo(): void {
  const str: string = readlineSync.question(
    "Ingrese la palabra a comprobar si es un palíndromo: "
  );

  const comprobacion: string = str.split("").reverse().join("");

  str === comprobacion
    ? console.log(`La palabra ${str} es un palíndromo`)
    : console.log(`La palabra ${str} no es un palíndromo`);
}

function esUnAnagrama(): void {
  const str1: string = readlineSync.question(
    "Ingrese la primera palabra a comprobar si es un anagrama: "
  );

  const str2: string = readlineSync.question(
    "Ingrese la segunda palabra a comprobar si es un anagrama: "
  );

  const str1Comprobacion: string = str1.split("").sort().join("");
  const str2Comprobacion: string = str2.split("").sort().join("");

  str1Comprobacion === str2Comprobacion
    ? console.log(`Las palabras ${str1} y ${str2} son anagramas`)
    : console.log(`Las palabras ${str1} y ${str2} NO son anagramas`);
}

function esUnIsograma(): void {
  const str: string = readlineSync.question(
    "Ingrese la palabra a comprobar si es un isograma: "
  );

  let comprobacion: string = "";
  let count: number = 0;
  for (let i = 0; i < str.length; i++) {
    if (!comprobacion.includes(str[i])) {
      comprobacion += str[i];
    } else {
      count++;
    }
  }

  count > 0
    ? console.log(`La palabra ${str} no es un isograma`)
    : console.log(`La palabra ${str} es un isograma`);
}

function main(): void {
  let bucle: boolean = true;
  while (bucle) {
    console.log("\n== Menú ==");
    console.log("1. ¿Es un palíndromo?");
    console.log("2. ¿Es una anagrama?");
    console.log("3. ¿Es un isograma?");
    console.log("4. Salir");

    const opcion = readlineSync.questionInt("Seleccione una opción: ");

    switch (opcion) {
      case 1:
        esUnPalindromo();
        break;
      case 2:
        esUnAnagrama();
        break;
      case 3:
        esUnIsograma();
        break;
      case 4:
        console.log("Saliendo de la aplicación. ¡Hasta luego!");
        bucle = false;
        break;
      default:
        console.log("Opción no válida. Inténtelo de nuevo.");
    }
  }
}

main();

