// Enum para representar los días de la semana
enum DiasSemana {
    LUNES,
    MARTES,
    MIERCOLES,
    JUEVES,
    VIERNES,
    SABADO,
    DOMINGO
}

// Función para obtener el nombre del día de la semana según el número

function obtenerDia(numeroDia: number): string {
    return DiasSemana[numeroDia];
}

console.log(obtenerDia(DiasSemana.LUNES)); 
console.log(obtenerDia(DiasSemana.JUEVES)); 

/*
    * DIFICULTAD EXTRA
*/

// Enum para representar el estado de los pedidos
enum EstadoPedido {
    PENDIENTE = "Pendiente",
    ENVIADO = "Enviado",
    ENTREGADO = "Entregado",
    CANCELADO = "Cancelado"
}


class Pedido {
    constructor(private id: number, private estado: EstadoPedido = EstadoPedido.PENDIENTE) { }

    enviar(): void {
        if (this.estado === EstadoPedido.PENDIENTE) {
            this.estado = EstadoPedido.ENVIADO;
            console.log(`El pedido ${this.id} ha sido enviado.`);
        } else {
            console.log(`El pedido ${this.id} no puede ser enviado porque su estado es ${this.estado}.`);
        }
    }

    entregar(): void {
        if (this.estado === EstadoPedido.ENVIADO) {
            this.estado = EstadoPedido.ENTREGADO;
            console.log(`El pedido ${this.id} ha sido entregado.`);
        } else {
            console.log(`El pedido ${this.id} no puede ser entregado porque su estado es ${this.estado}.`);
        }
    }

    cancelar(): void {
        if (this.estado !== EstadoPedido.ENTREGADO) {
            this.estado = EstadoPedido.CANCELADO;
            console.log(`El pedido ${this.id} ha sido cancelado.`);
        } else {
            console.log(`El pedido ${this.id} no puede ser cancelado porque ya ha sido entregado.`);
        }
    }

    mostrarEstado(): void {
        console.log(`Estado del pedido ${this.id}: ${this.estado}`);
    }
}


const pedido1 = new Pedido(1);
pedido1.mostrarEstado(); 
pedido1.enviar(); 
pedido1.entregar(); 
pedido1.mostrarEstado();

const pedido2 = new Pedido(2);
pedido2.cancelar(); 
pedido2.mostrarEstado();
