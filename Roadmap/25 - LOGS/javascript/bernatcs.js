// ** EJERCICIO 

console.trace('TRACE envía mensajes detallados sobre la ejecución del programa' )
console.debug('DEBUG son mensajes destinados a la depuración del software, prueba de código...')
console.info('INFO son mensajes informativos que indican funcionamiento normal del código')
console.warn('WARN son mensajes de advertencia que indican situaciones potencialmente problemáticas')
console.error('ERROR son errores que han ocurrido en la aplicación')

// además, hay más tipos de logs

console.log("Mensaje informativo");

console.group("Grupo de mensajes");
console.log("Mensaje dentro del grupo"); // Este mensaje sale como si fuera en un tabulador
console.groupEnd();

console.time("Tiempo de ejecución");
// Código cuya ejecución quieres medir
console.timeEnd("Tiempo de ejecución");

console.trace("Traza de pila"); // Output: stack trace

// ** DIFICULTAD EXTRA ** -------------------------------------------------------------------------------------------------------------------------------------------------------

const readline = require('node:readline')

const gestorTareas = [
    {Nombre: 'Tarea1', Descripcion: 'Esta es una tarea de prueba'}
]

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

function preguntaInicio() {
    rl.question('\n¿Qué quieres hacer?\n[Añadir] - [Eliminar]\n', (respuestaInicio) => {
        if (respuestaInicio === 'Añadir') {
            rl.question('Introduzca el nombre de la tarea que desea agregar: ', (tareaAgregar) => {
                rl.question(`Introduzca la descripción de la tarea ${tareaAgregar}: `, (descripcionAgregar) => {
                    console.time('Tiempo de ejecución')
                    gestorTareas.push({Nombre: tareaAgregar, Descripcion: descripcionAgregar})
                    console.group(`\nLa tarea ${tareaAgregar} se ha agregado satisfactoriamente`)
                    console.timeEnd('Tiempo de ejecución')
                    console.groupEnd()
                    preguntaInicio()
                })
            })
        } else if (respuestaInicio === 'Eliminar') {
            rl.question('Introduzca el nombre de la tarea que desea eliminar: ', (tareaEliminar) => {
                console.time('Tiempo de ejecución')
                gestorTareas.splice((gestorTareas.findIndex((tarea) => tarea.Nombre === tareaEliminar)), 1);
                console.group(`\nLa tarea ${tareaEliminar} se ha eliminado satisfactoriamente`)
                console.timeEnd('Tiempo de ejecución')
                console.groupEnd()
                preguntaInicio()
            })
            preguntaInicio()
        } else {
            console.warn('\nPor favor, introduzca una respuesta válida')
            preguntaInicio()
        }
    });
}

preguntaInicio()