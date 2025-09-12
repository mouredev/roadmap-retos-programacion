//Ejemplo de creación de estructuras de datos en JavaScript
//Array, Object, Map y Set son las estructuras de datos más comunes en JavaScript.

//Array es una colección de elementos, donde cada elemento tiene un índice numérico.
let array = [1, 2, 3, 4, 5];
console.log(array);
//Operaciones de inserción
array.push(6);
console.log(array);
//Operaciones de borrado
array.pop();
console.log(array);
//Operaciones de actualización
array[0] = 0;
console.log(array);
//Operaciones de ordenación
array.sort();
console.log(array);

//Object es una colección de pares clave-valor, donde la clave es una cadena y el valor puede ser de cualquier tipo.
let object = { name: "Joan", age: 25, city: "Barcelona" };
console.log(object);
//Operaciones de inserción
object.job = "Developer";
console.log(object);
//Operaciones de borrado
delete object.city;
console.log(object);
//Operaciones de actualización
object.age = 26;
console.log(object);
//Operaciones de ordenación
//No se pueden ordenar objetos

//Map es una colección de pares clave-valor, donde tanto la clave como el valor pueden ser de cualquier tipo.
let map = new Map();
map.set("name", "Joan");
map.set("age", 25);
map.set("city", "Barcelona");
console.log(map);
//Operaciones de inserción
map.set("job", "Developer");
console.log(map);
//Operaciones de borrado
map.delete("city");
console.log(map);
//Operaciones de actualización
map.set("age", 26);
console.log(map);
//Operaciones de ordenación
//No se pueden ordenar mapas

//Set es una colección de valores únicos, lo que significa que un valor solo puede estar una vez en un set.
let set = new Set([1, 2, 3, 4, 5]);
console.log(set);
//Operaciones de inserción
set.add(6);
console.log(set);
//Operaciones de borrado
set.delete(1);

console.log(set);
//Operaciones de actualización
//No se pueden actualizar elementos de un set
//Operaciones de ordenación
//No se pueden ordenar sets

//Ejercicio extra
//Crear una agenda:
//Declaración de variables
let opcion;
let nombre = "";
let numTelf = "";
let agenda = new Map();
let is_on = true;
//Bucle principal
while (is_on == true) {
  //Menú de opciones
  console.log("Buscar contacto --> 1");
  console.log("Insertar contacto --> 2");
  console.log("Actualizar contacto --> 3");
  console.log("Eliminar contacto --> 4");
  console.log("Salir --> 5");
  //Selección de opción
  opcion = parseInt(prompt("Elige una opcion: "));
  //Switch para cada opción
  switch (opcion) {
    case 1:
      //Buscar contacto
      //objecto.has(key) es un método que devuelve un booleano indicando si el objeto tiene la clave dada.
      //objecto.get(key) es un método que devuelve el valor asociado con la clave dada.
      nombre = prompt("Introduce el nombre del contacto: ");
      if (agenda.has(nombre)) {
        console.log(
          `El contacto ${nombre} tiene el número ${agenda.get(nombre)}`
        );
      } else {
        console.log("El contacto no existe");
      }
      break;
    case 2:
      //Insertar contacto
      //objecto.set(key, value) es un método que añade un nuevo par clave-valor al objeto.
      nombre = prompt("Introduce el nombre del contacto: ");
      numTelf = prompt("Introduce el número de teléfono: ");
      if (numTelf.length === 11) {
        agenda.set(nombre, numTelf);
        console.log("Contacto añadido correctamente");
      } else {
        console.log("Número de teléfono incorrecto");
      }
      break;
    case 3:
      //Actualizar contacto
      nombre = prompt("Introduce el nombre del contacto: ");
      if (agenda.has(nombre)) {
        nombre = prompt("Introduce el nuevo nombre del contacto: ");
        numTelf = prompt("Introduce el nuevo número de teléfono: ");
        if (numTelf.length === 11) {
          agenda.set(nombre, numTelf);
          console.log("Contacto actualizado correctamente");
        } else {
          console.log("Número de teléfono incorrecto");
        }
      } else {
        console.log("El contacto no existe");
      }
      break;
    case 4:
      //Eliminar contacto
      //objecto.delete(key) es un método que elimina la clave y su valor asociado del objeto.
      nombre = prompt("Introduce el nombre del contacto: ");
      if (agenda.has(nombre)) {
        agenda.delete(nombre);
        agenda.delete(numTelf);
        console.log("Contacto eliminado correctamente");
      } else {
        console.log("El contacto no existe");
      }
      break;
    case 5:
      console.log("Saliendo del programa. ¡Hasta luego!");
      is_on = false;
      break;
    default:
      console.log("Opción incorrecta. Introduce un número del 1 al 5");
      break;
  }
}
agenda();
