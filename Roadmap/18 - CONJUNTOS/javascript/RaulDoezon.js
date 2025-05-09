/*
  EJERCICIO:
  Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
  operaciones (debes utilizar una estructura que las soporte):
  - Añade un elemento al final.
  - Añade un elemento al principio.
  - Añade varios elementos en bloque al final.
  - Añade varios elementos en bloque en una posición concreta.
  - Elimina un elemento en una posición concreta.
  - Actualiza el valor de un elemento en una posición concreta.
  - Comprueba si un elemento está en un conjunto.
  - Elimina todo el contenido del conjunto.
*/

const marvelCharacters = ["Spider-Man", "Hawkeye", "Hulk"];
console.log('Arreglo inicial:', marvelCharacters);
marvelCharacters.push("Captain America");
console.log("Se agregó un elemento al final:", marvelCharacters);
marvelCharacters.unshift("Firestar");
console.log('Se agregó un elemento al principio:', marvelCharacters);
marvelCharacters.push("Iron Man", "Ant-Man");
console.log("Se agregaron varios elementos al final", marvelCharacters);
marvelCharacters.splice(5, 0, "Wolverine", "Thor");
console.log('Se agregaron 3 elementos en el índice 5:', marvelCharacters);
marvelCharacters.splice(6, 1);
console.log("Se eliminó el elemento del índice 6:", marvelCharacters);
marvelCharacters.splice(2, 1, "Iceman");
console.log("Se actualizó el elemento del índice 2:", marvelCharacters);
console.log("Se comprueba si existe el elemento Spider-Man:", marvelCharacters.includes("Spider-Man"));
marvelCharacters.splice(0, marvelCharacters.length);
console.log("Todo el contenido del arreglo se eliminó:", marvelCharacters);

/*
  DIFICULTAD EXTRA (opcional):
  Muestra ejemplos de las siguientes operaciones con conjuntos:
  - Unión.
  - Intersección.
  - Diferencia.
  - Diferencia simétrica.
*/

console.log("\n+++++++++ CONJUNTOS +++++++++");

let bountyHunters1 = new Set(["Gandrayda", "Samus", "Weavel", "Kanden", "Spire", "Noxus"]);
let bountyHunters2 = new Set(["Rundas", "Ghor", "Kanden", "Spire", "Gandrayda", "Sylux"]);
console.log(bountyHunters1);
console.log(bountyHunters2);

console.log("\nUNIÓN");
let union = new Set([...bountyHunters1, ...bountyHunters2]);
console.log(union);

console.log("\nINTERSECCIÓN");
let intersection = new Set([...bountyHunters1].filter((equal) => bountyHunters2.has(equal)));
console.log(intersection);

console.log("\nDIFERENCIA");
let difference1 = new Set([...bountyHunters1].filter((different1) => !bountyHunters2.has(different1)));
let difference2 = new Set([...bountyHunters2].filter((difference2) => !bountyHunters1.has(difference2)));

console.log("Diferencia del Conjunto 1", difference1);
console.log("Diferencia del Conjunto 2", difference2);


console.log("\nDIFERENCIA SIMÉTRICA");
let symmetricDifference = new Set([...union].filter((symmetric) => !intersection.has(symmetric)));
console.log(symmetricDifference);
