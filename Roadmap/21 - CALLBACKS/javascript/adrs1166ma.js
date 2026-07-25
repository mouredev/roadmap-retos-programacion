/* 🔥 EJERCICIO:
Explora el concepto de callback en tu lenguaje creando un ejemplo
simple (a tu elección) que muestre su funcionamiento.
*/

function saludar(nombre, callback) {
    console.log(`Procesando saludo para ${nombre}...`)
    setTimeout(() => {
        const mensaje = `¡Hola, ${nombre}!`
        callback(mensaje) // Invocamos el callback con el resultado
    }, 2000)
  }
  
  // Callback que maneja el resultado
  function mostrarMensaje(mensaje) {
    console.log(mensaje);
  }
  
  saludar("Anderson", mostrarMensaje);
  // Procesando saludo para Anderson...
  // ¡Hola, Anderson!
  
  
  
  /* 🔥 DIFICULTAD EXTRA (opcional): ----------------------------------------------------------------
  Crea un simulador de pedidos de un restaurante utilizando callbacks.
  Estará formado por una función que procesa pedidos.
  Debe aceptar el nombre del plato, una callback de confirmación, una
  de listo y otra de entrega.
  - Debe imprimir un confirmación cuando empiece el procesamiento.
  - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
    procesos.
  - Debe invocar a cada callback siguiendo un orden de procesado.
  - Debe notificar que el plato está listo o ha sido entregado.
   */
  
  // Principal que procesa pedidos
  function procesarPedido(plato, confirmacionCallback, listoCallback, entregaCallback) {
    console.log(`Iniciando procesamiento del pedido: ${plato}`)
  
    // Paso 1: Confirmación del pedido
    confirmacionCallback(plato)
  
    // Paso 2: Simular tiempo para preparar el plato
    const tiempoPreparacion = Math.floor(Math.random() * 10 + 1) * 1000 // Entre 1 y 10 segundos
    setTimeout(() => {
        console.log(`Plato "${plato}" está siendo preparado...`)
        listoCallback(plato) // Notificar que el plato está listo
  
        // Paso 3: Simular tiempo para entregar el plato
        const tiempoEntrega = Math.floor(Math.random() * 10 + 1) * 1000 // Entre 1 y 10 segundos
        setTimeout(() => {
            entregaCallback(plato) // Notificar que el plato ha sido entregado
        }, tiempoEntrega)
    }, tiempoPreparacion)
  }
  
  // Callbacks específicos
  function confirmarPedido(plato) {
    console.log(`[Confirmación] Pedido recibido para el plato: ${plato}`)
  }
  
  function notificarListo(plato) {
    console.log(`[Listo] El plato "${plato}" está listo para ser entregado.`)
  }
  
  function notificarEntregado(plato) {
    console.log(`[Entregado] El plato "${plato}" ha sido entregado al cliente.`)
  }
  
  procesarPedido("Pizza Margherita", confirmarPedido, notificarListo, notificarEntregado)
  // Procesando saludo para Anderson...
  // Iniciando procesamiento del pedido: Pizza Margherita
  // [Confirmación] Pedido recibido para el plato: Pizza Margherita
  // ¡Hola, Anderson!
  // Plato "Pizza Margherita" está siendo preparado...
  // [Listo] El plato "Pizza Margherita" está listo para ser entregado.
  // [Entregado] El plato "Pizza Margherita" ha sido entregado al cliente.