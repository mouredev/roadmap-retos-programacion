// Arreglos
const arreglo = [1, 2, 3, 4, 5];

// Objetos
const objeto = {
    nombre: "Juan",
    apellido: "Pérez",
    edad: 30,
};

// Mapas
const mapa = new Map();
mapa.set("nombre", "Juan");
mapa.set("apellido", "Pérez");
mapa.set("edad", 30);

// Colecciones
const coleccion = new Set([1, 2, 3, 4, 5]);

// Operaciones
// Inserción
arreglo.push(6);
objeto.pais = "España";
mapa.set("pais", "España");
coleccion.add(6);

// Actualización{
arreglo[0] = 10;
objeto.apellido = "López";
mapa.set("edad", 31);

// Ordenamiento
arreglo.sort();

// Eliminación
arreglo.pop();
delete objeto.pais;
mapa.delete("pais");
coleccion.delete(6);

// DIFICULTAD EXTRA
function crearAgenda() {
    let agenda = []
    let run = true
    while (run) {

        const operacion = prompt(`Ingrese la operación a realizar:
            1. Buscar contacto
            2. Insertar contacto
            3. Actializar contacto
            4. Eliminar contacto
            5. Salir
        `)

        if (operacion === "1") {

            if (agenda.length === 0) {
                console.log("Agenda vacía")
                continue
            }
            const nombre = prompt("Ingrese el nombre del contacto a buscar:")

            for (let i = 0; i < agenda.length; i++) {
                if (agenda[i].nombre === nombre) {
                    console.log("Contacto encontrado:", agenda[i])
                } else {
                    console.log("Contacto no encontrado")
                }
            }
        } else if (operacion === "2") {

            const nombre = prompt("Ingrese el nombre del contacto a insertar:")
            const phone = prompt("Ingrese el teléfono del contacto a insertar:")

            if (!/^\d{6,11}$/.test(phone)) {
                console.log("El número de teléfono no es válido.");
                break;
            }

            const contacto = {
                nombre: nombre,
                phone: phone
            }

            agenda.push(contacto)
            console.log("Contacto insertado:", contacto)


        } else if (operacion === "3") {
            const nombre = prompt("Ingrese el nombre del contacto a actualizar:")
            for (let i = 0; i < agenda.length; i++) {
                if (agenda[i].nombre === nombre) {
                    agenda[i].phone = prompt("Ingrese el nuevo teléfono del contacto:")
                    console.log("Contacto actualizado:", agenda[i])
                } else {
                    console.log("Contacto no encontrado")
                }
            }
        } else if (operacion === "4") {
            const nombre = prompt("Ingrese el nombre del contacto a eliminar:")
            for (let i = 0; i < agenda.length; i++) {
                if (agenda[i].nombre === nombre) {
                    agenda.splice(i, 1)
                    console.log("Contacto eliminado:")
                } else {
                    console.log("Contacto no encontrado")
                }
            }
        } else if (operacion === "5") {
            run = false;
            console.log("Agenda creada:", agenda)
            break;
        } else {
            console.log("Operación no válida")
        }
    }
    console.log("Agenda creada:", agenda)
}