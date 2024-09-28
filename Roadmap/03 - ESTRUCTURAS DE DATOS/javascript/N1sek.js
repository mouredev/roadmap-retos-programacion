/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 */

// Arrays, sets, objects, map

let array = ["JavaScript", "Python", "Bash"]

console.log("++++++ ARRAYS ++++++")
console.log("Array original: "+array)
array.push("PHP") // Insertar
console.log("Array con inserción al final: "+array)
array.unshift("Ruby")
console.log("Array con insercion al inicio: "+array)
array[2] = "Lua" // Modificar en X posicion
console.log("Array con modificacion: "+array)
array.shift() //Elimina el primer elemento del array
console.log("Array con primer elemento eliminado: "+array)
array.pop(); //Elimina el ultimo elemento del array
console.log("Array con ultimo elemento eliminado: "+array)

/* SPLICE y SLICE */
let arraySplice = ["JavaScript", "Python", "Bash", "Lua", "PHP"]
console.log("--- SPLICE: modifica el array original ---")
console.log("Array original: "+arraySplice)
console.log("Elementos eliminados del array con 'splice(2)': "+arraySplice.splice(2)) // splice con un parametro
console.log("Resultado array: "+arraySplice)
arraySplice.push("Bash", "Lua", "PHP")
console.log("Elementos eliminados del array con 'splice(2,1)': "+arraySplice.splice(2,1)) // splice con dos parametros
console.log("Resultado array: "+arraySplice)
arraySplice.push("Bash")
console.log("Elemento eliminado y reemplazado del array con 'splice(2,1,'Ruby')': "+arraySplice.splice(2,1,"Ruby")) //splice con tres parametros
console.log("Resultado array: "+arraySplice)

let arraySlice = ["JavaScript", "Python", "Bash", "Lua", "PHP"]
console.log("--- SLICE: no modifica el array original ---")
console.log("Array original: "+arraySlice)
let arraySlice2 = arraySlice.slice(2) //Aray original no es modificado, por eso hay que guardar el resultado
console.log("Resultado array con 'slice(2)': "+arraySlice2) // slice con un parametro
let arraySlice3 = arraySlice.slice(1,3)
console.log("Resultado array con 'slice(1,3)': "+arraySlice3)

console.log("++++++ SETS ++++++")
let miSet = new Set([1, 2, 3, 4])
miSet.add(3) //Esto no hace nada porque los valores son unicos, no puede haber dos iguales
miSet.add(5) //Inserta
miSet.add("Hola") //Inserta
miSet.delete(1) //Elimina
console.log(miSet)

console.log("++++++ OBJETOS ++++++")
let yo = {
    nombre: "Dennis",
    apellido: "Cizma",
    edad: 20,
    nombreCompleto: function(){ return this.nombre + " " + this.apellido;}
}

yo["colorOjos"] = 'Azules' // Insercion
yo["nombre"] = 'Denis' // Modificacion
delete yo.edad // Elimina propiedad
console.log(yo)
console.log(yo.nombreCompleto())

console.log("++++++ MAP ++++++")
let miMapa = new Map([
    [1, "uno"],
    [2, "dos"],
    [3, "tres"]
])

miMapa.set(4, "cuatro") // Insercion
miMapa.set(2, "dos sobreescrito") // Modificacion
miMapa.delete(1) // Borrado

//Borra TODOS los elementos
//miMapa.clear()

console.log(miMapa)
console.log(miMapa.has(2)) // Busca elemento y devuelve true si existe