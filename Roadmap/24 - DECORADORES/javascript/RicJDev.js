//EJERCICIO
class BasicPizza {
	constructor(size) {
		this.price = this.pricesList[size];
	}

	toppings = ['salsa', 'mozzarella', 'pepperoni'];

	//Precios en dólares, jajs
	pricesList = {
		small: '$5.00',
		medium: '$9.00',
		large: '$12.00',
		extralarge: '$16.00',
	};

	getPrice() {
		console.log(this.price);
	}
}

class HawaianPizza extends BasicPizza {
	constructor(size) {
		super(size);
		this.toppings.push('jamón', 'piña');
		this.price = this.pricesList[size];
	}

	pricesList = {
		small: '$6.70',
		medium: '$10.50',
		large: '$13.50',
		extralarge: '$16.30',
	};
}

class PizzaDecorator extends BasicPizza {
	constructor(pizza) {
		super(pizza.size, pizza.toppings);
		this.pizza = pizza;
	}

	getPrice() {
		this.pizza.getPrice();
	}
}

let pizza1 = new HawaianPizza('small');

pizza1.getPrice();
