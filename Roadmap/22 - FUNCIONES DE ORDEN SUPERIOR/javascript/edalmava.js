const array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
// El método forEach() ejecuta la función indicada una vez por cada elemento del array.
array.forEach(e => console.log(e))

// El método map() crea un nuevo array con los resultados de la llamada a la función indicada aplicados a cada uno de sus elementos.
const dobles = array.map(e => e * 2)
console.log(dobles) // Devuelve un array con los dobles de cada elemento

// El método filter() crea un nuevo array con todos los elementos que cumplan la condición implementada por la función dada.
const pares = array.filter(e => e % 2 == 0)
console.log(pares) // Devuelve un array con los números pares

// El método reduce() ejecuta una función reductora sobre cada elemento de un array, devolviendo como resultado un único valor.
const suma = array.reduce((acc, e) => acc + e, 0)
console.log(suma)  // Suma los elementos del array

// El método some() comprueba si al menos un elemento del array cumple con la condición implementada por la función proporcionada.
const cero = array.some(e => e == 0)
console.log(cero)  // Verifica si por lo menos uno de los elementos es cero

// El método sort() ordena los elementos de un arreglo (array) localmente y devuelve el arreglo ordenado.
const array2 = [5, 4, 8, 7, 0]
array2.sort((a, b) => a - b) // Ordenar de forma ascendente
console.log(array2)

array2.sort((a, b) => b - a) // Ordenar de forma descendente
console.log(array2)

// El método findIndex() devuelve el índice del primer elemento de un array que cumpla con la función de prueba proporcionada. 
console.log(array.findIndex(e => e % 2 == 0))

// DIFICULTAD EXTRA

const estudiantes = [{ nombres: "Juan Perez", 
                      fecha_nacimiento: "01/01/2010", 
                      calificaciones: [4.0, 6.0, 10.0] }, 
                     { nombres: "Simon Becerra", 
                      fecha_nacimiento: "02/05/2011", 
                      calificaciones: [10.0, 9.0, 8.0] }, 
                     { nombres: "Angel Martinez", 
                      fecha_nacimiento: "03/04/2010", 
                      calificaciones: [10.0, 2.0, 6.0] }, 
                     { nombres: "Jorge Vanegas", 
                      fecha_nacimiento: "08/09/2011", 
                      calificaciones: [7.0, 9.0, 10.0] }, 
                     { nombres: "Alberto Maldonado", 
                      fecha_nacimiento: "03/04/2011", 
                      calificaciones: [10, 10, 10] }
                    ]

// Promedio de calificaciones

const listadoPromedio = estudiantes.map(e => 
    ({ nombres: e.nombres, 
      promedio: e.calificaciones.reduce((a, e) => a + e, 0)/e.calificaciones.length  
    }))
console.log(listadoPromedio)

// Mejores estudiantes - promedio superior o igual a 9
const mejoresEstudiantes = listadoPromedio.filter(e => e.promedio >= 9)
console.log(mejoresEstudiantes)

// Mayor calificación
const mayorCalificacion = listadoPromedio.sort((a, b) => b.promedio - a.promedio)
console.log(mayorCalificacion[0].promedio)
