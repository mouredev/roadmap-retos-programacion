//--------------------------------> Estructuras de datos de JS
//Array
console.log('Estructura de dato: Array');
let lista = ["Mani", "Nuez", "Castaña de Cajú", "Avellana"]
console.log(lista);
console.log('---------------------------------');

//Agregar elemento al final del array
console.log('Agregar al final → push()');
lista.push("Almendra", "Girasol");
console.log(lista);
console.log('---------------------------------');

//Eliminar del array
console.log('Eliminar primer item → pop()');
lista.pop();
console.log(lista);
console.log('---------------------------------');

//Agregar elemento al comienzo del array
console.log('Agregar al comienzo → unshift()');
lista.unshift("Girasol");
console.log(lista);
console.log('---------------------------------');
//Eliminar primer elemento de la lista
console.log('Eliminar al comienzo → shift()');
lista.shift();
console.log(lista);
console.log('---------------------------------');

//Encontrar el índice de un elemento del array
console.log('Indice → idexOf("x")');
let posicion = lista.indexOf("Nuez");
console.log(`La posición en la lista de la Nuez es: ${posicion}`);
console.log('---------------------------------');

//Eliminar un elemento con posición del array → Quitar, reemplazar o agregar nuevos elementos del medio del array
//Splice (index, borrar, agregar)
console.log('Eliminar/agregar un elemento en el medio → splice()');
console.log(lista);
lista.splice(4, 0, 'Girasol');
console.log(lista);
console.log('---------------------------------');

// Array de objetos
console.log('Estructura de dato: Array de objetos');
const verduleria = [
    { nombre: "papa", costo: 1200, unidad: "kg" },
    { nombre: "cebolla", costo: 800, unidad: "kg" },
    { nombre: "zanahoria", costo: 400, unidad: "kg" },
    { nombre: "palta", costo: 1500, unidad: "unidad" },]

verduleria.push({ nombre: "lechuga", costo: 2800, unidad: "kg" }); // agregar un dato
verduleria.splice(1, 1); //Elimina 1 dato
verduleria[3].nombre = "Lechuga Francesa" //Actualiza dato
verduleria.sort((a, b) => a.costo - b.costo); //Ordena datos
//Busqueda
let buscaVerdura = "Zanahoria";
let verdura = verduleria.find(verdura => verdura.nombre.toLocaleLowerCase().includes(buscaVerdura.toLocaleLowerCase()));
if (verdura) {
    console.log(`La ${verdura.nombre} sale $${verdura.costo} por ${verdura.unidad}`);
}
else { console.log(`No tenemos stock de ${buscaVerdura}. Vuelva prontos`) };
console.log('---------------------------------');

//--------------------------------> Ejercicio extra
/*
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

//También instale npm install prompt-sync
// Y se debe colocar const prompt = require("prompt-sync")({sigint:true}); al comienzo del código
const prompt = require("prompt-sync")({ sigint: true });

let agendaContactos = [
    { nombre: "Sara Garrett", tel: 4958572 },
    { nombre: "Gilbert Robinson", tel: 8259704 },
    { nombre: "Pedro Byrd", tel: 4714090 },
    { nombre: "Hannah Ryan", tel: 9847358 },
    { nombre: "Lisa Spencer", tel: 8577432 },
    { nombre: "Ivan Shaw", tel: 3872149 },
]

function mi_agenda() {
    let is_on = true;
    while (is_on) {
    console.log("1. Buscar contacto");
    console.log("2. Insertar contacto");
    console.log("3. Actualizar contacto");
    console.log("4. Eliminar contacto");
    console.log("5. salir");
    let usuarioResponde = prompt('Seleccione una opción: ');
    
    switch (usuarioResponde) {
        // 1. Buscar
        case "1":
            let buscaNombre = prompt('Introduce el nombre del contacto a buscar: ');
            let contactoEncontrado = agendaContactos.find(contacto => contacto.nombre.toLocaleLowerCase().includes(buscaNombre.toLocaleLowerCase()));

            if (contactoEncontrado) {
                console.log(`El teléfono de ${contactoEncontrado.nombre} es: ${contactoEncontrado.tel}`);
            } else {
                console.log(`El contacto ${buscaNombre} no existe`);
            }
            break;
        // 2. Agregar
        case "2":
            let nombreNuevo = prompt('Inserte el nombre: ');
            let telNuevo = prompt('Inserte el tel nuevo: ');
            while (!(!isNaN(telNuevo) && telNuevo.length > 0 && telNuevo.length <= 11)) {
                tel = prompt('Inserte un número válido de no más de 11 caracteres');
            }
            telNuevo = parseInt(telNuevo);
            agendaContactos.push({ nombre: nombreNuevo, tel: telNuevo });
            console.log(agendaContactos)
            break;
        // 3. Modificar
        case "3":
            let modificaNombre = prompt('Introduce el nombre del contacto a modificar: ');
            let encuentraContacto = agendaContactos.find(contacto => contacto.nombre.toLocaleLowerCase().includes(modificaNombre.toLocaleLowerCase()));
            if(encuentraContacto){
                encuentraContacto.tel = prompt('Introduce el nuevo número: ');
                console.log(`El nuevo número de ${encuentraContacto.nombre} es ${encuentraContacto.tel}`);
            } else {console.log(`El contacto ${modificaNombre} no existe`);
        }
            break;
        // 4. Eliminar
        case "4":  
            let eliminaNombre = prompt('Introduce el nombre del contacto a eliminar: ');
            let contactoEliminado = agendaContactos.find(contacto => contacto.nombre.toLocaleLowerCase().includes(eliminaNombre.toLocaleLowerCase()));
            let indexContacto = agendaContactos.indexOf(contactoEliminado)
            agendaContactos.splice(indexContacto, 1);
            console.log(`Se elimino a ${contactoEliminado.nombre} de la agenda.`)
            break;
        // 5. Salir
            case "5":
            console.log("Gracias, vuelva pronto.");
            is_on = false;
            break;
        default:
            console.log("Opción inválida\n Elija un numero del 1 al 5");
            break;
    }
}
}

mi_agenda();