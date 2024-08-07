/* 
  El tipo Enumerado no existe en JavaScript
*/

const diasSemana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
const numerosValidos = [1, 2, 3, 4, 5, 6, 7]

const getDiaSemana = (numero) => numerosValidos.includes(numero)
                                 ?diasSemana[numero - 1]
                                 :diasSemana[numero % 7 - 1]

for (let i = 1; i <= 7; i++) console.log(getDiaSemana(i))

/* Reto Extra */

class Pedido {
    estadoPedido = {
        'PENDIENTE': 'Pendiente', 
        'ENVIADO': 'Enviado', 
        'ENTREGADO': 'Entregado',
        'CANCELADO': 'Cancelado'
    }

    constructor(id) {
      this.estado = 'PENDIENTE'
      this.id = id
    }

    enviarPedido() {
      if (this.estado === 'PENDIENTE') {
        this.estado = 'ENVIADO'        
      } else {
        return 'No se puede enviar el pedido'
      } 
      return 'Pedido Enviado'
    }

    entregarPedido() {
      if (this.estado === 'ENVIADO') {
        this.estado = 'ENTREGADO'
      } else {
        return 'No se puede entregar un pedido que no se ha enviado'
      }
      return 'Pedido Entregado'
    }

    cancelarPedido() {
        if (this.estado === 'ENTREGADO') {
            return 'No se puede cancelar el pedido ya fue entregado'
        } else {
            this.estado = 'CANCELADO'
            return 'Pedido Cancelado'
        }
    }

    mostrarEstadoPedido() {
      console.log(`Pedido ${this.id}: ${this.estadoPedido[this.estado]}`)
    }
}


/* Creando Pedidos */
console.log('\n\nCreando Pedidos')

const pedido1 = new Pedido(101)
const pedido2 = new Pedido(102)
const pedido3 = new Pedido(103)

pedido1.mostrarEstadoPedido()
pedido2.mostrarEstadoPedido()
pedido3.mostrarEstadoPedido()

/* Modificando estado de los pedidos */
console.log('')
console.log('Interactuando con los pedidos')

console.log(pedido1.enviarPedido())
console.log(pedido2.entregarPedido())
console.log(pedido3.cancelarPedido())
console.log(pedido1.entregarPedido())
console.log(pedido2.enviarPedido())
console.log(pedido3.enviarPedido())

/* Mostrar estado de los Pedidos tras interactuar */
console.log('\nEstado de los pedidos tras interactuar: ')
pedido1.mostrarEstadoPedido()
pedido2.mostrarEstadoPedido()
pedido3.mostrarEstadoPedido()