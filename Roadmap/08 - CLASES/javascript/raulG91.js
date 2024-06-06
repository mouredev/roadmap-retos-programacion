class MyClass{

    constructor(value1,value2){

        this.public_attibute = value1;
        this._privateAttribute = value2;
    }
    get_private_attribute(){
        return this._privateAttribute;
    }
    set_private_attribute(value){
        this._privateAttribute = value;
    }
    get_public_attribute(){
        return this.public_attibute;
    }
    set_public_attribute(value){
        this.public_attibute = value;
    }
}

let my_object = new MyClass(2,3);
console.log("Initial value private attribute ",my_object.get_private_attribute());
console.log("Initial value public attribute ",my_object.get_public_attribute());
my_object.set_private_attribute(8);
my_object.set_public_attribute(19);
console.log("Value private attribute ",my_object.get_private_attribute())
console.log("Value public attribute ",my_object.get_public_attribute())

//Extra exercise

class Stack{

    constructor(){
        this.array = [];
    }
    push(element){
        this.array.push(element)
    }
    pop(){

        if (this.array.length > 0){
            this.array.pop();
        }
    }
    count(){
        return this.array.length;
    }
    print(){
        console.log(this.array)
    }

}

let my_stack = new Stack();
my_stack.push("hi");
my_stack.push(4);
console.log("Number of elements",my_stack.count());
my_stack.print()
my_stack.pop()
console.log("Number of elements",my_stack.count());
my_stack.print()


class myQueue{

    constructor(){
        this.array = []
    }
    push(element){

        this.array.push(element);
    }
    pop(){

        if(this.array.length > 0){
            this.array.shift();
        }
    }
    count(){
        return this.array.length;
    }
    print(){
        console.log(this.array);
    }
}

let my_queue = new myQueue();
my_queue.push("Hi!")
my_queue.push("Bye");
console.log("Number of records: ",my_queue.count());
my_queue.print()
my_queue.pop()
console.log("Number of records: ",my_queue.count());
my_queue.print()