// DATA STRUCTURES

// ARRAYS
const fruitsArr = ["Banana", "Pear", "Apple", "Apricot", "Banana"];
console.log("Fruits:", fruitsArr, "\n");

console.log("Array length:", fruitsArr.length);

// Acceder a las posiciones de un Array
console.log("fruitsArr[2] =>", fruitsArr[2]);
console.log("fruitsArr[3] =>", fruitsArr[3]);

console.log("\nMétodos de los Arrays:")


// Push -- Añadir (Modifica el array original)
fruitsArr.push(['Pear', 'Apple']);
console.log("- Push =>", fruitsArr);

// Filter
const bananasArr = fruitsArr.filter((fruit) => fruit === "Banana");
console.log("- Filter =>", bananasArr);

// Find
const foundFruit = fruitsArr.find((fruit) => fruit.startsWith("Apr"));
console.log("- Find =>", foundFruit);

// Reverse
console.log("- Reverse =>", fruitsArr.reverse());

// Flat
console.log("- Flat =>", fruitsArr.flat());

