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
console.log(anotherVillain.name);

//EXTRA
class UserSession {
	constructor() {
		if (typeof UserSession.instance === 'object') {
			return UserSession.instance;
		}

		UserSession.instance = this;
		return this;
	}
}
