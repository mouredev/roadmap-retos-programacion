// * EdiedRamos

// * Exercise

class Car {
  constructor(
    private brand: string,
    private doors: number,
    private color: string
  ) {}

  set setBrand(brand: string) {
    this.brand = brand;
  }

  set setDoors(doors: number) {
    this.doors = doors;
  }

  set setColor(color: string) {
    this.color = color;
  }

  get toString(): string {
    return `Marca: ${this.brand}\nPuertas: ${this.doors}\nColor: ${this.color}`;
  }
}

// * Extra exercise

class Stack<T> {
  constructor(private data: T[]) {}

  push(item: T) {
    this.data.unshift(item);
  }

  pop() {
    if (!this.data.length) throw new Error("La pila está vacía");
    this.data.shift();
  }

  size() {
    return this.data.length;
  }

  show() {
    if (!this.data.length) throw new Error("La pila está vacía");
    console.log(`[${this.data.join(",")}]`);
  }
}

class Queue<T> {
  constructor(private data: T[]) {}

  push(item: T) {
    this.data.push(item);
  }

  pop() {
    if (!this.data.length) throw new Error("La cola está vacía");
    this.data.pop();
  }

  size() {
    return this.data.length;
  }

  show() {
    if (!this.data.length) throw new Error("La cola está vacía");
    console.log(`[${this.data.join(",")}]`);
  }
}

// * Main
(() => {
  // * First exercise
  const car = new Car("Porshe", 2, "black");
  console.log(car.toString);
  car.setBrand = "Mazda";
  car.setDoors = 4;
  car.setColor = "red";
  console.log(car.toString);

  // * Second exercise
  console.log("== PILA ==");
  const stack = new Stack<number>([1]);
  stack.push(33);
  stack.push(12);
  stack.show();
  stack.pop();
  stack.show();

  console.log("== COLA ==");
  const queue = new Queue<number>([1]);
  queue.push(33);
  queue.push(12);
  queue.show();
  queue.pop();
  queue.show();
})();
