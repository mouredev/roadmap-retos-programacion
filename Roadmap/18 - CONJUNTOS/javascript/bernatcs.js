// ** EJERCICIO 

let conjuntoDeDatos = ['dato1', 'dato2', 'dato3']
conjuntoDeDatos.push('dato4') // Añade elemento al final
conjuntoDeDatos.unshift('dato0') // Añade elemento al principio
conjuntoDeDatos.push('dato5', 'dato6') // Añade varios elementos al final
conjuntoDeDatos.splice(2, 0, 'dato1.3', 'dato1.6') // Añade varios elementos en un sitio en concreto
conjuntoDeDatos.splice(2, 2) // Elimina elementos desde una posición dada
conjuntoDeDatos.pop() // Elimina elemento al final
conjuntoDeDatos.shift() // Elimina elemento al principio
conjuntoDeDatos[1] = 'datoDos' // Actualiza el valor de un elemento en una posición concreta
conjuntoDeDatos.includes('dato1') // Comprueba si en elemento está en un conjunto (True)
conjuntoDeDatos.indexOf('dato1') // Devuelve el índice del primer elemento coincidente
conjuntoDeDatos = [] // Elimina todo el contenido

// ** DIFICULTAD EXTRA ** -------------------------------------------------------------------------------------------------------------------------------------------------

let conjuntoDatos1 = ['dato1', 'dato2', 'dato3', 'datoRepe', 'datoRepe2']
let conjuntoDatos2 = ['dato4', 'dato5', 'dato6', 'datoRepe', 'datoRepe2']

// Unión

console.log(conjuntoDatos1.concat(conjuntoDatos2)) 

// Intersección

let interseccion = []

conjuntoDatos1.forEach(element => {
    if (conjuntoDatos2.includes(element)) {
        interseccion.push(element)
    }
});

interseccion


// Diferencia

let diferencia = []

conjuntoDatos1.forEach(element => {
    if (!conjuntoDatos2.includes(element)) {
        diferencia.push(element)
    }
});

diferencia

// Diferencia simétrica

let diferenciaSim = []

conjuntoDatos1.forEach(element => {
    if (!conjuntoDatos2.includes(element)) {
        diferenciaSim.push(element)
    }
});

conjuntoDatos2.forEach(element => {
    if (!conjuntoDatos1.includes(element)) {
        diferenciaSim.push(element)
    }
});

diferenciaSim