//Tipo de estructura de datos JS

//1. Arrays(Arreglos)
let numérico = [1, 3, 5, 2, 100, 0];
let personas = ['Mario', 'Marco', 'Marcelo', 'Martin'];
console.log('El arreglo numérico contiene los siguientes números:', numérico); // El arreglo numérico contiene los siguientes números: [ 1, 2, 2, 3 ]
console.log('El arreglo personas contiene las siguientes personas:', personas); // El arreglo personas contiene las siguientes personas: [ 'Mario', 'Marco', 'Marcelo', 'Martin' ]
console.log(`.........................................`);
//1.1 inserción
personas.push('Matias');
console.log('Se agrego al final a  Matias', personas); // Se agrego al final a  Matias [ 'Mario', 'Marco', 'Marcelo', 'Martin', 'Matias' ]
personas.unshift('Primero');
console.log('Se agrego al inicio a "Primero"', personas); //[ 'Primero' , 'Mario', 'Marco', 'Marcelo', 'Martin', 'Matias' ]
//1.2 borrado
personas.shift();
console.log('Eliminación del inicio "Primero" ', personas); //Eliminación del inicio "Primero"  [ 'Mario', 'Marco', 'Marcelo', 'Martin', 'Matias' ]
personas.splice(2, 2); //
console.log('Eliminación especifica Martin', personas); //Eliminación especifica Martin [ 'Mario', 'Marco', 'Matias' ]
personas.pop();
console.log('Eliminación de la ultima posición: ', personas); // Eliminación de la ultima posición:  [ 'Mario', 'Marco' ]
//1.3 actualización
personas[0] = 'Máximo';
console.log('Mario se cambio por Máximo:', personas); // Mario se cambio por Máximo: [ 'Máximo', 'Marco' ]
//1.4 ordenación
personas.sort;
console.log('Se ordeno alfabéticamente ', personas); // Se ordeno alfabéticamente  [ 'Máximo', 'Marco' ]
numérico.sort((a, b) => a - b);
console.log('Se ordeno el array numérico de menor a mayor:', numérico); // Se ordeno el array numérico de menor a mayor: [ 0, 1, 2, 3, 5, 100 ]
console.log(`.........................................`);

//2.Object(Objetos){Almacena datos pares clave-valor}
let marioObject = {
  nombre: 'Mario',
  apellido: 'Bros',
  edad: '24',
  ciudad: 'Champiñon',
};
console.log('Los datos de la Mario son:', marioObject); // Los datos de la Mario son: { nombre: 'Mario', apellido: 'Bros', edad: '24', ciudad: 'Champiñon' }
console.log('Nombre de la persona. Su nombre es: ', marioObject.nombre); //Nombre de la persona. Su nombre es: Mario
//2.1 inserción
//2.2 borrado
delete marioObject.ciudad;
console.log('Se elimino la ciudad', marioObject); // Se elimino la ciudad { nombre: 'Mario', apellido: 'Bros', edad: '24' }
console.log(`.........................................`);
//3 Map(Map){Almacena pares clave-valor//Diferencia cualquier clave}
let miMapa = new Map();
miMapa.set('a', 1);
miMapa.set('b', 2);
console.log('Mi map es:', miMapa); // Mi map es: Map(2) { 'a' => 1, 'b' => 2 }
//3.1 inserción
miMapa.set('c', 3);
console.log('Se agrego C con 3', miMapa); //Se agrego C con 3 Map(3) { 'a' => 1, 'b' => 2, 'c' => 3 }
//3.2 borrado
miMapa.delete('a');
console.log('Se elimino a ', miMapa); //Se elimino a  Map(2) { 'b' => 2, 'c' => 3 }
//3.3 actualización
miMapa.set('b', 1);
console.log('Se actualizo el valor de "b" ', miMapa); // Se actualizo el valor de "b"  Map(2) { 'b' => 1, 'c' => 3 }
console.log(`.........................................`);

//4 Set(Set) {valores únicos }
let conjuntoUnico = new Set([1, 2, 3, 3, 4]);
console.log(conjuntoUnico); // Set(4) { 1, 2, 3, 4 }
//4.1 inserción
conjuntoUnico.add(6);
console.log(conjuntoUnico); // Set(5) { 1, 2, 3, 4, 6 }
//4.2 borrado
conjuntoUnico.delete(2);
console.log(conjuntoUnico); //Set(4) { 1, 3, 4, 6 }
console.log(`.........................................`);

//Otras estructura de datos

//5. string
let mensaje = 'Hola, mundo!';
//6. number
let edad = 24;
//7. booleano
let esMayorDeEdad = true; // o false
//8. Undefined
let variableNoDefinida;
//9. Null
let valorNulo = null;

/*
 EJERCICIO:
 DIFICULTAD EXTRA (opcional):
 */

// realizar operaciones de entrada y salida de manera más sencilla
const readline = require('readline');

// Creamos una interfaz de lectura para interactuar con la terminal
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Objeto para almacenar los contactos
const agenda = {}; // Cada contacto debe tener un nombre y un número de teléfono. // Global

// Función para mostrar el menú de operaciones
function mostrarMenu() {
  console.log('\n** Agenda de Contactos **');
  console.log('1. Buscar contacto');
  console.log('2. Insertar contacto');
  console.log('3. Actualizar contacto');
  console.log('4. Eliminar contacto');
  console.log('5. Mostrar contacto');
  console.log('6. Salir');
}

//1. Función para buscar un contacton
function buscarContacto() {
  rl.question(
    'Ingrese el nombre o número de teléfono del contacto a buscar: ',
    (entrada) => {
      // Verificar si la entrada coincide con un nombre
      const contactoPorNombre = agenda[entrada];

      // Verificar si la entrada coincide con un número de teléfono
      const contactoPorTelefono = Object.entries(agenda).find(
        ([nombre, telefono]) => telefono === entrada
      );

      if (contactoPorNombre) {
        console.log(`Teléfono de ${entrada}: ${contactoPorNombre}`);
      } else if (contactoPorTelefono) {
        console.log(
          `Nombre de la persona con el teléfono ${entrada}: ${contactoPorTelefono[0]}`
        );
      } else {
        console.log(`Contacto ${entrada} no encontrado.`);
      }

      mostrarMenu();
      seleccionarOperacion();
      console.log('\n Viendo si entran los datos:', agenda);
    }
  );
}
//2. Insertar un conctato
function insertarContacto() {
  rl.question('Ingrese el nombre del contacto: ', (nombre) => {
    rl.question('Ingrese el número de teléfono: ', (telefono) => {
      if (!isNaN(telefono) && telefono.length <= 11) {
        agenda[nombre] = telefono;
        console.log(`Contacto ${nombre} insertado con éxito.`);
      } else {
        console.log(
          'Número de teléfono no válido. Debe ser numérico y tener hasta 11 dígitos.'
        );
      }
      mostrarMenu();
      seleccionarOperacion();
      console.log('\n Viendo si entran los datos:', agenda);
    });
  });
}
//3. actualziar contacto./ isNaN:Is Not a Number(No es un número)
function actualizarContacto() {
  rl.question('Ingrese el nombre del contacto a actualizar: ', (nombre) => {
    if (agenda[nombre]) {
      rl.question('Ingrese el nuevo número de teléfono: ', (telefono) => {
        if (!isNaN(telefono) && telefono.length <= 11) {
          agenda[nombre] = telefono;
          console.log(`Contacto ${nombre} actualizado con éxito.`);
        } else {
          console.log(
            'Número de teléfono no válido. Debe ser numérico y tener hasta 11 dígitos.'
          );
        }
        mostrarMenu();
        seleccionarOperacion();
      });
    } else {
      mostrarMenu();
      seleccionarOperacion();
      console.log('\n Viendo si entran los datos:', agenda);
    }
  });
}
//4. Eliminar conctto
function eliminarContacto() {
  rl.question('Ingrese el nombre del contacto a eliminar: ', (nombre) => {
    if (agenda[nombre]) {
      delete agenda[nombre];
      console.log(`Contacto ${nombre} eliminado con éxito.`);
    } else {
      console.log(`Contacto ${nombre} no encontrado.`);
    }
    mostrarMenu();
    seleccionarOperacion();
    console.log('\n Viendo si entran los datos:', agenda);
  });
}
//5.Mostrar a los contactos
function mostrarTodosLosContactos() {
  console.log('\n** Todos los contactos **');
  for (const [nombre, telefono] of Object.entries(agenda)) {
    console.log(`${nombre}: ${telefono}`);
  }
  mostrarMenu();
  seleccionarOperacion();
  console.log('Viendo si entran los datos:', agenda);
}
//6. Función para seleccionar la operación
function seleccionarOperacion() {
  rl.question('Seleccione una operación (1-6): ', (opcion) => {
    switch (opcion) {
      case '1':
        buscarContacto();
        break;
      case '2':
        insertarContacto();
        break;
      case '3':
        actualizarContacto();
        break;
      case '4':
        eliminarContacto();
        break;
      case '5':
        mostrarTodosLosContactos();
        break;
      case '6':
        console.log('Saliendo del programa.');
        rl.close();
        break;
      default:
        console.log('Opción no válida. Inténtelo de nuevo.');
        mostrarMenu();
        seleccionarOperacion();
        break;
    }
  });
}

// Inicio del programa
mostrarMenu();
seleccionarOperacion();

//Esto no es eficiente pero funciona. Puede haber datos repetidos, no hay una id
