// Ejemplo de array

let array: number[] = [1, 2, 3, 4, 5];
console.log(array);

// Añadiendo un elemento al final del array

array.push(6);
console.log(array);

// Añadiendo un elemento al principio del array

array.unshift(0);
console.log(array);

// Añadir en un índice concreto

array.splice(3, 0, 3.5);
console.log(array);

// Eliminar el último elemento del array

array.pop();
console.log(array);

// Eliminar el primer elemento del array

array.shift();
console.log(array);

// Eliminar un elemento en un índice concreto

array.splice(3, 1);
console.log(array);

// Ejemplo de objeto

let objeto: { [key: string]: string | number } = {
    nombre: "Miguel",
    apellidos: "Delgado",
    edad: 20
}

console.log(objeto);

// Añadir campo a un objeto

objeto.direccion = "Calle falsa 123";
console.log(objeto);

// Eliminar campo de un objeto

delete objeto.edad;
console.log(objeto);

// Ejemplo de map

let mapa: Map<string, string | number> = new Map();

mapa.set("nombre", "Miguel");
mapa.set("apellidos", "Delgado");
mapa.set("edad", 20);

console.log(mapa);

// Añadir al mapa

mapa.set("direccion", "Calle falsa 123");
console.log(mapa);

// Eliminar del mapa

mapa.delete("edad");
console.log(mapa);

// Ejemplo de set

let set: Set<string | number> = new Set();

set.add("Miguel");
set.add("Delgado");
set.add(20);

console.log(set);

// Añadir al set

set.add("Calle falsa 123");
console.log(set);

// Eliminar del set

set.delete(20);
console.log(set);

// Extra

import readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const agenda: { [key: string]: string } = {};

function validarNumeroTelefono(numero: string): boolean {
  return /^\d{1,11}$/.test(numero);
}

function ejecutarPrograma(): void {
  rl.question('¿Qué operación deseas realizar? (buscar, insertar, actualizar, eliminar, salir): ', (operacion: string) => {
    operacion = operacion.toLowerCase();

    if (operacion === 'salir') {
      console.log('Saliendo del programa. ¡Hasta luego!');
      rl.close();
    } else if (operacion === 'buscar') {
      rl.question('Ingrese el nombre del contacto a buscar: ', (nombre: string) => {
        if (agenda[nombre]) {
          console.log(`Nombre: ${nombre}, Teléfono: ${agenda[nombre]}`);
        } else {
          console.log(`El contacto "${nombre}" no se encuentra en la agenda.`);
        }
        ejecutarPrograma(); 
      });
    } else if (operacion === 'insertar') {
        rl.question('Ingrese el nombre del nuevo contacto: ', (nombre: string) => {
        rl.question('Ingrese el número de teléfono del nuevo contacto: ', (telefono: string) => {
          if (validarNumeroTelefono(telefono)) {
            agenda[nombre] = telefono;
            console.log(`Contacto "${nombre}" insertado correctamente.`);
          } else {
            console.log('Número de teléfono no válido. Debe ser numérico y tener entre 1 y 11 dígitos.');
          }
          ejecutarPrograma(); 
        });
      });
    } else if (operacion === 'actualizar') {
        rl.question('Ingrese el nombre del contacto a actualizar: ', (nombre: string) => {
        if (agenda[nombre]) {
          rl.question('Ingrese el nuevo número de teléfono: ', (nuevoTelefono: string) => {
            if (validarNumeroTelefono(nuevoTelefono)) {
              agenda[nombre] = nuevoTelefono;
              console.log(`Contacto "${nombre}" actualizado correctamente.`);
            } else {
              console.log('Número de teléfono no válido. Debe ser numérico y tener entre 1 y 11 dígitos.');
            }
            ejecutarPrograma(); 
          });
        } else {
          console.log(`El contacto "${nombre}" no se encuentra en la agenda.`);
          ejecutarPrograma(); 
        }
      });
    } else if (operacion === 'eliminar') {
        rl.question('Ingrese el nombre del contacto a eliminar: ', (nombre: string) => {
        if (agenda[nombre]) {
          delete agenda[nombre];
          console.log(`Contacto "${nombre}" eliminado correctamente.`);
        } else {
          console.log(`El contacto "${nombre}" no se encuentra en la agenda.`);
          ejecutarPrograma(); 
        }
      });
    }
  });
}

ejecutarPrograma();
