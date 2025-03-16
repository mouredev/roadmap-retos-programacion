/*
 * TEORÍA DE CALLBACKS EN JAVASCRIPT:
 *
 * Un callback es una función que se pasa como argumento a otra función y se ejecuta
 * después de que ocurra un evento específico o se complete una tarea. En JavaScript,
 * los callbacks son muy comunes debido a su naturaleza asíncrona.
 *
 * Los callbacks son fundamentales en JavaScript para:
 * 1. Manejar operaciones asíncronas
 * 2. Event handling (manejo de eventos)
 * 3. Funciones de orden superior
 *
 * En JavaScript, los callbacks pueden ser:
 * 1. Funciones anónimas
 * 2. Funciones flecha
 * 3. Referencias a funciones nombradas
 */

// Ejemplo simple de callback
function procesarTarea(tarea, callback) {
  console.log(`Iniciando tarea: ${tarea}`);

  // Simulamos un proceso asíncrono con setTimeout
  setTimeout(() => {
    callback();
  }, 1000);
}

// Ejemplo de uso simple
console.log("=== Ejemplo Simple de Callback ===");
procesarTarea("Tarea de prueba", () => {
  console.log("¡Tarea completada!");
});

// Simulador de pedidos de restaurante
class RestaurantePedidos {
  procesarPedido(plato, onConfirmacion, onListo, onEntrega) {
    console.log("\n=== Simulador de Restaurante ===");

    // Callback de confirmación
    onConfirmacion(`Pedido confirmado: ${plato}`);

    // Simular preparación
    const tiempoPreparacion = this.#tiempoAleatorio();
    console.log(`Preparando... (${tiempoPreparacion} segundos)`);

    setTimeout(() => {
      // Callback de listo
      onListo(`¡${plato} está listo!`);

      // Simular entrega
      const tiempoEntrega = this.#tiempoAleatorio();
      console.log(`Llevando a la mesa... (${tiempoEntrega} segundos)`);

      setTimeout(() => {
        // Callback de entrega
        onEntrega(`${plato} ha sido entregado. ¡Buen provecho!`);
      }, tiempoEntrega * 1000);
    }, tiempoPreparacion * 1000);
  }

  // Método privado para generar tiempo aleatorio
  #tiempoAleatorio() {
    return Math.floor(Math.random() * 10) + 1;
  }
}

// Crear instancia del restaurante
const restaurante = new RestaurantePedidos();

// Procesar un pedido
restaurante.procesarPedido(
  "Paella Valenciana",
  (mensaje) => console.log(`CONFIRMACIÓN: ${mensaje}`),
  (mensaje) => console.log(`LISTO: ${mensaje}`),
  (mensaje) => console.log(`ENTREGA: ${mensaje}`)
);

// Para evitar que el programa termine antes de que se completen los callbacks
console.log("Esperando a que se procese el pedido...");
