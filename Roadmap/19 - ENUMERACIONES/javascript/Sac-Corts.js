const DaysOfWeek = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday" 
};

function getDayName(dayNumber) {
    return DaysOfWeek[dayNumber] || "Invalid day number";
}

console.log(getDayName(1));
console.log(getDayName(7));
console.log(getDayName(8));

// Extra Exercise //
const OrderStatus = {
    PENDING: "pending",
    SENT: "sent",
    DELIVERED: "delivered", 
    CANCELED: "canceled"
}

class Order {
    constructor(id) {
        this.id = id;
        this.status = OrderStatus.PENDING;
    }

    sendOrder() {
        if (this.status === OrderStatus.PENDING) {
            this.status = OrderStatus.SENT;
            console.log(`Order ${this.id} has been sent.`);
        } else {
            console.log(`Order ${this.id} cannot be sent in status ${this.status}.`);
        }
    }

    cancelOrder() {
        if (this.status === OrderStatus.DELIVERED) {
            console.log(`Order ${this.id} cannot be canceled, because it has already been delivered.`);
        } else {
            this.status = OrderStatus.CANCELED;
            console.log(`Order ${this.id} has been canceled.`);
        }
    }

    deliverOrder() {
        if (this.status === OrderStatus.SENT) {
            this.status = OrderStatus.DELIVERED;
            console.log(`Order ${this.id} has been delivered`);
        } else {
            console.log(`Order ${this.id} cannot be delivered in status ${this.status}`);
        }
    }

    showStatus() {
        console.log(`Order ${this.id} status is ${this.status}`);
    }
}

const order1 = new Order(1);
order1.showStatus();
order1.sendOrder();
order1.deliverOrder();
order1.cancelOrder();

const order2 = new Order(2);
order2.sendOrder();
order2.cancelOrder();
order2.showStatus();