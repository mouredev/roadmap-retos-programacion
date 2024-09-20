
// /*
//  * EJERCICIO:
//  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
//  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
//  *
//  * DIFICULTAD EXTRA (opcional):
//  * Crea una agenda de contactos por terminal.
//  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
//  * - Cada contacto debe tener un nombre y un número de teléfono.
//  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
//  *   los datos necesarios para llevarla a cabo.
//  * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
//  *   (o el número de dígitos que quieras)
//  * - También se debe proponer una operación de finalización del programa.
//  */

// ESTRUCTURAS(8) -> - array - sets - maps - stacks - queueus - arboles - grafos

// {* ARRAYSS *} (arreglos)

const array = [1,2,3,4,"hola", "tambien", 501, "array"]
console.log("array", array, "soy de tipo:", typeof(array))

// Operaciones:
const insertado = "metidito"                      // insercion:
array.push(insertado)
console.log("insertamos a ", insertado, " en el array: ", array)

array.splice(3, 1)                                // borrado:
console.log("borramos el 3er elemento, ahora estamos: ", array)
array.pop(insertado)
console.log("ay sacamos el ultimo:", array)
array.unshift(insertado)
console.log("arrepentido lo ponemos primero: ", array)

array[7] = "actualiz4d0"                        // actualizacion:
console.log("hubo una actualizacion, ", array)

array.sort()                                    // ordenacion:
console.log("ordenamos un poco: ", array)

// {*  SETS  *} -> coleccion de valores unicos, no permite duplicados y mantienen el orden en que fueron insertados
// pueden contener cualquier tipo, incluidos objetos, funciones y otros sets

const sets = new Set([1, 2, 3])
sets.add("metidito");                           // Inserción
console.log("sets después de inserción:", sets)
sets.delete(2);                                 // Borrado
console.log("sets después de borrado:", sets)

// {* DICCIONARIOS (mapas) *} -> 

const diccionario = new Map();
diccionario.set('nombre', 'Pauli')                              // Inserción
diccionario.set('edad', 30);
console.log("Diccionario después de inserción:", diccionario)
diccionario.set('edad', 31);                                    // Actualización
console.log("Diccionario después de actualización:", diccionario)
diccionario.delete('nombre');                                   // Borrado
console.log("Diccionario después de borrado:", diccionario)

// {* OBJETOS *} -> pares CLAVE - VALOR 

const persona = {
  nombre: 'Pau',
  edad: 30
};

console.log('la persona es:', persona.nombre)
persona.edad = 31            // Actualización
console.log('actualizamos la edad a:', persona.edad)  
delete persona.edad       // Borrado
console.log('hemos eliminado la edad de la persona', persona.nombre)