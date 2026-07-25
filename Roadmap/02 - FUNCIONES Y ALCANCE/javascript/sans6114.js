//TIPOS DE FUNCIONES EN JAVASCRIPT
//DECLARACIÓN FUNCTION
function saludar(nombre) {
    console.log(`¡Hola ${nombre}!`)
}
//EXPRESIÓN DE FUNCIÓN (ASIGNO UN VALOR ANONIMO A LA FUNCIÓN)
const saludarAnonimo = function (nombre) {
    console.log(`!hola ${nombre}!`)
}
//FUNCIÓN DE FLECHA
const saludarFlecha = (nombre) => {
    return `hola ${nombre}`
}
//FUNCIÓN CONSTRUCTORA
function Persona(nombre, edad) {
    this.nombre = nombre;
    this.edad = edad;
}
const natalia = new Persona('natalia', 40)
//METODOS DE OBJETOS
const persona = {
    nombre: 'santiago',
    saludar() {
        console.log(`hola soy ${this.nombre}`)
    }
}
//HIGH ORDER FUNCTION
function printNumberWith(number, action) {
    //si el numero es mayor o igual a 5, ejecuto la acción y retorno el nuevo valor
    if (number >= 5) return action(number)
}
const sumarDos = (numero) => {
    return numero + 2
}
//FUNCIONES YA CREADAS POR EL LENGUAJE
const getDate = () => {
    const date = new Date("December 26, 1995 23:15:30");
    const weekday = date.getDay();
    return weekday // 2
}
//VARIABLES LOCALES Y GLOBALES
const miPersona = 'Juan Martin'

const saludarLocal = () => {
    let miPersona
    //va a saludar a mi variable local, no a la variable global
    miPersona = 'santiago'
    return `hola, ${miPersona},`
}



//EJECUCIÓN DE FUNCIONES
saludar('santiago')
saludarAnonimo('martin')
saludarFlecha('juan')
console.log(saludarFlecha(natalia.nombre))
persona.saludar()
console.log(printNumberWith(5, sumarDos))
console.log(getDate())
console.log(saludarLocal(), `hola ${miPersona}`)



/* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

//EJERCICIO
const miFunction = (...args) => {
    let contadorNumeros = 0;
    args = args.slice(0, 2)
    const cadenas = args.every(e => typeof e === 'string')
    if (!cadenas) {
        args = args.map(e => {
            return (typeof e !== 'string') ? e.toString() : e
        })
    }
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(`${args[0]} y ${args[1]}`)
        } else if (i % 3 === 0) {
            console.log(args[0])
        } else if (i % 5 === 0) {
            console.log(args[1])
        } else {
            console.log(i)
            contadorNumeros++
        }
    }
    return contadorNumeros
}


//EJECUCIÓN DE EJERCICIO
console.log(miFunction('multiplos de 3', 'multiplos de 5'))
//SIEMPRE LOS ARGUMENTOS PASADOS A MI FUNCION VAN A CAMBIAR A CADENAS DE TEXTO Y SOLO SE TOMARAN LOS DOS PRIMEROS ELEMENTOS COMO ARGUMENTOS
console.log(miFunction(123, 'multiplos de 5', 'hola!', 'otro argumento'))
