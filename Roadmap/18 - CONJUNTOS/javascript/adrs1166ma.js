/* 🔥 EJERCICIO:
Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
operaciones (debes utilizar una estructura que las soporte):
- 1. Añade un elemento al final.
- 2. Añade un elemento al principio.
- 3. Añade varios elementos en bloque al final.
- 4. Añade varios elementos en bloque en una posición concreta.
- 5. Elimina un elemento en una posición concreta.
- 6. Actualiza el valor de un elemento en una posición concreta.
- 7. Comprueba si un elemento está en un conjunto.
- 8. Elimina todo el contenido del conjunto.
*/
let conjunto = [1, 2, 3, 4, 5];
console.log("Conjunto inicial:", conjunto);

// 1. Añade un elemento al final.
conjunto.push(6);
console.log("Añadir un elemento al final:", conjunto);

// 2. Añade un elemento al principio.
conjunto.unshift(0);
console.log("Añadir un elemento al principio:", conjunto);

// 3. Añade varios elementos en bloque al final.
conjunto.push(7, 8, 9);
console.log("Añadir varios elementos en bloque al final:", conjunto);

// 4. Añade varios elementos en bloque en una posición concreta
const nuevosElementos = [10, 11];
const posicion = 3; // Posición donde insertar los nuevos elementos
conjunto.splice(posicion, 0, ...nuevosElementos);
console.log("Añadir varios elementos en bloque en una posición concreta:", conjunto);

// 5. Elimina un elemento en una posición concreta.
const posicionEliminar = 5;
conjunto.splice(posicionEliminar, 1);
console.log("Eliminar un elemento en una posición concreta:", conjunto);

// 6. Actualiza el valor de un elemento en una posición concreta.
const posicionActualizar = 4;
conjunto[posicionActualizar] = 99;
console.log("Actualizar el valor de un elemento en una posición concreta:", conjunto);

// 7. Comprueba si un elemento está en un conjunto.
const elementoBuscar = 99;
const existe = conjunto.includes(elementoBuscar);
console.log(`¿El elemento ${elementoBuscar} está en el conjunto?:`, existe);

// 8. Elimina todo el contenido del conjunto.
conjunto = [];
console.log("Eliminar todo el contenido del conjunto:", conjunto);


/* 🔥 DIFICULTAD EXTRA (opcional): ----------------------------------------------------------------------
Muestra ejemplos de las siguientes operaciones con conjuntos:
- 1. Unión.
- 2. Intersección.
- 3. Diferencia.
- 4. Diferencia simétrica.
 */
// Conjuntos iniciales
const conjuntoA = new Set([1, 2, 3, 4, 5]);
const conjuntoB = new Set([4, 5, 6, 7, 8]);

// 1. Unión
const union = new Set([...conjuntoA, ...conjuntoB]);
console.log("Unión:", [...union]);

// 2. Intersección
const interseccion = new Set([...conjuntoA].filter((x) => conjuntoB.has(x)));
console.log("Intersección:", [...interseccion]);

// 3. Diferencia (A - B)
const diferencia = new Set([...conjuntoA].filter((x) => !conjuntoB.has(x)));
console.log("Diferencia (A - B):", [...diferencia]);

// 4. Diferencia simétrica
const diferenciaSimetrica = new Set(
    [...conjuntoA].filter((x) => !conjuntoB.has(x)).concat(
        [...conjuntoB].filter((x) => !conjuntoA.has(x))
    )
);
console.log("Diferencia simétrica:", [...diferenciaSimetrica]);