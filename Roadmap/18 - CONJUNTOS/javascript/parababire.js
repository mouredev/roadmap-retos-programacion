let fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.push("Kiwi"); // Añadir un elemento al final.
fruits.unshift("Pear"); // Añadir un elemento al principio.
fruits.push("Lemon", "Grape"); // Añade varios elementos en bloque al final.
fruits.splice(6, 0, "Strawberry", "Blueberry"); // Añadir varios elementos en bloque en una posición concreta.
fruits.splice(5, 1); // Elimina un elemento en una posición concreta.
fruits[5] = "Kiwi"; // Actualiza el valor de un elemento en una posición concreta.
fruits.includes("Strawberry"); // Comprueba si un elemento está en un conjunto.
fruits.splice(0, fruits.length); // Elimina todo el contenido del conjunto.
console.log(fruits);

// Extra

/* Union: A U B */

let arr1 = [1, 2, 3, 4];
let arr2 = [3, 4, 5];

function union(a, b) {
  const result = [];

  for (const item of a) {
    if (!result.includes(item)) {
      result.push(item);
    }
  }
  for (const item of b) {
    if (!result.includes(item)) {
      result.push(item);
    }
  }
  return result;
}

console.log(union(arr1, arr2));

/* Intersección: A ∩ B */

let arr3 = [1, 2, 3, 4, 5];
let arr4 = [1, 6, 3, 7, 5];

console.log(arr3.filter(data => arr4.includes(data)));

/* Diferencia: A \ B */

function diferencia(a, b) {
  let result = [];
  for (const item of a) {
    if (!b.includes(item)) {
      result.push(item);
    }
  }
  return result;
}

console.log(diferencia(arr3, arr4));

/* Diferencia asimétrica : A Δ B */

function diferenciaAsimetrica(a, b) {
  let result = [];
  for (const item of a) {
    if (!b.includes(item)) {
      result.push(item);
    }
  }
  for (const item of b) {
    if (!a.includes(item)) {
      result.push(item);
    }
  }
  return result;
}

console.log(diferenciaAsimetrica(arr3, arr4));