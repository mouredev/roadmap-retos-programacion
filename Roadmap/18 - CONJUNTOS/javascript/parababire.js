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

let verduras = ["Papa", "Apio", "Ocumo"];
let vegetales = ["Tomates", "Cebolla", "Zanahoria"];
let verdurasYVegetales = verduras.concat(vegetales);
console.log(verdurasYVegetales);