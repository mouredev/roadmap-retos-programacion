// No hay Enum en JavaScript
// Ejercicio

let dias = {1: "Lunes", 2: "Martes", 3: "Miercoles", 4: "Jueves", 5: "Viernes", 6: "Sabado", 7: "Domingo"}

console.log(dias[1]); // Lunes
console.log(dias[6]); // Sabado

// DIFICULTAD EXTRA
class Pedidos
{
    constructor(id)
    {
        this.id = id
        this.nombreEstado = ["PENDIENTE", "ENVIADO", "ENTREGADO", "CANCELADO"]
        this.estado = this.nombreEstado[0]
    }

    consultar()
    {
        console.log(`Pedido: ${this.id}\nEstado: ${this.estado}`);
    }

    enviado()
    {
        if(this.estado == this.nombreEstado[0])
        {
            this.estado = this.nombreEstado[1]
            console.log("El envio se realizo correctamente");
        }
        else if(this.estado == this.nombreEstado[1])
        {
            console.log("El pedido ya estaba en estado enviado");
        }
        else if(this.estado == this.nombreEstado[2])
        {
            console.log("El pedido fue entregado");
        }
        else
        {
            console.log("El pedido fue cancelado");
        }
    }

    entregado()
    {
        if(this.estado == this.nombreEstado[1])
        {
            this.estado = this.nombreEstado[2]
            console.log("El pedido ha sido entregado con exito");
        }
        else if(this.estado == this.nombreEstado[2])
        {
            console.log("El pedido ya estaba en estado entregado");
        }
        else if(this.estado == this.nombreEstado[0])
        {
            console.log("El pedio sigue en estado de pendiente, ni quiera ha sido enviado");
        }
        else
        {
            console.log("El pedido fue cancelado");
        }
    }

    cancelado()
    {
        if(this.estado != this.nombreEstado[3])
        {
            this.estado = this.nombreEstado[3]
            console.log("El pedido se cancelo con exito");
        }
        else
        {
            console.log("El peido ya estaba en estado de cancelado");
        }
    }
}


let pedido52 = new Pedidos(52)
let pedido89 = new Pedidos(89)
let pedido101 = new Pedidos(101)


pedido52.entregado()
pedido52.consultar()

pedido52.enviado()
pedido52.entregado()

pedido89.enviado()
pedido89.cancelado()

pedido101.enviado()

pedido52.consultar()
pedido89.consultar()
pedido101.consultar()