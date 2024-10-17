/*
 * TEORÍA DE CALLBACKS EN TYPESCRIPT:
 *
 * TypeScript extiende JavaScript añadiendo tipos estáticos. Para callbacks,
 * esto significa que podemos definir claramente:
 * 1. Los tipos de los parámetros que el callback acepta
 * 2. El tipo de valor que el callback retorna
 *
 * Ventajas de usar callbacks en TypeScript:
 * 1. Mejor intellisense y autocompletado en IDEs
 * 2. Detección temprana de errores de tipo
 * 3. Documentación más clara a través de tipos
 * 4. Refactorización más segura
 */

// Definición de tipos para los callbacks
type SimpleCallback = () => void;
type MessageCallback = (message: string) => void;

// Interface para estructurar los callbacks del restaurante
interface RestaurantCallbacks {
  onConfirmation: MessageCallback;
  onReady: MessageCallback;
  onDelivery: MessageCallback;
}

// Clase para manejar pedidos del restaurante
class RestaurantOrders {
  // Método privado para generar tiempo aleatorio
  private getRandomTime(): number {
    return Math.floor(Math.random() * 10) + 1;
  }

  // Método para procesar un pedido
  public processOrder(dish: string, callbacks: RestaurantCallbacks): void {
    const { onConfirmation, onReady, onDelivery } = callbacks;

    // Confirmación inmediata
    onConfirmation(`Order confirmed: ${dish}`);

    // Simular preparación
    const prepTime = this.getRandomTime();
    console.log(`Preparing... (${prepTime} seconds)`);

    setTimeout(() => {
      // Plato listo
      onReady(`${dish} is ready!`);

      // Simular entrega
      const deliveryTime = this.getRandomTime();
      console.log(`Delivering to table... (${deliveryTime} seconds)`);

      setTimeout(() => {
        // Entrega completada
        onDelivery(`${dish} has been delivered. Enjoy your meal!`);
      }, deliveryTime * 1000);
    }, prepTime * 1000);
  }
}

// Ejemplo simple de callback
function processTask(task: string, callback: SimpleCallback): void {
  console.log(`Starting task: ${task}`);

  setTimeout(() => {
    callback();
  }, 1000);
}

// Función principal asíncrona
async function main() {
  console.log("=== Simple Callback Example ===");

  // Ejemplo simple usando Promise para manejar el callback
  await new Promise<void>((resolve) => {
    processTask("Test task", () => {
      console.log("Task completed!");
      resolve();
    });
  });

  console.log("\n=== Restaurant Simulator ===");

  const restaurant = new RestaurantOrders();

  // Creamos un Promise que se resolverá cuando se complete todo el proceso
  await new Promise<void>((resolve) => {
    restaurant.processOrder("Paella Valenciana", {
      onConfirmation: (message: string) => {
        console.log(`CONFIRMATION: ${message}`);
      },
      onReady: (message: string) => {
        console.log(`READY: ${message}`);
      },
      onDelivery: (message: string) => {
        console.log(`DELIVERY: ${message}`);
        resolve(); // Resolvemos el Promise cuando se complete la entrega
      },
    });
  });
}

// Ejecutar el programa principal
console.log("Starting the program...");
main().then(() => {
  console.log("\nProgram completed successfully!");
});
