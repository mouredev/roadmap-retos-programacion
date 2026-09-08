/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
*/


// EMULAMOS UN ENUM EN JASCRIPT PORQUE JS NO LO TIENE DE FORMA NATIVA.
const DiasSemana = Object.freeze({ // ¿Qué hace Object.freeze()? hace que el objeto no pueda modificarse después.
                                   // Sin freeze: sería posible. Con freeze: no cambia nada. Esto se parece más al comportamiento de un enum, porque los valores de un enum normalmente son constantes.
    LUNES: 1,
    MARTES: 2,
    MIERCOLES: 3,
    JUEVES: 4,
    VIERNES: 5,
    SABADO: 6,
    DOMINGO: 7
})
console.log(DiasSemana.MIERCOLES)

// Acccedemos al día que está dentro de DiasSemana y lo comparamos con el número introducido.
function obtenerNombreDia(numero) {

        for(const dia in DiasSemana) {
            if(DiasSemana[dia] === numero) {
                return dia
            }
        }
    return "¡Dato introducido incorrecto!"
}
console.log(obtenerNombreDia(3))



/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
*/

// Enum simulado
const EstadoPedido = Object.freeze({
     PENDIENTE: "PENDIENTE",
     ENVIADO: "ENVIADO",
     ENTREGADO:"ENTREGADO",
     CANCELADO:"CANCELADO"
})


// Clase pedido
class Pedido {
    constructor(id) {
        this.id= id
        this.estado = EstadoPedido.PENDIENTE //this.estado no lo pasamos por parámetro al constructor porque NO exitía fuera de la clase, por lo que si se crea desde cero, lo correcto es dentro del cosntructor de la clase sin pasarlo por parametro a dicho constructor.
    }

    // Cambiar estado a ENVIADO
    enviarPedido() {
        if(this.estado === EstadoPedido.PENDIENTE) {
            this.estado = EstadoPedido.ENVIADO
            console.log(`Pedido ${this.id} se ha enviado correctamente.`)
        }else {
            console.log(`¡El pedido ${this.id} no se ha podido enviar!`)
        }
    }
    // Cambiar estado a ENTREGADO

    entregarPedido() {
        if(this.estado === EstadoPedido.ENVIADO) {
            this.estado = EstadoPedido.ENTREGADO
            console.log(`El pedido ${this.id} ha sido entregado.`)
        }else {
            console.log(`El pedido ${this.id} no se ha podido entregar.`)
        }
    }

    // Cambiar estado a CANCELADO

    cancelarPedido() {
        if(this.estado === EstadoPedido.PENDIENTE) {
            this.estado = EstadoPedido.CANCELADO
            console.log(`El pedido ${this.id} ha sido cancelado.`)
        }else {
            console.log(`El pedido ${this.id} no se puede cancelar`)
        }
    }


    // Mostrar información del pedido
    mostrarEstado() {

        switch(this.estado) {
            case EstadoPedido.PENDIENTE:
                return `Pedido ${this.id} se está preparando para ser enviado.`
            case EstadoPedido.ENVIADO:
                return `El pedido ${this.id} está en camino.`
            case EstadoPedido.ENTREGADO:
                return `El pedido ${this.id} se entregó.`
            case EstadoPedido.CANCELADO:
                return `El pedido ${this.id} fué cancelado.`

        }
    }
}

const pedido1 = new Pedido(101) // Creamos el objeto pedido
const pedido2 = new Pedido(102)
const pedido3 = new Pedido(103)

console.log(pedido1.mostrarEstado()) // Lo mostramos por terminal

pedido1.entregarPedido() // Probamos cada caso del switch case y a ver si falla.
console.log(pedido1.mostrarEstado())

pedido1.enviarPedido() // Probamos cada caso del switch case
console.log(pedido1.mostrarEstado())

pedido1.entregarPedido() // Probamos cada caso del switch case
console.log(pedido1.mostrarEstado())

pedido1.cancelarPedido() // Probamos cada caso del switch case
console.log(pedido1.mostrarEstado())
