/*EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.*/

//Añade un elemento al final
const dias = ["miércoles", "jueves"];
dias.push("viernes");
console.log(dias);

//Añade un elemento al principio
dias.unshift("martes");
console.log(dias);

//Añade varios elementos en bloque al final
const finde = ["sábado", "domingo"];
dias.push(...finde);
console.log(dias);

//Añade varios elementos en bloque en una posición concreta.
const inicioSemana = ["Comenzamos!", "lunes"];
dias.splice(0, 0, ...inicioSemana);
console.log(dias);

//Elimina un elemento en una posición concreta
dias.splice(0, 1);
console.log(dias);

//Actualiza el valor de un elemento en una posición concreta.
dias[0] = "Maldito lunes";
console.log(dias);

//Comprueba si un elemento está en un conjunto.
const estaSabado = dias.includes("sábado");
console.log(estaSabado);

//Elimina todo el contenido del conjunto.
dias.length = 0;
console.log(dias);

/*DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.*/

//Unión
const names = ["Pepe", "Bartolo", "Benito"];
const names2 = ["Paco", "Avelino", "Benito"];
const union = new Set();

names.forEach(nombres => union.add(nombres));
names2.forEach(nombres => union.add(nombres));
console.log(union); //Set(5) { 'Pepe', 'Bartolo', 'Benito', 'Paco', 'Avelino' }

//Intersección
const interseccion = new Set();

names.forEach(nombre => {
    if(names2.includes(nombre)) {
        interseccion.add(nombre);
    }
});
console.log(interseccion); //[ 'Benito' ]

//Diferencia
const diferencia = new Set();

names.forEach(nombre => {
    if(!names2.includes(nombre)) {
        diferencia.add(nombre);
    }
})
console.log(diferencia); //[ 'Pepe', 'Bartolo' ]

//Diferencia simétrica.
const diferenciaSimetrica = new Set();

names.forEach(nombre => {
    if(!names2.includes(nombre)){
        diferenciaSimetrica.add(nombre);
    }
})
names2.forEach(nombre => {
    if(!names.includes(nombre)){
        diferenciaSimetrica.add(nombre);
    }
});
console.log(diferenciaSimetrica); //{ 'Pepe', 'Bartolo', 'Paco', 'Avelino' }
