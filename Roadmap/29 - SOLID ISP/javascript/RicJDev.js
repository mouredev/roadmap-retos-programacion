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
//Interfaces
class PrinterInterface {
	print(document) {
		console.log(`Imprimiendo ${document} en blanco y negro`)
	}
}

class ColorPrinterInterface {
	print(document) {
		console.log(`Imprimiendo ${document} a color`)
	}
}

class ScanInterface {
	scan(document) {
		console.log(`Se ha escaneado el documento ${document}`)
	}
}
class FaxInterface {
	send(document) {
		console.log(`Se ha enviado el documento ${document} via fax`)
	}
}

//Implementacion
class Printer extends PrinterInterface {}

class ColorPrinter extends ColorPrinterInterface {}

class MultiFunction {
	constructor() {
		this.blackAndWhite = new Printer()
		this.color = new ColorPrinter()
		this.scanner = new ScanInterface()
		this.fax = new FaxInterface()
	}

	print(document) {
		this.blackAndWhite.print(document)
	}

	printColor(document) {
		this.color.print(document)
	}

	scan(document) {
		this.scanner.scan(document)
	}

	sendFax(document) {
		this.fax.send(document)
	}
}

//Probando ISP
let doc = 'miDocumento.docx'

const printer = new Printer()
const colorPrinter = new ColorPrinter()
const multiFunction = new MultiFunction()

printer.print(doc)
colorPrinter.print(doc)

multiFunction.print(doc)
multiFunction.printColor(doc)
multiFunction.scan(doc)
multiFunction.sendFax(doc)
