const Semana = Object.freeze({
  LUNES: 'LUNES',
  MARTES: 'MARTES',
  MIERCOLES: 'MIERCOLES',
  JUEVES: 'JUEVES',
  VIERNES: 'VIERNES',
  SABADO: 'SABADO',
  DOMINGO: 'DOMINGO'
})

function diaDeLaSemana(num) {
  if (num > 7) num %= 7
  switch (num) {
    case 1: return(Semana.LUNES);
    case 2: return(Semana.MARTES);
    case 3: return(Semana.MIERCOLES);
    case 4: return(Semana.JUEVES);
    case 5: return(Semana.VIERNES);
    case 6: return(Semana.SABADO);
    default: return(Semana.DOMINGO);
  }
}

console.log(diaDeLaSemana(15))
console.log(diaDeLaSemana(2))
console.log(diaDeLaSemana(24))
console.log(diaDeLaSemana(53))
console.log(diaDeLaSemana(6))
console.log(diaDeLaSemana(49))
// --------------------------------- DIFICULTAD EXTRA ---------------------------------
const Estado = Object.freeze({
  PENDIENTE: 'PENDIENTE',
  ENVIADO: 'ENVIADO',
  ENTREGADO: 'ENTREGADO',
  CANCELADO: 'CANCELADO'
})

class Pedido {
  constructor(id) {
    this.id = id
    this.estado = 'CREADO'
  }

  cambiarEstado(estado) {
    switch (estado) {
      case Estado.PENDIENTE:
        (this.estado === 'CREADO') ? console.log(`Se ha cambiado el estado de su pedido a: ${this.estado = Estado.PENDIENTE}`)
                                    : console.log(`No se podido cambiar el estado a pendiente, el estado de su pedido es: ${this.estado}`)
        break;
      case Estado.ENVIADO:
        (this.estado === Estado.PENDIENTE) ? console.log(`Se ha cambiado el estado de su pedido a: ${this.estado = Estado.ENVIADO}`)
                                            : console.log(`No se podido cambiar el estado a enviado, el estado de su pedido es: ${this.estado}`)
        break;
      case Estado.ENTREGADO:
        (this.estado === Estado.ENVIADO) ? console.log(`Se ha cambiado el estado de su pedido a: ${this.estado = Estado.ENTREGADO}`)
                                          : console.log(`No se podido cambiar el estado a entregado, el estado de su pedido es: ${this.estado}`)
        break;
      case Estado.CANCELADO:
        (this.estado === Estado.ENTREGADO || this.estado === Estado.CANCELADO) ? console.log('No se ha podido cancelar su pedido')
        : (this.estado !== Estado.ENVIADO) ? console.log(`Su pedido se ha ${this.estado = Estado.CANCELADO}`) // se cancela si esta en estado pendiente o creado
                                              : console.log(`Su pepido se ha ${this.estado = Estado.CANCELADO} el repartidor tuvo un accidente`)
        break;
      default:
        console.log('El estado solicitado para el pedido no existe')
        break;
    }
  }

  estadoActual() {
    switch (this.estado) {
      case Estado.PENDIENTE:
        console.log('Su pedido esta pendiente seguramente dentro de unos minutos sera enviado')
        break;
      case Estado.ENVIADO:
        console.log('Su pedido ya ha sido enviado, en unos minutos le llegara\n¡Esperamos que lo disfrute!')
        break;
      case Estado.ENTREGADO:
        console.log('El pedido ha sido entregado\nDeje un comentario de como fue su experiencia')
        break;
      case Estado.CANCELADO:
        console.log('Ups su pedido esta cancelado, esperemos que no pase la proxima ;)')
        break;
      default:
        console.log('El pedido se ha creado con exito, dentro de unos minutos ya estara pendiente')
        break;
    }
  }
}

const pedidoEntregado = new Pedido(159753)
pedidoEntregado.cambiarEstado(Estado.PENDIENTE)
pedidoEntregado.cambiarEstado(Estado.ENVIADO)
pedidoEntregado.cambiarEstado(Estado.ENTREGADO)
console.log('\n')
const pedidoCancelado = new Pedido(159753)
pedidoCancelado.cambiarEstado(Estado.PENDIENTE)
pedidoCancelado.cambiarEstado(Estado.ENVIADO)
pedidoCancelado.cambiarEstado(Estado.CANCELADO)
pedidoCancelado.estadoActual()
console.log('\n')
const pedidoVerEstados = new Pedido(159753)
pedidoVerEstados.estadoActual()
pedidoVerEstados.cambiarEstado(Estado.PENDIENTE)
pedidoVerEstados.estadoActual()
pedidoVerEstados.cambiarEstado(Estado.ENVIADO)
pedidoVerEstados.estadoActual()
pedidoVerEstados.cambiarEstado(Estado.ENTREGADO)
pedidoVerEstados.estadoActual()
console.log('\n')
const pedidoCambiarMalEstados = new Pedido(159753)
pedidoCambiarMalEstados.cambiarEstado(Estado.PENDIENTE)
pedidoCambiarMalEstados.cambiarEstado(Estado.ENTREGADO)
pedidoCambiarMalEstados.cambiarEstado(Estado.ENVIADO)