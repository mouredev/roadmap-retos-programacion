//Utiliza operaciones de inserción, borrado, actualización y ordenación
//stack | Pilas

class Stack {
  items: Array<number>;

  constructor() {
    this.items = [];
  }

  insert(numberInserted: number) {
    this.items.push(numberInserted);
  }

  remove() {
    this.items.pop();
  }

  update(numberUpdated: number) {
    if (this.items.length > 0) {
      this.items[this.items.length - 1] = numberUpdated;
    } else {
      console.log('La lista está vacía');
    }
  }

  ordination() {
    this.items.sort((a, b) => a - b);
  }
}

const stack: Stack = new Stack();
stack.insert(1);
stack.insert(2);
stack.insert(3);
stack.insert(4);
stack.insert(5);
console.log(`insert: ${stack.items}`);
stack.remove();
console.log(`Remove: ${stack.items}`);
stack.update(6);
console.log(`Update: ${stack.items}`);
stack.ordination();
console.log(`Ordination: ${stack.items}`);

//Queue | Colas

class Queue {
  items: Array<number> = [];
  constructor() {
    this.items = [];
  }

  insert(item: number) {
    this.items.push(item);
  }

  remove() {
    this.items.shift();
  }

  update(item: number) {
    this.items[0] = item;
  }

  ordenation() {
    this.items.sort((a, b) => a - b);
  }
}

const queue = new Queue();
queue.insert(1);
queue.insert(2);
queue.insert(3);
queue.insert(4);
console.log(`Inserted: ${queue.items}`);
queue.remove();
console.log(`Removed: ${queue.items}`);
queue.update(5);
console.log(`Updated: ${queue.items}`);
queue.ordenation();
console.log(`Ordered: ${queue.items}`);

//Linked list | Listas linkeadas
class PrincipalNode {
  data: number;
  next: PrincipalNode | null;
  constructor(value: number) {
    this.data = value;
    this.next = null;
  }
}

class LinkedList {
  head: PrincipalNode | null;

  constructor() {
    this.head = null;
  }

  insertAtEnd(value: number) {
    const newNode = new PrincipalNode(value);

    if (!this.head) {
      this.head = newNode;
      return;
    }

    let current = this.head;
    while (current.next !== null) {
      current = current.next;
    }

    current.next = newNode;
  }

  deleteNode(value: number) {
    if (!this.head) {
      return;
    }

    if (this.head.data === value) {
      this.head = this.head.next;
      return;
    }

    let current = this.head;
    while (current.next !== null) {
      if (current.next.data === value) {
        current.next = current.next.next;
        return;
      }
      current = current.next;
    }
  }

  updateNode(oldValue: number, newValue: number) {
    let current = this.head;
    while (current !== null) {
      if (current.data === oldValue) {
        current.data = newValue;
        return;
      }
      current = current.next;
    }
  }

  sortList() {
    if (!this.head || !this.head.next) {
      return;
    }

    let current: PrincipalNode | null = this.head;
    let index: PrincipalNode | null;
    let temp: number;

    while (current !== null) {
      index = current.next;
      while (index !== null) {
        if (current.data > index.data) {
          temp = current.data;
          current.data = index.data;
          index.data = temp;
        }
        index = index.next;
      }
      current = current.next;
    }
  }
}

const myList = new LinkedList();
myList.insertAtEnd(3);
myList.insertAtEnd(1);
myList.insertAtEnd(2);
myList.insertAtEnd(5);

console.log("Lista original:");
let current = myList.head;
while (current !== null) {
  console.log(`Node: ${current.data}`);
  current = current.next;
}

myList.deleteNode(2);
console.log("Lista después de eliminar el nodo con valor 2:");
current = myList.head;
while (current !== null) {
  console.log(`Node: ${current.data}`);
  current = current.next;
}

myList.updateNode(1, 4);
console.log("Lista después de actualizar el nodo con valor 1 a 4:");
current = myList.head;
while (current !== null) {
  console.log(`Node: ${current.data}`);
  current = current.next;
}

myList.sortList();
console.log("Lista ordenada:");
current = myList.head;
while (current !== null) {
  console.log(`Node: ${current.data}`);
  current = current.next;
}


//tablas de hash
class HashTable {
  private table: Array<Array<[string, any]>>;
  private size: number;

  constructor(size: number) {
      this.table = new Array(size);
      this.size = size;
  }

  private hash(key: string): number {
      let hash = 0;
      for (let i = 0; i < key.length; i++) {
          hash += key.charCodeAt(i);
      }
      return hash % this.size;
  }

  set(key: string, value: any): void {
      const index = this.hash(key);
      if (!this.table[index]) {
          this.table[index] = [];
      }
      this.table[index].push([key, value]);
  }

  get(key: string): any {
      const index = this.hash(key);
      const bucket = this.table[index];
      if (bucket) {
          for (const pair of bucket) {
              if (pair[0] === key) {
                  return pair[1];
              }
          }
      }
      return undefined;
  }

  remove(key: string): void {
      const index = this.hash(key);
      const bucket = this.table[index];
      if (bucket) {
          this.table[index] = bucket.filter((pair) => pair[0] !== key);
      }
  }
}

// Uso de la tabla hash
const myHashTable = new HashTable(10);
myHashTable.set("apple", 5);
myHashTable.set("banana", 10);
myHashTable.set("orange", 15);

console.log(myHashTable.get("apple"));  // Output: 5
console.log(myHashTable.get("banana")); // Output: 10
console.log(myHashTable.get("orange")); // Output: 15

myHashTable.remove("banana");
console.log(myHashTable.get("banana")); // Output: undefined