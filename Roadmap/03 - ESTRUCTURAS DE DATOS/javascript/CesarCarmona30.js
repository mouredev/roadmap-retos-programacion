/**
 * EJERCICIO
 */

// Arreglos
let my_array = [0, 5, 6, 2, 7, 2, 6, 8, 9, 4, 3, 3];

// Objetos
let my_object = {
    name: "César",
    surname: "Carmona",
    age: 20,
};

// Mapas
let my_map = new Map();
mapa.set("name", "Leroy");
mapa.set("surname", "González");
mapa.set("age", 21);

// Colecciones
let my_set = new Set(["Mexico, España, Argentina, Colombia, Chile, Peru"]);

// Operaciones
// Inserción
my_array.push(6);
my_object.city = "Mexico City";
my_map.set("country", "Mexico");
my_set.add("Ecuador");

// Actualización{
my_array[0] = 10;
my_object.surname = "González";
my_map.set("age", 20);

// Ordenamiento
my_array.sort();

// Eliminación
my_array.pop();
delete my_object.city;
my_map.delete("country");
my_set.delete("España");

// DIFICULTAD EXTRA
function myContacts() {
    let agenda = []
    let run = true
    while (run) {

        const operation = prompt(`Ingrese la operación a realizar:
            1. Buscar contacto
            2. Insertar contacto
            3. Actializar contacto
            4. Eliminar contacto
            5. Salir
        `)

        if (operation === "1") {

            if (agenda.length === 0) {
                console.log("Agenda vacía")
                continue
            }
            const name = prompt("Ingrese el nombre del contacto a buscar:")

            for (let i = 0; i < agenda.length; i++) {
                if (agenda[i].name === name) {
                    console.log("Contacto encontrado:", agenda[i])
                } else {
                    console.log("Contacto no encontrado")
                }
            }
        } else if (operation === "2") {

            const name = prompt("Ingrese el nombre del contacto a insertar:")
            const phone = prompt("Ingrese el teléfono del contacto a insertar:")

            if (!/^\d{6,11}$/.test(phone)) {
                console.log("El número de teléfono no es válido.");
                break;
            }

            const contact = {
                name: name,
                phone: phone
            }

            agenda.push(contact)
            console.log("Contacto insertado:", contact)


        } else if (operation === "3") {
            const name = prompt("Ingrese el nombre del contacto a actualizar:")
            for (let i = 0; i < agenda.length; i++) {
                if (agenda[i].name === name) {
                    agenda[i].phone = prompt("Ingrese el nuevo teléfono del contacto:")
                    console.log("Contacto actualizado:", agenda[i])
                } else {
                    console.log("Contacto no encontrado")
                }
            }
        } else if (operation === "4") {
            const name = prompt("Ingrese el nombre del contacto a eliminar:")
            for (let i = 0; i < agenda.length; i++) {
                if (agenda[i].name === name) {
                    agenda.splice(i, 1)
                    console.log("Contacto eliminado:")
                } else {
                    console.log("Contacto no encontrado")
                }
            }
        } else if (operation === "5") {
            run = false;
            console.log("Agenda creada:", agenda)
            break;
        } else {
            console.log("Operación no válida")
        }
    }
    console.log("Agenda creada:", agenda)
}