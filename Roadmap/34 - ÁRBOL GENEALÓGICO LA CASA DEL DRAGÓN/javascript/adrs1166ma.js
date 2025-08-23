/*
EJERCICIO:
¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
¿Alguien se entera de todas las relaciones de parentesco
entre personajes que aparecen en la saga?
Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
Requisitos:
1. Estará formado por personas con las siguientes propiedades:
- Identificador único (obligatorio)
- Nombre (obligatorio)
- Pareja (opcional)
- Hijos (opcional)
2. Una persona sólo puede tener una pareja (para simplificarlo).
3. Las relaciones deben validarse dentro de lo posible.
Ejemplo: Un hijo no puede tener tres padres.
Acciones:
1. Crea un programa que permita crear y modificar el árbol.
- Añadir y eliminar personas
- Modificar pareja e hijos
2. Podrás imprimir el árbol (de la manera que consideres).

NOTA: Ten en cuenta que la complejidad puede ser alta si
se implementan todas las posibles relaciones. Intenta marcar
tus propias reglas y límites para que te resulte asumible.
*/
// 🔥 SIMULADOR: ÁRBOL GENEALÓGICO DE LA CASA DEL DRAGÓN 🔥
console.log("🐉 ¡Bienvenido al árbol genealógico de La Casa del Dragón! 🐉");
// Base de datos para almacenar personas
const personas = {};

// Función principal del programa
function iniciarPrograma() {
    let continuar = true;

    while (continuar) {
        console.log("\n--- MENÚ PRINCIPAL ---");
        console.log("1. Añadir persona.");
        console.log("2. Modificar pareja.");
        console.log("3. Modificar hijos.");
        console.log("4. Eliminar persona.");
        console.log("5. Mostrar árbol genealógico.");
        console.log("6. Salir del programa.");

        const opcion = prompt("Seleccione una opción (1-6): ");

        switch (opcion) {
            case "1":
                añadirPersona();
                break;
            case "2":
                modificarPareja();
                break;
            case "3":
                modificarHijos();
                break;
            case "4":
                eliminarPersona();
                break;
            case "5":
                mostrarArbolGenealogico();
                break;
            case "6":
                console.log("👋 ¡Gracias por usar el simulador del árbol genealógico! 👋");
                continuar = false;
                break;
            default:
                console.log("❌ Opción no válida. Intente de nuevo.");
        }
    }
}

// 1. Añadir persona
function añadirPersona() {
    const id = prompt("Ingrese un identificador único para la persona: ");
    if (personas[id]) {
        console.log("❌ Ya existe una persona con ese identificador.");
        return;
    }

    const nombre = prompt("Ingrese el nombre de la persona: ");
    if (!nombre) {
        console.log("❌ El nombre es obligatorio.");
        return;
    }

    personas[id] = { id, nombre, pareja: null, hijos: [] };
    console.log(`✅ Persona "${nombre}" añadida con ID ${id}.`);
}

// 2. Modificar pareja
function modificarPareja() {
    const id = prompt("Ingrese el ID de la persona cuya pareja desea modificar: ");
    const persona = personas[id];
    if (!persona) {
        console.log("❌ No se encontró ninguna persona con ese ID.");
        return;
    }

    const idPareja = prompt("Ingrese el ID de la nueva pareja (o 'null' para eliminar pareja): ");
    if (idPareja === "null") {
        // Eliminar pareja actual
        if (persona.pareja) {
            const parejaActual = personas[persona.pareja];
            if (parejaActual) parejaActual.pareja = null; // Actualizar pareja de la otra persona
        }
        persona.pareja = null;
        console.log(`✅ Pareja eliminada para "${persona.nombre}".`);
        return;
    }

    const pareja = personas[idPareja];
    if (!pareja) {
        console.log("❌ No se encontró ninguna persona con ese ID de pareja.");
        return;
    }

    // Validar que la pareja no tenga ya otra pareja
    if (pareja.pareja && pareja.pareja !== id) {
        console.log(`❌ ${pareja.nombre} ya tiene una pareja asignada.`);
        return;
    }

    // Actualizar relaciones
    if (persona.pareja) {
        const parejaAnterior = personas[persona.pareja];
        if (parejaAnterior) parejaAnterior.pareja = null; // Desvincular pareja anterior
    }
    persona.pareja = idPareja;
    pareja.pareja = id;

    console.log(`✅ ${persona.nombre} ahora está vinculado/a con ${pareja.nombre}.`);
}

// 3. Modificar hijos
function modificarHijos() {
    const idPadre = prompt("Ingrese el ID del padre/madre: ");
    const padre = personas[idPadre];
    if (!padre) {
        console.log("❌ No se encontró ninguna persona con ese ID.");
        return;
    }

    const accion = prompt("¿Desea añadir o eliminar un hijo? (añadir/eliminar): ").toLowerCase();
    if (!["añadir", "eliminar"].includes(accion)) {
        console.log("❌ Acción no válida.");
        return;
    }

    const idHijo = prompt("Ingrese el ID del hijo: ");
    const hijo = personas[idHijo];
    if (!hijo) {
        console.log("❌ No se encontró ninguna persona con ese ID de hijo.");
        return;
    }

    if (accion === "añadir") {
        // Validar que el hijo no tenga más de dos padres
        const padresActuales = Object.values(personas).filter(p => p.hijos.includes(idHijo));
        if (padresActuales.length >= 2) {
            console.log("❌ Este hijo ya tiene dos padres asignados.");
            return;
        }

        padre.hijos.push(idHijo);
        console.log(`✅ ${hijo.nombre} añadido como hijo de ${padre.nombre}.`);
    } else if (accion === "eliminar") {
        const index = padre.hijos.indexOf(idHijo);
        if (index === -1) {
            console.log("❌ Este hijo no está registrado como hijo de esta persona.");
            return;
        }

        padre.hijos.splice(index, 1);
        console.log(`✅ ${hijo.nombre} eliminado como hijo de ${padre.nombre}.`);
    }
}

// 4. Eliminar persona
function eliminarPersona() {
    const id = prompt("Ingrese el ID de la persona que desea eliminar: ");
    const persona = personas[id];
    if (!persona) {
        console.log("❌ No se encontró ninguna persona con ese ID.");
        return;
    }

    // Eliminar referencias de pareja e hijos
    if (persona.pareja) {
        const pareja = personas[persona.pareja];
        if (pareja) pareja.pareja = null;
    }

    for (const p of Object.values(personas)) {
        const index = p.hijos.indexOf(id);
        if (index !== -1) p.hijos.splice(index, 1);
    }

    delete personas[id];
    console.log(`✅ Persona "${persona.nombre}" eliminada.`);
}

// 5. Mostrar árbol genealógico
function mostrarArbolGenealogico() {
    console.log("\n--- ÁRBOL GENEALÓGICO ---");
    for (const persona of Object.values(personas)) {
        console.log(`ID: ${persona.id}, Nombre: ${persona.nombre}`);
        if (persona.pareja) {
            const pareja = personas[persona.pareja];
            console.log(`   Pareja: ${pareja ? pareja.nombre : "Sin pareja"}`);
        } else {
            console.log("   Pareja: Sin pareja");
        }

        if (persona.hijos.length > 0) {
            const nombresHijos = persona.hijos.map(idHijo => personas[idHijo]?.nombre || "Desconocido");
            console.log(`   Hijos: ${nombresHijos.join(", ")}`);
        } else {
            console.log("   Hijos: Ninguno");
        }
    }
}

iniciarPrograma();