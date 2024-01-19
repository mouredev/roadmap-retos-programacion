/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

// Arrays  conjunto de elementos del mismo tipo

let mi_array = [1,2,3,4,5]
//Insertar un elemento en un array
mi_array.push(6)
console.log(mi_array)

//Borrar un elemento del array 
mi_array.pop()
console.log(mi_array)

//Actualizar un valor de un array
mi_array.splice(2,1,33) // Primer parámetro (2) indico la posición del número a modificar
console.log(mi_array)   // Segundo parámetro (1) indico cuantos elementos quiero modificar
                        // Tercer parámetro (33) indico el valor nuevo modificado
//Ordenar arrays
mi_array.sort((a,b)=> a-b) // con esa arrow function indico que me los ordene de menor a mayor
console.log(mi_array)


// Sets Colección de valores únicos donde no puede haber duplicados
let miSet = new Set ([1,2,3,4,5])
console.log(miSet)
//Insertar un elemento en un Set
miSet.add(6)
console.log(miSet)

//Borrar un elemento del set
miSet.delete(4)
console.log(miSet)

//Actualizar un elemento en el set
/*No se puede cambiar el valor de un elemento pero
si podemos quitar y añadir como hemos visto antes*/

//Ordenar sets 
/*
 *Para ordenar los elementos de un set primero lo convertimos a array 
 *y luego ordenamos sus elementos como hemos hecho anteriormente 
 */



//Maps almacenan pares clave-valor pero con más flexibilidad que los objetos
let miMapa = new Map()
miMapa.set("lenguaje","Javascript")
miMapa.set("nombre","alexdevrep")
console.log(miMapa)

//Insertar un elemento en un Map
miMapa.set("edad","24")
console.log(miMapa)

//Borrar un elemento del mapa
miMapa.delete("nombre")
console.log(miMapa)

//Actualizar el valor de un mapa
miMapa.set("edad","30")
console.log(miMapa)

