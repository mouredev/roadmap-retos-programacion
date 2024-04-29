/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado
 *, actualización y ordenación.
 */

//***ARRAYS***
let frutasQueMeGustan = ['mango', 'fresa', 'pera', 'manzana', 'uva', 'durazno'];
console.log(frutasQueMeGustan);

for(let i = 0; i < frutasQueMeGustan.length; i++) { //iteracion de los elementos de un array
    console.log(frutasQueMeGustan[i]);
};

//-Insercion-
frutasQueMeGustan.push('guanabana'); //inserta un elemento al final
console.log(frutasQueMeGustan);

frutasQueMeGustan.unshift('aguacate'); //inserta un elemento al incio
console.log(frutasQueMeGustan);

frutasQueMeGustan.splice(2, 1, 'papaya'); //inserta un elemento en una ubicacion especifica
console.log(frutasQueMeGustan);

//-Borrado-
frutasQueMeGustan.pop(); //borra un elemento al final
console.log(frutasQueMeGustan);

frutasQueMeGustan.shift(); //borra un elemento al incio
console.log(frutasQueMeGustan);

frutasQueMeGustan.splice(1, 1); //borra un elemento en una ubicacion especifica
console.log(frutasQueMeGustan);

//-Actualizacion-
frutasQueMeGustan[2] = 'piña'; //reasigna el valor del elemento Arr[indice]
console.log(frutasQueMeGustan);

frutasQueMeGustan.splice(1, 1, 'parchita'); //reasigna el valor en una ubicacion especifica
console.log(frutasQueMeGustan);

frutasQueMeGustan.fill('tamarindo', 2, 3); //reasigna el valor en una ubicacion especifica
console.log(frutasQueMeGustan);

//-Ordenado-
let nuevoArray = [12, 10, 34, 25, 82];
console.log(nuevoArray);
nuevoArray.sort((a, b) => a - b); //ordena los numeros de menor a mayor
console.log(nuevoArray);

let nuevoArray2 = [12, 10, 34, 25, 82];
console.log(nuevoArray2);
nuevoArray2.sort((a, b) => b - a); //ordena los numeros de mayor a menor
console.log(nuevoArray2);


//***SETS***
const animales = new Set([
    'gallina',
    'foca',
    'lagarto'
]);
console.log(animales);

//-Insercion-
animales.add('gato');
animales.add('perro');
animales.add('araña');
animales.add('gato'); //no se ejecuta debido a que los sets no admiten duplicados
console.log(animales);

//-Borrado-
animales.delete('lagarto');
animales.delete('perro');
console.log(animales);

//-Ordenado-
// los sets no tienen indice, por lo que no es posible ordenarlos sin antes convertirlos en un array
const miNuevoSet = new Set([12, 23, 45, 87, 43, 67, 12, 87]);
console.log(miNuevoSet);

let arrayDelSet = Array.from(miNuevoSet).sort((a, b) => a - b);
console.log(arrayDelSet);

//***MAPS***
const miMap = new Map([
    ['clave1', 'valor1'],
    ['uno', 1],
    ['dos', 2],
]);
console.log(miMap);

//-Insercion-
miMap.set('nombre', 'Ric');
console.log(miMap);

//-Actualizacion-
miMap.set('nombre', 'Josue'); //se utiliza el mismo metodo
console.log(miMap);

//-Borrado-
miMap.delete('dos'); //elimina una clave-valor existente
console.log(miMap);

//-Otras operaciones-
console.log(miMap.get('nombre')); //obtiene el valor de una clave
console.log(miMap.get('uno'));

console.log(`Mi map contiene la clave 'dos': ${miMap.has('dos')}`); //verfica si el map contiene una clave

console.log(miMap.size); //nos indica la cantidad de claves-valor

//***OBJETOS***
const persona = {
    nombre : 'Ricardo',
    edad : 21,
    sexo : 'masculino',
    casado: false,
    estatura: 159,
};
console.log(persona);

//-Insercion-
persona.pasatiempos = ['escribir', 'dibujar', 'leer'];
console.log(persona);

//-Borrado-
delete persona.estatura;
console.log(persona);

//-Actualizacion-
persona.pasatiempos[1] = 'escuchar musica';
console.log(persona);