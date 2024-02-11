// ESTRUCTURA DE DATOS

// arrays:

const arr: number[] = [1, 2, 3, 4, 5];

arr.pop();

console.log(arr);

// Tuples

const tuple: [string, number] = ["Daniel", 23];

// Objetos:

const obj: {
  nombre: string;
  edad: number;
  online: boolean;
} = {
  nombre: "Pablo",
  edad: 42,
  online: false,
};

// Clases

class Person {
  name: string;
  constructor(name: string) {
    this.name = name;
  }

  sayHello() {
    console.log(`Hola ${this.name}`);
  }
}

const person1 = new Person("Pablo");
console.log(person1.sayHello());

// Interface

interface Animal {
  name: string;
  age: number;
}

let perro: Animal = { name: "Pupi", age: 9 };

perro = { name: "Dodo", age: 3 };

console.log(perro);

// Enum

enum Colores {
  Rojo,
  Verde,
  Azul,
}

let color: Colores = Colores.Verde;

color = Colores.Azul;

// Sets

let someSet: Set<number> = new Set();

someSet.add(23);
someSet.add(44);
someSet.add(109);

someSet.delete(23);

console.log(someSet);

// Map

let mapa: Map<string, number> = new Map();

mapa.set("uno", 1);
mapa.set("dos", 2);
mapa.set("tres", 3);

mapa.delete("dos");

mapa.set("uno", 10);

console.log(mapa);

//Extra

import * as readlineSync from "readline-sync";

const agenda: {
  nombre: string;
  telefono: string;
}[] = [];

function agregarContacto(): void {
  try {
    const nombre: string = readlineSync.question(
      "Ingrese el nombre del nuevo contacto: "
    );
    let telefono: string;
    while (true) {
      telefono = readlineSync.question(
        "Ingrese el teléfono del nuevo contacto: "
      );

      if (/^\d{1,11}$/.test(telefono)) {
        break;
      } else {
        console.log(
          "El teléfono debe ser numérico y tener 11 dígitos. Inténtelo de nuevo."
        );
      }
    }

    const nuevoContacto = { nombre, telefono };

    agenda.push(nuevoContacto);

    console.log("El nuevo registro ha sido creado con éxito");
  } catch (error) {
    console.error(error);
  }
}

function mostrarAgenda(): void {
  if (agenda.length !== 0) {
    agenda.forEach((contacto) => {
      console.log(
        `\nNombre: ${contacto.nombre} \nTeléfono: ${contacto.telefono}`
      );
    });
  } else {
    console.log("No hay contactos aún. Ingrese un nuevo contacto");
  }
}

function buscarContacto(): void {
  const nombre: string = readlineSync.question(
    "Ingrese el nombre del contacto que busca: "
  );
  const encontrado = agenda.find(
    (valor) => valor.nombre.toLocaleLowerCase() === nombre.toLocaleLowerCase()
  );
  if (encontrado) {
    console.log(
      `El contacto es ${encontrado.nombre} y su teléfomo es ${encontrado.telefono}`
    );
  } else {
    console.log("No se encuentra el contacto");
  }
}

function eliminarContacto(): void {
  const nombre: string = readlineSync.question(
    "Ingrese el nomnre del contacto que quiere elminar: "
  );
  const encontrado = agenda.find(
    (valor) => valor.nombre.toLocaleLowerCase() === nombre.toLocaleLowerCase()
  );
  if (encontrado) {
    const confirmacion: string = readlineSync.question(
      `¿Quiere eliminar a ${encontrado.nombre} cuyo teléfono es ${encontrado.telefono}? Escriba: si / no: `
    );
    switch (confirmacion) {
      case "si":
        eliminar(encontrado);
        break;
      case "no":
        console.log("No se elimna el contacto");
        break;
      default:
        console.log("Opción no válida. Inténtelo de nuevo.");
    }
  } else {
    console.log("No se encuentra el contacto");
  }

  function eliminar(contacto: { nombre: string; telefono: string }): void {
    const index = agenda.findIndex((c) => c.nombre === contacto.nombre);
    agenda.splice(index, 1);
    console.log("El contacto ha sido eliminado con éxito.");
  }
}

function editarContacto(): void {
  const nombre: string = readlineSync.question(
    "Ingrese el nombre del contacto que quiere editar: "
  );

  const indice = agenda.findIndex(
    (c) => c.nombre.toLocaleLowerCase() === nombre.toLocaleLowerCase()
  );

  if (indice !== -1) {
    console.log(
      `Contacto encontrado: ${agenda[indice].nombre} - ${agenda[indice].telefono}`
    );

    const nuevoNombre: string = readlineSync.question(
      "Ingrese el nuevo nombre (deje en blanco para mantener el actual): "
    );
    const nuevoTelefono: string = readlineSync.question(
      "Ingrese el nuevo teléfono (deje en blanco para mantener el actual): "
    );

    agenda[indice].nombre = nuevoNombre || agenda[indice].nombre;
    agenda[indice].telefono = nuevoTelefono || agenda[indice].telefono;

    console.log("El contacto ha sido actualizado con éxito.");
  } else {
    console.log("No se encuentra el contacto en la agenda.");
  }
}

function main(): void {
  let bucle: boolean = true;
  while (bucle) {
    console.log("\n== Menú ==");
    console.log("1. Agregar contacto");
    console.log("2. Mostrar contactos");
    console.log("3. Buscar contactos");
    console.log("4. Eliminar contacto");
    console.log("5. Actualizar contacto");
    console.log("6. Salir");

    const opcion = readlineSync.questionInt("Seleccione una opción: ");

    switch (opcion) {
      case 1:
        agregarContacto();
        break;
      case 2:
        mostrarAgenda();
        break;
      case 3:
        buscarContacto();
        break;
      case 4:
        eliminarContacto();
        break;
      case 5:
        editarContacto();
        break;
      case 6:
        console.log("Saliendo de la aplicación. ¡Hasta luego!");
        bucle = false;
        break;
      default:
        console.log("Opción no válida. Inténtelo de nuevo.");
    }
  }
}

main();
