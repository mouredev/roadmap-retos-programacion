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

// Create contactos
let contactos = []

// INSERT
const insertContacto = (nombre, numero) => {
    contactos.push([nombre, numero]);
}

insertContacto("Pedro Lama", "+555-555-5555");
insertContacto("Lola Campbell", "+555-555-5556");
insertContacto("May Yates", "+555-555-4444");
insertContacto("Nicholas Sanders", "+555-555-3333");
insertContacto("Edgar Morgan", "+555-555-7777");
insertContacto("Gene Johnson", "+555-555-1111");

// DELETE
const deleteContact = (nombre) => {
    contactos = contactos.filter((contacto) => contacto[0] != nombre);
}

deleteContact("Cristian");

// UPDATE
const updateContact = (nombre, nuevoNumero) => {
    const index = contactos.findIndex(contacto => contacto[0] === nombre);
    return (index !== -1) ? contactos[index][1] = nuevoNumero : console.log(`Contacto "${nombre}" no encontrado.`);
}

updateContact("Pedro Lama", "+555-555-2222");


// SORT
/*
contactos.sort((a, b) => {
    const nombreA = a[0].toLowerCase();
    const nombreB = b[0].toLowerCase();

    if (nombreA < nombreB) return -1;
    if (nombreA > nombreB) return 1;
    return 0;
});

console.log(contactos);

*/
for (let i = 0; i < contactos.length - 1; i++) {
    for (let j = 0; j < contactos.length - 1 - i; j++) {
        const nombreA = contactos[j][0].toLowerCase();
        const nombreB = contactos[j + 1][0].toLowerCase();
        if (nombreA > nombreB) {
            const temp = contactos[j];
            contactos[j] = contactos[j + 1];
            contactos[j + 1] = temp;
        }
    }
}

console.log(contactos);