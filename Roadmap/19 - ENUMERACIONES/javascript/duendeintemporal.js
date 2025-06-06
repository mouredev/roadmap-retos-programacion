//#19 ENUMERACIONES
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

What are Enums?
Enums are a way to define a set of named constants. They are used to represent a group of related values, making the code more readable and easier to maintain. For example, you might have an enum for the days of the week, the statuses of an order, or colors. */

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #19.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #19. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #19'); 
});

let log = console.log;

const DaysOfWeek = {
    MONDAY: 'Monday',
    TUESDAY: 'Tuesday',
    WEDNESDAY: 'Wednesday',
    THURSDAY: 'Thursday',
    FRIDAY: 'Friday',
    SATURDAY: 'Saturday',
    SUNDAY: 'Sunday'
};

Object.freeze(DaysOfWeek);

const showDay = (day)=>{    
    const w_days = Object.keys(DaysOfWeek);
    return (w_days[day - 1])? DaysOfWeek[w_days[day - 1]] : 'You enter a invalid day, try between 1 and 7'; 
} 

log(DaysOfWeek.MONDAY); // Monday
log(showDay(3)) // Wednesday
//Extra Dificulty Exercise

//Enum simulation
const OrderStatus = {
    PENDING: 'Pending',
    SHIPPED: 'Shipped',
    DELIVERED: 'Delivered',
    CANCELED: 'Canceled'
};

Object.freeze(OrderStatus);

class Order{
    constructor(id){
        this.id = id;
        this.state = OrderStatus.PENDING;
    }

    setState(state){
        this.state = OrderStatus[state];
    }

    getState(){
        return this.state;
    }

    shipOrder(){
        if(this.state.toLowerCase() == OrderStatus.PENDING.toLowerCase()){
            log('The order is Shipped');
            this.setState('SHIPPED');
        }else {
            log(`Cannot ship. Current state: ${this.state}`);
        }
    }

    deliverOrder(){
        if(this.state.toLowerCase() == OrderStatus.SHIPPED.toLowerCase()){
            log('The order is Delivered');
            this.setState('DELIVERED');
        }else{
            log(`Cannot deliver. The order state is: ${this.state}`);
        }
    }

    cancelOrder(){
        if(this.state.toLowerCase() == OrderStatus.DELIVERED.toLowerCase()){
            log('Cannot cancel. The order has already been delivered.')
        }
            log('The order is Canceled');
            this.setState('CANCELED');
        }

        describeOrder() {
            log(`Order ID: ${this.id}, Current State: ${this.state}`);
        }
    }

let order15 = new Order('001');
let order16 = new Order('002');
let order17 = new Order('003');

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

