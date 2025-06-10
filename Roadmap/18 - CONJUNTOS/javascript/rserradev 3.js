// Crear conjunto de datos
let conjunto = ["elemento1", "elemento2", "elemento3", "elemento4", "elemento5"];
console.log(conjunto);

// Añadir un elemento al final
conjunto.push("elemento6");
console.log(conjunto);

// Añadir un elemento al comienzo
conjunto.unshift("elemento0");
console.log(conjunto);

// Añadir varios elementos en bloque al final
let conjunto2 = ["elemento7", "elemento8", "elemento9", "elemento10", "elemento11"];

conjunto2.forEach(Element => {
    conjunto.push(Element);
});
console.log(conjunto);

// Añadir varios elementos en bloque en una posición concreta

let conjunto3 = ["elemento12", "elemento13", "elemento14", "elemento15", "elemento16"];

conjunto3.forEach(element => {
    conjunto.splice(0, 0 , element);
});

console.log(conjunto);

// Eliminar un elemento en una posición en concreto
conjunto.splice(0,1);
console.log(conjunto);

// Actualizar valor de un elemento en una posición en concreto
conjunto.splice(0, 1, "Valor reemplazado");
console.log(conjunto);

// Comprobar si un elemento esta en el conjunto
conjunto.forEach(element => {
    if (element === "elemento100") {
        console.log("El elemento si esta en el conjunto y es el: " + element);
    } else {
        console.log("El elemento no esta en el array: " + element);
    }
});
console.log("Se recorrieron todos los elementos y no se encontró el que se esperaba");

// Eliminar todo el contenido del conjunto
let tamañoConjunto = conjunto.length;

for (let index = 0; index < tamañoConjunto; index++) {
    conjunto.splice(0, 1,);
    console.log(conjunto);
}

// Ejemplo de unión
const conjuntoSet1 = new Set(["uno", "dos", "tres", "cuatro", "cinco"]);
const conjuntoSet2 = new Set(["uno", "elemento20", "elemento21", "elemento22", "elemento23", "elemento24"]);

let unionConjuntos = new Set([...conjuntoSet1, ...conjuntoSet2]);

console.log(unionConjuntos);

// Ejemplo de intersección
console.log("Ejemplo de interseccion");
for (const i of conjuntoSet1) {
    if (conjuntoSet2.has(i)) {
        console.log(i);
    }
}

// Ejemplo de diferencias
console.log("Ejemplo de diferencia");
for (const element of conjuntoSet1) {
    if (conjuntoSet2.has(element)) {
        conjuntoSet1.delete(element);
        console.log("El elemento " + element + " se a eliminado porque no es diferente");
    }
}
console.log(conjuntoSet1);

// Diferencia simétrica
const conjuntoNum1 = new Set([1,2,3,4,5]);
const conjuntoNum2 = new Set([1,2,3,6,7]);

const conjuntoSimétrico = new Set([]);

// Calcular la diferencia simétrica
for (const element of conjuntoNum1) {
    if (conjuntoNum2.has(element)) {
        conjuntoNum1.delete(element);
    } else {
        conjuntoSimétrico.add(element);
    }
}

console.log(conjuntoSimétrico);