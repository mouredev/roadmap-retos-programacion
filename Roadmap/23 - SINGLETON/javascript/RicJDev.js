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
	app = 'Ric-JS-Sandbox';

	user = null;

	constructor() {
		if (typeof UserSession.instance === 'object') {
			return UserSession.instance;
		}

		UserSession.instance = this;
		return this;
	}

	init(name, username, userID, email) {
		if (this.user === null) {
			this.user = {
				name: name,
				username: username,
				userID: userID,
				email: email,
			};

			return this.user;
		}
	}

	getData() {
		console.table(this.user);
	}

	close() {
		this.user = null;
	}
}

console.log('\nIniciamos la sesión, pero no se ha ingresado ningún usuario');
let session = new UserSession();
console.log(session);
session.getData();

console.log('\nIngresamos un usuario y mostramos sus datos');
session.init('Fred', 'CrazyFred4564', 7880003, 'crazyfred@gmail.com');
console.log(session);
session.getData();

console.log('\nCerramos la instancia del usuario');
session.close();
console.log(session);
session.getData();

console.log(
	'\nIngresamos a otro usuario. Como ya existe un instancia de este no es posible ingresar uno nuevo, a menos que se cierre la instancia'
);
session.init('Fred', 'CrazyFred4564', 7880003, 'crazyfred@gmail.com');
session.getData();

session.init('Sarah', 'SunshineSarah2435', 6550099, 'sarahmilanesa@gmail.com');
session.getData();

console.log('\nY eso hacemos acá');
session.close();
console.log(session);
session.getData();

session.init('Sarah', 'SunshineSarah2435', 6550099, 'sarahmilanesa@gmail.com');
session.getData();
