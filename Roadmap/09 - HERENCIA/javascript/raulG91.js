class Animal{

    constructor(name){
        this.name = name;
    }
    sound(){
        console.log("Animal sound");
    }
    get_name(){
        return this.name
    }
}

class Dog extends Animal{

    sound(){
        console.log("Guau!");
    }
}

class Cat extends(Animal){

    sound(){
        console.log("Miau!")
    }
}

let my_dog = new Dog("Luna");
console.log("Dog name: ",my_dog.get_name());
my_dog.sound();
let my_cat = new Cat("Miso");
console.log("Cat name: ",my_cat.get_name());
my_cat.sound();