// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23 
"use strict";

// Definición del Enum para los días de la semana
const Week = {
    LUNES: 1,
    MARTES: 2,
    MIERCOLES: 3,
    JUEVES: 4,
    VIERNES: 5,
    SABADO: 6,
    DOMINGO: 7
};

// Función para mostrar el nombre del día de la semana
const getNameWeek = numeroDia => {
    switch(numeroDia) {
        case Week.LUNES:
            return "Lunes";
        case Week.MARTES:
            return "Martes";
        case Week.MIERCOLES:
            return "Miércoles";
        case Week.JUEVES:
            return "Jueves";
        case Week.VIERNES:
            return "Viernes";
        case Week.SABADO:
            return "Sábado";
        case Week.DOMINGO:
            return "Domingo";
        default:
            return "Número de día inválido";
    }
}

// Ejemplo de uso
console.log("************ EJERCICIO ***************");
const day = 4;
console.log(`El día ${ day } es: ${ getNameWeek(day) }`);

console.log("\n************ EJERCICIO EXTRA ***************");

// Definición del Enum para los estados de pedido
const EstadoPedido = {
    PENDIENTE: 1,
    ENVIADO: 2,
    ENTREGADO: 3,
    CANCELADO: 4
};

// Clase Pedido
class Pedido {
    constructor(_id) {
        this.id = _id;
        this.estado = EstadoPedido.PENDIENTE;
    }

    // Método para marcar el pedido como enviado
    marcarEnviado() {
        if (this.estado === EstadoPedido.PENDIENTE) {
            this.estado = EstadoPedido.ENVIADO;
            console.log(`El pedido con ID ${ this.id } ha sido enviado.`);
        } else {
            console.log(`El pedido con ID ${ this.id } no se puede enviar en su estado actual.`);
        }
    }

    // Método para marcar el pedido como entregado
    marcarEntregado() {
        if (this.estado === EstadoPedido.ENVIADO) {
            this.estado = EstadoPedido.ENTREGADO;
            console.log(`El pedido con ID ${ this.id } ha sido entregado.`);
        } else {
            console.log(`El pedido con ID ${ this.id } no se puede entregar en su estado actual.`);
        }
    }

    // Método para cancelar el pedido
    cancelarPedido() {
        if (this.estado !== EstadoPedido.CANCELADO) {
            this.estado = EstadoPedido.CANCELADO;
            console.log(`El pedido con ID ${ this.id } ha sido cancelado.`);
        } else {
            console.log(`El pedido con ID ${ this.id } ya está cancelado.`);
        }
    }

    // Método para mostrar el estado del pedido
    mostrarEstado() {
        const estado_str = {
            [EstadoPedido.PENDIENTE]: "Pendiente",
            [EstadoPedido.ENVIADO]: "Enviado",
            [EstadoPedido.ENTREGADO]: "Entregado",
            [EstadoPedido.CANCELADO]: "Cancelado"
        };
        console.log(`Estado del pedido con ID ${ this.id }: ${ estado_str[this.estado] }`);
    }
}

// Creando pedidos
const pedido1 = new Pedido(1);
const pedido2 = new Pedido(2);

// Mostrar el estado inicial de los pedidos
pedido1.mostrarEstado();
pedido2.mostrarEstado();

// Interactuar con los pedidos
pedido1.marcarEnviado();
pedido2.marcarEnviado();
pedido1.marcarEntregado();
pedido2.cancelarPedido();

// Mostrar el estado final de los pedidos
pedido1.mostrarEstado();
pedido2.mostrarEstado();
