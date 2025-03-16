let data: number[] = [2, 3, 4];

// Añade un elemento al final
data.push(5);
console.log("Añade un elemento al final:", data); // [2, 3, 4, 5]

// Añade un elemento al principio
data.unshift(1);
console.log("Añade un elemento al principio:", data); // [1, 2, 3, 4, 5]

// Añade varios elementos en bloque al final
data.push(6, 7, 8);
console.log("Añade varios elementos en bloque al final:", data); // [1, 2, 3, 4, 5, 6, 7, 8]

// Añade varios elementos en bloque en una posición concreta
data.splice(4, 0, 9, 10);
console.log("Añade varios elementos en bloque en una posición concreta:", data); // [1, 2, 3, 4, 9, 10, 5, 6, 7, 8]

// Elimina un elemento en una posición concreta
data.splice(4, 1);
console.log("Elimina un elemento en una posición concreta:", data); // [1, 2, 3, 4, 10, 5, 6, 7, 8]

// Actualiza el valor de un elemento en una posición concreta
data[4] = 11;
console.log("Actualiza el valor de un elemento en una posición concreta:", data); // [1, 2, 3, 4, 11, 5, 6, 7, 8]

// Comprueba si un elemento está en un conjunto
let contains = data.includes(11);
console.log("Comprueba si un elemento está en un conjunto:", contains); // true

// Elimina todo el contenido del conjunto
data = [];
console.log("Elimina todo el contenido del conjunto:", data); // []

/**************/
const setA: Set<number> = new Set([1, 2, 3, 4, 5]);
const setB: Set<number> = new Set([4, 5, 6, 7, 8]);

// Unión
const union = new Set([...setA, ...setB]);
console.log("Unión:", union); // Set { 1, 2, 3, 4, 5, 6, 7, 8 }

// Intersección
const intersection = new Set([...setA].filter(x => setB.has(x)));
console.log("Intersección:", intersection); // Set { 4, 5 }

// Diferencia
const difference = new Set([...setA].filter(x => !setB.has(x)));
console.log("Diferencia:", difference); // Set { 1, 2, 3 }

// Diferencia Simétrica
const symmetricDifference = new Set([...setA].filter(x => !setB.has(x)).concat([...setB].filter(x => !setA.has(x))));
console.log("Diferencia Simétrica:", symmetricDifference); // Set { 1, 2, 3, 6, 7, 8 }

