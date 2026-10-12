/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
*/


// Función como argumento

function aplicarFunc(func, x) {
    return func(x)
}

/*
    SOBRE LAS ARROW FUNCTION:
    1. Un solo parámetro → los paréntesis son opcionales. 2. Si hay más de un parámetro, los paréntesis son obligatorios.
    3. Si el cuerpo tiene una sola expresión, el return es implícito. 4. Si usas llaves {}, debes escribir return
*/
const contar = str => str.length

console.log(aplicarFunc(contar, "Antonio"))

// Retorno de fución
// 1.
function aplicaMultiplicador(n) {
    function multiplicador(x) {
        return x * n
    }
    return multiplicador // No ejecuta la función. No hace esto: return multiplicador(); Hace esto: "Devuelve la función completa para poder usarla después."
}
/*
    Llamamos a aplicaMultiplicador(2), El parámetro n recibe el valor 2, Dentro de esa ejecución se crea la función: 
    function multiplicador(x) {
        return x * n;
    }
    Y luego: return multiplicador; devuelve la función, no el resultado. Por eso multiplicador2 ahora contiene una función:
*/

/*
    Y podrías crear otras:

    const multiplicadorPor10 = aplicaMultiplicador(10);

    console.log(multiplicadorPor10(5)); // 50

    Ahí se ve la magia del closure: aplicaMultiplicador fabrica funciones que ya llevan "guardado" el número por el que multiplican.
*/

 multiplicador2 = aplicaMultiplicador(2)
 console.log(multiplicador2(5))



console.log(aplicaMultiplicador(5)(5))


// map()
let numbers = [1, 2, 3, 6, 5 ,4]
function aplicarDoble(p) {
    return p * 2
}

let mapDelArray = numbers.map(aplicarDoble)

console.log(mapDelArray)

// O TAMBIÉN SIN GUARDARLO EN LA VARIABLE mapDelArray Y DIRECTAMENTE EN EL console.log().


console.log(numbers.map(aplicarDoble))


// Filter()
function pares(p) {
    return p % 2 === 0
}

console.log(numbers.filter(pares))
console.log(`Los números pares son: ${numbers.filter(pares)}`)
console.log(`Los números pares son: ${numbers.filter(pares).join(", ")}`)

/*
    sort:

    "Resta b a a. Si sale negativo, significa que a es menor y va primero. Si sale positivo, significa que a es mayor y debe ir después."

    Por eso funciona para ordenar de menor a mayor.

    EXPLICACIÓN DETALLADA:
    si la resta (a, b) => a - b   da un número positivo: +5 va detrás y si da un número negativo : -5  va delante porque se busca ordenar de menos a mayor, si es cero se mantiene igual,
    si quisiéramos ordenar a la inversa , osea de mayor a menor invertiríamos el orden de los operadores así: (a, b) => b - a
    o lo que es lo mismo: (a) pequeño primero → ascendente , (b) grande primero → descendente.
*/

// sort()
console.log(`Los números pares son: ${numbers.filter(pares).sort((a, b) => a - b).join(", ")}`)

console.log(numbers.sort((a, b) => a - b).reverse()) // Para tenerlos ordenados de mayor a menor,  primero los ordenamos con sort() y después invertimos el resultado con reverse().


// reduce()
const suma = (a, b) => a + b

console.log(numbers.reduce(suma))

/*
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
*/


let estudiantes = [
    { nombre: "Manolo", fechaNacimiento: "12-04-1982", notas: [8, 7, 5, 10, 9, 7]},
    { nombre: "Adolfo", fechaNacimiento: "06-08-1986", notas: [4, 8, 5, 6, 9, 10]},
    {nombre: "Pepi", fechaNacimiento: "22-09-1982", notas: [6, 3, 5, 8, 4, 6]},
    //{ nombre: "Paco", fechaNacimiento: "15-12-1991", notas: [9, 9, 9, 9, 9, 9]},
    { nombre: "Pacual", fechaNacimiento: "15-12-1991", notas: [9, -1, 8, 7, 7, 9]},
    { nombre: "Sara", fechaNacimiento: "15-12-1991", notas: [9, 6, 8, 7, 7, 9]}
    
]


function promedioNotasAlumnos() {

    // LOS PARENTESIS DESPUÉS DE LA FLECHA SIGNIFICAN: DEVUELVE ESE OBJETO.
    /*
        Regla fácil de recordar
        expresión → devuelve esa expresión automáticamente.
        ({ ... }) → devuelve un objeto.
        { ... } → has abierto un bloque de código, así que necesitas return si quieres devolver algo.

        Esa diferencia entre ({}) (objeto) y {} (bloque de código) es una de las peculiaridades de las funciones flecha en JavaScript.
    */

    // CALCULAR EL PROMEDIO
    return  estudiantes.map (estudiante => ({ // No necesitas una variable intermedia para devolverla en el return, porque el return se hace directamente del resultado de map().

        nombre: estudiante.nombre,
        promedio:
            estudiante.notas.reduce((suma, nota) => suma + nota, 0) / estudiante.notas.length
    }))
}


const calcularElPromedio = promedioNotasAlumnos()

// FORMATEAR EL RESULTADO POR PANTALLA
calcularElPromedio.forEach(estudiante => {
        console.log(`${estudiante.nombre}: ${estudiante.promedio.toFixed(2)}`) // Con toFixed(2) limitamos a 2 los números decimales.
})


// Calcular los alumnos con una media mayor o igual a 9
const promedioNotas = promedioNotasAlumnos()

const estudiantesMatricula = promedioNotas
.filter(estudiante => estudiante.promedio >= 9)
.map(estudiante => estudiante.nombre)

if(estudiantesMatricula.length === 0) {
    console.log("No hay estudianes con Matrícula de Honor")
}

console.log(estudiantesMatricula)

// Mejores estudiantes

const mejoresEstudiantes = [...promedioNotas]
.sort((a, b) => a.promedio - b.promedio).reverse()
console.log("Los mejores estudiantes son: ")

mejoresEstudiantes.forEach(estudiante => {
    console.log(`${estudiante.nombre}: ${estudiante.promedio}`)
})

// Mayor calificación de todos los alumnos

const notaMasAlta = estudiantes.reduce((max, estudiante) => {
    const maxNotaAlumno = Math.max(...estudiante.notas) // El operador Spread ...; 1: Dentro de un array: const copiaNotas = [...notas]; → crea otro array, pero 2: Como argumento de una función: Math.max(...notas); → separa los elementos,
                                                        // Math.max() no recibe un array:Recibe números separados:Math.max(8, 7, 5, 10, 9, 7); // Entonces:...notas expande el array para convertirlo en una lista de argumentos.
                                                        // Una buena regla mental: 
                                                        // [...array] ➡️ "quiero otro array con esos elementos";
                                                        // funcion(...array) ➡️ "quiero pasar esos elementos como argumentos separados"
                                                        // Es el mismo operador, pero el contexto cambia su comportamiento.

    return maxNotaAlumno > max ? maxNotaAlumno : max
}, 0)
console.log(`La nota más alta es: ${notaMasAlta}`)


/*
RESUMEN:
Una forma sencilla de recordarlo:

reduce() → recorre y acumula un resultado.
Math.max() → compara números y devuelve el mayor.

En este ejercicio:

reduce compara los máximos de cada alumno.
Math.max encuentra el máximo dentro de las notas de cada alumno.

Son dos niveles de búsqueda: primero la mejor nota de cada alumno y después la mejor nota de todos los alumnos.
*/

/*
  EXPLICACIÓN PASO POR PASO:

  Vamos paso a paso:

1. Para cada alumno sacamos su nota máxima

Ejemplo con Manolo:

Math.max(...[8, 7, 5, 10, 9, 7])

El ... convierte:

[8, 7, 5, 10, 9, 7]

en:

8, 7, 5, 10, 9, 7

Entonces:

Math.max(8, 7, 5, 10, 9, 7)

devuelve:

10
2. reduce compara todas esas máximas

Empieza con:

max = 0

Alumno Manolo:

maxNotaAlumno = 10
10 > 0 → nuevo máximo = 10

Alumno Adolfo:

maxNotaAlumno = 10
10 > 10 → no cambia

Y así con todos.

También podrías hacerlo en dos pasos, que quizá sea más claro para el punto en el que estás:

const todasLasNotas = estudiantes.flatMap(estudiante => estudiante.notas);

const notaMasAlta = Math.max(...todasLasNotas);

console.log(notaMasAlta);

Aquí:

flatMap()

convierte:

[
 [8,7,5,10,9,7],
 [4,8,5,6,9,10]
]

en:

[
8,7,5,10,9,7,4,8,5,6,9,10
]

y luego Math.max busca la mayor.

Para el ejercicio de funciones de orden superior, esta segunda opción es muy interesante porque practicas:

flatMap() → transformar y aplanar arrays.
Math.max() → obtener máximo.
reduce() → acumular un resultado.

Aunque si quieres practicar específicamente reduce, la primera versión encaja mejor.
*/


//Una calificación debe estar comprendida entre 0 y 10 (admite decimales).

const notasInvalidas = estudiantes
.flatMap(estudiante => estudiante.notas
    .filter(nota => nota < 0 || nota > 10)
    .map(nota => ({   // APROVECHAMOS QUE ESTAMOS DENTRO DEL CONTEXTO DE ESTUDIANTES GRACIAS A flatMap PARA ACCEDER A estudiante.nombre y nota.
        nombre: estudiante.nombre,
        nota: nota
    }))
)

console.log("Esta notas son iválidas")
console.log(notasInvalidas)

notasInvalidas.forEach(estudiante => {
        console.log(`Esta nota: ${estudiante.nota}, de este alumno: ${estudiante.nombre}, es inválida: : `)
})

/*
De hecho, hay una forma muy útil de recordar para qué sirve cada función de orden superior:

Función	Piensa en ella como...
map()	"Transforma cada elemento."
filter()	"Quédate solo con los que cumplen una condición."
reduce()	"Convierte todos los elementos en un único resultado."
forEach()	"Haz algo con cada elemento, pero no construyas nada."
sort()	"Reordena los elementos."
flatMap()	"Transforma y aplana el resultado."
*/

/*
    ¡¡¡ IMPORTANTE !!!

    De hecho, es una buena forma de recordar qué métodos modifican el array:

    map, filter, slice, concat → CREAN UN NUEVO ARRAY. 
    sort, reverse, push, pop, shift, unshift, splice → MODIFICAN EL ARRAY EXISTENTE. 

    Es una distinción muy importante en JavaScript y aparece constantemente cuando trabajas con funciones de orden superior.
*/