//EJERCICIO
class OverkillerCharacter {
	constructor(name) {
		this.name = name;

		if (typeof OverkillerCharacter.instance === 'object') {
			return OverkillerCharacter.instance;
		}

		OverkillerCharacter.instance = this;
		return this;
	}
}

let villain = new OverkillerCharacter('Jeff');
console.log(villain.name);

let anotherVillain = new OverkillerCharacter('Henry');
console.log(anotherVillain.name); //Imprime Jeff, ya que esa es la única instancia que puede tener la clase OverkillerCharacter

//EXTRA
class UserSession {
	constructor() {}
}
