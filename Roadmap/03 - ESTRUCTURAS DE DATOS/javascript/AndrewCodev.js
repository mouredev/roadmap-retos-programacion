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

//Array: Lista ordenada de elementos accesibles por índice.
const frutas = ["manzana", "banana", "pera"];
frutas.push("Naranja"); //Agregamos elemento al final
frutas.unshift("Mango"); //Agregamos elemento al inicio
frutas.splice(2, 0, "kiwi"); // Inserta "kiwi" en la posición 2
console.log(frutas);

//Modificamos frutas en la posición 1 Manzana por mandarina
frutas[1] = "mandarina";
console.log(frutas);

//Recorriendo el array de frutas y modificando el valor de banana
frutas.forEach((fruta, index) => {
  if (fruta === "banana") {
    frutas[index] = "plátano";
  }
});
console.log(frutas);

//Eliminar elementos
frutas.pop(); // ➜ elimina el último ("Naranja")
console.log(frutas);

frutas.shift(); // ➜ elimina el primero ("mango")
console.log(frutas);

frutas.splice(1, 1); // Elimina 1 elemento en la posición 1 (kiwi)
console.log(frutas);

const nuevasFrutas = [...frutas, "sandía"]; // Agrega "sandía" sin tocar el original
console.log(nuevasFrutas);

//Objeto: Conjunto de pares clave-valor, útil para representar entidades.
const persona = {
  nombre: "Andrew",
  apellido: "code",
  edad: 31,
};
console.log(persona);

//Agregamos elementos al objeto persona con .
persona.pais = "colombia";
console.log(persona);

//Agregamos elementos al objeto persona con []
const nuevaClave = "ciudad";
persona[nuevaClave] = "Medellín";
console.log(persona);

//Modificamos elementos al objeto persona edad = 31
persona.edad = 33;
console.log(persona);

//Eliminamos elementos al objeto persona edad = 31
delete persona.edad;
console.log(persona);

//Agregar multiples elementos
Object.assign(persona, {
  hobbies: ["leer", "música"],
  activo: true,
});

console.log(persona);

//Set: Conjunto de valores únicos, sin duplicados.
const numerosUnicos = new Set([1, 2, 3, 3]);
numerosUnicos.add(4);
numerosUnicos.add(5);
numerosUnicos.add(5); // ❌ No se agrega porque ya existe

console.log(numerosUnicos);

numerosUnicos.delete(5); // Elimina "pera"
console.log(numerosUnicos);

//Map Estructura clave-valor como un objeto, pero con orden y flexibilidad.
const mapa = new Map();
mapa.set("nombre", "Andrew");
mapa.set("apellido", "Codev");
mapa.set("edad", "31");

console.log(mapa);

mapa.delete("edad"); // Elimina "pera"
console.log(mapa);

//DIFICULTAD EXTRA

const agenda = [
  { nombre: "Juan", telefono: 36598855441 },
  { nombre: "Camila", telefono: 36598877441 },
  { nombre: "Andres", telefono: 32569874111 },
];
const MAX_CARACTERES = 11;
let programaActivo = true; // Bandera para controlar si el programa sigue activo

const iniciarAgenda = (MAX_CARACTERES) => {
  if (!programaActivo) return; // Si el programa no está activo, no sigue ejecutándose.

  const opcion = parseInt(
    prompt(
      "Bienvenid@ a tu Agenda. ¿Qué deseas hacer? presiona\n1 para Agregar\n2 para Buscar\n3 para Modificar\n4 para Eliminar\n5 para Listar\n6 para Cerrar"
    )
  );

  switch (opcion) {
    case 1:
      agregarContanto();
      break;
    case 2:
      buscarContacto(
        prompt("Escribe el nombre o el número de teléfono:").trim()
      );
      break;
    case 3:
      let contactoModificado = buscarContacto(
        prompt(
          "Escribe el nombre o teléfono del contacto que deseas modificar:"
        ).trim()
      );
      if (contactoModificado) modificarContanto(contactoModificado);
      break;
    case 4:
      eliminarContacto();
      break;
    case 5:
      listarContactos();
      break;
    case 6:
      cerrarPrograma();
      break;
    default:
      alert("Opción no válida. Inténtalo de nuevo.");
  }

  if (programaActivo) iniciarAgenda(MAX_CARACTERES); // Solo vuelve a llamar a la función si el programa sigue activo
};

// Función para validar el teléfono
const validarTelefono = (telefono) => {
  if (!/^\d+$/.test(telefono)) {
    alert("El teléfono debe contener solo números.");
    return false;
  }
  if (telefono.length > MAX_CARACTERES) {
    alert(`El teléfono no puede tener más de ${MAX_CARACTERES} dígitos.`);
    return false;
  }
  return true;
};

// Función para verificar si un contacto ya existe
const contactoExistente = (telefono) =>
  agenda.some((contacto) => contacto.telefono === telefono);

// Función común para mostrar un mensaje de error
const mostrarError = (mensaje) => {
  alert(mensaje);
};

// Buscar un contacto por nombre o teléfono
const buscarContacto = (contactoBuscado) => {
  console.log("🔍 BUSCANDO...");
  const contactoEncontrado = agenda.find(
    (contacto) =>
      contacto.nombre.toLowerCase() === contactoBuscado.toLowerCase() ||
      contacto.telefono === parseInt(contactoBuscado)
  );

  if (contactoEncontrado) {
    console.log("✅ Contacto encontrado:", contactoEncontrado);
    return contactoEncontrado;
  } else {
    console.log("❌ Contacto no encontrado.");
    return null;
  }
};

// Agregar un nuevo contacto
const agregarContanto = () => {
  let nombre = prompt("Escribe el nombre del contacto:").trim();
  if (!nombre) return alert("El nombre no puede estar vacío.");

  let telefono = prompt(
    `Escribe el teléfono (solo números, máx. ${MAX_CARACTERES} dígitos):`
  ).trim();

  if (!validarTelefono(telefono)) return;

  if (contactoExistente(telefono)) {
    mostrarError("El contacto con este teléfono ya existe.");
  } else {
    agenda.push({ nombre, telefono });
    alert("Contacto agregado correctamente ✅");
    listarContactos();
  }
};

// Listar todos los contactos
const listarContactos = () => {
  if (agenda.length > 0) {
    console.log("MIS CONTACTOS");
    agenda.forEach((contacto) => {
      console.log(`Nombre: ${contacto.nombre}, Teléfono: ${contacto.telefono}`);
    });
  } else {
    console.log("La agenda no tiene contactos.");
  }
};

// Modificar un contacto
const modificarContanto = (contacto) => {
  console.log("El contacto a modificar es:", contacto);
  contacto.nombre = prompt("Ingresa el nuevo nombre:").trim();
  let telefono = prompt("Ingresa el nuevo teléfono:").trim();

  if (!validarTelefono(telefono)) return;

  contacto.telefono = telefono;
  console.log("Contacto modificado:", contacto);
};

// Eliminar un contacto
const eliminarContacto = () => {
  let telefono = prompt(
    "Escribe el teléfono del contacto que deseas eliminar:"
  ).trim();

  if (!validarTelefono(telefono)) return;

  const contactoAEliminar = agenda.find(
    (contacto) => contacto.telefono === telefono
  );

  if (contactoAEliminar) {
    const confirmacion = confirm(
      `¿Estás seguro de que deseas eliminar el contacto de ${contactoAEliminar.nombre} con el teléfono ${contactoAEliminar.telefono}?`
    );
    if (confirmacion) {
      const index = agenda.indexOf(contactoAEliminar);
      agenda.splice(index, 1);
      console.log("Contacto eliminado:", contactoAEliminar);
      alert("El contacto ha sido eliminado.");
    } else {
      console.log("Eliminación cancelada.");
    }
  } else {
    mostrarError("No se encontró un contacto con ese teléfono.");
  }
};

// Cerrar el programa
const cerrarPrograma = () => {
  console.log("Programa cerrado.");
  programaActivo = false; // Cambiar la bandera a false para cerrar el programa
  alert("Programa cerrado.");
};

iniciarAgenda(MAX_CARACTERES);
