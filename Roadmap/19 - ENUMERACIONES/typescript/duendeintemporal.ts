//#19  { Retos para Programadores } ENUMERACIONES
//I use GPT as a reference for concepts
/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
 */

/* In JavaScript, Enums (short for "enumerations") are not a native feature of the language like in other programming languages (for example, TypeScript, C#, Java). However, you can simulate the behavior of enums using objects.
/* 
 * In TypeScript, Enums (short for "enumerations") are a native feature of the language.
 * Enums allow you to define a set of named constants, making your code more readable and maintainable.
 * Unlike JavaScript, where you need to simulate enums using objects, TypeScript provides built-in support for enums.
 * 
 * Example:
 * enum Direction {
 *   Up = "UP",
 *   Down = "DOWN",
 *   Left = "LEFT",
 *   Right = "RIGHT"
 * }
 * 
 * This creates a type-safe way to work with a fixed set of values.
 */
// What are Enums?
// Enums are a way to define a set of named constants. They are used to represent a group of related values, making the code more readable and easier to maintain. For example, you might have an enum for the days of the week, the statuses of an order, or colors. */

let log = console.log;

// Conditional check for browser environment
if (typeof window !== 'undefined') {
    window.addEventListener('load', () => {
        const body: HTMLBodyElement | null = document.querySelector('body');
        const title = document.createElement('h1');

        body?.style.setProperty('background', '#000');
        body?.style.setProperty('text-align', 'center');

        title.textContent = 'Retosparaprogramadores #19.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '100vh');

        body?.appendChild(title);

        setTimeout(() => {
            alert('Retosparaprogramadores #19. Please open the Browser Developer Tools.');
        }, 2000);
        log('Retosparaprogramadores #19');
});
} else {
    log('This code is designed to run in a browser environment. Skipping window-related code.');
    log('Retosparaprogramadores #19');
}
for(let i = 1; i <= 10; i++){
    log(i);
} // print numbers from 1 to 10

const DaysOfWeek: { [key: string]: string } = {
    MONDAY: 'Monday',
    TUESDAY: 'Tuesday',
    WEDNESDAY: 'Wednesday',
    THURSDAY: 'Thursday',
    FRIDAY: 'Friday',
    SATURDAY: 'Saturday',
    SUNDAY: 'Sunday'
};

Object.freeze(DaysOfWeek);

const showDay = (day: number): string=>{    
    const w_days = Object.keys(DaysOfWeek);
    return (w_days[day - 1])? DaysOfWeek[w_days[day - 1]] : 'You enter a invalid day, try between 1 and 7'; 
} 

log(DaysOfWeek.MONDAY); // Monday
log(showDay(3)) // Wednesday

//Extra Dificulty Exercise

//Enum simulation
const OrderStatus: { [key: string]: string } = {
    PENDING: 'Pending',
    SHIPPED: 'Shipped',
    DELIVERED: 'Delivered',
    CANCELED: 'Canceled'
};

Object.freeze(OrderStatus);

class Order{
    id: string;
    state: string;

    constructor(id: string){
        this.id = id;
        this.state = OrderStatus.PENDING;
    }

    setState(state: string){
        this.state = OrderStatus[state];
    }

    getState(): string{
        return this.state;
    }

    shipOrder(): void{
        if(this.state.toLowerCase() == OrderStatus.PENDING.toLowerCase()){
            log('The order is Shipped');
            this.setState('SHIPPED');
        }else {
            log(`Cannot ship. Current state: ${this.state}`);
        }
    }

    deliverOrder(): void{
        if(this.state.toLowerCase() == OrderStatus.SHIPPED.toLowerCase()){
            log('The order is Delivered');
            this.setState('DELIVERED');
        }else{
            log(`Cannot deliver. The order state is: ${this.state}`);
        }
    }

    cancelOrder(): void{
        if(this.state.toLowerCase() == OrderStatus.DELIVERED.toLowerCase()){
            log('Cannot cancel. The order has already been delivered.')
        }
            log('The order is Canceled');
            this.setState('CANCELED');
        }

        describeOrder(): void {
            log(`Order ID: ${this.id}, Current State: ${this.state}`);
        }
    }

let order15: Order = new Order('001');
let order16: Order = new Order('002');
let order17: Order = new Order('003');

order16.shipOrder(); // The order is Shipped
order15.deliverOrder(); // Cannot Deliver. The order state is: Pending
order17.shipOrder(); // The order is Shipped

order16.deliverOrder(); // The order is Delivered
order15.shipOrder(); // The order is Shipped
order17.cancelOrder(); // The order is Canceled

log(order16.getState()); // Delivered
log(order15.getState()); // Shipped
log(order17.getState()); // Canceled

order16.shipOrder() // Cannot ship. Current state: Delivered

