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
		let result = [];
		Object.keys(this.user).forEach((element) => {
			result.push(this.user[element]);
		});
		return result;
	}

	close() {
		return (this.user = {
			instances: 0,
		});
	}
}

let session = new UserSession();

console.log(session);

console.log(session.getData());

session.init('Fred', 'CrazyFred4564', 7880003, 'crazyfred@gmail.com');

console.log(session);

session.close();

console.log(session.getData());

session.init('Fred', 'CrazyFred4564', 7880003, 'crazyfred@gmail.com');

console.log(session.getData());

session.init('Sarah', 'SunshineSarah2435', 6550099, 'sarahmilanesa@gmail.com');

console.log(session.getData());
