// ** EJERCICIO 

const diasSemana = Object.freeze({
    1: 'Lunes',
    2: 'Martes',
    3: 'Miércoles',
    4: 'Jueves',
    5: 'Viernes',
    6: 'Sábado',
    7: 'Domingo'
})

function diaSemana(num) {
    return diasSemana[num] || console.error('Número inválido')
}

console.log(diaSemana(7))


// ** DIFICULTAD EXTRA ** -------------------------------------------------------------------------------------------------------------------------------------

const EstadoPedido = Object.freeze({
    1: 'PENDIENTE',
    2: 'ENVIADO',
    3: 'ENTREGADO',
    4: 'CANCELADO'
});

class Pedido {
    constructor(id) {
        this.id = id;
        this.estado = EstadoPedido[1];
    }

    enviar() {
        if (this.estado === EstadoPedido[1]) {
            this.estado = EstadoPedido[2];
            console.log(`El estado del pedido ha cambiado a: ${EstadoPedido[2]}`);
        } else {
            console.log(`El pedido no se puede enviar porque se encuentra en estado: ${this.estado}`);
        }
    }

    cancelar() {
        if (this.estado !== EstadoPedido[4]) {
            this.estado = EstadoPedido[4];
            console.log(`El estado del pedido ha cambiado a: ${EstadoPedido[4]}`);
        } else {
            console.log(`El pedido ya está cancelado.`);
        }
    }

    entregar() {
        if (this.estado === EstadoPedido[2]) {
            this.estado = EstadoPedido[3];
            console.log(`El estado del pedido ha cambiado a: ${EstadoPedido[3]}`);
        } else {
            console.log(`El pedido no se puede entregar porque se encuentra en estado: ${this.estado}`);
        }
    }

    mostrarEstado() {
        switch (this.estado) {
            case EstadoPedido[1]:
                console.log(`El pedido ${this.id} está en estado: ${EstadoPedido[1]}`);
                break;
            case EstadoPedido[2]:
                console.log(`El pedido ${this.id} está en estado: ${EstadoPedido[2]}`);
                break;
            case EstadoPedido[3]:
                console.log(`El pedido ${this.id} está en estado: ${EstadoPedido[3]}`);
                break;
            case EstadoPedido[4]:
                console.log(`El pedido ${this.id} está en estado: ${EstadoPedido[4]}`);
                break;
            default:
                console.log(`Estado desconocido para el pedido ${this.id}`);
        }
    }
}

// Crear un pedido
const pedido1 = new Pedido(1);

pedido1.mostrarEstado(); // El pedido 1 está en estado: PENDIENTE
pedido1.enviar(); // El estado del pedido ha cambiado a: ENVIADO
pedido1.enviar(); // El pedido no se puede enviar porque se encuentra en estado: ENVIADO
pedido1.entregar(); // El estado del pedido ha cambiado a: ENTREGADO
pedido1.cancelar(); // El estado del pedido ha cambiado a: CANCELADO
pedido1.mostrarEstado(); // El pedido 1 está en estado: CANCELADO