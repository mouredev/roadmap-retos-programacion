const diasDeLaSemana = Object.freeze({
  1: 'Lunes',
  2: 'Martes',
  3: 'Miércoles',
  4: 'Jueves',
  5: 'Viernes',
  6: 'Sábado',
  7: 'Domingo'
})

const obtenerDiaSemana = (dia) => {
  switch (dia) {
    case 1:
      console.log(diasDeLaSemana[1])
      break
    case 2:
      console.log(diasDeLaSemana[2])
      break
    case 3:
      console.log(diasDeLaSemana[3])
      break
    case 4:
      console.log(diasDeLaSemana[4])
      break
    case 5:
      console.log(diasDeLaSemana[5])
      break
    case 6:
      console.log(diasDeLaSemana[6])
      break
    case 7:
      console.log(diasDeLaSemana[7])
      break
    default:
      console.log('Día de la semana no encontrado.')
  }
}

obtenerDiaSemana(4)

const estado = Object.freeze({
  PENDIENTE: 'PENDIENTE',
  ENVIADO: 'ENVIADO',
  ENTREGADO: 'ENTREGADO',
  CANCELADO: 'CANCELADO'
})


// DIFICULTAD EXTRA
class Pedido {

  constructor() {
    this._id = Date.now()
    this._estado = 'PENDIENTE'
  }

  getId() {
    return this._id
  }

  getEstado() {
    return this._estado
  }

  setEstado(estado) {
    const estadoActual = this.getEstado()
    if (estadoActual === 'PENDIENTE') {
      if (estado === 'ENVIADO' || estado === 'CANCELADO') this._estado = estado
    }
    if (estadoActual === 'ENVIADO') {
      if (estado === 'ENTREGADO' || estado === 'CANCELADO') this._estado = estado
    }
  }

  mostrarDetalle() {
    return `#${this.getId()} - Estado: ${this.getEstado()}`
  }

}

console.log('---  PEDIDO 1  ---')
const pedido1 = new Pedido()
console.log(pedido1.mostrarDetalle())
pedido1.setEstado(estado.ENVIADO)
console.log(pedido1.mostrarDetalle())
pedido1.setEstado(estado.ENTREGADO)
console.log(pedido1.mostrarDetalle())

console.log('---  PEDIDO 2  ---')
const pedido2 = new Pedido()
console.log(pedido2.mostrarDetalle())
pedido2.setEstado(estado.CANCELADO)
console.log(pedido2.mostrarDetalle())