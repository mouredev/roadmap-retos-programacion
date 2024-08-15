/**
 * Creacion de todas las estructuras soportadas por defecto en Typescript.
 */

/**
 * Arrays
 */

// Array de strings
const cadenas: string[] = ["Hola", "Mundo", "TypeScript"];

// Array de numeros
const numeros: number[] = [1, 2, 3, 4, 5];

// Array de objetos (con la misma estructura)
const Personas = [
  {
    nombre: "Juan",
    edad: 25,
    direccion: "Calle 123",
  },
  {
    nombre: "Ana",
    edad: 30,
    direccion: "Calle 456",
  },
];

/**
 * Sets
 */

// Set de strings
const setCadenas = new Set(["Hola", "Mundo", "TypeScript"]);

// Set de numeros

const setNumeros = new Set([1, 2, 3, 4, 5]);

// Set de objetos (con la misma estructura)

const setPersonas = new Set([
  {
    nombre: "Juan",
    edad: 25,
    direccion: "Calle 123",
  },
  {
    nombre: "Ana",
    edad: 30,
    direccion: "Calle 456",
  },
]);

/**
 * Maps
 */

// Map de strings como llaves y numeros como valores

const mapCadenasNumeros = new Map([
  ["Hola", 1],
  ["Mundo", 2],
  ["TypeScript", 3],
]);

// Map de objetos (con la misma estructura) como llaves y strings como valores

const mapPersonasCadenas = new Map([
  [
    {
      nombre: "Juan",
      edad: 25,
      direccion: "Calle 123",
    },
    "Persona 1",
  ],
  [
    {
      nombre: "Ana",
      edad: 30,
      direccion: "Calle 456",
    },
    "Persona 2",
  ],
]);

/**
 * Operaciones de inserción, borrado, actualización y ordenación
 */

// Insercion
// Arrays
strings.push("Nueva cadena");
numbers.push(6);

// Sets
setStrings.add("Nueva cadena");
setNumbers.add(6);

// Maps
mapStringsNumbers.set("Nueva cadena", 4);
mapPersonasStrings.set(
  {
    nombre: "Jose",
    edad: 35,
    direccion: "Calle 789",
  },
  "Persona 3"
);

// Borrado
// Arrays
strings.splice(strings.indexOf("Nueva cadena"), 1);
numbers.splice(numbers.indexOf(6), 1);

// Sets
setStrings.delete("Nueva cadena");
setNumbers.delete(6);

// Maps
mapStringsNumbers.delete("Nueva cadena");
mapPersonasStrings.delete({
  nombre: "Jose",
  edad: 35,
  direccion: "Calle 789",
});

// Actualización
// Arrays

strings[strings.indexOf("Hola")] = "Nuevo Hola";

// Sets
setStrings.forEach((value, key, set) => {
  if (value === "Hola") {
    set.delete(value);
    set.add("Nuevo Hola");
  }
});

// Maps
mapStringsNumbers.forEach((value, key, map) => {
  if (key === "Hola") {
    map.delete(key);
    map.set("Hola", 5);
  }
});

// Ordenación
// Arrays

strings.sort();
numbers.sort((a, b) => b - a);

// Sets
const sortedSetStrings = new Set([...setStrings].sort());
const sortedSetNumbers = new Set([...setNumbers].sort((a, b) => b - a));

// Maps
const sortedMapStringsNumbers = new Map([...mapStringsNumbers].sort());
const sortedMapPersonasStrings = new Map([...mapPersonasStrings].sort());