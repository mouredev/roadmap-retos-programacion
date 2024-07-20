//EJERCICIO
//Incorrecto ❎
class BookNoISP {
	constructor(title, author, price) {
		this.title = title
		this.author = author
		this.price = price
	}

	getPrice() {
		//Le muestra el precio del libro al cliente
	}

	getReviews() {
		//Muestra los comentarios acerca del libro
	}
}

class FreeBookNoISP extends BookNoISP {
	constructor(title, author) {
		super(title, author)
		this.price = 0
	}

	//Hereda el método para mostrar el precio, lo cual no tendría sentido para un libro gratuito
}

//Correcto ✅
class Book {
	constructor(title, author) {
		this.title = title
		this.author = author
	}

	getReviews() {
		//Muestra los comentarios acerca del libro
	}
}

class PurchasableBook extends Book {
	constructor(title, author, price) {
		super(author, title)
		this.price = price
	}

	getPrice() {
		//Le muestra el precio del libro al cliente
	}
}

class FreeBook extends Book {
	constructor(title, author) {
		super(title, author)
	}
}

//EXTRA
class Printer {
	print(document) {
		console.log(`Se ha imprimido ${document}`)
	}
}

class ColorPrinter extends Printer {
	print(document) {
		console.log(`Se ha imprimido ${document} a color`)
	}
}

class BlackAndWhitePrinter extends Printer {
	print(document) {
		console.log(`Se ha imprimido ${document} en blanco y negro`)
	}
}

class MultifuntionalPrinter extends Printer {
	print(document) {
		console.log(`Se ha imprimido ${document} en multifunción`)
	}

	scan(document) {
		console.log(`Se ha escaneado ${document}`)
	}

	sendFax(document) {
		console.log(`Se ha enviado ${document} por medio de fax`)
	}
}

const printer = new Printer()
const colorPrinter = new ColorPrinter()
const blackAndWhitePrinter = new BlackAndWhitePrinter()
const multifuntionalPrinter = new MultifuntionalPrinter()

let doc = 'document.docx'

printer.print(doc)
colorPrinter.print(doc)
blackAndWhitePrinter.print(doc)

multifuntionalPrinter.print(doc)
multifuntionalPrinter.scan(doc)
multifuntionalPrinter.sendFax(doc)

