/*
* #03 ESTRUCTURAS DE DATOS
*/

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
*/

/*
*Arrays o Arreglos

Los arrays son una colección ordenada de elementos, donde cada elemento se accede mediante un índice numérico.
Características:
Pueden almacenar cualquier tipo de dato (números, cadenas, objetos, funciones, etc.).
Tienen un tamaño dinámico, es decir, pueden crecer o reducirse según se añadan o eliminen elementos.

*/ 

const arr = new Array(10);
console.log(arr);

const arra = [];
console.log(arra);

//ahora crearemos un arreglo con video juegos

let videoJuegos = ['fifa','AsseAssassins Creed','Forza'];
console.log({videoJuegos})

//Insercion 
 videoJuegos.push ('Call of Duty');
 console.log({videoJuegos})

 //Borrado

let ultimoJuegoBorrado = videoJuegos.pop(); //Pop elimina el ultimo elemento del arreglo.
console.log({ultimoJuegoBorrado,videoJuegos});

let posicionJuegoBorrado = videoJuegos.splice(1,1); //Splice elimina el elemento de acuerdo a la posicion indicada.
console.log({posicionJuegoBorrado,videoJuegos});

//Acceso
console.log(videoJuegos[1]);

//Actualizacion 
let actualizacionVideoJuego = 'Mario Bros'
videoJuegos[1] = actualizacionVideoJuego
console.log({videoJuegos,actualizacionVideoJuego});

//Ordenacion 
let ordenVideoJuegos = videoJuegos.sort();
console.log({ordenVideoJuegos});

/*
*Sets
En JavaScript, un Set es una colección de valores únicos, y se implementa como un objeto especial
 que proporciona una manera eficiente de almacenar y manejar conjuntos de datos sin duplicados. 
 Aunque se considera un tipo de objeto, tiene su propia interfaz y métodos específicos que lo diferencian 
 de los objetos regulares y de otros tipos de colecciones como los arrays.
*/

 let marcaCars = ['Renault','Mazda','Toyota','Jeep','Porche','Tesla']

 let setsMarcasCars = new Set(marcaCars);
 console.log({setsMarcasCars});

//Inserccion 

let inserSet = setsMarcasCars.add('mercedes')
console.log({inserSet});

//Borrado

let borrarSet = setsMarcasCars.delete('Toyota');
console.log(borrarSet);
console.log(setsMarcasCars);

//Acceso 
/*A diferencia de los arrays, los Set en JavaScript no tienen un índice para acceder 
directamente a sus elementos. Sin embargo, puedes iterar sobre los elementos de un Set para acceder a ellos*/

let elemento = Array.from (setsMarcasCars);
console.log(elemento [2]);

//Actualizacion 

if (setsMarcasCars.has('Renault')){
    setsMarcasCars.delete('Renault');
    setsMarcasCars.add('BMW');
}

console.log(setsMarcasCars);

//Ordenacion

let ordenCars = Array.from(setsMarcasCars);
//para ordenar el arreglo utilizo sort asi:

ordenCars.sort();

//creo un nuevo set

let carsOrdenado = new Set(ordenCars);
console.log(carsOrdenado);

/* 
* Objetos 
Los objetos son colecciones de pares clave-valor, donde cada clave es una cadena (o un símbolo) 
y cada valor puede ser cualquier tipo de dato.
*/

let serieHouseOfDragon = {

    reina:'RaineRhaenyra Targaryen',
    villano:'Aemond Targaryen',
    temporadas:2,
    numeroDeDragones:17,
    NombreDeLasCasas: ['Casa Targaryen','Casa Hightower','Casa Velaryon']

}

//insercion 
serieHouseOfDragon.villano ='Aegon II Targaryen';
console.log({serieHouseOfDragon})

serieHouseOfDragon['NumeroDeSoldados'] = 1000

//Borrado 
delete serieHouseOfDragon.temporadas;
console.log({serieHouseOfDragon});

//acceso 
console.log(serieHouseOfDragon.NombreDeLasCasas[1]);

//Actualizacion 

serieHouseOfDragon.NombreDeLasCasas[0] = 'Casa Stark ';
console.log({serieHouseOfDragon});

//Ordenar 

let ordenHouse = Object.entries(serieHouseOfDragon);
ordenHouse.sort((a,b)=>a[0].localeCompare(b[0]));
let houseOrdenada = Object.fromEntries(ordenHouse);

console.log({houseOrdenada});


/*
 *   DIFICULTAD EXTRA (opcional):
 *   Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */


const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let contactos = {}; // Objeto para almacenar los contactos
let ejecutar = true;

const mostrarMenu = () => {
  console.log("\nOpciones:");
  console.log("1: Búsqueda");
  console.log("2: Inserción");
  console.log("3: Actualización");
  console.log("4: Eliminación de Contactos");
  console.log("5: Salir");
};

const preguntarAccion = () => {
  rl.question('Por favor ingrese el número de la acción que desea realizar: ', (dato) => {
    let opcion = parseInt(dato, 10);

    switch (opcion) {
      case 1:
        rl.question('Por favor ingrese el nombre del contacto a buscar: ', (nombre) => {
          if (contactos[nombre]) {
            console.log(`Contacto encontrado: Nombre - ${nombre}, Teléfono - ${contactos[nombre]}`);
          } else {
            console.log('Nombre no encontrado');
          }
          preguntarAccion(); // Volver a preguntar después de la operación
        });
        break;
      case 2:
        rl.question('Por favor ingrese su nombre: ', (nombre) => {
          rl.question('Ingrese su número telefónico: ', (telefono) => {
            let telefonoStr = telefono.toString();
            if (telefonoStr.length > 11) {
              console.log('El número no es válido, es mayor a 11 dígitos');
            } else {
              contactos[nombre] = telefono;
              console.log(`Contacto agregado: Nombre - ${nombre}, Teléfono - ${telefono}`);
            }
            preguntarAccion(); // Volver a preguntar después de la operación
          });
        });
        break;
      case 3:
        rl.question('Ingrese el nombre del contacto a actualizar: ', (nombre) => {
          if (contactos[nombre]) {
            rl.question('Ingrese el nuevo número telefónico: ', (nuevoTelefono) => {
              let nuevoTelefonoStr = nuevoTelefono.toString();
              if (nuevoTelefonoStr.length > 11) {
                console.log('El número no es válido, es mayor a 11 dígitos');
              } else {
                contactos[nombre] = nuevoTelefono;
                console.log(`Contacto actualizado: Nombre - ${nombre}, Nuevo Teléfono - ${nuevoTelefono}`);
              }
              preguntarAccion(); // Volver a preguntar después de la operación
            });
          } else {
            console.log('Nombre no encontrado');
            preguntarAccion(); // Volver a preguntar después de la operación
          }
        });
        break;
      case 4:
        rl.question('Ingrese el nombre del contacto a eliminar: ', (nombre) => {
          if (contactos[nombre]) {
            delete contactos[nombre];
            console.log(`Contacto eliminado: Nombre - ${nombre}`);
          } else {
            console.log('Nombre no encontrado');
          }
          preguntarAccion(); // Volver a preguntar después de la operación
        });
        break;
      case 5:
        console.log('Saliendo del programa.');
        ejecutar = false; // Cambiar la variable de control para salir del bucle
        rl.close(); // Cerrar la interfaz
        break;
      default:
        console.log("Operación no reconocida");
        preguntarAccion(); // Volver a preguntar si la operación no es válida
    }
  });
};

const iniciar = () => {
  while (ejecutar) {
    mostrarMenu();
    preguntarAccion();
    break; // Salir del bucle para permitir que preguntarAccion maneje la entrada del usuario
  }
};

iniciar();
