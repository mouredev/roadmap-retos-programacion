/* Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).*/

const dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"];

function diaDeLaSemana (numero) {
    if (numero >= 1 && numero <= 7) {
        return dias[numero - 1];
    } else{
        return "Número no válido"
    }
};

console.log(diaDeLaSemana(7));

/*DIFICULTAD EXTRA (opcional):
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

const EstadoPedido = Object.freeze({
    PENDIENTE: 'Pendiente',
    ENVIADO: 'Enviado',
    ENTREGADO: 'Entregado',
    CANCELADO: 'Cancelado'
});

class Pedido {
    constructor(id) {
        this.id = id;
        this.estado = EstadoPedido.PENDIENTE; // Estado inicial
    }

    enviar() {
        if (this.estado === EstadoPedido.PENDIENTE) {
            this.estado = EstadoPedido.ENVIADO;
        } else {
            console.log(`No se puede enviar el pedido ${this.id}. Estado actual: ${this.estado}`);
        }
    }

    entregar() {
        if (this.estado === EstadoPedido.ENVIADO) {
            this.estado = EstadoPedido.ENTREGADO;
        } else {
            console.log(`No se puede entregar el pedido ${this.id}. Estado actual: ${this.estado}`);
        }
    }

    cancelar() {
        if (this.estado === EstadoPedido.PENDIENTE || this.estado === EstadoPedido.ENVIADO) {
            this.estado = EstadoPedido.CANCELADO;
        } else {
            console.log(`No se puede cancelar el pedido ${this.id}. Estado actual: ${this.estado}`);
        }
    }

    mostrarEstado() {
        return `El estado del pedido ${this.id} es el siguiente: ${this.estado}`;
    }
}

const pedido1 = new Pedido(1);
console.log(pedido1.mostrarEstado()); // El estado del pedido 1 es el siguiente: Pendiente
