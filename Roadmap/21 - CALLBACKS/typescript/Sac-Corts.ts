function greet(name: string, callback: () => void): void {
    console.log('Hi ' + name);
    callback();
}

function callMe(): void {
    console.log('I am callback function');
}

greet('Isaac', callMe);

// ** Extra Exercise ** //
function processOrder(
    dish: string,
    confirmation: (dish: string) => void,
    ready: (dish: string) => void,
    delivery: (dish: string) => void
): void {
    setTimeout(() => {
        console.log(`Order confirmed: ${dish}`);
        confirmation(dish);
        
        setTimeout(() => {
            console.log(`The dish ${dish} is ready.`);
            ready(dish);

            setTimeout(() => {
                console.log(`The dish ${dish} has been delivered.`);
                delivery(dish);
            }, Math.random() * 9000 + 1000);
        }, Math.random() * 9000 + 1000);
    }, Math.random() * 9000 + 1000);
}

function confirmDish(dish: string): void {
    console.log(`Processing order: ${dish}`);
}

function readyDish(dish: string): void {
    console.log(`Preparing the dish: ${dish}`);
}

function deliverDish(dish: string): void {
    console.log(`Delivering the dish: ${dish}`);
}

processOrder('Pizza', confirmDish, readyDish, deliverDish);
