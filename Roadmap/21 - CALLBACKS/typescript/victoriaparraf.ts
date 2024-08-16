// Definimos un tipo de callback que toma un número y devuelve void
type Callback = (result: number) => void;

function add(a: number, b: number, callback: Callback): void {
    const result = a + b;
    callback(result);
}

// Función callback que imprime el resultado
const printResult: Callback = (result) => {
    console.log('Resultado:', result);
};

// Llamamos a la función `add` con el callback `printResult`
add(3, 4, printResult); // Resultado: 7


/******************************************************************* */

type ConfirmationCallback = (dishName: string) => void;
type ReadyCallback = (dishName: string) => void;
type DeliveryCallback = (dishName: string) => void;

function processOrder(
    dishName: string,
    confirmation: ConfirmationCallback,
    ready: ReadyCallback,
    delivery: DeliveryCallback
): void {
    // Confirmar el pedido
    confirmation(dishName);

    // Simular el tiempo de preparación del plato
    setTimeout(() => {
        // El plato está listo
        ready(dishName);

        // Simular el tiempo de entrega del plato
        setTimeout(() => {
            // El plato ha sido entregado
            delivery(dishName);
        }, getRandomTime());
    }, getRandomTime());
}

function getRandomTime(): number {
    return Math.floor(Math.random() * 10000) + 1000; // Tiempo aleatorio entre 1 y 10 segundos
}

const confirmOrder: ConfirmationCallback = (dishName) => {
    console.log(`Pedido confirmado: ${dishName}`);
};

const dishReady: ReadyCallback = (dishName) => {
    console.log(`El plato está listo: ${dishName}`);
};

const deliverDish: DeliveryCallback = (dishName) => {
    console.log(`El plato ha sido entregado: ${dishName}`);
};

// Simulación de un pedido
processOrder("Pizza Margherita", confirmOrder, dishReady, deliverDish);
