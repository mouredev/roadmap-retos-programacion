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

class Users {
	constructor(username, password, email, id) {
		this.username = username;
		this.password = password;
		this.email = email;
		this.id = id;
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
	constructor(username, password, email, id) {
		this.username = username;
		this.password = password;
		this.email = email;
		this.id = id;
	}

	//Crear al usuario
}

class UserValidation {
	constructor(user) {
		this.user = user;
	}

	//Validar contraseñas o permisos del usuario
}

class EmailService {
	constructor(emailAddress, emailObject, emailContent) {
		this.emailAddress = emailAddress;
		this.emailObject = emailObject;
		this.emailContent = emailContent;
	}

	//Enviar un correo
}

//EXTRA
class LibraryNoSRP {
	#users = [];
	#books = [];
	#loans = [];

	registerBook(title, author, avalaibleCopies) {
		let newBook = {
			id: this.#books.length + 1,
			title: title,
			author: author,
			avalaibleCopies: avalaibleCopies,
		};

		this.#books.push(newBook);
	}

	registerUser(name, emailAddress) {
		let newUser = {
			id: this.#users.length + 1,
			name: name,
			emailAddress: emailAddress,
		};

		this.#users.push(newUser);
	}

	#searchByID(arr, item) {
		return arr.find((obj) => obj.id === item);
	}

	loanBook(userID, bookID) {
		let user = this.#searchByID(this.#users, userID);
		let book = this.#searchByID(this.#books, bookID);

		let loan = {
			id: this.#loans.length + 1,
			userID: user.id,
			bookID: book.id,
		};

		if (user && book) {
			if (book.avalaibleCopies > 0) {
				console.log(`Se ha prestado el libro \"${book.title}\" a ${user.name}`);

				book.avalaibleCopies--;

				this.#loans.push(loan);
			} else {
				console.log('No hay copias disponibles');
			}
		} else {
			console.log('No existe el usuario o el libro solicitado');
		}
	}

	returnBook(userID, bookID) {
		let loan = this.#loans.find((obj) => {
			return obj.userID === userID && obj.bookID === bookID;
		});

		if (loan) {
			let user = this.#searchByID(this.#users, loan.userID);
			let book = this.#searchByID(this.#books, loan.bookID);

			console.log(`${user.name} ha regresado el libro \"${book.title}\"`);

			book.avalaibleCopies++;

			this.#loans.splice(this.#loans.indexOf(loan), 1);
		} else {
			console.log('Ese préstamo no está en el registro');
		}
	}
}

let libraryNoSRP = new LibraryNoSRP();

libraryNoSRP.registerBook('Dracula', 'Bram Stoker', 3);
libraryNoSRP.registerUser('Juan', 'juanloquillo16@gmail.com');

libraryNoSRP.loanBook(1, 1);

libraryNoSRP.returnBook(1, 1);
libraryNoSRP.returnBook(1, 1);

//REFACTORIZANDO
class Book {
	constructor(title, author, avalaibleCopies) {
		this.title = title;
		this.author = author;
		this.avalaibleCopies = avalaibleCopies;
	}
}

class LibraryUser {
	constructor(name, emailAddress) {
		this.name = name;
		this.emailAddress = emailAddress;
	}
}

class LoansService {
	loans = [];

	loanBook(user, book) {
		let loan = {
			userID: user.id,
			bookID: book.id,
		};

		if (book.avalaibleCopies > 0) {
			loan.id = this.loans.length + 1;
			this.loans.push(loan);
			book.avalaibleCopies--;

			console.log(`Se le ha prestado el libro \"${book.title}\" a ${user.name}`);
		}
	}

	returnBook(user, book) {
		let result;

		this.loans.forEach((loan) => {
			if (loan.userID === user.id && loan.bookID === book.id) {
				result = loan;
			}
		});

		if (result) {
			this.loans.splice(this.loans.indexOf(result, 1));
			book.avalaibleCopies++;
			console.log(`${user.name} ha regresado el libro \"${book.title}\"`);
		} else {
			console.log('Préstamo no registrado');
		}
	}
}

class Library {
	#users = [];
	#books = [];
	#loans = new LoansService();

	addUser(user) {
		user.id = this.#users.length + 1;
		this.#users.push(user);
	}

	addBook(book) {
		book.id = this.#books.length + 1;
		this.#books.push(book);
	}

	#searchByID(database, itemID) {
		return database.find((obj) => obj.id === itemID);
	}

	loanBook(userID, bookID) {
		let user = this.#searchByID(this.#users, userID);
		let book = this.#searchByID(this.#books, bookID);

		if (user && book) {
			this.#loans.loanBook(user, book);
		} else {
			console.log('No existe el libro o el usuario solicitados');
		}
	}

	returnBook(userID, bookID) {
		let user = this.#searchByID(this.#users, userID);
		let book = this.#searchByID(this.#books, bookID);

		this.#loans.returnBook(user, book);
	}
}

const library = new Library();

library.addUser(new LibraryUser('Lissa', 'lissalunita2003@gmail.com'));
library.addBook(new Book('La Milla Verde', 'Stephen King', 4));

library.loanBook(1, 1);

library.returnBook(1, 1);
library.returnBook(1, 1);
