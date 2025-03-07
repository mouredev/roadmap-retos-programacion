//CREACION 

//ARRAYS
let numeros = [1, 2, 3, 4, 5];

//ACCESO
console.log(numeros[0]);
console.log(numeros[1]);

//MODIFICACION
numeros[0] = 6;
console.log(numeros[0]);

//AGREGAR ELEMENTOS
numeros.push(6);
numeros.unshift(0);

//ELIMINAR ELEMENTOS
numeros.pop();
numeros.shift();

//ELIMINAR ELEMENTO DE UNA ZONA ESPECIFICA
numeros.splice(2, 1);
console.log(numeros)

//OTROS METODOS
console.log(numeros.includes(3));
console.log(numeros.indexOf(3));
console.log(numeros.reverse());
console.log(numeros.sort());
console.log(numeros.sort().reverse());


//OBJETOS

//CREACION
let persona = {
    nombre: "Josue",
    edad: 20,
    ciudad: "Guatemala"
};

//ACCESO
console.log(persona.nombre);
console.log(persona.edad);

//MODIFICACION
persona.edad = 21;
console.log(persona.edad);

//AGREGAR PROPIEDAD
persona.profesion = "Estudiante";
console.log(persona.profesion);

//ELIMINAR PROPIEDAD

delete persona.ciudad;
console.log(persona);

//OTROS METODOS

console.log(Object.keys(persona));

console.log(Object.values(persona));

console.log(Object.entries(persona));

//MAPAS (MAPS)

//CREACION
let mapa = new Map();

//AGREGAR ELEMENTOS
mapa.set("nombre", "Josue");
mapa.set("edad", 20);

//ACCESO
console.log(mapa.get("nombre"));


//ACTUALIZACION
mapa.set("edad", 21);

//ELIMINAR ELEMENTO
mapa.delete("edad");

//VERIFICAR EXISTENCIA

console.log(mapa.has("nombre"));

//OTROS METODOS

console.log(mapa.size);
mapa.clear();
console.log(mapa.size);

//SETS

//CREACION
let set = new Set();

//AGREGAR ELEMENTOS
set.add(1);
set.add(2);

//ELIMINAR ELEMENTOS
set.delete(1);

//VERIFICAR EXISTENCIA
console.log(set.has(2));

//OTROS METODOS
console.log(set.size);
set.clear();
console.log(set.size);


//EXTRA

const readline = require("readline");
const input = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const agenda = new Map();


function showMenu() {
    console.log("\n1. Mostrar contactos");
    console.log("2. Añadir contacto");
    console.log("3. Actualizar contacto");
    console.log("4. Eliminar contacto");
    console.log("Salir");
    input.question("Selecciona una opcion: ", (opcion) => {
        optionUser(opcion);
    })
}

function validarTelefono(telefono) {
    const number = Number(telefono);
    if (isNaN(number)) {
        console.log("Telefono no valido");
        showMenu();
        return false;
    } else {
        return true;
    }
}

function addContact() {
    input.question("Ingresa el Nombre: ", (nombre) => {
        input.question("Ingresa el Telefono: ", (telefono) => {
            if (validarTelefono(telefono)) {
                agenda.set(nombre.toUpperCase(), telefono);
                console.log("Contacto agregado correctamente!!");
                showMenu();
            }
        })
    })
}

function updateContact() {
    input.question("Ingresa el nombre del contacto que quieres actualizar: ", (nombre) => {
        const filter = nombre.toUpperCase()
        const contact = agenda.get(filter);

        if (contact) {
            input.question("Ingresa el nuevo numero de telefono: ", (telefono) => {
                if (validarTelefono(telefono)) {
                    agenda.set(filter, telefono);
                    console.log("Contacto actualizado");
                    showMenu();
                }
            })
        } else {
            console.log("Contacto no encontrado");
            showMenu();
        }
    })
}

function deleteContact() {
    input.question("Ingresa el nombre del contacto que quieres eliminar: ", (nombre) => {
        const filter = nombre.toUpperCase();

        if (agenda.has(filter)) {
            agenda.delete(filter);
            console.log("Contacto eliminado");
            showMenu();
        } else {
            console.log("Contacto no encontrado");
            showMenu();
        }
    })
}


function optionUser(opcion) {
    switch (opcion) {
        case "1":
            console.log(agenda);
            showMenu();
            break;
        case "2":
            addContact();
            break;
        case "3":
            updateContact();
            break;
        case "4":
            deleteContact();
            break;
        case "5":
            input.close();
            break;
        default:
            console.log("Opcion no valida");
            showMenu();
            break;
    }
}

showMenu();