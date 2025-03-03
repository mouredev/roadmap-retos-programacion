/* 🔥 EJERCICIO:
Empleando tu lenguaje, explora la definición del tipo de dato
que sirva para definir enumeraciones (Enum).
Crea un Enum que represente los días de la semana del lunes
al domingo, en ese orden. Con ese enumerado, crea una operación
que muestre el nombre del día de la semana dependiendo del número entero
utilizado (del 1 al 7).
*/
const DiasSemana = {
    LUNES: 1,
    MARTES: 2,
    MIERCOLES: 3,
    JUEVES: 4,
    VIERNES: 5,
    SABADO: 6,
    DOMINGO: 7,
};

function obtenerNombreDia(numero) {
    switch (numero) {
        case DiasSemana.LUNES:
            return "Lunes";
        case DiasSemana.MARTES:
            return "Martes";
        case DiasSemana.MIERCOLES:
            return "Miércoles";
        case DiasSemana.JUEVES:
            return "Jueves";
        case DiasSemana.VIERNES:
            return "Viernes";
        case DiasSemana.SABADO:
            return "Sábado";
        case DiasSemana.DOMINGO:
            return "Domingo";
        default:
            return "Número inválido. Debe estar entre 1 y 7.";
    }
}

console.log(obtenerNombreDia(1))
console.log(obtenerNombreDia(5))
console.log(obtenerNombreDia(8))

// Lunes
// Viernes
// Número inválido. Debe estar entre 1 y 7.

/* 🔥 DIFICULTAD EXTRA (opcional): ---------------------------------------------------------
Crea un pequeño sistema de gestión del estado de pedidos.
Implementa una clase que defina un pedido con las siguientes características:
- El pedido tiene un identificador y un estado.
- El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
- Implementa las funciones que sirvan para modificar el estado:
  - Pedido enviado
  - Pedido cancelado
  - Pedido entregado
  (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
- Implementa una función para mostrar un texto descriptivo según el estado actual.
- Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
*/
const EstadoPedido = {
    PENDIENTE: "PENDIENTE",
    ENVIADO: "ENVIADO",
    ENTREGADO: "ENTREGADO",
    CANCELADO: "CANCELADO",
};

class Pedido {
    constructor(id) {
        this.id = id
        this.estado = EstadoPedido.PENDIENTE
    }

    enviar() {
        if (this.estado === EstadoPedido.PENDIENTE) {
            this.estado = EstadoPedido.ENVIADO
            console.log(`Pedido ${this.id}: Enviado.`)
        } else {
            console.log(`Pedido ${this.id}: No se puede enviar. Estado actual: ${this.estado}`)
        }
    }

    entregar() {
        if (this.estado === EstadoPedido.ENVIADO) {
            this.estado = EstadoPedido.ENTREGADO;
            console.log(`Pedido ${this.id}: Entregado.`)
        } else {
            console.log(`Pedido ${this.id}: No se puede entregar. Estado actual: ${this.estado}`)
        }
    }

    cancelar() {
        if (this.estado !== EstadoPedido.ENTREGADO) {
            this.estado = EstadoPedido.CANCELADO
            console.log(`Pedido ${this.id}: Cancelado.`)
        } else {
            console.log(`Pedido ${this.id}: No se puede cancelar porque ya fue entregado.`)
        }
    }

    mostrarEstado() {
        console.log(`Pedido ${this.id}: Estado actual -> ${this.estado}`)
    }
}

// Crear pedidos y probar las funciones
const pedido1 = new Pedido(1)
pedido1.mostrarEstado()
pedido1.enviar()
pedido1.entregar()
pedido1.cancelar()
pedido1.mostrarEstado()

console.log("")

const pedido2 = new Pedido(2)
pedido2.mostrarEstado()
pedido2.cancelar()
pedido2.mostrarEstado()

// Pedido 1: Estado actual -> PENDIENTE
// Pedido 1: Enviado.
// Pedido 1: Entregado.
// Pedido 1: No se puede cancelar porque ya fue entregado.
// Pedido 1: Estado actual -> ENTREGADO
//
// Pedido 2: Estado actual -> PENDIENTE
// Pedido 2: Cancelado.
// Pedido 2: Estado actual -> CANCELADO