//EJERCICIO
/*
CUANDO NO SE SIGUE EL PRINCIPIO DE RESPONSABILIDAD ÚNICA:

- Se complica la tarea de implementar procesos en otras clases.
- De la misma manera la clase vendrá con métodos que no necesitará en todos los casos que será implementada.
- Complica el mantenimiento, al juntar demasiados procesos.
- Hace más difícil definir los test unitarios.
- El código es algo más ilegible, pues no queda claro para qué es la clase.

En general, este principio busca simplificar y facilitar el desarrollo, sobre todo si se trabaja con código que luego será leído y editado por otras personas.
*/

class UsersNoSRP {
	constructor(username, password, email, userID) {
		this.username = username;
		this.password = password;
		this.email = email;
		this.userID = userID;
	}

	registerUser() {
		//Registrar el usuario
	}

	validateUser() {
		//Validar la contraseña del usuario
	}

	sendEmail() {
		//Enviar un email al ususario
	}
}

/*
PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP):

"Una clase debe hacer una cosa y, por lo tanto, debe tener una sola razón para cambiar"

Esto quiere decir que cada clase tiene un objetivo y una sola razón de ser. El único motivo por el que se debería modificar una clase es que este objetivo o la manera en que debe cumplirse sean modificados también.
*/

class User {
	constructor(username, password, email, userID) {
		this.username = username;
		this.password = password;
		this.email = email;
		this.userID = userID;
	}

	//Lógica que necesite la creación de un usuario
}

class UserRegister {
	constructor(user) {
		this.user = user;
	}

	//Registrar al usuario
}

class UserValidation {
	constructor(user) {
		this.user = user;
	}

	//Validar contraseñas o permisos del usuario
}

class EmailSender {
	constructor(emailAddress, emailObject, emailContent) {
		this.emailAddress = emailAddress;
		this.emailObject = emailObject;
		this.emailContent = emailContent;
	}

	//Lógica para crear y enviar un correo
}

/*
* DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestión de Users
 * y el procesamiento de préstamos de libros.

 * Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
 * información básica como título, autor y número de copias disponibles.
 * 2. Registrar Users: El sistema debe permitir agregar nuevos Users con
 * información básica como name, número de identificación y correo electrónico.
 * 3. Procesar préstamos de libros: El sistema debe permitir a los Users
 * tomar prestados y devolver libros.

 * Instrucciones:
 * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * Users y procesamiento de préstamos).
 * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Única.
 */

class Library {
	userDataBase = [];
	bookDataBase = [];

	registerNewBook(bookID, title, author, avalaibleCopies) {
		let newBook = {
			bookID: bookID,
			title: title,
			author: author,
			avalaibleCopies: avalaibleCopies,
		};

		this.bookDataBase.push(newBook);
	}

	registerNewUser(name, userID, emailAddress) {
		let newUser = {
			name: name,
			userID: userID,
			emailAddress: emailAddress,
		};

		this.userDataBase.push(newUser);
	}

	search(elementID, searchType) {
		let result;

		if (searchType === 'book') {
			this.bookDataBase.forEach((element) => {
				if (element.bookID === elementID) {
					result = element;
				}
			});
		} else if (searchType === 'user') {
			this.userDataBase.forEach((element) => {
				if (element.userID === elementID) {
					result = element;
				}
			});
		}

		return result;
	}

	lendBook(userID, bookID) {
		let bookToLend = this.search(bookID, 'book');
		let userLender = this.search(userID, 'user');

		if (bookToLend.avalaibleCopies > 0) {
			console.log(
				`Se le ha prestado el libro \"${bookToLend.title}\" de ${bookToLend.author} a ${userLender.name}`
			);
			bookToLend.avalaibleCopies--;
		} else {
			console.log('No hay copias disponibles');
		}
	}
}

let myLibrary = new Library();

myLibrary.registerNewBook(1, 'Dracula', 'Bram Stoker', 3);
myLibrary.registerNewUser('Juan', 1, 'juanloquillo16@gmail.com');
myLibrary.lendBook(1, 1);
