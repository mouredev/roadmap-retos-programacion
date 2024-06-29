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

//EXTRA
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
		let pendingLender = this.search(this.userDataBase, userID);
		let bookToLend = this.search(this.bookDataBase, bookID);

		if (pendingLender) {
			if (bookToLend) {
				if (bookToLend.avalaibleCopies > 0) {
					console.log(
						`Se le ha prestado el libro \"${bookToLend.title}\", de ${bookToLend.author}, a ${pendingLender.name}`
					);

					bookToLend.avalaibleCopies--;

					this.pendingLenders.push(pendingLender);
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
		let pendingLender = this.search(this.pendingLenders, userID);
		let bookReceived = this.search(this.bookDataBase, bookID);

		if (pendingLender) {
			console.log(`${pendingLender.name} ha regresado el libro \"${bookReceived.title}\"`);

			bookReceived.avalaibleCopies++;

			this.pendingLenders.splice(this.pendingLenders.indexOf(pendingLender), 1);
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
class PendingLender {
	constructor(user, bookID, dataBase = myLibraryDataBase) {
		this.userID = user.userID;
		this.name = user.name;
		this.emailAddress = user.emailAddress;
		this.bookID = bookID;
	}
}

function search(arr, item) {
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

class LibraryDataBase {
	books = [];
	users = [];
	pendingLenders = [];
}

class LendingManager {
	constructor(dataBase = myLibraryDataBase) {
		this.dataBase = dataBase;
	}

	lendBook(userID, bookID) {
		let pendingLender = search(this.dataBase.users, userID);
		let bookToLend = search(this.dataBase.books, bookID);

		if (pendingLender) {
			if (bookToLend) {
				if (bookToLend.avalaibleCopies > 0) {
					console.log(
						`Se le ha prestado el libro \"${bookToLend.title}\", de ${bookToLend.author}, a ${pendingLender.name}`
					);
					bookToLend.avalaibleCopies--;

					this.dataBase.pendingLenders.push(new PendingLender(pendingLender, bookToLend.bookID));
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
		let pendingLender = search(this.dataBase.pendingLenders, userID);
		let book = search(this.dataBase.books, bookID);

		if (pendingLender) {
			console.log(`${pendingLender.name} ha regresado el libro \"${book.title}\"`);

			book.avalaibleCopies++;
			this.dataBase.pendingLenders.splice(this.dataBase.pendingLenders.indexOf(pendingLender), 1);
		} else {
			console.log('Ese préstamo no está en el registro');
		}
	}
}

const myLibraryDataBase = new LibraryDataBase();
const myLendingManager = new LendingManager();

new Book('Christine', 'Stephen King', 5);
new Book("El Misterio de Salem's Lot", 'Stephen King', 3);
new LibraryUser('Ana', 'anitalahuerfanita2233@gmail.com');
new LibraryUser('Julia', 'soyjuliaparasiempre@gmail.com');

myLendingManager.lendBook('Ana', 1);
myLendingManager.receiveBook('Ana', 1);
myLendingManager.lendBook('Julia', 'Libro inexistente');
