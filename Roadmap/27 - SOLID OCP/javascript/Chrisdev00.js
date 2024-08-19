/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
 */

// Forma Incorrecta de aplicar el principio OCP

class Order {
    constructor() {
        this.items = [];
        this.quantities = [];
        this.prices = [];
        this.status = "open";
    }

    addItem(name, quantity, price) {
        this.items.push(name);
        this.quantities.push(quantity);
        this.prices.push(price);
    }

    totalPrice() {
        let total = 0;
        for (let i = 0; i < this.prices.length; i++) {
            total += this.quantities[i] * this.prices[i];
        }
        return total;
    }
}

class PaymentProcessor {
    payDebit(order, securityCode) {
        console.log("Procesando el tipo de pago 'débito'");
        console.log(`Verificando código de seguridad: ${securityCode}`);
        order.status = "paid";
    }

    payCredit(order, securityCode) {
        console.log("Procesando el tipo de pago 'crédito'");
        console.log(`Verificando código de seguridad: ${securityCode}`);
        order.status = "paid";
    }

    payPaypal(order, securityCode) {
        console.log("Procesando el tipo de pago 'Paypal'");
        console.log(`Verificando código de seguridad: ${securityCode}`);
        order.status = "paid";
    }
}

const order1 = new Order();
order1.addItem("Keyboard", 1, 50);
order1.addItem("SSD", 1, 150);
order1.addItem("USB Cable", 2, 5);

console.log(`El precio total es: ${order1.totalPrice()}`);
const processor = new PaymentProcessor();
processor.payDebit(order1, "0372846");
console.log(`Estatus: ${order1.status}`);

// Forma Correcta de aplicar el principio OCP

class Order {
    constructor() {
        this.items = [];
        this.quantities = [];
        this.prices = [];
        this.status = "open";
    }

    addItem(name, quantity, price) {
        this.items.push(name);
        this.quantities.push(quantity);
        this.prices.push(price);
    }

    totalPrice() {
        let total = 0;
        for (let i = 0; i < this.prices.length; i++) {
            total += this.quantities[i] * this.prices[i];
        }
        return total;
    }
}

class PaymentProcessor {
    pay(order, securityCode) {
        throw new Error("This method should be overridden");
    }
}

class DebitPaymentProcessor extends PaymentProcessor {
    pay(order, securityCode) {
        console.log("Procesando el tipo de pago 'débito'");
        console.log(`Verificando código de seguridad: ${securityCode}`);
        order.status = "paid";
    }
}

class CreditPaymentProcessor extends PaymentProcessor {
    pay(order, securityCode) {
        console.log("Procesando el tipo de pago 'crédito'");
        console.log(`Verificando código de seguridad: ${securityCode}`);
        order.status = "paid";
    }
}

class PaypalPaymentProcessor extends PaymentProcessor {
    pay(order, securityCode) {
        console.log("Procesando el tipo de pago 'Paypal'");
        console.log(`Verificando código de seguridad: ${securityCode}`);
        order.status = "paid";
    }
}

const order = new Order();
order.addItem("Keyboard", 1, 50);
order.addItem("SSD", 1, 150);
order.addItem("USB Cable", 2, 5);

console.log(`El precio total es: ${order.totalPrice()}`);

const debitProcessor = new DebitPaymentProcessor();
debitProcessor.pay(order, "0372846");
console.log(`Estatus: ${order.status}`);

const creditProcessor = new CreditPaymentProcessor();
creditProcessor.pay(order, "1234567");
console.log(`Estatus: ${order.status}`);

const paypalProcessor = new PaypalPaymentProcessor();
paypalProcessor.pay(order, "7654321");
console.log(`Estatus: ${order.status}`);


//////////// ------------------------------ EXTRA ------------------------------------------- //////////////////////


class Calculator{
    constructor(){
        this.operations = {
            "suma": new SumaOperation(),
            "resta": new RestaOperation(),
            "multiplicacion": new MultiOperation(),
            "division": new DivisionOperation()
        };
    }

    addOperation(name,operation){
        this.operations[name] = operation;
    }

    getOperation(name){
        return this.operations[name];
    }

    execute(name,num1,num2){
        const operation = this.getOperation(name);
        if(operation){
            return operation.calculate(num1,num2);
        }else{
            throw new error(`Operacion '${name}' no soportada.`);
        }
    }
}

class Operation {
    calculate(num1, num2){
        throw new Error("This method should be overridden");
    }
}

class SumaOperation extends Operation{
    calculate(num1,num2){
        return num1 + num2;
    }
}

class RestaOperation extends Operation{
    calculate(num1, num2){
        return num1 - num2;
    }
}

class MultiOperation extends Operation{
    calculate(num1, num2){
        return num1 * num2;
    }
}

class DivisionOperation extends Operation{
    calculate(num1,num2){
        if(num2===0){
            throw new Error("Cannot divide by zero");
        }
        return num1 / num2;
    }
}

class PotenciaOperation extends Operation{
    calculate(num1,num2){
        return num1 ** num2;
    }
}

const calculadora = new Calculator();
calculadora.addOperation("potencia", new PotenciaOperation());

console.log(`Suma: ${calculadora.execute('suma', 4,3)}`)
console.log(`Resta: ${calculadora.execute('resta', 10,5)}`)
console.log(`Multiplicacion: ${calculadora.execute('multiplicacion', 7,6)}`)
console.log(`Division: ${calculadora.execute('division', 8,2)}`)
console.log(`Potencia: ${calculadora.execute('potencia', 2,3)}`)

try {
    console.log(`Mod: ${calculadora.execute('mod', 10, 3)}`);
} catch (e) {
    console.error(e.message);
}