class Human {
  constructor(name,username,age){
    this.name = name;
    this.username = username;
    this.age = age;
    this.nickName = "No tengo apodo"; // Está propiedad no es necesario introducirla en el momento de crear la instancia
  }

  // Métodos GET y SET para el atributo "privado" nickName
  get getNickname(){
    return this.nickName
  }

  set setNickName(value){
    this.nickName = value;
  }
}

//CASO DE USO
let humano1 = new Human("Mimi","Bébe",26);
humano1.getNickname;
humano1.setNickName = "Tio Billete";
humano1.getNickname;

/* DIFICULTAD EXTRA */

class Stack {
  constructor(){
    this.nameStack = null;
    this.stateStack = [];
  }
  // ADD or Push
  add(num) {
    this.stateStack.push(num)
  }

  // REMOVE o Pop
  pop(){
    this.stateStack.pop();
  }

  get getState(){
    return this.stateStack;
  }

  get getName(){
    return this.nameStack;
  }

  set setName(value){
      this.nameStack = value;
    }

}


// CASO DE USO
let stack1 = new Stack();

stack1.add(1);
stack1.add(2);
stack1.add(3);

stack1.getState;

stack1.pop();

stack1.getState;

stack1.getName;
stack1.setName = "pila1";
stack1.getName;


class Queue{
  constructor(){
    this.stateQueue = [];
  }

  add(num){
    this.stateQueue.push(num);
  }

  pop(){
    this.stateQueue.shift();
  }

  get getState() {
    return this.stateQueue;
  }
}

let cola = new Queue();
cola.add(1);
cola.add(2);
cola.add(3);

cola.getState;

cola.pop();

cola.getState;

