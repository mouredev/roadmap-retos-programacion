// Ejecicio

class Burger {
  constructor() {
    this._description = undefined;
    this._price = undefined;
  }
  /**
   * @param {number} price
   */
  set price(price) {
    this._price = price;
  }

  get price() {
    return this._price;
  }

  set description(burger) {
    this._description = burger;
  }

  get description() {
    return this._description;
  }

  getBurger() {
    return `Tu orden es: ${this.description} precio a pagar ${this.price}`;
  }
}

// Subclase
/* Se pueden tener tantas subclases como tipos de burgers tenga el menu */

class CheeseBurger extends Burger {
  constructor() {
    super();
    this.description = 'Cheeseburger';
    this.price = 100;
  }
}

/* Decorador */

class BurgerDecorator extends Burger {
  constructor(burger) {
    super();
    this.burger = burger;
  }
}

// Decoradores
/* Podemos tener tantos decoradores como extras se quieran agregar en el menu */

class ExtraMeatDecorator extends BurgerDecorator {
  constructor(burger) {
    super(burger);
  }

  get description() {
    return `${this.burger.description} con extra carne`;
  }

  get price() {
    return this.burger.price + 20;
  }
}

const cheeseBurger = new CheeseBurger();
const cheeseBurgerWithExtraMeat = new ExtraMeatDecorator(cheeseBurger);
console.log(cheeseBurger.getBurger());
console.log(cheeseBurgerWithExtraMeat.getBurger());

// Extra
/* Falta pulir */
class Person {
  static count = 0; // Creando un contador para que el decorador muestre
  constructor(name, age) {
    this.name = name;
    this.age = age;
    this.instance = Person.count++;
  }
}

class CountDecorator extends Person {
  constructor() {
    super();
  }
  get instance() {
    return Person.count;
  }
}
