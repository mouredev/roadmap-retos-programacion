/* ESTRUCTURAS DE DATOS EN JAVASCRIPT */

// VARIABLES
let variableLet = "variable let";
const variableConst = "variable const";

// TIPOS DATOS PRIMARIOS
const string = "cadena de texto";
const number = "número";
const boolean = true;
let undefined;
const nullVariable = null;

//ARRAYS
let array = [1, 2, 3, "cuatro", true];
console.log(array);

let elementoArray = array[3]; //Acceder a un elemento dentro del array
console.log(elementoArray);

array = array[3] = "cinco"; //Cambiar un elemento dentro del array
console.log(array);

let frutas = ["banana", "manzana", "pera", "uva"];
console.log(frutas);
frutas = frutas.toString(); //Convierte el array en un string
console.log(frutas);

console.log(array.length); // length = Devuelve la longitud del array

let numeros = [1, 2, 3, 4, 5, 6];
numeros.forEach((numero) => console.log((numero += 1)));

let colores = ["amarillo", "azul", "rojo"];
console.log(colores);
colores.push("negro"); //Agrega un elemento al final de array
console.log(colores);

colores[colores.length] = "marrón";
console.log(colores);

colores.shift(colores); //.shift = Elimina el primer elemento dentro de un array
console.log(colores);

let edades = [20, 15, 33, 46, 18, 25];
edades.sort(); // .sort() = Ordena los elemento dentrode un array
console.log(edades);

/*OBJETOS*/
const objeto = {
  nombre: "Javier",
  edad: 34,
  saludar: function saludo() {
    console.log(`hola`);
  },
};

objeto.saludar(); // Acceder a una propiead del objeto

objeto.apellido = "Rojas"; // Agregar propiedades a un objeto
console.log(objeto);

const persona = {
  nombre: "Pedro",
  apellido: "Perez",
  edad: 30,
  nombreCompleto: function () {
    //Un método es una función almacenada como una propiedad
    console.log(`${this.nombre} ${this.apellido}`);
  },
};
persona.nombreCompleto();
console.log(persona);

/* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

let agenda = [];
let contacto = {};

const readline = require("readline");

const read = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const menu = () => {
  read.question(
    "¡BIENVENIDO! \n Ingrese el número de la operación a realizar \n  1.Agregar | 2.Buscar | 3.Actualizar | 4.Eliminar | 5.Contactos | 6.Finalizar  \n ",
    (operar = (operacion) => {
      switch (operacion) {
        case "1":
          agregarContacto();
          break;
        case "2":
          buscarContacto();
          break;
        case "3":
          actualizarContacto();
          break;
        case "4":
          eliminarContacto();
          break;
        case "5":
          mostrarTodosLosContactos();
          break;
        case "6":
          finalizar();
          break;
        default:
          console.log("Operación no válida");
          read.close();
      }
    })
  );
};
menu();

const repetirOperacion = () => {
  read.question("¿Desea realizar otra operación? 1.Si | 2.No \n", (ope) => {
    if (ope === "1") menu();
    else {
      console.log("Hasta luego");
      read.close();
    }
  });
};

const agregarContacto = () => {
  console.log("Agregar Contacto:");
  read.question("Nombre del Contacto: ", (nombre) => {
    read.question("Número de Teléfono: ", (telefono) => {
      if (isNaN(telefono) | (telefono.length > 11)) {
        console.log("El número de teléfono no es correcto, Intente de nuevo");
        agregarContacto();
      } else contacto = { nombre, telefono };
      agenda.push(contacto);
      console.log(`Contacto ${nombre} agregado con éxtio`);
      repetirOperacion();
    });
  });
};

const buscarContacto = (callback) => {
  console.log("Buscar Contacto:");
  read.question("Nombre del Contacto: ", (nombre) => {
    const encontrado = agenda.filter((contacto) => contacto.nombre === nombre);
    if (encontrado.length > 0) {
      console.log(
        `CONTACTO: \n Nombre: ${contacto.nombre} \n Teléfono: ${contacto.telefono}`
      );
      if (callback) callback(encontrado);
    } else console.log("Contacto no encontrado");
    repetirOperacion();
  });
};

const mostrarTodosLosContactos = () => {
  if (agenda.length < 1) console.log("No hay contactos agregados");
  else console.log(agenda);
  repetirOperacion();
};

const actualizarContacto = () => {
  buscarContacto((encontrado) => {
    if (encontrado) {
      read.question("Nuevo Nombre: ", (nombre) => {
        read.question("Nuevo Teléfono: ", (telefono) => {
          encontrado[0].nombre = nombre;
          encontrado[0].telefono = telefono;
          console.log(`Contacto Actualizado ${nombre} con éxito`);
          repetirOperacion();
        });
      });
    } else {
      console.log("Contacto no encontrado");
    }
  });
};

const eliminarContacto = () => {
  read.question("Nombre: ", (nombre) => {
    agenda = agenda.filter((contacto) => contacto.nombre !== nombre);
    console.log(`Contacto ${nombre} eliminado con éxito`);
    repetirOperacion();
  });
};

const finalizar = () => {
  console.log("Operación Finalizada, !Hasta Luego!");
  read.close();
};
