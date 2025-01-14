// Creamos un array vacío para representar nuestro conjunto de datos
let conjunto = ["elemento"];
console.log("Conjunto inicial:", conjunto);

// Añadir un elemento al final
conjunto.push("elemento_final");
console.log("Conjunto después de añadir un elemento al final:", conjunto);

// Añadir un elemento al principio
conjunto.unshift("elemento_inicio");
console.log("Conjunto después de añadir un elemento al principio:", conjunto);

// Añadir varios elementos en bloque al final
conjunto.push("elemento1", "elemento2", "elemento3");
console.log(
  "Conjunto después de añadir varios elementos en bloque al final:",
  conjunto
);

// Añadir varios elementos en bloque en una posición concreta
conjunto.splice(2, 0, "bloque_elemento1", "bloque_elemento2");
console.log(
  "Conjunto después de añadir varios elementos en bloque en una posición concreta:",
  conjunto
);

// Eliminar un elemento en una posición concreta
conjunto.splice(3, 1); // Eliminamos el elemento en la posición 3
console.log(
  "Conjunto después de eliminar un elemento en una posición concreta:",
  conjunto
);

// Actualizar el valor de un elemento en una posición concreta
conjunto[1] = "nuevo_valor_elemento";
console.log(
  "Conjunto después de actualizar el valor de un elemento en una posición concreta:",
  conjunto
);

// Comprobar si un elemento está en un conjunto
let elementoBuscado = "elemento1";
let estaEnConjunto = conjunto.includes(elementoBuscado);
console.log(
  `¿El elemento "${elementoBuscado}" está en el conjunto? ${estaEnConjunto}`
);

// Eliminar todo el contenido del conjunto
conjunto = []; // Asignamos un array vacío para vaciar el conjunto
console.log("Conjunto después de eliminar todo su contenido:", conjunto);

// Ejercicio extra

// Conjuntos de ejemplo
let conjunto1 = new Set([1, 2, 3, 4, 5]);
let conjunto2 = new Set([4, 5, 6, 7, 8]);
console.log("Conjunto 1:", conjunto1);
console.log("Conjunto 2:", conjunto2);

// Unión
let union = new Set([...conjunto1, ...conjunto2]);
console.log("Unión de los conjuntos:", union);

// Intersección
let interseccion = new Set([...conjunto1].filter((x) => conjunto2.has(x)));
console.log("Intersección de los conjuntos:", interseccion);

// Diferencia
let diferencia1 = new Set([...conjunto1].filter((x) => !conjunto2.has(x)));
let diferencia2 = new Set([...conjunto2].filter((x) => !conjunto1.has(x)));
console.log("Diferencia entre conjunto1 y conjunto2:", diferencia1);
console.log("Diferencia entre conjunto2 y conjunto1:", diferencia2);

// Diferencia simétrica
let diferenciaSimetrica = new Set(
  [...conjunto1]
    .filter((x) => !conjunto2.has(x))
    .concat([...conjunto2].filter((x) => !conjunto1.has(x)))
);
console.log("Diferencia simétrica entre los conjuntos:", diferenciaSimetrica);
