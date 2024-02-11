//Cadenas literales

const miNombre = "Ángel Nárvaez";
console.log(miNombre);

//Cadena objeto

const thirdRockFromTheSun = new String("Tierra");
console.log(thirdRockFromTheSun);

//Acceso a un caracter específico

console.log(miNombre.charAt(6));
console.log(thirdRockFromTheSun[2]);

//Subcadenas

console.log(miNombre.substring(0, 6));

//Longitud de cadenas

console.log(miNombre.length);

//Concatenar

let saludo = "Hola ";
console.log(saludo + miNombre);

//Repetición

console.log(saludo.repeat(3) + thirdRockFromTheSun);

//Conversión a mayusculas

console.log(miNombre.toUpperCase());

//Conversión a minusculas

console.log(thirdRockFromTheSun.toLowerCase());

//Recorrido

let miNombreMinu = miNombre.toLocaleLowerCase();
for (let i = 0; i < miNombreMinu.length; i++) {
  console.log(miNombreMinu[i]);
}

//Reemplazo

console.log(miNombre.replace("Ángel", "Lcdo."));

//Dividir cadenas

let str = "Hola programadores de la ruta de programación 2024.";

let palabrasStr = str.split(" ");
console.log(palabrasStr);

//Unir cadenas

let unionDeStr = str.concat(" Mi nombre es ", miNombre);
console.log(unionDeStr);

//Interpolación

let saludo_interpolado = `${str} Bienvenidos, esta es mi solución al reto #04. Mi nombre es ${miNombre}`;
console.log(saludo_interpolado);

//Verificación

console.log(saludo_interpolado.includes(miNombre));//El método includes() es case sensible.

//Dificultad extra

function esPalindromo(txt1) {
  let str1 = txt1.split("").reverse().join("");
  return (txt1 === str1);
}

console.log(esPalindromo("anilina"));

function esAnagrama(txt1, txt2) {
  let word1 = txt1.split("").sort();
  let word2 = txt2.split("").sort();
  for (let i = 0; i < word1.length; i++) {
    if (word1[i] !== word2[i]) {
      return false;
    }
  }
  return true;
}

console.log(esAnagrama("letras", "lastre"));

function contarLetras(txt) {
  let textoSinNumerosNiSignos = txt.replace(/\d+\D/, "").toLowerCase();
  let textoSinAcento = textoSinNumerosNiSignos.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  let letras = {};
  for (let i = 0; i < textoSinAcento.length; i++) {
    letras[textoSinAcento[i]] = (letras[textoSinAcento[i]] || 0) + 1;
  }
  return letras;
}

function esIsograma(txt) {
  let palabra = contarLetras(txt);
  let contador = 0;
  for (const key in palabra) {
    if (contador === 0) {
      contador = palabra[key];
    }
    if (contador !== palabra[key]) {
      return false;
    }
  }
  return true;
}

console.log(esIsograma("murciélago"));