// Ejercicio 1
    // Un enum es una lista de constantes.
    enum diasSemana {Lunes = 1, Martes = 2, Miércoles = 3, Jueves = 4, Viernes = 5, Sábado = 6, Domingo = 7};

    console.log('Introduce un número')
    console.log(`Hoy es ${diasSemana[2]}`);
    console.log(`Quedan 7 días para él ${diasSemana[1]}`);
    console.log(`Mi cumple cuadra un ${diasSemana[3]}`);

// Ejercicio Extra

    enum EstadoPedido{PENDIENTE, ENVIADO, ENTREGADO, CANCELADO}

    class Pedido {
        constructor(private _id : number, private _estado : EstadoPedido){}

        set id(id : number){
            this._id = id;
        } 

        get id() : number{
            return this._id;
        }

        set estado(estado : EstadoPedido){
            this._estado = estado;
        }
        
        get estado() : EstadoPedido{
            return this._estado;
        }
    
        public ActualizarEstado(nuevoEstado : EstadoPedido) : void {
            this._estado = nuevoEstado;
        }
    }

    // Ciclo de vida de nuestro Pedido 1
    let pedido1 = new Pedido(1, EstadoPedido.PENDIENTE);
    console.log(`Día de hoy: ${diasSemana[2]}. Tu pedido con identificador ${pedido1.id} está ${EstadoPedido[pedido1.estado]}, llegará el ${diasSemana[4]}`);
    //Mandando el pedido
    pedido1.ActualizarEstado(EstadoPedido.ENVIADO)
    console.log(`Día de hoy: ${diasSemana[3]}. Tu pedido con identificador ${pedido1.id} está ${EstadoPedido[pedido1.estado]}, llegará el ${diasSemana[4]}`);
    //Pedido Entregado
    pedido1.ActualizarEstado(EstadoPedido.ENTREGADO)
    console.log(`Día de hoy: ${diasSemana[4]}. Tu pedido con identificador ${pedido1.id} está ${EstadoPedido[pedido1.estado]}`);
    
    // Ciclo de vida de nuestro Pedido 2
    let pedido2 = new Pedido(2, EstadoPedido.PENDIENTE);
    console.log(`Día de hoy: ${diasSemana[2]}. Tu pedido con identificador ${pedido2.id} está ${EstadoPedido[pedido2.estado]}, llegará el ${diasSemana[6]}`);
    //Mandando el pedido
    pedido2.ActualizarEstado(EstadoPedido.ENVIADO)
    console.log(`Día de hoy: ${diasSemana[3]}. Tu pedido con identificador ${pedido2.id} está ${EstadoPedido[pedido2.estado]}, llegará el ${diasSemana[6]}`);
    //Pedido Cancelado
    pedido2.ActualizarEstado(EstadoPedido.CANCELADO)
    console.log(`Día de hoy: ${diasSemana[4]}. El cliente decidió cancelar su pedido con identificador ${pedido2.id}, el pedido está ${EstadoPedido[pedido2.estado]}`);
