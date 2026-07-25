/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#19 ENUMERACIONES
---------------------------------------
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos.
*/
// ________________________________________________________

const Weekday = Object.freeze({
    MONDAY: 1,
    TUESDAY: 2,
    WEDNESDAY: 3,
    THURSDAY: 4,
    FRIDAY: 5,
    SATURDAY: 6,
    SUNDAY: 7,
});

function getDay(num) {
    for (const [key, value] of Object.entries(Weekday)) {
        if (value === num) {
            return key;
        }
    }
    return "'o'";
}

function getNumDay(day) {
    return Weekday[day] || 0;
}

console.log(getDay(7)); // SUNDAY
console.log(getDay(3)); // WEDNESDAY
console.log(getDay(8)); // 'o'

console.log(getNumDay("TUESDAY")); // 2
console.log(getNumDay("FRIDAY")); // 5
console.log(getNumDay("abc")); // 0

// ________________________________________________________
// DIFICULTAD EXTRA

console.log("\nEJERCICIO 2:");

// Enum para el estado de pedidos
const Status = Object.freeze({
    PENDING: 1,
    SHIPPED: 2,
    DELIVERED: 3,
    CANCELED: 4,
});

class Order {
    constructor(identifier) {
        this.identifier = identifier;
        this._status = Status.PENDING;
    }

    send() {
        console.log("\nEnviar:");
        if (this._status === Status.PENDING) {
            this._status = Status.SHIPPED;
            console.log(this.info());
        } else {
            console.log(`Operación inválida:`, this.info());
        }
    }

    cancel() {
        console.log("\nCancelar:");
        if (this._status === Status.PENDING) {
            this._status = Status.CANCELED;
            console.log(this.info());
        } else {
            console.log(`Operación inválida:`, this.info());
        }
    }

    deliver() {
        console.log("\nEntregar:");
        if (this._status === Status.SHIPPED) {
            this._status = Status.DELIVERED;
            console.log(this.info());
        } else {
            console.log(`Operación inválida:`, this.info());
        }
    }

    info() {
        const statusName = Object.keys(Status).find(
            key => Status[key] === this._status
        );
        return `${this.identifier} -> ${statusName}`;
    }
}

const libro1 = new Order("libro1");
const libro2 = new Order("libro2");
const libro3 = new Order("libro3");

console.log("\n-----\nOperaciones exitosas:\n-----");
libro1.send();
libro1.deliver();
libro2.cancel();

console.log("\n-----\nOperaciones inválidas:\n-----");
libro3.deliver();
libro2.cancel();
libro1.send();
