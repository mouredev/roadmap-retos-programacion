/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 */

/**
 *
 * DATOS PRIMITIVOS
 *
 *  */
// undefined
const noDefinido: undefined = undefined;
console.log(typeof noDefinido);

// null
const isNull: null = null;
console.log(typeof isNull);

// booleano
const tengoFe: boolean = true;
console.log(typeof tengoFe);

// number
const partidosGanados: number = 5;
console.log(typeof partidosGanados);

// string
const titulo: string = "La casa de papel";
console.log(typeof titulo);

/**
 *
 * OBJETOS
 *
 * */

// Arrays
let misHobbies: string[] = ["Fotografía", "Cómics"];
let edatAmigos: number[] = [23, 25, 21, 24];

// Tuplas
let artist: [string, number] = ["Bon Iver", 2];

/**
 *  Maps ( a diferència de los arrays no se tiene en cuenta el orden de los elementos,
 *  se accede a ellos mediante la clave).
 *
 * */

let myMap = new Map<string, number>([
  ["Guillem", 34],
  ["Carol", 23],
]);

myMap.set("Anna", 35); // Añade una clave y un valor.

myMap.get("Carol"); // Obtenemos el valor de la clave 'Carol', 23.

myMap.has("Carol"); // Comprueba que exista la clave 'Carol'.

myMap.delete("Carol"); // Elimina esta clave.

console.log(myMap.get("Carol")); // Devuelve undefined.

for (const [key, value] of myMap) {
  console.log(key + " - " + value); // Mostramos todas las claves y valores.
}

// Set los elementos pueden ser de qualquier tipo y no se tiene en cuenta el orden;

let misDatos = new Set();

misDatos.add(20);
misDatos.add(["pepino", "almendras"]);
misDatos.add({ nombre: "Pepe", edad: 14 });
misDatos.add("Escuela de dibujo");
misDatos.has(20); // true.

for (const iterator of misDatos) {
  console.log(iterator); // Mostramos los diferentes elementos.
}

/**
 * Stack (Pila) - datos estructurados en forma de lista.
 *
 * LIFO last in first out - El último que entra, es el primero en salir.
 *
 * */

// Ejemplo con un array.
let misFrutas: string[] = ["Fresas", "Manzanas", "Platanos"];

misFrutas.push("Naranjas");
console.log(misFrutas);
misFrutas.pop();
console.log(misFrutas);

/**
 * QUEU (Cola) - datos estructurados en forma de lista
 *
 * FIFO First in first out - El primero que entra, es el primero en salir.
 *
 */

let pedidos: string[] = ["Enviar pedido 1", "Enviar pedido 2"];
pedidos.push("Enviar pedido 3");
console.log(pedidos);
pedidos.shift();
console.log(pedidos);

/**
 * LISTAS ENLAZADAS
 *
 * Similares a un array
 * los elementos NO son almacenados en memoria o indice en particular
 * cada elemento es un objecto que apunta al siguiente objeto.
 * Cada elemento contiene un nodo que se compone de un valor y enlace al siguiente nodo.
 * Si una lista esta vacía, la cabezera es una referencia nula.
 *
 * Ventajas: removidos o agregados sin importar orden. Al contrario que los arrays.
 * Desventajas: las operaciones de busqueda son lentas.
 *              uso mayor de memoria que los arreglos
 *
 * Tipos de listas enlazadas:
 *  - individuales
 *  - doblemente enlazadas
 *  - circulares enlazadas
 *
 * Ejemplo lista enlazada individual:
 */

class Nodo {
  constructor(private value: number, public siguiente: any = null) {
    this.value = value;
    this.siguiente = null;
  }
}

class listaEnlazada {
  private cabezera: any;
  private cola: any;
  constructor() {
    this.cabezera = null;
    this.cola = null;
  }

  append(valor: number) {
    const newNode = new Nodo(valor);
    if (!this.cabezera) {
      this.cabezera = newNode;
    } else {
      this.cola.siguiente = newNode;
    }

    this.cola = newNode;
  }

  traverse(callback: any) {
    let currentNode = this.cabezera;

    while (currentNode !== null) {
      callback(currentNode);
      currentNode = currentNode.siguiente;
    }
  }
}

const printNode = (node: any) => console.log(node.value);

let miLista = new listaEnlazada();

miLista.append(6);
miLista.append(8);
miLista.append(9);

miLista.traverse(printNode);

/**
 * Trees (Arboles) - Estructura de datos en forma de arbol.
 *
 * Parten de un nodo raiz, y tienen una relación padre / hijo.
 * Los nodos que no tienen hijo, se llaman nodos hoja (leaf nodes).
 * La altura del arbol, se determina por la cantidad de connexiones padre /hijo.
 *
 * Un ejemplo de estructura de arbol seria el model DOM (Document Object Model).
 *
 * Hay diferentes tipos de estructuras de arbol, però las más comunes són:
 *  - Binary trees
 *  - Heaps
 *  */

/**
 * Graphs (Grafos) - Estructura de datos en forma de gràfico.
 *
 * No parten de un nodo raiz. Todos los nodos estan conectados entre ellos.
 *
 * Las estructuras de datos gràfico són útiles para la creacion de aplicaciones
 * de redes sociales.
 *
 * Hay diferentes tipos de grafos
 *  - Directos e indirectos
 *  - Pesado o ligeros.
 */

/*
 * EJERCICIO EXTRA:
 *
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */

interface tipoContacto {
  nombre: string;
  telefono: number | null;
}

class Contacto implements tipoContacto {
  public nombre: string;
  public telefono: number;
  constructor(nombre: string, telefono: number) {
    this.nombre = nombre;
    this.telefono = telefono;
  }
}

class ListaContactos {
  private lista: tipoContacto[];
  private contacto: Contacto;
  constructor() {
    this.lista = [];
    this.contacto = { nombre: "", telefono: 0 };
  }

  // Buscar
  buscar(nombre: string) {
    if (this.lista.length > 0) {
      let encontrado = false;
      this.lista.forEach((element) => {
        if (element.nombre == nombre) {
          console.log(`Se ha encontrado este contacto ${element.nombre} - ${element.telefono}`);
          encontrado = true;
        }
      });
      if (!encontrado) {
        console.log(`No se ha encontrado ningun contacto con el nombre ${nombre}`);
      }
    } else {
      console.log("No existe ningun contacto.");
    }
  }

  // Inserir
  inserir(nombre: string, telefono: number) {
    const contacto = new Contacto(nombre, telefono);
    this.lista.push(contacto);
    console.log(`El contacto (${contacto.nombre}) se ha inscrito correctamente`);
  }

  // Actualizar
  actualizar(nombre: string, telefono: number) {
    let encontrado = false;
    this.lista.forEach((element) => {
      if (element.nombre === nombre) {
        element.telefono = telefono;
        console.log(`El contacto (${element.nombre}) se ha actualizado correctamente`);
        encontrado = true;
      }
    });
    if (!encontrado) {
      console.log(`El contacto ${nombre} no existe, por eso no se puede actualizar.`);
    }
  }

  // Eliminar
  eliminar(nombre: string) {
    const index = this.lista.findIndex((item) => item.nombre === nombre);

    if (index !== -1) {
      this.lista.splice(index, 1);
      console.log(`El contacto ${nombre} se ha eliminado de la Agenda de Contactos.`);
    } else {
      console.log(`El contacto  ${nombre} no existe.`);
    }
  }

  // Mostrar todos los contactos
  mostrarContactos() {
    console.log("======== CONTACTOS =======");
    if (this.lista.length > 0) {
      this.lista.forEach((element, indice) => {
        console.log(`Nombre: ${element.nombre}, teléfono: ${element.telefono}`);
      });
    } else {
      console.log("No hay contactos que mostrar.");
    }

    console.log("==========================");
  }
}

let miListaContactos = new ListaContactos();
let salirContactos = false;

while (salirContactos === false) {
  // Menú inicial
  const accion = prompt(`
    ==================
    AGENDA CONTACTOS
    ==================
    ______________________________________________
    
    Qué acción quieres realizar? (teclear el número) 
    
    Buscar (1) 
    Inserir (2)
    Actualizar (3)
    Mostar (4)
    Eliminar (5) 
    Salir (6)
    ______________________________________________`);

  switch (accion) {
    case "1": // Buscar
      const buscarNombre = prompt("Escribe el nombre del contacto a buscar.");
      if (buscarNombre) {
        miListaContactos.buscar(buscarNombre);
      }
      break;
    case "2": // Inserir
      const inserirNombre = prompt("Escribe el nombre");
      const inserirTelefono: any = prompt("Escribe el telefono (max 11 números)");

      // Validación todo números
      const regExp = /[a-z A-Z]/;
      const tieneLetras = regExp.test(inserirTelefono.toString());

      // Validación cantidad caracteres
      let tieneMas = false;
      if (inserirTelefono.length >= 11) {
        tieneMas = true;
      } else {
        tieneMas = false;
      }

      if (inserirNombre && inserirTelefono && !tieneLetras && tieneMas === false) {
        miListaContactos.inserir(inserirNombre, parseInt(inserirTelefono));
      } else {
        console.log(`El contacto ${inserirNombre}, no se ha podido inserir correctamente.`);
      }
      break;
    case "3": // Actualizar
      const contactoActualizar = prompt("Escribe el nombre del contacto a buscar.");
      const telefonoActualizar = prompt("Escribe el nuevo telefono.");
      if (contactoActualizar && telefonoActualizar) {
        miListaContactos.actualizar(contactoActualizar, parseInt(telefonoActualizar));
      } else {
        console.log(`Por falta de datos, el contacto ${contactoActualizar} no se ha podido actualizar.`);
      }
      break;

    case "4": // Mostrar
      miListaContactos.mostrarContactos();
      break;

    case "5": // Eliminar
      const contactoEliminar = prompt("Escribe el nombre del contacto a eliminar.");
      if (contactoEliminar) {
        miListaContactos.eliminar(contactoEliminar);
      } else {
        console.log("No has escrito ningun nombre.");
      }
      break;

    case "6": // Salir
      salirContactos = true;
      console.log("Saliste de la Agenda de Contactos, hasta pronto!");
      break;

    default:
      console.log("Hola seleccione un número de acción a realizar!");
      break;
  }
}

/**
 * Recursos consultados:
 *
 *  - https://www.freecodecamp.org/news/data-structures-in-javascript-with-examples/
 *  - https://www.youtube.com/watch?v=yxqBvC6YMgA
 *
 */
