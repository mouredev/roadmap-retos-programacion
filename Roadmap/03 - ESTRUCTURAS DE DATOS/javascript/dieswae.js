/* Arrays */

// creación

let myArray = [10, 45, 89, 100, 120];

// inserción
myArray.push(70); // añade un elemento al final del array
myArray.unshift(0); // añade un elemento al inicio del array
myArray.splice(3, 0, 110); // añade un elemento en cierta pocision, en este caso despues del 100 agrega el 110

// borrado
myArray.pop(); // elimina el ultimo elemento del array
myArray.shift(); // elimina el primer elemento del array
myArray.splice(2, 1); // elimina un elemento en la posición 2

// actualización
myArray[2] = 58; // actualiza el valor en la posición 2

// ordenación
myArray.sort(); // ordena el array

/* Objects */

// creación
let myObject = {
  nombre: 'Diego',
  edad: 22,
  ciudad: 'Buenos Aires',
  hobbies: {
    inside: 'Practicar coding',
    outside: 'Jugar Futbol',
  }
};

// inserción
myObject.trabajo = 'Developer' // mostrara una propiedad nueva con el valor de 'Developer'

// actualización
myObject.nombre = 'Diklaus' // actualizara la propiedad nombre a 'Diklaus'

// Borrado
delete myObject.trabajo; // borrará a propiedad que acabamos de crear llamada trabajo

/* Sets */

// creación
let mySet = new Set([1, 2, 3]);

// inserción
mySet.add(4);

// borrado
mySet.delete(2);

/* Maps */

// creación 
let myMap = new Map();

// inserción
myMap.set(1, 'lunes');
myMap.set(true, 10);

// borrado
myMap.delete('hola1');

// actialización
myMap.set('hola2', 'newValue');

console.log(map.has(1)); // verificar si existe un valor // sirve para set tambien

console.log(map.size); // ver numero de elementos que hay // sirve para set tambien

/* EXTRA */

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




