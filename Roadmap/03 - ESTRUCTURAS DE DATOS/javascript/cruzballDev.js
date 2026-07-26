//------ARRAY-------

let frutas = ["Melón", "Pera", "Manzana", "Naranja"]

console.log(frutas)

// Inserción
frutas.push("Sandía", "Melocotón", "Piña") // Añade después del último.
console.log(frutas)
frutas.unshift("Tomate") // Añade al principio del array.
console.log(frutas)
frutas.splice(1, 0, "Kiwi"); // Añade un elemento en una posición específica SIN eliminar otro elemento.
console.log(frutas);

// Borrado
frutas.pop() // Elimina el ultimo elemento del array.
console.log(frutas)
frutas.shift() // Elimina el primer elemento del array.
console.log(frutas)
frutas.splice(1, 2) // Elimina dos elementos partiendo desde la posición 1 (este incluido).
console.log(frutas)

// Actualización
frutas[0] = "Ciruela" // Accediendo mediante el indice.
console.log(frutas) // Actualiza o sustituye Melón que estaba en el índice 0 por Ciruela.
frutas.splice(1, 1, "Mango") // Actualiza o sustituye Manzana que estaba en la posición 1 por Mango.
console.log(frutas)

// Ordenación
frutas.sort() // Ordena los elementos alfabéticamente.
console.log(frutas)

let num = [1, 4, 3, 2 , 16]
console.log(num)

num.sort()
console.log(num)

num.sort((a, b) => a - b); // Ordenar de manera ascendente.
console.log(num)

num.sort((a, b) => b - a); // Ordenar de manera descendente.
console.log(num)

//------SET-------

let mySet = new Set(["Melón", "Pera", "Manzana", "Naranja", "Manzana"])
console.log(mySet)
console.log(mySet instanceof Set ) // Para comprobar que es de tipo set.

let datos = new Set()

datos.add(10) // con add añadimos cualquier tipo de dato al set, incluso objetos.
datos.add("Hola")
datos.add(true)
datos.add(null)

let persona = {
    nombre: "Ana",
    apellido: "Garcia"
}

datos.add(persona)
console.log(datos)
console.log(datos.size) // Nos devuelve el número de elementos.

datos.add("hola")
console.log(datos)

datos.delete("hola") // Con delete borramos elementos del set.
console.log(datos)

console.log(datos.has("hola")) // Con has comprobamos si un elemento existe en el set.
console.log(datos.has("Hola"))

datos.clear() // Vacía completamente el set.
console.log(datos)

let vehiculos = new Set()

vehiculos.add("Coche")
vehiculos.add("Moto")
vehiculos.add("Camión")

for(let vehiculo of vehiculos.values()) { // Devuelve los valores a través del iterador.
    console.log(vehiculo)
}

for(let vehiculo of vehiculos.keys()) { // Lo mismo que values().
    console.log(vehiculo)
}

for(let vehiculo of vehiculos) { // Para recorrer el Set.
    console.log(`Recorrer el Set con for of ${vehiculo}`)
}

vehiculos.forEach((vehiculo) => { // Para recorrer el Set.
    console.log(`Recorrer el Set con for each ${vehiculo}`);
});


// Convertir de Array a Set.
let arrayMotos = ["Yamaha", "Honda", "Suzuki", "Ducati",  "Suzuki"]
console.log(arrayMotos)

let setMotos = new Set(arrayMotos)
console.log(setMotos)


// Convertir de Set a Array.
let arrayOtravez = Array.from(setMotos) // La más común mediante .from().
console.log(arrayOtravez)

setMotos = new Set(arrayOtravez)
console.log(setMotos)

arrayOtravez = [...setMotos] // Otra manera mediante propagación.
console.log(arrayOtravez)

//------MAP-------

let marcaModelo = new Map([
    ["Toyota", "Yaris"],
    ["BMW", "E36"],
    ["Ford", "Fiesta"],
    ["Dacia", "Sandero"]
])
console.log(marcaModelo)
console.log(marcaModelo.get("Dacia"))

// Otra manera de crear un Map
let coche = new Map()

coche.set("Marca", "BMW") // Con .set añadimos o modificamos datos en el Map.
coche.set("Modelo", "E36")
coche.set("Cilindrada", "1.600c.c")
console.log(coche)

coche.set("Cilindrada", "2.000c.c")// Si el valor existe se actuliza.
console.log(coche)

coche.delete("Cilindrada") // Para borrar datos se hace con .delete().
console.log(coche)

console.log(coche.size) // Devuelve la cantidad de pares almacenados.
console.log("Devuelve la Marca con .ge() = " + coche.get("Marca"))

console.log(coche.get("Plazas")) // Si el dato consultado no existe, devuelve undefined.

console.log(coche.has("Marca")) // Para comprobar si el Map contiene un dato específico.

for(let elemento of coche) { // Para recorrer el Map.
    console.log(elemento)
}

coche.forEach((valor, clave) => { // Recorre el Map.
    console.log("Recorre con un for each: " + clave, valor)
})


for(let[clave, valor] of coche) { // Recorre el Map.
    console.log("Recorre con un for of: " + clave, valor)
}

for(let clave of coche.keys()) { // Solo devuelve las keys.
    console.log("Devuelve la clave: " + clave)
}

for(let valor of coche.values()) { // Solo devuelve los valores.
    console.log(valor)
}

for(let elemento of coche.entries()) { // Devuelve los pares clave, valor.
    console.log(elemento)
}

coche.clear() // Con clear vaciamos completamente el Map.
console.log(coche)

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
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
*/

// DIFICULTAD EXTRA (opcional):

/* const prompt = require("prompt-sync")(); */

const readline = require("node:readline/promises");
const { stdin, stdout } = require("node:process");

const rl = readline.createInterface({
    input: stdin,
    output: stdout
});


async function miAgenda(){
    let agenda = new Map([
    ["Manolo", 672934725],
    ["Pepe", 652839712],
    ["Antonio", 923684571]
    ])

    let opcion
    let activo = true
    let nombre
    let nuevoNombre
    let telefono
    let nuevoTelefono

    while (activo) {

        console.log (`

            ======= AGENDA ========
            1. Buscar contacto
            2. Añadir contacto
            3. Eliminar contacto
            4. Actualizar contacto
            5. Mostrar agenda
            6. Salir del programa `
        )

        opcion = (await rl.question("Elige una opción: ")).trim();

        switch(opcion) {
            case "1":
                // Buscar contacto
                nombre = (await rl.question ("Introduce un nombre: ")).trim()

                if(!isNaN(nombre) || nombre === "") {
                    console.log(`Debes de introducir un nombre \n ¡Solo se admiten letras!`)
                    break;
                }
                if(!agenda.has(nombre) ) {
                    console.log(`¡El nombre introducido: ${nombre} no está en la agenda!.\n`)
                }
                else {
                    console.log(`Teléfono de ${nombre} es : ${agenda.get(nombre)}`)
                }
                break;
            case "2":
                // Añadir contacto
                nombre = (await rl.question("Introduce un nombre: ")).trim()
                if(!isNaN(nombre) || nombre === "") {
                    console.log(`Debes de introducir un nombre \n ¡Solo se admiten letras!`)
                    break;
                }else {
                    console.log(`Se ha añadido el contacto: ${nombre};\n`)
                }
                telefono = (await rl.question("Introduce un número de telefono: ")).trim()
                if( isNaN(telefono) ||  telefono.length >11 || telefono === "" ) {
                    console.log("¡Datos incorrectos!\nSolo se adminten números entre el 0 y el 11.")
                }else {
                    agenda.set(nombre, telefono)
                    console.log(`Se ha añadido el usuario con nombre: ${nombre}; y el  telefono: ${telefono};\n`)
                }
                break;
            case "3":
                // Eliminar contacto

                nombre = (await rl.question(`Introduce un nombre: `)).trim()
                if(!agenda.has(nombre) ){
                    console.log("¡Has introducido un nombre incorrecto!\n Intentalo de nuevo.\n")
                    break;
                }

                telefono = agenda.get(nombre)
                agenda.delete(nombre)
                console.log(`El usuario con el nombre: ${nombre}, y el telefono ${telefono} ha sido eliminado.\n`)
                break;
            case "4":
                // Actualizar contacto

                nombre = (await rl.question("Introduce un nombre: ")).trim()

                if(!agenda.has(nombre) ) {
                    console.log("Este contacto no existe.")
                    break;
                }

                nuevoNombre = (await rl.question(`Introduce el nuevo nombre: `)).trim()

                if(!isNaN(nuevoNombre) || nuevoNombre === "" ) {
                  console.log(`Debes de introducir un nombre \n ¡Solo se admiten letras!`)
                  break;
                }else {
                    console.log(`Se ha modificado el contacto a: ${nuevoNombre};\n`)
                }

                nuevoTelefono = (await rl.question(`Introduce el nuevo número de telefono: `)).trim()

                if(isNaN(nuevoTelefono)  || nuevoTelefono.length > 11 || nuevoTelefono === "")  {
                    console.log("¡Datos incorrectos!\nSolo se adminten números entre el 0 y el 11.")
                }else {
                    agenda.delete(nombre)
                    agenda.set(nuevoNombre, nuevoTelefono)
                    console.log(`¡\n El nombre del usuario se ha actualizado a:  ${nuevoNombre} y\n el telefono del usuario se ha actualizado a: ${nuevoTelefono}!`)
                }
                break;
            case "5":
                // Mostrar agenda

                console.log("\nContendido de la Agenda: \n")
                for(const[nombre, telefono] of agenda) {

                    console.log(` ${nombre}: ${telefono}`)
                }
                break;
            case "6":
                // Salir del programa
                activo = false
                console.log("Fin del programa")
                break;
            default:
                console.log("¡Opción incorrecta!")
        }
    }
    rl.close();
}

miAgenda()