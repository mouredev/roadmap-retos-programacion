console.log(`----------(◉◉∖____/◉◉)---------- Estructura de datos ----------(OO∖____/OO)----------
    Utilizando operaciones de inserción, borrado, actualización y ordenación.
    - Array[]           - Set()                    - Map()
    let Array = [,,]    let set = new Set([,,])    let map = new Map([[clave,valor],])

    - Object{}
    let object = {clave: valor,}
    `
)
console.log("-------------------------------- Array[] --------------------------------")
let arrayED = [1, 2 ,3 , 4, 5, 6, 7, 8, 9, 10]
console.log(arrayED)
console.log("El tipo de dato del Arreglo es: " + typeof(arrayED)) // typeOf arrayED
console.log("Longitud del Arreglo: " + arrayED.length)
console.log(`Extraer datos del Array[0]: ${arrayED[0]}`)
console.log(`Extraer datos del Array[1]: ${arrayED[1]}`)
console.log(`Extraer datos del Array[2]: ${arrayED[2]}`)
console.log(`Extraer datos del Array[3]: ${arrayED[3]}`)
console.log(`Extraer datos del Array[4]: ${arrayED[4]}`)
console.log(`Extraer datos del Array[5]: ${arrayED[5]}`)
console.log(`Extraer datos del Array[6]: ${arrayED[6]}`)
console.log(`Extraer datos del Array[7]: ${arrayED[7]}`)
console.log(`Extraer datos del Array[8]: ${arrayED[8]}`)
console.log(`Extraer datos del Array[9]: ${arrayED[9]}`)
console.log(`Extraer datos del Array[10]: ${arrayED[10]}`) // No contiene datos

arrayED[10] = 11 // Insetando valores en la posición del Array[10]
arrayED[11] = 12 // Insetando valores en la posición del Array[11]
arrayED[12] = 13 // Insetando valores en la posición del Array[12]
arrayED[13] = 14 // Insetando valores en la posición del Array[13]
arrayED[14] = 15 // Insetando valores en la posición del Array[14]
console.log(arrayED)

// Insertando un valor al principio del arreglo con un unshift()
console.log("con unshift() insertamos un valor al principio del Array")
arrayED.unshift(0)
console.log(arrayED)

// Insetamos un valor al final del arreglo con push()
console.log("Con push() insertamos un valor al final del Array")
arrayED.push(16, 17)
console.log(arrayED)

// Borrar elemento en Array
console.log("Con splice() indicamos cuales son los valores del Array que deseamos eliminar");
// splice("indiceInsertar, "cantidadELiminar", "elemento1")
// splice("indiceEliminar, "cantidadELiminar")
console.log(`El valor que eliminaremos del Array es: ${arrayED.splice(10, 1)}`)
console.log(arrayED)

// Actualización de valores del Array
console.log(arrayED)
console.log("Actualizar valores del Array mediante la posición del Array[posición]")
arrayED[5] = "Ivett"
arrayED[11] = "Samantha"
arrayED[2] = "Miguel"
arrayED[16] = "Aixa"
arrayED[6] = "Rox"
arrayED[17] = "Jenifer"
arrayED[3] = "Marce"
arrayED[0] = "Leonel"
arrayED[13] = "Xochitl"
arrayED[14] = "Nikol"
console.log(arrayED)

// Ordenar
// arrayED.sort((a, b) => a - b)  Ordena siempre y cuando sea del mismo dato string o number.
// console.log(arrayED)

console.log("-------------------------------- Set() --------------------------------")
let setED = new Set()
// Set no permite repetir los valores
setED = new Set([
    "McLaren", "Acura", "Peugeot",
    "Apollo", "Ferrari", "Bugatti",
    "Chevrolet", "Porsche", "Alfa Romeo",
    "Mercedez-Benz", "Lamborghini", "BMW",
    "Cadillac" ,"Nissan", "Mitsubishi",
    "Lexus", "Apex", "Mazda",
    "Pagani", "Jaguar", "Koenigsegg",
    "Rezvani", "Pannfarina", "Rimac",
    "Volkswagen", "Zenvo", "Lotus",
    "Volkswagen", "Zenvo", "Lotus",
])
console.log(setED)

console.log(`El tipo de dato del Set es: ${typeof(setED)}`) // typeOf setED
console.log("Tamaño del Set: " + setED.size)

// Con set.add() insertamos elementos (si no esta repetido)
console.log("Con .add() insertaremos elementos al Set")
setED.add("Trion")
setED.add("Jeep")
setED.add("Ford")
console.log(setED)
console.log("Longitud del Set: " + setED.size)

// Con set.has() comprobamos si elemento ya existe en el conjunto true o false
console.log(setED.has("Ford")) // true si existe.
console.log(setED.has("Mini")) // false no existe.

console.log("Con .delete() eliminaremos el elementos deseado del Set")
setED.delete("Trion")
setED.delete("Lotus")
console.log(setED)
console.log("Longitud del Set: " + setED.size)

console.info("No es posible actualizar elementos en un set en JavaScript. Esto se debe a que los sets no tienen índices para obtener un elemento específico, a diferencia de los arrays.")

/* 
No es posible reordenar los elementos de un set ni obtener un elemento directamente por su número. Pero sí, es posible ordenar elementos en un set en JavaScript, pero no de forma directa.

    * Un set en JavaScript es una colección ordenada de elementos únicos, que se recuperan en el mismo orden en el que se insertaron.
    * Para ordenar un set en JavaScript, se debe convertir primero en un Array, ordenar el Array y luego volver a convertirla en un set.
*/
console.log("Convertiremos el Set en Array")
let arraySet = [...setED]
console.log(arraySet)
console.log("Ordenaremos los valores del Array con .sort()")
arraySet.sort() // Con .sort() ordenamos los valores del Array
console.log(arraySet)
console.log("Convertiremos el Array en Set nuevamente")
let setEDNew = new Set(arraySet)
console.log(setEDNew)

console.log("-------------------------------- Map() --------------------------------")
let mapED = new Map() // Declaración
mapED = new Map([ // Inicialización
    ["Lamborghini", "Asterión"],
    ["Pagani", "Zonda R"],
    ["Porsche", "Panamera Turbo S"],
    ["Mercedes Benz", "AMG GT-S"],
])
console.log(mapED)
console.log(`El tipo de dato del Map es: ${typeof(mapED)}`) // typeOf setED
console.log("Tamaño del Map: " + mapED.size)

console.log("Accediendo a los elementos del Map() mediante la clabe Key")
console.log(mapED.get("Lamborghini")) // Accediendo a los valores del Map mediante la key
console.log(mapED.get("Pagani"))

console.log("Insertando elementos con set()")
mapED.set("McLaren", "SENNA GTR")
mapED.set("Puritalia", "Berlinetta")
mapED.set("Ford Mustang", "GT-500")
mapED.set("Ultima", "RS")
mapED.set("Chevrolet Corvette", "Stingray")
console.log(mapED)

console.log("Eliminando elementos con delete()")
mapED.delete("Ultima") // Eliminando elementos del Map con la clave Key
console.log(mapED)

console.log("Actualizando elementos con set()")
// El metodo .set() modifica tanto como agrega nuevos elementos al Map
mapED.set("Lamborghini", "Terzo Millennio")
mapED.set("Pagani", "Huayra BC")
mapED.set("Porsche", "911 GT1 Evolution")
mapED.set("porsche", "918 Spyder")
console.log(mapED)

console.log("-------------------------------- Object[] --------------------------------")
let objectED = {
    "Lamborghini": "Termario",
    "Porsche": "Taycan Turbo S",
    "Pagani": "Zonda R",
    "McLaren": "SENNA GTS",
}
console.log(objectED)
console.log(`El tipo de dato del Object es: ${typeof(objectED)}`) // typeOf objectED

console.log("Accediendo a las propiedades del Object")
// Hay dos formas de acceder a las propiedades
console.log(objectED.Lamborghini) // Notación por punto "."
console.log(objectED["Porsche"]) // Notación por corchetes "[]"
console.log(objectED.Pagani) // Notación por punto "."
console.log(objectED["McLaren"]) // Notación por corchetes "[]"

console.log("Insertando propiedades al Object")
objectED.Maserati = "MC20 GT2" // Insetando propiedades con Notación por punto "."
objectED["Jaguar"] = "C-X75" // Insetando propiedades con Notación por corchetes "[]"
objectED.Honda = "Civic Type-R" // Insetando propiedades con Notación por punto "."
objectED["Arrinera"] = "Hussarya 33" // Insetando propiedades con Notación por corchetes "[]"
objectED.Apollo = "N" // Insetando propiedades con Notación por punto "."
objectED["Edad"] = 24 // Insetando propiedades con Notación por corchetes "[]"
console.log(objectED)

console.log("Eliminando propiedades del Object")
delete objectED.Apollo
console.log(objectED)

console.info("Modificando propiedades del Object")
objectED.Porsche = "911 GT1 Evolution" // Modificando propiedades del objecto usando la Notación por punto "."
objectED["McLaren"] = "P1" // Modificando propiedades del objecto usando la Notación por corchetes "[]"
console.log(objectED)

// Mostrando el tipo de dato mediante la clave 
console.log(typeof objectED.Lamborghini)
console.log(typeof objectED.Edad)

// Ejercició Extra
console.info(`----------(◉◉∖____/◉◉)---------- Ejercicio Extra ----------(OO∖____/OO)----------
    Creando una agenda de contactos`)
// Primero debemos requerir el módulo "readline". Este módulo está integrado en Node.js, por lo que no nesitamos instalarlo.
const readline = require('readline')
// Crear una interfaz para leer y escribir
// Usamos el metodo "createInterface()" de "readline" para crear una interfaz que nos permita leer y escribir en la consola
const rl = readline.createInterface({
    input: process.stdin, // Entrada desde la consola
    output: process.stdout // Salida hacia la consola
})

// Creamos nuestro Array vació
let agendaContactos = []

// Declaramos nuestra función
function agenda_contactos() {
    console.log("")
    // Hacemos uso de la varialbe "rl" llamando al metodo "question", al usuario le haremos una consulta, donde nos tendra que decir que desar hacer, su respuesta se almacenara en el parametro (operacion). 
    rl.question("¿Que operación desea realizar? \n1.- Agregar: \n2.- Buscar: \n3.- Actualizar: \n4.- Eliminar: \n5.- Salir: \n= ", (operacion) => {
        // Haremos uso de una condicion, donde le pasaremos el parametro "operacion", donde evaluara si coincide con con los casos "case"
        switch (operacion) {
            // Caso 1.- Agregar
            case "agregar":
                // Con el metodo question, haremos una pregunta al usuario. 
                // La respuesta que nos de se pasara como parametro a (nombre)
                rl.question("Nombre de la persona: ", (nombre) => {
                    rl.question("Contacto de la persona: ", (contacto) => {
                        let contactoNum = parseInt(contacto) // convertimos la variable contacto a tipo Number
                        // Comparamos si lo que nos como parametro el Usuario es de tipo Numbrer, si es podra agregar el nombre y el contacto
                        if (!isNaN(contactoNum)) {
                            // con push agregamos el nombre y el contacto al array, pero como object dentro del array
                            agendaContactos.push({nombre: nombre, contacto: contactoNum})
                            //console.log(`Se agrego a la persona ${agendaContactos["nombre"] = nombre} y su contacto ${agendaContactos["contacto"] = contactoNum}`)
                            console.log(`Se agrego a la persona ${nombre} y su contacto ${contactoNum}`)
                            console.log(agendaContactos) // Mostrar los elementos del object para verificar
                        } else {
                            console.log("El número de contacto, no debe de contener palabras.")
                        }
                        // Si la condicion se cumple velvemos a las operaciones de nuevo
                        agenda_contactos()
                    })
                })
                break
            // Caso 2.- Buscar
            case "buscar":
                // Con el metodo question, haremos una pregunta al usuario. 
                // La respuesta que nos de se pasara como parametro a (nombre)
                rl.question("Nombre de la persona: ", (nombre) => {
                    // agendaContactos.find: El metodo find() devuelve el primer objecto que cumpla con la condiciòn, busca un nombre cuyo nombre conincida con el nombre que el usuario ingreso. La funcion callback
                    // buscar_callback (Callback: compara .nombre de todos los objectos del arreglo si es igual al parametro nombre. Ussamos una funcion flecha (Arrow function)
                    let buscar = agendaContactos.find(buscar_callback => buscar_callback.nombre === nombre)
                    // Si "buscar" es verdadero
                    if (buscar) {
                        // Se imprime por consola el nombre y el contacto
                        console.log(`Datos de ${nombre}: Contacto ${buscar.contacto}`)
                    } else {
                        console.log("No se ha podido encontrar a la Persona")
                    }
                    // rl.close()
                    agenda_contactos()
                })
                break
            // Caso 3.- Actualizar
            case "actualizar":
                // Con el metodo question, haremos una pregunta al usuario. 
                // La respuesta que nos de se pasara como parametro a (nombre)
                rl.question("Persona: ", (nombre) => {
                    // agendaContacto.findIndex(): buscar el índice del primer nombre en la agendaContactos cuyo nombre coincida con el nombre que ingreso el usuario. Si se encuentra el nombre, findIndex() devuelve el índice del elemento; si no, devuelve -1.
                    let actualizar_nombre = agendaContactos.findIndex((actualizar_callback) => actualizar_callback.nombre === nombre)
                    // Si actualizar_nombre !== -1 es estrictamente no igual
                    if (actualizar_nombre !== -1) {
                        // Imprimimos por consola el nombre y el contacto
                        console.log(`Datos de la persona: \n  Nombre: ${nombre} \n  Contacto: ${agendaContactos[actualizar_nombre].contacto}`) // Mostramos el nombre y el contacto de la persona buscada
                        // Le hacemos una preguntamos al usuario, la respuesta que nos de se pasara como parametro a (nuevoElemento)
                        rl.question("Ahora que desea hacer, cambiar el Nombre o cambiar el Contacto: ", (nuevoElemento) => {
                            // Si el parametro "nuevoElemento" es igual a "nombre"
                            if (nuevoElemento == "nombre") {
                                // Le decimos al usuario que escriba el nuevo nombre, la respuesta que nos de se pasara como parametro a (nuevoNombre)
                                rl.question("Ingrese el nuevo nombre: ", (nuevoNombre) => {
                                    // Accedemos al array agendaContacto[actualizar_nombre] en la posicion indice especificada por "actualizar_nombre"
                                    // Para acceder al valor del nombre: agendaContactos[actualizar_nombre].nombre
                                    agendaContactos[actualizar_nombre].nombre = nuevoNombre // Asignamos el nuevo valor del usuario que ingreso
                                    console.log("Se ha actualizado el nombre.") // mostramos un mensaje
                                    console.log(agendaContactos) // Mostramos los cambios
                                    agenda_contactos() // Nos regresamos al Inicio
                                })
                            }
                            // Si el parametro "nuevoElemento" es igual a "contacto"
                            else if (nuevoElemento == "contacto") {
                                // Le decimos al usuario que ingrese el nuevo contacto, la respuesta que nos de se pasara como parametro a (nuevoContacto)
                                rl.question("Ingrese el nuevo número del contacto: ", (nuevoContacto) => {
                                    // Convertimos el parametro a Number inicializandolo con una nueva variable contactoNum_actualizar
                                    let contactoNum_actuailzar = parseInt(nuevoContacto)
                                    // Comparamos si "contactoNum_actuailzar" no es de tipo Number, pero si es tipo Number pasa.
                                    if (!isNaN(contactoNum_actuailzar)) {
                                        // Accedemos al array agendaContacto[actualizar_nombre] en la posicion indice especificada por "actualizar_nombre"
                                        // Para acceder al valor del nombre: agendaContactos[actualizar_nombre].contacto
                                        agendaContactos[actualizar_nombre].contacto = contactoNum_actuailzar // Asignamos el nuevo valor del usuario que ingreso
                                        console.log("Se ha actualizado el contacto") // Mostramos el mensaje
                                        console.log(agendaContactos) // Mostramos el array
                                        agenda_contactos() // Nos regresamos al Inicio           
                                    } else {
                                        console.log("El número de contacto, no debe de contener palabras.")
                                        agenda_contactos() // Nos regresamos al Inicio            
                                    }
                                })                                
                            } else {
                                // Si el usuario no elige ni "nombre" ni "contacto": Si el usuario ingresa algo diferente a "nombre" o "contacto", se muestra un mensaje de error solicitando que elija una opción válida
                                console.log("Indique que desea hacer. ¡Por Favor!")
                                agenda_contactos() // Nos regresamos al Inicio
                            }
                        })
                    } else {
                        console.error("No se ha podido encontrar a la Persona. \nVerifique si se encuentra. ¡Por Favor!")
                        agenda_contactos() // Nos regresamos al Inicio
                    }
                })
                break
            // Caso 4.- Eliminar
            case "eliminar":
                // Mostramos los elementos del array
                console.log(agendaContactos)
                // Con el metodo question, haremos una pregunta al usuario. 
                // La respuesta que nos de se pasara como parametro a (nombre)
                rl.question("Nombre de la Persona: ", (nombre) => {
                    // agendaContacto.findIndex(): buscar el índice del primer nombre en la agendaContactos cuyo nombre coincida con el nombre que ingreso el usuario. Si se encuentra el nombre, findIndex() devuelve el índice del elemento; si no, devuelve -1.
                    let eliminar = agendaContactos.findIndex(eliminar_Persona => eliminar_Persona.nombre === nombre)
                    // Comparamos si eliminar es indiferente de -1
                    if (eliminar !== -1) {
                        // Accedemos al array, usando el metodo splice()
                        // eliminar: especificamos el indice en el que se desea modificar el array
                        // 1: le indicamos cuantos elemento queremos eliminar desde ese indice, en este caso es 1
                        agendaContactos.splice(eliminar, 1) // eliminamos el elemento en la posición encontrada por findIndex().
                        console.log("Se ha eliminado correctamente") // Mostramos el mensaje
                        console.log(agendaContactos)// Mostramos el array modificado
                    } else {
                        console.log("La persona que usted desea eliminar, no exite.")
                    }
                    agenda_contactos() // Volvemos al inicio
                })
                break
            // Caso 5.- Salir
            case "salir":
                // Aquí se está utilizando el método close() del objeto readline.Interface (almacenado en rl), que cierra la interfaz de lectura.
                // Esto termina la sesión interactiva con el usuario, es decir, deja de escuchar las entradas del usuario y finaliza el programa o el ciclo de preguntas.
                // Cuando se ejecuta rl.close(), el programa termina, y el proceso de Node.js se detiene si no hay más código que ejecutar.
                rl.close()
                break
            default:
                // Si en dado caso se escribe mal uno de los casos se muestra el mensaje
                console.warn("De las opciones indique que desea hacer. ¡Por favor!")
                agenda_contactos() // Nuevamente nos vamos al inicio si no se repeta los "case"
        }            
    })
}
agenda_contactos() // Imprimimos por consola la función