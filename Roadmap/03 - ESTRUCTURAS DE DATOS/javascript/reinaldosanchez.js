//Estructuras de datos
//arreglos
let frutas = ["manzana", "banana", "naranja"];

// Insertar
frutas.push("pera"); // Añade al final
frutas.splice(1, 0, "kiwi"); // Inserta en el índice 1

// Borrar
frutas.pop(); // Elimina el último
frutas.splice(2, 1); // Elimina 1 elemento desde índice 2

// Actualizar
frutas[0] = "mango";

// Ordenar
frutas.sort(); // Orden alfabético
console.log(frutas);
//objetos
let persona = {
    nombre: "Juan",
    edad: 30,
    ciudad: "Madrid"
};

// Insertar
persona.pais = "España"; // Añade una nueva propiedad
persona.edad = 31; // Actualiza una propiedad existente

// Borrar
delete persona.ciudad; // Elimina una propiedad

// Acceder
console.log(persona.nombre); // Accede a una propiedad
console.log(persona["edad"]); // Accede a una propiedad con nombre dinámico


//reto

let agenda = [
    {
        nombre: "Reinaldo",
        telefono: "123456789"
    },
    {
        nombre: "Juan",
        telefono: "123456789"
    },
    {
        nombre: "Pedro",
        telefono: "123456789"
    }
]; //agenda de contactos

//funcion validar telefono
function validarTelefono(telefono) {
    let regex = /^\d{1,11}$/;
    return regex.test(telefono);
};

//funcion agregar contacto
function agregarContacto() {
    let nombre = prompt("Ingrese el nombre");
    let telefono = prompt("Ingrese el telefono");
    if (!validarTelefono(telefono)) {
        alert("Numero invalido. Solo numeros y maximo 11 digitos");
        return;
    }
    agenda.push({ nombre, telefono });
    alert("Contacto agregado");
};

//funcion mostrar agenda
function mostrarAgenda() {
    if (agenda.length === 0) {
        alert("Agenda vacia");
        return;
    }
    let lista = "Contactos:\n";
    agenda.forEach((c, i) => {
        lista += `$(i + 1). ${c.nombre} - {c.telefono}\n`;
    });

    alert(lista);
};

//funcion buscar contacto
function buscarContacto() {
    let nombre = prompt("Nombre a buscar:");
    let resultados = agenda.filter(c => c.nombre.toLowerCase() === nombre.toLowerCase());

    if (resultados.length === 0) {
        alert("No se encontró ningún contacto con ese nombre.");
    } else {
        let lista = "Resultados:\n";
        resultados.forEach(c => lista += `${c.nombre} - ${c.telefono}\n`);
        alert(lista);
    }
};

//funcion actualizar contacto
function actualizarContacto() {
    let nombre = prompt("Nombre del contacto a actualizar:");
    let contacto = agenda.find(c => c.nombre.toLowerCase() === nombre.toLowerCase());

    if (!contacto) {
        alert("Contacto no encontrado.");
        return;
    }

    let nuevoTelefono = prompt("Ingresa el nuevo teléfono:");
    if (!validarTelefono(nuevoTelefono)) {
        alert("Número inválido.");
        return;
    }

    contacto.telefono = nuevoTelefono;
    alert(`${nombre} actualizado/a correctamente.`);
};

//funcion eliminar contacto
function eliminarContacto() {
    let nombre = prompt("Nombre del contacto a eliminar:");
    let indice = agenda.findIndex(c => c.nombre.toLowerCase() === nombre.toLowerCase());

    if (indice === -1) {
        alert("Contacto no encontrado.");
        return;
    }

    agenda.splice(indice, 1);
    alert(`${nombre} eliminado/a de la agenda.`);
};

//funcion principal
function menu() {
    let opcion = prompt("Seleccione una opción:\n1. Agregar contacto\n2. Mostrar agenda\n3. Buscar contacto\n4. Actualizar contacto\n5. Eliminar contacto\n6. Salir");

    switch (opcion) {
        case "1":
            agregarContacto();
            break;
        case "2":
            mostrarAgenda();
            break;
        case "3":
            buscarContacto();
            break;
        case "4":
            actualizarContacto();
            break;
        case "5":
            eliminarContacto();
            break;
        case "6":
            alert("Hasta luego!");
            break;
        default:
            alert("Opción inválida. Intente de nuevo.");
    }
};