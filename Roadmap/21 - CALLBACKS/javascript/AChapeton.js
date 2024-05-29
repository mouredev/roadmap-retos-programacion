// Confirmar pedido
const confirmarPedido = (name) => {
  console.log("Confirmando pedido de ".concat(name));
};
// Pedido listo
const confirmarPedidoListo = () => {
  console.log('Pedido listo!!!');
};
// Pedido entregado
const confirmarPedidoEntregado = (name) => {
  console.log("Pedido entregado! Gracias por confiar en nosotros ".concat(name));
};
const crearPedido = (pedido, confirmarPedido, confirmarPedidoListo, confirmarPedidoEntregado) => {
  setTimeout(() => {
      confirmarPedido(pedido.name);
      setTimeout(() => {
          confirmarPedidoListo();
          setTimeout(() => {
              confirmarPedidoEntregado(pedido.name);
          }, 3000);
      }, 3000);
  }, 2000);
};

crearPedido(
  {
      id: '1',
      name: 'Andres',
      item: ['8oz steak', 'Lemonade', 'Cheescake'],
      createdDate: new Date(),
      note: 'I am hungry'
  }, 
  confirmarPedido, 
  confirmarPedidoListo, 
confirmarPedidoEntregado
);
