class Hamburger {
	basicIngredients = ['bread roll', 'beef', 'tomato', 'lettuce', 'cheese', 'onion'];
}

class Cheeseburger extends Hamburger {
	constructor() {
		super();
		this.basicIngredients.push('more cheese');
	}
}

let burger1 = new Hamburger();
console.log(burger1);

let burger2 = new Cheeseburger();
console.log(burger2);
