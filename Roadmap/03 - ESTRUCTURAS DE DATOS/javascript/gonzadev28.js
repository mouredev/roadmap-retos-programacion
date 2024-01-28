/*EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.*/

//ARRAY 
let myArray = [1, 2, 3, 4, 5, 5, 2, 4];

myArray.push(0);//Insercion en array (agrega numero 0)
delete(myArray[0]);//Eliminacion en array en la posicion [0]
myArray[5] = 6;//Actualizacion en array (actualiza en la posicion [5])
myArray.sort();//Ordenacion de array

console.log(myArray);

//OBJETO
let persona = {
    nombre: 'Gonzalo',
    apellido: 'Lizama',
    edad: 30,
};
persona['ciudad'] = 'Ancud';//Insercion en objeto
delete persona.edad;//Eliminacion dentro de objeto
persona['nombre'] = 'Enrique'; //Actualizacion de 'nombre'

console.log(persona);

//MAP
let map= new Map([
    [1, 'Javascript'],
    [2, 'Python'],
    [3, 'C++'],
]);

map.set(4, 'Java');//Insercion en map
map.delete(3); //Elimina elemento con la clave '3' --> 'C++'
map.set(2, 'C#');//Actualiza en map elemento con la clave '2'

console.log(map);

//SET
let mySet = new Set([1, 1, 1, 2, 3, 4, 5]); 

mySet.add(6);//Insercion dentro de set
mySet.delete(1);//Eliminacion dentro de set

console.log(mySet);

/*DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.*/
  
//Funcion de node.js para enviar y recibir datos por consola 
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

const contactos = {};

//Menu de opciones
function opciones(){
  console.log('==========================================');
  console.log('Selecciona una de las siguientes opciones:');
  console.log('==========================================');
  console.log('1. Buscar contacto');
  console.log('2. Ingresar contacto');
  console.log('3. Actualizar contacto');
  console.log('4. Eliminar contacto');
  console.log('5. Salir\n');
}
//switch para cada opcion seleccionada
function selecionaOpcion(){
  readline.question('Por favor seleccione una opcion: ', (opcion) => {
    switch (opcion){
      case '1':
        buscarContacto();
        break;
      case '2':
        ingresarContacto();
        break;
      case '3':
        actualizarContacto();
        break;
      case '4':
        eliminarContacto();
        break;
      case '5':
        console.log('Saliendo...');
        readline.close();
        break;
      default:('Por favor seleccione una opcion');
      break;
    }
  });
}
opciones();
selecionaOpcion();

//Buscar contacto
function buscarContacto(){
  readline.question('Ingrese el nombre o telefono para comenzar a buscar: ', (ingresa) => {
    const busquedaNombre = contactos[ingresa];
    const busquedaNumero = Object.entries(contactos).find(
      ([nombre, telefono]) => telefono === ingresa
    );
    if(busquedaNombre){
      console.log(`El telefono de ${ingresa} es: ${busquedaNombre}`);
    }else if(busquedaNumero){
      console.log(`El telefono numero ${ingresa} pertenece a: ${busquedaNumero}`);
    }else{
      console.log(`Contacto ${contactos} no encontrado`);
    }
    opciones();
    selecionaOpcion();
  });
}

//Ingresar contacto
function ingresarContacto(){
  readline.question('Ingrese el nombre del contacto: ', (nombre) => {
    readline.question('Ingrese el telefono del contacto: ', (telefono) => {
      if(!isNaN(telefono) && telefono.length <= 11){
        contactos[nombre] = telefono;
        console.log(`${nombre} ha sido ingresado con exito`);
      }else{
        console.log('Telefono debe ser numerico y maximo de 11 digitos');
      }
      opciones();
      selecionaOpcion();
    });
  });
}

//Actualizar contacto
function actualizarContacto(){
  readline.question('Ingrese el nombre del contacto que desea actualizar: ', (nombre) => {
    if(contactos[nombre]){
      readline.question('Ingrese el telefono: ', (telefono) => {
        if (!isNaN(telefono) && telefono.length <= 11){
          contactos[nombre] = telefono;
          console.log(`${nombre} ha sido actualizado`);
        }else{
          console.log('Telefono debe ser numerico y de maximo 11 digitos');
        }
        opciones();
        selecionaOpcion();
      });
    }
  });
}

//Eliminar contacto
function eliminarContacto(){
  readline.question('Ingrese el nombre del contacto que desea eliminar: ', (nombre) => {
    if(contactos[nombre]){
      delete contactos[nombre];
      console.log(`${nombre} ha sido eliminado`);
    }else{
      console.log(`${nombre} no se encuentra`);
    }
    opciones();
    selecionaOpcion();
  });
}
