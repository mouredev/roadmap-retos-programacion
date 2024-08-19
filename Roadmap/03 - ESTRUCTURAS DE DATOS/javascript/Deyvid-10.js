// Estructuras 

// arreglo
let array = [2, 3, 4]
array.push(5) // insertar un elemento al final
array.unshift(1) // insertar un elemento al inicio
array.pop() // borra el ultimo elemento del array
array.shift() // borra el primer elemento del array
array.splice(2, 1) // borra 1 elemento del indice seleccionado
array[1] = 6 // actualiza el valor del indice seleccionado
array.splice(0, 1, 10) // actualiza solo 1 elemento en el indice seleccionado
array.sort((a, b) => a - b) // ordena un array con numeros

let array2 = ["d", "a", "z", "q", "p"]
array2.sort() // ordena un array con strings

// objeto
let objeto = {nombre: "Deyvid", profesion: "Informatica"}
objeto.pasatiempo = "Anime y videojuegos" // insertar un elemento 
objeto["segundoNombre"] = "Gabriel" // insertar un elemento 
delete objeto.pasatiempo // borrar un elemento
objeto.profesion = "Desarrollador de software" // actualizar un elemento

// mapas
let mapa = new Map()
mapa.set("nombre", "Deyvid") // insertar un elemento 
mapa.set("profesion", "Informatica") // insertar un elemento 
mapa.set("pasatiempo", "Anime y videojuegos") // insertar un elemento 
mapa.delete("pasatiempo") // borrar un elemento
mapa.set("profesion", "Desarrollador de software") // actualizar un elemento

// Conjuntos
let set = new Set()
set.add(1) // insertar un elemento 
set.add(2) // insertar un elemento 
set.add(3) // insertar un elemento 
set.delete(1) // borrar un elemento
set.delete(2); set.add(4); // actualizar un elemento