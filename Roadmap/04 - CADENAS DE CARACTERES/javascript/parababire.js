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

function check(word1, word2) {

  //Palindromo
  console.log(`Es ${word1} un palindromo?: ${word1 === word1.split("").reverse().join("")}`);
  console.log(`Es ${word2} un palindromo?: ${word2 === word2.split("").reverse().join("")}`);
  
  //Anagrama
  console.log(`Es ${word2} un anagrama de ${word1}?: ${word1.split("").sort().join("") === word2.split("").sort().join("")}`);

  //isograma
  function isograma(word) {
    let textoSinNumerosNiSignos = word.replace(/\d+\D/, "").toLowerCase();
    let textoSinAcento = textoSinNumerosNiSignos.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    let objLetras = {};
    for (const letras in textoSinAcento) {
      objLetras[textoSinAcento[letras]] = (objLetras[textoSinAcento[letras]] || 0) + 1;
    }
    let isograma = true;
    let values = Object.values(objLetras);
    let isogramaLen = values[0];
    for (let wordCount of values) {
      if (wordCount !== isogramaLen) {
        isograma = false;
      }
    }
    return isograma;
  }
  console.log(`Es ${word1} un isograma?: ${isograma(word1)}`);
  console.log(`Es ${word2} un isograma?: ${isograma(word2)}`);
}

check("caso", "saco");