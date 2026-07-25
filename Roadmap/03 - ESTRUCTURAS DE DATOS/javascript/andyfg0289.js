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

//Ejercicio:

//----Arreglos (Arrays) ----//

let arreglo = ["rojo", "azul", "amarillo"];

//insersión

arreglo.push("verde");
console.log(arreglo); //Array(4) [ "rojo", "verde", "amarillo", "verde" ]

//Borrado
arreglo.splice(3, 1);
console.log(arreglo); //Array(3) [ "rojo", "azul", "amarillo" ]

//Actualización

arreglo[0] = "verde";
console.log(arreglo); //Array(3) [ "verde", "azul", "amarillo" ]

//Ordenación
let numeros = [6, 3, 8, 21, 42, 11, 20];

numeros.sort((a, b) => a - b);

console.log(numeros); //Array(7) [ 3, 6, 8, 11, 20, 21, 42 ]

//---- Objetos ----//

let miObjeto = {
  nombre: "Andy",
  apellido: "Fernandez",
  edad: 30,
};

console.log(miObjeto);

//insersión

miObjeto.direccion = "La direccion";

console.log(miObjeto);

//Borrado
delete miObjeto.direccion;
console.log(miObjeto);

//Actualización
miObjeto.edad = 35;
//Ordenación

let listaD = { d: 4, c: 3, a: 1, b: 2 };

let keysOrdenadas = Object.keys(listaD).sort();
console.log("LLaves ordenadas", keysOrdenadas); //Array(4) [ "a", "b", "c", "d" ]

let objetoOrdenado = {};
keysOrdenadas.forEach((key) => (objetoOrdenado[key] = listaD[key]));
console.log(objetoOrdenado); //Object { a: 1, b: 2, c: 3, d: 4 }

//---- Sets ----//

let MiSet = new Set([1, 2, 3]);

//insersión
MiSet.add(4);
console.log(MiSet); //Set(4) [ 1, 2, 3, 4 ]

//Borrado
MiSet.delete(2);
console.log(MiSet); //Set(3) [ 1, 3, 4 ]

//Actualización
if (MiSet.has(1)) {
  MiSet.delete(1);
  MiSet.add(10);
}
console.log(MiSet); //Set(3) [ 3, 4, 10 ]

//Ordenación

let SetDes = new Set([7, 2, 4, 3, 1, 5, 6]);

let ordenado = Array.from(SetDes).sort((a, b) => a - b);
console.log(ordenado); //Array(7) [ 1, 2, 3, 4, 5, 6, 7 ]

//----  WeakSets ----//  WeakSet solo permite almacenar objetos y no admite ordenación directa.

let weakSet = new WeakSet();
let obj1 = { a: 1 };
let obj2 = { b: 2 };
let obj3 = { c: 3 };
//insersión
weakSet.add(obj1);
weakSet.add(obj2);
weakSet.add(obj3);

console.log(weakSet);
//Borrado

weakSet.delete(obj1);
console.log(weakSet);
// Actualización (no aplica en WeakSet)

// Ordenación (no aplica en WeakS

//---- Mapas o (Map) ----//

let map = new Map();
map.set("a", 1);
map.set("b", 2);

//insersión
map.set("c", 3);
console.log(map);
//Borrado
map.delete("b");
console.log(map);
//Actualización

map.set("a", 10);
console.log(map);
//Ordenación
let mapOrdenado = new Map([...map].sort((a, b) => a[1] - b[1]));
console.log(mapOrdenado);

//usando array from
let mapOrdenado2 = new Map(
  Array.from(map.entries()).sort((a, b) => a[1] - b[1])
);

//DIFICULTAD EXTRA (opcional):
/* Ejecutar en un navegador dado que no use linebyline para usarlo en cualquiuer consola con node
 -Se puede usar con el prompt o simplemente mediante los "COMANDOS" por la consola
 - Usar init() para iniciar el programa.
 */
console.log(`#     #            #                         
  ##   ## #         # #    ####  ###### #    # #####    ## 
  # # # # #        #   #  #    # #      ##   # #    #  #  #  
  #  #  # # ##### #     # #      #####  # #  # #    # #    # 
  #     # #       ####### #  ### #      #  # # #    # ###### 
  #     # #       #     # #    # #      #   ## #    # #    # 
  #     # #       #     #  ####  ###### #    # #####  #    #\n\ninit() --> PAra iniciar Agenda \nhelp() --> Ayuda"`);

let contactos = [
  { id: 1, nombre: "Juan Pérez", telefono: 123456789032 },
  { id: 2, nombre: "María García", telefono: 987654321074 },
  { id: 3, nombre: "Luis Rodríguez", telefono: 555123456735 },
  { id: 4, nombre: "Ana López", telefono: 777888999944 },
  { id: 5, nombre: "Carlos Fernández", telefono: 444555666622 },
];

let miagenda;

const help = () => {
  const ayuda = [
    {
      comando: "init()",
      accion: "Inicializar Agenda",
    },
    {
      comando: "miagenda.listar()",
      accion: "Muestra el listado de contactos",
    },
    {
      comando: "miagenda.actualizar()",
      accion: "Actualiza un contacto mediante la ID ",
    },
    {
      comando: "miagenda.agregar()",
      accion: "Agrega un contacto nuevo",
    },
    {
      comando: "miagenda.eliminar()",
      accion: "Elimina un contacto mediante la ID ",
    },
    {
      comando: "miagenda.buscar()",
      accion: "Buscar contacto",
    },
    {
      comando: "miagenda.salir()",
      accion: "Finaliza la Agenda",
    },
  ];

  console.table(ayuda);
};

class Agenda {
  constructor(contactos) {
    this.contactos = contactos;
    help();
  }
}

class miAgenda extends Agenda {
  mensage = (mensaje, color, fondo) => {
    console.log(
      `%c${mensaje}`,
      `background-color:${fondo};color:${color};padding: 5px 10px;`
    );
  };
  listar = () => {
    this.contactos.length == 0
      ? console.log("No hay contactos para mostrar")
      : console.table(this.contactos);

    inicio();
  };

  actualizar = () => {
    const secId = verfId(this.contactos);
    let id = 0;

    for (let i = 0; i < this.contactos.length; i++) {
      if (this.contactos[i].id === secId) {
        id = i;
        break;
      }
    }

    if (secId !== null) {
      const name = prompt("Actualizar nombre", this.contactos[id].nombre);

      if (name === null || name.trim() === "") {
        this.mensage("No se puede dejar el nombre vacío", "white", "red");
        inicio();
        return;
      }

      let telefono = prompt("Actualizar Teléfono", this.contactos[id].telefono);
      telefono = Number(telefono);
      if (!Number.isInteger(telefono) || telefono.toString().length > 11) {
        this.mensage(
          "Debe introducir un numero de teléfono de 11 digítos",
          "white",
          "red"
        );
        inicio();
        return;
      }

      this.contactos[id].nombre = name.toString();
      this.contactos[id].telefono = telefono;
      this.listar();
      inicio();
    }
  };
  agregar = () => {
    const secId =
      this.contactos.length > 0
        ? this.contactos[this.contactos.length - 1].id + 1
        : 0;

    const name = prompt("Nombre: ");

    if (name === null || name.trim() === "") {
      this.mensage("No se puede dejar el nombre vacío.", "white", "red");
      inicio();
      return;
    }

    let telefono = prompt("Telefono: ");
    telefono = Number(telefono);
    if (!Number.isInteger(telefono) || telefono.toString().length > 11) {
      this.mensage(
        "Debe introducir un numero de telefono de 11 digitos como monimo ",
        "white",
        "red"
      );
      inicio();
      return;
    }

    const nuevoContacto = {
      id: secId,
      nombre: name,
      telefono: telefono,
    };

    this.contactos.push(nuevoContacto);
    this.mensage("Nuevo contacto agregado", "white", "green");
    this.listar();
    inicio();
  };

  eliminar = () => {
    const secId = verfId(this.contactos);
    console.log(secId);
    if (secId !== null) {
      this.mensage("Contacto Eliminado ", "white", "red");
      const del = this.contactos.filter((contacto) => contacto.id !== secId);

      this.contactos = del;
      this.listar();
      inicio();
    }
  };

  buscar = () => {
    const input = prompt("Buscar en la agenda");
    const textRegex = new RegExp(/^[a-zA-Z\s]+$/);
    const numRegex = new RegExp(/^[0-9\s]+$/);
    const textNumRegex = new RegExp(/^(?=.*[a-zA-Z])(?=.*\d).+$/);
    let searchResult = [];

    if (input === null || input.trim() === "") {
      this.mensage("No se puede dejar el nombre vacío.", "white", "red");
      inicio();
      return;
    }

    if (textRegex.test(input)) {
      function eliminarAcentos(texto) {
        return texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
      }

      function eliminarAcentosYEspacios(texto) {
        return eliminarAcentos(texto).replace(/\s+/g, "").toLowerCase();
      }
      const palabrasInput = eliminarAcentos(input).toLowerCase().split(/\s+/);

      for (let i = 0; i < this.contactos.length; i++) {
        const nombreContacto = eliminarAcentosYEspacios(
          this.contactos[i].nombre
        );
        for (let j = 0; j < palabrasInput.length; j++) {
          const regex = new RegExp(palabrasInput[j], "i");

          if (regex.test(nombreContacto)) {
            searchResult.push(this.contactos[i]);
            break;
          }
        }
      }

      if (searchResult.length == 0) {
        miagenda.mensage("No se encontro el contacto", "white", "red");
        inicio();
        return;
      }

      console.table(searchResult);
    }

    if (numRegex.test(input)) {
      let telefono = input;
      telefono = Number(telefono);

      for (let i = 0; i < this.contactos.length; i++) {
        if (
          this.contactos[i].telefono.toString().includes(telefono.toString())
        ) {
          searchResult.push(this.contactos[i]);
        }
      }

      if (searchResult.length == 0) {
        miagenda.mensage("No se encontro el contacto", "white", "red");
        inicio();
        return;
      }
      console.table(searchResult);
    }

    if (textNumRegex.test(input)) {
      miagenda.mensage(
        "Introduzca una palabra clave o un numero telefononico correctos",
        "white",
        "red"
      );
      return;
    }
    console.log("Resultado de buscar:", input);
    inicio();
  };

  salir = () => {
    console.clear();
    miagenda = null;
    console.log("%cPrograma finalizado.", "color: red");
  };
}

const verfId = (lista) => {
  const id = prompt("Introduzca ID del contacto", "#id");
  let secId = Number(id);
  if (id === "") {
    miagenda.mensage(
      "Proporcione una id valida: No puede estar vacia",
      "white",
      "red"
    );
    inicio();
    return (secId = null);
  }

  if (!Number.isInteger(secId) || secId === "") {
    miagenda.mensage(
      "Proporcione una id valida: debe ser un número entero",
      "white",
      "red"
    );
    inicio();
    return (secId = null);
  }

  if (secId < 0) {
    console.log(lista[0]);
    miagenda.mensage(
      "Proporcione una id valida: Use listar() --> Mostrar contactos",
      "white",
      "red"
    );
    inicio();
    return (secId = null);
  }

  for (let i = 0; i < lista.length; i++) {
    if (lista[i].id === secId) {
      return secId;
    }
  }

  miagenda.mensage(
    "El id proporcionado no existe en los contactos",
    "white",
    "red"
  );
  inicio();
  return (secId = null);
};

const init = () => {
  console.log(
    "%cAgenda Iniciada",
    "color: white ; background-color:green;padding: 5px 10px;"
  );
  miagenda = new miAgenda(contactos);
  inicio();
};

const inicio = () => {
  const opcion = prompt(
    "(1: LIST - 2: UPDATE - 3: ADD - 4: DEL - 5: FIND - 6: QUIT)"
  );

  switch (opcion) {
    case "1":
      console.log("Hola mundo");
      miagenda.listar();
      break;

    case "2":
      miagenda.actualizar();
      break;

    case "3":
      miagenda.agregar();
      break;

    case "4":
      miagenda.eliminar();
      break;

    case "5":
      miagenda.buscar();
      break;

    case "6":
      miagenda.salir();
      break;

    default:
      // miagenda.salir();
      break;
  }
};
