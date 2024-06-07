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

	user = {
		instances: 0,
	};

	constructor() {
		if (typeof UserSession.instance === 'object') {
			return UserSession.instance;
		}

		UserSession.instance = this;
		return this;
	}

	init(name, username, userID, email) {
		if (this.user.instances === 0) {
			this.user.name = name;
			this.user.username = username;
			this.user.userID = userID;
			this.user.email = email;
			this.user.instances++;
			return this.user;
		}
	}

	getData() {
		console.table(this.user);
	}

	close() {
		return (this.user = {
			instances: 0,
		});
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
	'\nIngresamos al usuario. Cuando ya existe un instancia de este no es posible ingresar otro usuario a menos que se cierre la instancia'
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
