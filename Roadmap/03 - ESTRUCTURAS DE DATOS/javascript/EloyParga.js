// 1. Arrays
let arrayDatosSub = ["Spira", "Drazz", "Espaby", "Kainyan77"];
console.log("Array Inicial: ",arrayDatosSub);

//Insercción
arrayDatosSub.push("EloyParga"); //Añade un elemento al final
console.log("Despues de la insercción" , arrayDatosSub);

//Boorar
arrayDatosSub.slice(0,1);
console.log("Despues de Borrar", arrayDatosSub );

//Actualización
arrayDatosSub[2] = "ESPABY";
console.log("Despues de Actualizar ", arrayDatosSub)

//Ordenación
/**
 * @method sort()
 * por defecto ordena lexicograficamente
 * por @param podemos pasarle de forma OPCIONAL
 * una regla que defina el orden de los elementos
 */
arrayDatosSub.sort((a, b) => a.length - b.length); // Odena de menor a mayor longitud de palabra
console.log("Despues de ordenar " , arrayDatosSub)


//2. Objetos
let listaTrabajadores = {
    trabajador1: "Manolo",
    trabajador2: "Jony"
}
    console.log("Objeto Inicial ", listaTrabajadores);

//Insercción
listaTrabajadores.trabajador3 = "Pepe";
console.log ("Despues de insertar ", listaTrabajadores)

//Borrar
delete listaTrabajadores.trabajador1
console.log("Despues de borrar ", listaTrabajadores);

//Actualizar
listaTrabajadores.trabajador2 = "Jonathan";
console.log("Despues de actualizar ", listaTrabajadores);


// 3.Mapas
let mapa = new Map();
mapa.set("a", 1);
mapa.set("b", 2);
console.log("Mapa Inicial: ", mapa);

// Inserción
mapa.set("c", 3);
console.log("Despues de la Inserción: ", mapa);

// Borrar
mapa.delete("b");
console.log("Despues de Borrar: ", mapa);

// Actualizar
mapa.set("c", 10);
console.log("Despues de Actualizar: ", mapa);



//DIFICULTAD EXTRA: AGENDA DE CONTACTOS 
const readline = require("readline");

const agenda = new Map();

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

//validar que el numero sea válido
function validacionNum(numero){
    return /^[0-9]{1,11}$/.test(numero)
}

//Funciones para las operaciones de la agenda
function insertarContacto(nombre, numero) {
    if(!validacionNum(numero)){
        console.log("Numero de telefono no valido, debe contener solo numeros y maximo 11 digitos");
        return;
    }
    agenda.set(nombre, numero);
    console.log("Contacto añadido");
}

function buscarContacto(nombre) {
    if(agenda.has(nombre)) {
        console.log(`Contacto encontrado: ${nombre} - ${agenda.get(nombre)}`);
    }else{
        console.log("Contacto no encontrado");
    }
}

function actualizarContacto(nombre, Newnumero){
    if(!agenda.has(nombre)){
        console.log("El contacto no existe");
    }

    if(!validacionNum(Newnumero)){
        console.log("Numero de telefono no valido, debe contener solo numeros y maximo 11 digitos");
        return;
    }

    agenda.set({nombre, Newnumero});
    console.log("Contacto actualizado");
}

function eliminarContacto(nombre,){
    if(agenda.delete(nombre)){
        console.log("Contacto Eliminado");
    }else{
        console.log("El contacto no existe");
    }
}

function mostrarAgenda(){
    if(agenda.size === 0){
        console.log("La agenda esta vacia");
    }else{
        console.log("==CONTACTO DE LA AGENDA==");
        agenda.forEach((nombre, numero) => {
            console.log(`- ${nombre}: ${numero}`);
        })
    }
}


//MENU AGENDA

function menu(){
    console.log("\n=== AGENDA CONTACTOS ===");
    console.log("1. Insertar Contacto");
    console.log("2. Buscar Contacto");
    console.log("3. Actualizar Contacto");
    console.log("4. Eliminar Contacto");
    console.log("5. Mostrar todos los contacto");
    console.log("6. SALIR");

    rl.question("Selecciona una opción: ", (opcion) => {
        switch(opcion){
            case "1":
                rl.question("Introduce el nombre", (nombre)=> {
                    rl.question("Introduce el numero de telefono", (numero)=> {
                        insertarContacto(nombre, numero);
                        menu();
                    });
                });
                break;

            case "2":
                rl.question("Introduce el nombre del contacto", (nombre) => {
                    buscarContacto(nombre);
                    menu();
                });
                break;

            case "3":
                rl.question("Introduce el nombre", (nombre)=> {
                    rl.question("Introduce el nuevo numero de telefono", (numero)=> {
                        actualizarContacto(nombre, numero);
                        menu();
                    });
                });
                break;

            case "4":
                rl.question("Introduce el nombre del contacto que desea eliminar", (nombre) => {
                    eliminarContacto(nombre);
                    menu();
                });
                break;

            case "5":
                mostrarAgenda();
                menu();
                break;

            case "6":
                console.log("Ha salido de la agenda.  ¡ADIOS!");
                rl.close();
                break;

            default:
                console.log("Opcion no valida");
                menu();
        }
    });
}

//Inicializar el menu
menu();