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

// EJERCICIO:
// Arrays
let miArray = [1, 2, 3, 4, 5];
miArray.push(10);
miArray.pop();
miArray[0] = 23;
miArray.sort();
console.log(miArray);

// Sets
const miSet = new Set([1, 2, 3]);
miSet.add(4);
miSet.delete();
console.log(miSet);

// Objects
const miObjeto = {
  x: 10,
  y: 15,
  z: 20,
};
miObjeto.punto = 2;
delete miObjeto.z;
miObjeto["y"] = 45;
console.log(miObjeto);

// Maps
const miMap = new Map([
  ["a", 1],
  ["b", 2],
]);
miMap.set("c", 3);
miMap.delete();
miMap.set("a", "a");
console.log(miMap);

// DIFICULTAD EXTRA:
const agendaContactos = () => {
  let agenda = new Map();

  let opcion = 1;
  let nombre = "Hernan";
  let numero = 3413646464;
  let nombre2 = "Agustin";
  let numero2 = 3413646566;

  console.log(`
    1. Buscar
    2. Insertar
    3. Actualizar
    4. Eliminar
    5. Salir
  `);

  if (opcion >= 1 && opcion <= 5) {
    switch (opcion) {
      case 1:
        if (nombre !== "" && !isNaN(numero) && numero.toString().length <= 11) {
          agenda.set(nombre, numero);
          console.log(agenda);
        } else {
          console.log("Error, vuelva a insertar datos validos");
        }
        break;
      case 2:
        if (nombre !== "" && !isNaN(numero) && numero.toString().length <= 11) {
          agenda.set(nombre, numero);
        } else if (agenda.has(nombre)) {
          console.log(`El numero de ${nombre} es: ${agenda.get(nombre)}`);
        } else {
          console.log("El contacto no esta registrado");
        }
        break;
      case 3:
        agenda.set(nombre2, numero2);
        console.log(`El numero de ${nombre2} es: ${agenda.get(nombre2)}`);
        break;
      case 4:
        agenda.delete(nombre);
        console.log(agenda);
        break;
      case 5:
        console.log("Saliendo de la agenda..");
        break;
      default:
        break;
    }
  } else {
    console.log("Error de opcion, ingrese un numero entre el 1 y el 5");
  }
};

agendaContactos();
