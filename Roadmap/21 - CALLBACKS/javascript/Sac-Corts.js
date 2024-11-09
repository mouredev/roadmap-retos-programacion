function greet(name, callback) {
    console.log('Hi' + ' ' + name);
    callback();
}

function callMe() {
    console.log('I am callback function');
}

greet('Isaac', callMe);

// Extra Exercise //
function processOrder(dish, confirmation, ready, delivery) {
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

function confirmDish(dish) {
    console.log(`Processing order: ${dish}`);
}

function readyDish(dish) {
    console.log(`Preparing the dish: ${dish}`);
}

function deliverDish(dish) {
    console.log(`Delivering the dish: ${dish}`);
}

processOrder('Pizza', confirmDish, readyDish, deliverDish);