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

class UserRegister {
	constructor(username, password, email, userID) {
		this.username = username;
		this.password = password;
		this.email = email;
		this.userID = userID;
	}

	//Crear y registrar al usuario
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

	//Lógica para enviar un correo
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
	pendingLenders = [];

	//1. Registrar libros
	registerNewBook(title, author, avalaibleCopies) {
		let newBook = {
			bookID: this.bookDataBase.length + 1,
			title: title,
			author: author,
			avalaibleCopies: avalaibleCopies,
		};

		this.bookDataBase.push(newBook);
	}

	//2. Registrar users
	registerNewUser(name, emailAddress) {
		let newUser = {
			userID: this.userDataBase.length + 1,
			name: name,
			emailAddress: emailAddress,
		};

		this.userDataBase.push(newUser);
	}

	//3. Sistema de gestión de préstamos
	search(arr, item) {
		let result;

		arr.forEach((arrObject) => {
			Object.keys(arrObject).forEach((element) => {
				if (arrObject[element] === item) {
					result = arrObject;
				}
			});
		});

		return result;
	}

	lendBook(userID, bookID) {
		let userLender = this.search(this.userDataBase, userID);
		let bookToLend = this.search(this.bookDataBase, bookID);

		if (userLender) {
			if (bookToLend) {
				if (bookToLend.avalaibleCopies > 0) {
					console.log(
						`Se le ha prestado el libro \"${bookToLend.title}\" de ${bookToLend.author} a ${userLender.name}`
					);

					bookToLend.avalaibleCopies--;

					this.pendingLenders.push(userLender);
				} else {
					console.log('No hay copias disponibles');
				}
			} else {
				console.log('No existe el libro solictado');
			}
		} else {
			console.log('No existe el usuario');
		}
	}

	receiveBook(userID, bookID) {
		let userLender = this.search(this.pendingLenders, userID);
		let bookReceived = this.search(this.bookDataBase, bookID);

		if (userLender) {
			console.log(
				`${userLender.name} ha regresado el libro \"${bookReceived.title}\" de ${bookReceived.author}`
			);

			bookReceived.avalaibleCopies++;

			this.pendingLenders.splice(this.pendingLenders.indexOf(userLender), 1);
		} else {
			console.log('Ese préstamo no está en el registro');
		}
	}
}

let myLibrary = new Library();

myLibrary.registerNewBook('Dracula', 'Bram Stoker', 3);
myLibrary.lendBook(1, 1);
myLibrary.registerNewUser('Juan', 'juanloquillo16@gmail.com');
myLibrary.lendBook(1, 2);
myLibrary.lendBook(1, 1);
myLibrary.receiveBook(1, 1);
myLibrary.receiveBook(1, 1);

//REFACTORIZANDO
//1. Registrar libros
class Book {
	constructor(title, author, avalaibleCopies, dataBase = myLibraryDataBase) {
		this.bookID = dataBase.books.length + 1;
		this.title = title;
		this.author = author;
		this.avalaibleCopies = avalaibleCopies;

		dataBase.books.push(this);
	}
}

//2. Registrar users
class LibraryUser {
	constructor(name, emailAddress, dataBase = myLibraryDataBase) {
		this.userID = dataBase.users.length + 1;
		this.name = name;
		this.emailAddress = emailAddress;

		dataBase.users.push(this);
	}
}

//3. Sistema de gestión de préstamos
class LendingManager {
	constructor(dataBase = myLibraryDataBase) {
		this.dataBase = dataBase;
	}

	lendBook(bookID, userID) {
		let userLender = this.dataBase.search(this.dataBase.users, userID);
		let bookToLend = this.dataBase.search(this.dataBase.books, bookID);

		if (userLender) {
			if (bookToLend) {
				if (bookToLend.avalaibleCopies > 0) {
					console.log(
						`Se le ha prestado el libro \"${bookToLend.title}\" de ${bookToLend.author} a ${userLender.name}`
					);
					bookToLend.avalaibleCopies--;
					this.dataBase.pendingLenders.push(userLender);
				} else {
					console.log('No hay copias disponibles');
				}
			} else {
				console.log('No existe el libro solictado');
			}
		} else {
			console.log('No existe el usuario');
		}
	}

	receiveBook(bookID, userID) {
		let bookReceived = this.dataBase.search(this.dataBase.books, bookID);
		let userLender = this.dataBase.search(this.dataBase.pendingLenders, userID);

		if (userLender) {
			console.log(
				`${userLender.name} ha regresado el libro \"${bookReceived.title}\" de ${bookReceived.author}`
			);

			bookReceived.avalaibleCopies++;

			this.dataBase.pendingLenders.splice(this.dataBase.pendingLenders.indexOf(userLender), 1);
		} else {
			console.log('Ese préstamo no está en el registro');
		}
	}
}

class LibraryDataBase {
	books = [];
	users = [];
	pendingLenders = [];

	search(arr, item) {
		let result;

		arr.forEach((arrObject) => {
			Object.keys(arrObject).forEach((element) => {
				if (arrObject[element] === item) {
					result = arrObject;
				}
			});
		});

		return result;
	}
}

const myLibraryDataBase = new LibraryDataBase();

let book1 = new Book('Christine', 'Stephen King', 5);
let book2 = new Book("El Misterio de Salem's Lot", 'Stephen King', 3);
let user1 = new LibraryUser('Ana', 'anitalahuerfanita2233@gmail.com');
let user2 = new LibraryUser('Julia', 'soyjuliaparasiempre@gmail.com');

const myLendingManager = new LendingManager(myLibraryDataBase);

myLendingManager.lendBook(book1.title, user1.name);
myLendingManager.lendBook(book2.title, user1.name);
myLendingManager.receiveBook(book1.title, user1.name);
