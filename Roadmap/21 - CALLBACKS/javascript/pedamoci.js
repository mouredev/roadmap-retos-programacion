function sumar(a, b) {
  console.log( a + b)
}

function pedirNumeros(callback) {
  let a = 42
  let b = 56
  callback(a, b)
}

pedirNumeros(sumar) 

// -------------------------------------- DIFICULTAD EXTRA --------------------------------------
function confirmar(plato) {
    console.log(`Se ha confirmado el pedido de: ${plato}`)
}

function preparar(plato) {
    console.log(`Tu ${plato} ya esta listo`)
}

function entregar() {
    console.log(`Ya se ha entregado tu pedido`)
}

function seguimientoPedido(plato, comprobar, elaborar, repartir) {
  const functions = [comprobar, elaborar, repartir]
  console.log('Procesando...')
  for (let i = 0; i < functions.length; i++) {
    setTimeout(() => {
      functions[i](plato)
    }, 1000 + Math.floor(Math.random() * 10000))
  }
}

seguimientoPedido('ramen', confirmar, preparar, entregar)