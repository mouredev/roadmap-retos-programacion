/*
Ejercicio
*/

class Programmer{

    surname = null;

    constructor ( name, age, languages){
        this.name = name;
        this.age = age;
        this.languages = languages;
    };

    imprimir(){
        console.log(`Nombre: ${this.name} Apellido: ${this.surname} Edad: ${this.age}; Lenguajes: ${this.languages}`);
    };
};

let myProgrammer = new Programmer("Emanuel", 18, ["Javascript", "Html", "CSS"]);
myProgrammer.imprimir();
myProgrammer.surname = "Aristizabal";
myProgrammer.age = 37;
myProgrammer.imprimir();


/*
Extra
*/ 


//LIFO

class Stack {

    constructor(){
        this.stack = [];
    };

    push(item){
        this.stack.push(item);
    };

    pop(){
        if(this.stack.length > 0){
            return this.stack.pop();
        };
        return null;
    };

    count(){
        return this.stack.length;
    };

    print(){
        for(let i = this.stack.length - 1; i >= 0; i--){
            console.log(this.stack[i]);
        };
    };
};

let myStack =  new Stack();
myStack.push("A");
myStack.push("B");
myStack.push("C");
console.log(myStack.count());
myStack.print();
myStack.pop();
console.log(myStack.count());
myStack.print();
myStack.pop();
console.log(myStack.count());
myStack.print();
myStack.pop();
console.log(myStack.count());
myStack.print();



//FIFO

class Queue{

    constructor(){
        this.queue = [];
    };

    enqueue(item){
        this.queue.push(item);
    };

    dequeue(){
        if(this.queue.length > 0){
            return this.queue.shift();
        };
        return null;
    };

    count(){
        return this.queue.length;
    };

    print(){
        for(let item of this.queue){
            console.log(item);
        };
    };
};

let myQueue = new Queue();
myQueue.enqueue("A");
myQueue.enqueue("B");
myQueue.enqueue("C");
console.log(myQueue.count());
myQueue.print();
myQueue.dequeue();
console.log(myQueue.count());
myQueue.print();
myQueue.dequeue();
console.log(myQueue.count());
myQueue.print();
myQueue.dequeue();
console.log(myQueue.count());
myQueue.print();
myQueue.dequeue();
console.log(myQueue.count());
myQueue.print();