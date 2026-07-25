//! operaciones con cadenas
function mayuscula_minusculas(text) {
  //? transformar toda la cadena a mayuscula, toUpperCase()
  console.log("\n texto en mayusculas toUpperCase() \n");
  console.log(
    `texto normal: ${text} \ntexto en mayusculas: `,
    text.toUpperCase()
  );

  //? transformar toda la cadena en minuscula, toLowerCase()
  console.log("\n texto en minusculas toLowerCase() \n");
  console.log(
    `texto normal: ${text} \ntexto en mayusculas: `,
    text.toLowerCase()
  );
}

function f_charAt(text) {
  //? devolver un caracter de la cadena, con la posicion, con charAt()
  console.log("\n caracer de una cadena , charAt() \n");
  let c = 0;
  console.log(`el caracter ${c} es : ${text.charAt(c)}`);
  console.log(`el caracter ${c + 1} es : ${text.charAt(c + 1)}`);
}

function f_indexOf(text) {
  //? idexOf()
  //* El método indexOf() retorna el primer índice en el que se puede encontrar un elemento
  //* dado en el array, ó retorna - 1 si el elemento no esta presente.
  //* devuelve la paosicion donde se encuentre el primer incice
  console.log("\n indexOf \n");
  console.log(text);
  console.log(`indexOf: l es:  ${text.indexOf("l")}`);
  console.log(`indexOf: todos : ${text.indexOf("todos")}`);
  //* se puede indicar desde que posicion comenzar a buscar
  //* en ejemplo para imprimir los nombres de las personas que empiecen por la letra A
  let personas = ["Ana", "Juan", "Marcos", "Armando", "Miguel", "Amelia"];
  for (let iterador in personas) {
    if (personas[iterador].indexOf("A") == 0) {
      console.log(personas[iterador]);
    }
  }
}

function f_lastIndexOf(text) {
  console.log("\n ultima coicidencia lastIndexOf()\n");
  //? lastIndexOf(), es igual a indexOf, solo que este, en vez de enviar la posicion de la primira coincidencia
  //* devuelve la posicionde la última coincidenta, si no la encontró devuelve -1
  console.log(text);
  console.log(
    `devolver el indice de la ultima coincidencia: ${text.lastIndexOf("o")}`
  );
}

function f_replace(text) {
  console.log("\n replace()\n");
  //? replace(),
  //* devuelve una nueva cadena con los cambios realizados
  console.log(text);
  console.log(text.replace("todos", "muchos"));
}
function opereacionesConCadenas() {
  let text = "Hola a todos";

  mayuscula_minusculas(text);
  f_charAt(text);
  f_indexOf(text);
  f_lastIndexOf(text);
  f_replace(text);
  console.log(`\n ----------------tamaño de el espacio----------\n`);
  console.log(`tamaño: ${text.length}`);
  console.log("\n ------ conectar cadenas de caracteres-----------\n");
  console.log(`cadena unida: ${text + " mucho gusto"}`);
  console.log("\n ----- extraer cadnas ---------------");
  //* subsctring(), extrae subcadenas, develve la cadenas extraidas desde los indices firstIn y lastOut-1
  console.log(
    `extrayedo desde la poisicon 2 hasta la 5: ${text.substring(2, 5)}`
  );
  console.log(`esxtrayendo todo desde la posicion 7: ${text.substring(7)}`);
}

opereacionesConCadenas();

//! Ejercicio extra

const redline = require("readline");
const rl = redline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const ask = (texto) => {
  return new Promise((resolve) => rl.question(texto, resolve));
};
const palindromo = (palabra) => {
  let copia = palabra.split("").reverse().join("");
  return palabra === copia;
};

const anagrama = (palabra1, palabra2) => {
  if (palabra1.length !== palabra2.length) {
    return false;
  }
  palabra1 = palabra1.split("").sort().join("");
  palabra2 = palabra2.split("").sort().join("");

  return palabra1 == palabra2;
};

const isograma = (palabra) => {
  for (let i = 0; i < palabra.length - 1; i++) {
    for (let j = i + 1; j < palabra.length; j++) {
      if (palabra[i] == palabra[j]) {
        return false;
      }
    }
  }
  return true;
};
async function ejercicioExtra() {
  const rejex = /\s+/g;
  let respuesta1, respuesta2, respuesta3;
  let palabra1 = await ask("ingresa la primera palabra: ");
  let palabra2 = await ask("ingresa la segunda palabar: ");
  let comprimido1 = palabra1.replace(rejex, "").toLowerCase();
  let comprimido2 = palabra2.replace(rejex, "").toLowerCase();
  respuesta1 = palindromo(comprimido1);
  respuesta2 = palindromo(comprimido2);
  console.log("\n");
  if (respuesta1) {
    console.log(`la palabra: ${palabra1} es un palindromo`);
  } else {
    respuesta1 = isograma(comprimido1);
    if (respuesta1) {
      console.log(`la palabra: ${palabra1} es un isograma`);
    }
  }

  if (respuesta2) {
    console.log(`la palabra: ${palabra2} es un palindromo`);
  } else {
    respuesta2 = isograma(comprimido2);
    if (respuesta2) {
      console.log(`la palabra: ${palabra2} es un isograma`);
    }
  }
  respuesta3 = anagrama(comprimido1, comprimido2);
  if (respuesta3) {
    console.log("\n");
    console.log(
      `las palabras: ${palabra1} y ${palabra2} conforman un anagrama`
    );
  }

  rl.close();
}

ejercicioExtra();
