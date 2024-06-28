/*
 * EJERCICIO:
 1 - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 1.1 DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

//------------------------------------------------------------------------------------------------------

/* 1
    Arrays */

    let array = [1, 6, 54, "Joaquin"]

console.log(array) // [1, 6, 56, "Joaquin"]

 // operacion de insercion de datos al final de array

    array.push("Lopez");

console.log(array) // [1, 6, 54, "Joaquin", "Lopez"]

 // operacion de insercion de datos al principio de un array

    array.unshift(1000);

console.log(array) // [1000, 1, 6, 54, "Joaquin", "Lopez"]

// operacion de eliminacion al final de un array

    array.pop();

console.log(array) //[1000, 1, 6, 54, "Joaquin"]

// operacion de eliminacion al principio de un array

    array.shift();

console.log(array) //[1, 6, 54, "Joaquin"]

// actualizar el valor de un elemento del array 

  array[2] = "Lopez" // donde [2] es el lugar donde se encuentra "54"

console.log(array) //[1, 6, "Lopez", "Joaquin"]

// ordenar un array

  array.sort()

console.log(array); // [1, 6, "Joaquin", "Lopez"]



// Objetos

let Aprendiz = {
    nombre: "Joaquin",
    apellido: "Lopez",
    lenguaje: "Javascript",
    edad: 25
  };
  
  // Insertar una propiedad nueva al objeto
  Aprendiz.pais = "Argentina";

  console.log(Aprendiz); // {nombre: "Joaquin", apellido: "Lopez", lenguaje: "Javascript", edad: 25, pais: "Argentina"}
  
  // Eliminar una propiedad
  delete Aprendiz.pais;

  console.log(Aprendiz); // {nombre: "Joaquin", apellido: "Lopez", lenguaje: "Javascript", edad: 25}
  
  // Actualizar una propiedad
  Aprendiz.apellido = "Lopez Sanchez";

  console.log(Aprendiz); // {nombre: "Joaquin", apellido: "Lopez Sanchez", lenguaje: "Javascript", edad: 25}
  


// Sets 

  // Creación
    const Numeros = new Set([1, 2, 3, 6, 8, 20]);

// Añadir un nuevo elemento
    Numeros.add(50);

    console.log(Numeros); // Set(7) { 1, 2, 3, 6, 8, 20, 50 }

// Eliminar un elemento
    Numeros.delete(2);

    console.log(Numeros); // Set(6) { 1, 3, 6, 8, 20, 50 }


// Maps 

  // Creación
const Mascota = new Map([
    ["nombre", "Vuelto"],
    ["tipo", "Gato"],
    ["edad", "1 Año"]
  ]);
  
  // Añadir un nuevo dato
  Mascota.set("color", "Naranja");

  console.log(Mascota); // Map(4) { 'nombre' => 'Vuelto', 'tipo' => 'Gato', 'edad' => '1 Año', 'color' => 'Naranja' }
  
  // Eliminar un dato
  Mascota.delete("tipo");

  console.log(Mascota); // Map(3) { 'nombre' => 'Vuelto', 'edad' => '1 Año', 'color' => 'Naranja' }
  
  // Actualizar un dato
  Mascota.set("edad", "1 Año y 6 Meses");

  console.log(Mascota); // Map(3) { 'nombre' => 'Vuelto', 'edad' => '1 Año y 6 Meses', 'color' => 'Naranja' }
  


// 1.1
    // Dificultad Extra

    const readline = require("readline");
    const rl = readline.createInterface({
        input:process.stdin,
        output: process.stdout
    });

    const agenda = new Map();

    function showMenu () {
        console.log("\n1. Mostrar contactos");  //n1 salto de linea.
        console.log("2. Añadir contacto");
        console.log("3. Actualizar contacto");
        console.log("4. Eliminar contacto");
        console.log("Salir");
    }

    function showContact () {
        console.log("\n-Contactos-");
            if (agenda.size === 0) {
                console.log("No hay conctactos")
            } else {
                agenda.forEach((telefono, nombre) => {
                    console.log(`${nombre}: ${telefono}`)
                })
            }
    }

    function addContact () {
        rl.question("Nombre del contacto", (nombre) => {
            rl.question("Numero de telefono:", (telefono) => {
                if (/^\d{1,11}$/.test(telefono)) {   ///^\d{1,11}$/ => la cadena debe consistir en entre 1 y 11 dígitos, tampoco debe contener ningún otro caracter.
                agenda.set(nombre, telefono);
                console.log("Contacto añadido");
            } else {
                console.log("Numero no valido");
            }
            showMenu();
            })
        })
    }

    function updateContact() {
        rl.question("Nombre del contacto a actualizar: ", (nombre) => {
            if (agenda.has(nombre)) {
                rl.question("Nuevo numero de teléfono ", (telefono) => {
                    if(/^\d{1,11}$/.test(telefono)) {
                        agenda.set(nombre, telefono);
                        console.log("Contacto actualizado");
                    } else {
                        console.log("Numero no válido");
                    }
                    showMenu();
                });
            } else {
                console.log("Contacto no encontrado");
                showMenu();
            }
        });
    }
    
    function deleteContact () {
        rl.question("Nombre del contacto que quieres eliminar ", (nombre) => {
            if (agenda.has(nombre)) {
                agenda.delete(nombre);
                console.log("Contacto eliminado");
            } else {
                console.log("Contacto no encontrado");
            }
            showMenu();
        })
    }
    
    function optionUser (opcion) {
        switch (opcion) {
            case "1":
                showContact ();
                break;
            case "2":
                addContact ();
                break;
            case "3":
                updateContact ();
                break;
            case "4":
                deleteContact ();
                break;
            case "5":
                console.log("Saliendo");
                rl.close();
                break;
            default:
                console.log("Accion invalida. Introduce un número del 1 al 5");
        }
    }
    