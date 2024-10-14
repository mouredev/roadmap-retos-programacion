interface Pedido {
  id: string,
  name: string,
  item: Array<string>
  createdDate: Date,
  note: string
}

// Confirmar pedido
const confirmarPedido = (name: string) => {
  console.log(`Confirmando pedido de ${name}`)
}

// Pedido listo
const confirmarPedidoListo = () => {
  console.log('Pedido listo!!!')
}

// Pedido entregado
const confirmarPedidoEntregado = (name: string) => {
  console.log(`Pedido entregado! Gracias por confiar en nosotros, ${name}`)
}

const crearPedido = (
  pedido: Pedido, 
  confirmarPedido: Function,
  confirmarPedidoListo: Function,
  confirmarPedidoEntregado: Function
) => {
  setTimeout(() => {
    confirmarPedido(pedido.name)
    
    setTimeout(() => {
      confirmarPedidoListo()
      
      setTimeout(() => {
        confirmarPedidoEntregado(pedido.name)
      }, 3000)  
    }, 3000) 
  }, 2000) 
}

crearPedido(
  {
    id: '1',
    name: 'Andres',
    item: ['8oz steak', 'Lemonade', 'Cheescake'],
    createdDate:  new Date(),
    note: 'I am hungry'
  },
  confirmarPedido,
  confirmarPedidoListo,
  confirmarPedidoEntregado
)