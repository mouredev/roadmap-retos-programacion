// console.warn(), console.error(), console.info() console.log(first)

// El Tiempo de ejecución
console.time('Se ejecuto el programa tiempo:');
// Errror
let error = new Error("error en la coneccion")
console.warn("fallo en el internet")
console.error(`Error grave: ${error} `)





//table
const tabla = [1,2,3,4]
tabla.map(num => console.table(num))
//count
function countData(item){
    console.count("some data")
}
 countData("item1")
 countData("item2")
 countData("item3")
console.count("comenzar un nuevo contador")

countData("nuevoItem1")
countData("nuevoItem2")
console.count("comenzar un nuevo contador")

console.countReset("some data"); // Resets the "some data" counter de mu funcion 
countData("Newitem1");

console.timeEnd('Se ejecuto el programa tiempo:');
 
// * DIFICULTAD EXTRA (opcional):
//  * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
//  * y listar dichas tareas.
//  * - Añadir: recibe nombre y descripción.
//  * - Eliminar: por nombre de la tarea.
//  * Implementa diferentes mensajes de log que muestren información según la
//  * tarea ejecutada (a tu elección).
//  * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.

class Tareas {
    constructor() {
        
        this.tareas = []
    }
    
    getTareas(){
               
        return console.table(this.tareas)
        
    }

    addTarea(tarea, descripcionDeTarea){
        this.tareas.push({nombre:tarea, descripcion: descripcionDeTarea})
    }
    deleteTarea(nombre){
        console.time("funcion deleteTarea Ejecutando")
        const inicialContador = this.tareas.length
        this.tareas = this.tareas.filter(nom => nom. nombre !== nombre)
    //   let deleteTarea = this.tareas.filter(nom => nom.nombre !== nombre )
        
        if ( this.tareas.length < inicialContador ) {
            console.warn(`la tarea: ${nombre} fue eleiminada`)
        }  else{
            console.error("no se encontro tarea, verifique su lista de tareas ")
        } 
        console.timeEnd("funcion deleteTarea Ejecutando")
      return this.tareas
    }
}

const tarea1 = new Tareas()

tarea1.addTarea("barrer", "tomarmar una escoba y dejar limpio el espacio")
tarea1.addTarea("trapear", "se trapea despues de barrer para dejar brilloso el piso")
tarea1.getTareas()
tarea1.deleteTarea("barrer")
tarea1.getTareas()
tarea1.deleteTarea("comprar")
tarea1.addTarea("comprar", "pan y leche")
tarea1.getTareas()


