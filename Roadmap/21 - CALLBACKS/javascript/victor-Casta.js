/*
  * EJERCICIO:
  * Explora el concepto de callback en tu lenguaje creando un ejemplo
  * simple (a tu elección) que muestre su funcionamiento.
*/

//Ejemplo 1
function updatelist(list, callback) {
  list.push(7)
  callback()
}

const MyList = [1, 2, 3, 4, 5, 6]

updatelist(MyList, function () {
  console.log(MyList)
})

// Ejemplo 2
function getDataToUrl(callback) {
  fetch('https:api.escuelajs.co/api/v1/products')
    .then(response => response.json())
    .then(data => {
      let contentURL = data
      callback(contentURL)
    })
    .catch(error => console.error('Error:', error))
}

getDataToUrl((content) => {
  console.log(content)
})

//  Ejemplo 3
function multiply(a, b, callback) {
  setTimeout(() => {
    let result = a * b
    callback(result)
  }, 4000)
}

multiply(3, 4, (result) => {
  console.log(result)
})

/*
  * DIFICULTAD EXTRA (opcional):
  * Crea un simulador de pedidos de un restaurante utilizando callbacks.
  * Estará formado por una función que procesa pedidos.
  * Debe aceptar el nombre del plato, una callback de confirmación, una
  * de listo y otra de entrega.
  * - Debe imprimir un confirmación cuando empiece el procesamiento.
  * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
  *   procesos.
  * - Debe invocar a cada callback siguiendo un orden de procesado.
  * - Debe notificar que el plato está listo o ha sido entregado.
*/

function getRandomArbitrary(min, max) {
  let number = Math.random() * (max - min) + min
  return Math.round(number)
}

function orderProcess(orderName, checkCallback, readyCallback, deliveredCallback) {
  checkCallback(orderName)
  setTimeout(() => {
    readyCallback(orderName)
    setTimeout(() => {
      deliveredCallback(orderName)
    }, getRandomArbitrary(1000, 10000))
  }, getRandomArbitrary(1000, 10000))
}

function checkOrder(orderName) {
  console.log(`Su pedido ${orderName} ha sido confirmado`)
}

function readyOrder(orderName) {
  console.log(`Su pedido ${orderName} está listo`)
}

function deliveredOrder(orderName) {
  console.log(`Su pedido  ${orderName} ha sido entregado`)
}

orderProcess('Hamburguesa sencilla', checkOrder, readyOrder, deliveredOrder)

