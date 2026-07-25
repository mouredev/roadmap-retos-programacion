//* formas de crear un objeto

// comun

let persona = {
  nombre: "juan",
  apellido: "martines",
};

// console.log(persona);
// usando la funcion constructura Object()

let productos = new Object();
productos.nombre = "pera";
productos.precio = 1.3;

// console.log(productos);
// objetos con comportamiento, objetos orientados a objetos

class verduras {
  constructor(nombre, precio) {
    this.nombre = nombre;
    this.precio = precio;
  }
}

let verdura = new verduras("brocoli", 2);

// console.log(verdura);

//* arreglos

let arreglo_frutas = ["manzana", "platano", "pera", "zandia"];
let numeros = [1, 2, 3, 4, 5, 6];

// metodo para saber el tamaño del arreglo, se usa .length
//* console.log("el tamaño del arreglo es: ", arreglo_frutas.length);
// un metodo para recorrerlo, seria un for
console.log("--------------------for clasico--------------------------");
for (let i = 0; i < arreglo_frutas.length; i++) {
  console.log(arreglo_frutas[i]);
}

// otra forma seria usando forEach
console.log("-------------------forEach---------------------------------");
arreglo_frutas.forEach((elemento) => {
  console.log(elemento);
});

// otra forma seia con un map, este crea un nuevo arreglo con los resultados de la llamada a
// a la funcion , esto se aplica a cada uno de sus elementos

console.log("------------------------map------------------------------------");
dobles = numeros.map((elemento) => {
  return elemento * elemento;
});

console.log("numeros antes: ");
console.log(numeros);
console.log("numeros al cuadrado ");
console.log(dobles);

//* push(), añade un elemento al final del array y devuelve el tamaño
nuevo_tamaño = arreglo_frutas.push("zanahoria");
// console.log("el nuevo tamañlo del arreglo es: ", nuevo_tamaño);

//* pop(), elimina el último elemento del arreglo y lo devuelte
eliminado = arreglo_frutas.pop();
// console.log("eliminado: ", eliminado);

//* reduce(), ejecuta una funcion reductora sobre cada elemento del array
//* devolviendo como resultado unico valor
// en este caso vamos a sumar los elementos del arreglo numeros

let valor_inicial = 0;
let resultado = numeros.reduce(
  (acumulador, currentValue) => acumulador + currentValue,
  valor_inicial
);
// console.log(" la suma es: ", resultado);

//! Set, son colecciones de valores
// crear un set con valores, los valores tienen que ser unicos
let set = new Set(["nombre", 1]);
console.log(set);
// agregar
set.add(2);
console.log(set);

let nombres = { nombre: "juan", apellido: "parodi" };

set.add(nombres);
console.log(set);
//* has() devuelve un booleano afirmando si un valor está en objeto set o no
console.log(set.has(2));
console.log(set.has(nombres));

//* tamaño del objeto
console.log(set.size);

//* eliminar un elemento del objeto delete(), devuelve un booleano confirmando si se elimino el elemento

console.log(set.delete(nombres));
console.log(set);

//* probando ingresar datos desde el terminal con readline

const { exit } = require("process");
const readline = require("readline");
const rl = readline.createInterface({
  //* rl, es la interface de readline
  //* configurado para
  input: process.stdin, //*  recibir entradas del usuario
  output: process.stdout, //* y mostrar salida
});

// rl.question("ingrese un numero: ", (numero) => {
//   console.log(`el numero es: ${numero}`);
//   rl.close(); // supongo que es para cerrar
// });

//! ejercicio extra:

const patronNumeros = /^\d{1,11}$/; // Expresión regular para validar números de 1 a 11 dígitos;
let ejecutando = true; //* funcion para ejecutar bucle en el menu
//* array con las opciones del menu
let CONTACTOS = [{ nombre: "pedro", telefono: 98999878978 }];
const datos_menu = [
  { num: "1.", option: " ingresar contacto" },
  { num: "2.", option: " buscar contacto " },
  { num: "3.", option: " actualizar contacto" },
  { num: "4.", option: "borrar contacto" },
  { num: "5.", option: " ordenar contactos" },
  { num: "6.", option: " salir" },
];

class InfoContacto {
  constructor(nombre, telefono) {
    this.nombre = nombre;
    this.telefono = telefono;
  }
}

//* funcion para hacer preguntas de forma asincrona
const ask = (text) => {
  return new Promise((resolve) => rl.question(text, resolve));
};

//* 1. funcion para ingresar un nuevo contacto:
async function ingresarContacto() {
  console.log("\n\t ingresar contactos \n");
  let nombre = await ask("ingresa el nombre del contacto: ");
  let telefono = await ask("ingresa el telefono: ");
  if (patronNumeros.test(telefono)) {
    let contacto = new InfoContacto(nombre, telefono);
    CONTACTOS.push(contacto);
    console.log(
      `nuevo contacto: ${contacto.nombre} \n Movil:${contacto.telefono}\n`
    );
    console.log("contacto agregado\n");
  } else {
    console.warn(" solo se permiten un maximo de 11 numeros ");
  }
}

//* 2. funcion para buscar contacto:
async function buscarContacto(buscar) {
  let i = 0;
  let encontrado = false;
  for (const elemento of CONTACTOS) {
    if (Object.is(elemento.nombre, buscar)) {
      console.log(" se encontro el contacto ");
      encontrado = true;
      break;
    }
    i++;
  }
  if (!encontrado) {
    console.log("no se encontro el contacto");
    return false;
  } else {
    console.log(
      `contacto: ${CONTACTOS[i].nombre} \n Movil: ${CONTACTOS[i].telefono}`
    );
    return i;
  }
}

//* 3. actualizar contacto
async function actualizarContacto() {
  console.log("\n\t actualizar contacto\n");
  let buscar = await ask("ingrese el nombre a buscar: ");
  let i = await buscarContacto(buscar);
  if (i !== false) {
    console.log("ingrese datos a actualizar: ");
    let new_nombre = await ask("ingrese el nombre: ");
    let new_telefono = await ask("ingrese el numero: ");
    CONTACTOS[i].nombre = new_nombre;
    CONTACTOS[i].telefono = new_telefono;
    console.info(
      `contacto actualizado: \n ${CONTACTOS[i].nombre} \n Movil: ${CONTACTOS[i].telefono}`
    );
  }
}

//* 4. borrar contacto
async function borrarContacto() {
  console.log("\n\t eliminar contacto: \n");
  let buscar = await ask("ingrese el nombre del contacto: ");
  let i = await buscarContacto(buscar);
  if (i !== false) {
    CONTACTOS.splice(i, 1);
    console.log("contacto eliminado");
  }
}

//* 5. funcion para mostrar los contactos ordenados:
function ordenarContactos() {
  console.log("\n\t contactos: \n");
  CONTACTOS.forEach((element) => {
    console.log(`${element.nombre} \n Movil:${element.telefono}\n`);
  });
}

//* 6. funcion para salir
const salir = () => {
  console.log("\n adiosssssssssssss");
  ejecutando = false;
  rl.close();
  process.exit(0);
};

//* funcion principal, menu
const menu = async () => {
  while (ejecutando) {
    console.log("\n\t menu: \n");
    console.table(datos_menu);
    let answer = await ask("ingrese la opcion: ");
    switch (answer) {
      case "1":
        await ingresarContacto();
        break;
      case "2":
        console.log("\n\t bucar contacto: \n");
        let buscar = await ask("nombre a buscar: ");
        await buscarContacto(buscar);
        break;
      case "3":
        await actualizarContacto();
        break;
      case "4":
        await borrarContacto();
        break;
      case "5":
        ordenarContactos();
        break;
      case "6":
        salir();
        break;
      default:
        console.info("\nopcion no valida\n");
        break;
    }
  }
};

menu();
