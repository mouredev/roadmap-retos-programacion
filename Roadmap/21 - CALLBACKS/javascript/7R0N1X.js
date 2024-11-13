const procesarNombres = (nombres, callback) => {
  nombres.forEach(nombre => {
    console.log(nombre.toUpperCase())
  });
  callback()
}

const mostrarMensajeFinal = () => {
  console.log('Procesamiento terminado.')
}

const nombres = ['7r0n1x', 'eduardo', 'ana', 'pedro']
procesarNombres(nombres, mostrarMensajeFinal)

// DIFICULTAD EXTRA

const procesarPedidos = (nombreDelPlato, cbConfirmacion, cbListo, cbEntrega) => {
  setTimeout(() => {
    cbConfirmacion(nombreDelPlato)
    setTimeout(() => {
      cbListo(nombreDelPlato)
      setTimeout(() => {
        cbEntrega(nombreDelPlato)
      }, Math.floor((Math.random() * (10 - 1 + 1)) + 1) * 1000)
    }, Math.floor((Math.random() * (10 - 1 + 1)) + 1) * 1000)
  }, Math.floor((Math.random() * (10 - 1 + 1)) + 1) * 1000)
}

const confirmacion = (nombreDelPlato) => {
  console.log(`El pedido de ${nombreDelPlato} a sido confirmado.`)
}

const listo = (nombreDelPlato) => {
  console.log(`El pedido de ${nombreDelPlato} está listo.`)
}

const entraga = (nombreDelPlato) => {
  console.log(`El pedido de ${nombreDelPlato} a sido entregado.`)
}

procesarPedidos('Ceviche', confirmacion, listo, entraga)