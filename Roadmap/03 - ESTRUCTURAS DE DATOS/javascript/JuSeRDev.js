
//  * EJERCICIO:
//  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
//  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.


//! ARRAY

const number = [1, 2, 3]

console.log(number)
number.push(4) // añade al final
console.log(number)
number.unshift(0) // añade al inicio
console.log(number)
number.pop() // elimina al final
console.log(number)
number.shift() // elimina al inicio
console.log(number)
number[2] = 4 // modifica
console.log(number)
number.sort((a,b)=> b- a) // ordena de menor a mayor
console.log(number)
number.sort((a,b)=> a-b) // ordena de menor a mayor
console.log(number)

//! OBJETOS

let persona = {
    nombre: "Sebastian",
    apellido: "rodriguez"
}
console.log(persona)
persona.edad = 33 // Añade una nueva propiedad
console.log(persona)
delete persona.apellido // elimina una propiedad
console.log(persona)
persona.nombre = "Juan Sebastian" // actualiza una propiedad
console.log(persona)
let keys = Object.keys(persona).sort();  // Ordena las claves alfabéticamente
console.log(keys)

//! SET

let personas = new Set(["juan", "sebatian", "Laura"]) // aqui me muestra la posicion y su valor
console.log(personas); 
personas.add("Daniel") // aqui me muestra la posicion y su valor
console.log(personas); 
personas.add("persona5") // aqui me muestra la posicion y su valor
console.log(personas); 
personas.delete("persona5")// aqui me muestra la posicion y su valor
console.log(personas); 


//! MAP

let personas2 = new Map([["persona1", "Sebastian"],["persona2", "Laura"]])

// para crear un mapa debe ser un array dentro de un array [[llave, valor]] 
console.log(personas2);
personas2.set("persona3", "Maxi") //añade la clave
console.log(personas2);
personas2.delete("persona3") // Elimina la clave
console.log(personas2);
personas2.set("persona1", "Juan") //modifica la clave
console.log(personas2);

//  * DIFICULTAD EXTRA (opcional):
//  * Crea una agenda de contactos por terminal.
//  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
//  * - Cada contacto debe tener un nombre y un número de teléfono.
//  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
//  *   los datos necesarios para llevarla a cabo.
//  * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
//  *   (o el número de dígitos que quieras)
//  * - También se debe proponer una operación de finalización del programa.

const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


const contactos = new Map()

const agregarContacto = ()=>{
    rl.question("Escriba el nombre: ",(nombre)=>{
        rl.question("Escriba el celular: ", (telefono)=>{
            contactos.set(nombre, telefono)
            console.log(`contacto agregado: ${nombre} - ${telefono}`)
            console.log("Volveras al menu principial")
            agenda()
        })
    })
   
}

const BuscarContacto = ()=>{
    rl.question("Escribe el nombre del contacto que desdeas buscar: ", (nombre)=>{
        if (contactos.has(nombre)) {
            const telefono = contactos.get(nombre)
            console.log(`Contacto encontrado: ${nombre} - ${telefono}`);
        } else{
            console.log(`El contacto ${nombre} no existe`);
        }
        agenda()
    })
}

const actualizarContacto = ()=>{
    rl.question("Escribe el nombre del contacto que quieres actualizar: ",(nombre)=>{
        if (contactos.has(nombre)) {
            rl.question("Escrible en telefono actulizado: ",(telefono)=>{
                contactos.set(nombre,telefono)
                console.log("Contacto actualizado exitosamente")
                console.log(`Contacto: ${nombre} - ${telefono}`)
                agenda()
            })
        }else{
            console.log("El contacto no se puede actualizar por que no existe existe")
            agenda()
        }
    })
}

const eliminarContacto = ()=>{
    rl.question("escribe el nombre del contacto que deseas eliminar: ", (nombre)=>{
        if (contactos.has(nombre)) {
            contactos.delete(nombre)
            console.log("contacto eliminado");
            agenda()
        } else {
            console.log("El contacto no esta en la base de datos");
        }
    })
}

const mostrarContactos = ()=>{
    console.table(contactos)
    agenda()
}

const salir = ()=>{
    console.log("saliste de la aplicacion");
    rl.close()
    process.exit(0)
}


const agenda = ()=>{
    console.log("escribe la opcion que deseas")
    console.log("1. agregar contacto")
    console.log("2. Buscar contacto")
    console.log("3. actualizar contacto")
    console.log("4. eliminar contacto")
    console.log("5. mostrar contactos existentes")
    console.log("6. salir")
    
    rl.question("Que vas a hacer?", (respuesta)=>{
        if (respuesta === "1") {
            agregarContacto()
        } else if (respuesta === "2") {
            BuscarContacto()
        }else if (respuesta === "3") {
            actualizarContacto()
        }else if(respuesta === "4"){
            eliminarContacto()
        }else if(respuesta === "5"){
            mostrarContactos()
        }else if(respuesta === "6"){
            salir()
        }else{
            console.log("No seleccionaste una opcion valida")
            agenda()
        }
    })
}

agenda()
