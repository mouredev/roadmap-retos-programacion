//EJERCICIO
const elements = [1, 2, 3, 4];
console.log('\nElemento original: ', elements);

elements.push(5);
console.log('\nAñadiendo un elemento al final: ', elements);

elements.unshift(0);
console.log('\nAñadiendo un elemento al principio: ', elements);

let newElements = [6, 7, 8];
elements.push(...newElements);
console.log('\nAñadiendo varios elementos en bloque al final: ', elements);

newElements = [-3, -2, -1];
elements.unshift(...newElements);
console.log('\nAñadiendo varios elementos en bloque al principio: ', elements);

elements.splice(7, 1);
console.log('\nEliminando un elemento en una posición concreta: ', elements);

elements[5] = 34;
console.log('\nActualizando un elemento en una posición concreta: ', elements);

console.log(
	`\nComprobando si un elemento está en el conjunto: ${elements.includes(12)}`
);
console.log(
	`\nComprobando si un elemento está en el conjunto: ${elements.includes(8)}`
);

elements.length = 0;
console.log('\nEliminando todos los elementos: ', elements);

//EXTRA
const letters1 = new Set(['a', 'b', 'c']);
const letters2 = new Set(['b', 'd', 'e', 'f']);

const united = new Set([...letters1, ...letters2]);
console.log('\nUnión:', united);

const intersection = new Set(
	[...letters1].filter((element) => letters2.has(element))
);
console.log('\nIntersección:', intersection);

const diference1 = new Set(
	[...letters1].filter((element) => !letters2.has(element))
);
console.log('\nDiferencia:', diference1);

const diference2 = new Set(
	[...letters2].filter((element) => !letters1.has(element))
);
console.log('\nDiferencia:', diference2);

console.log('\nDiferencia simétrica:', new Set([...diference1, ...diference2]));
