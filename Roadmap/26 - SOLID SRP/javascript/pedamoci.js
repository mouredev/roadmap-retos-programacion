// SRP MAL HECHO
class WrongSRP {
  sumar(num1, num2) {
    console.log(num1 + num2)
  }

  dateNow() {
    const date = new Date 
    console.log(date.toDateString())
  }
}

const wrongSRP = new WrongSRP
wrongSRP.sumar(45, 321)
wrongSRP.dateNow()

// SRP BIEN HECHO
class SumarSRP {
  sumar(num1, num2) {
    console.log(num1 + num2)
  }
}

class DateNowSRP {
  dateNow() {
    const date = new Date 
    console.log(date.toDateString())
  }
}

const sumarSRP = new SumarSRP
sumarSRP.sumar(56, 987)

const dateNowSRP = new DateNowSRP
dateNowSRP.dateNow()

// ------------------------------------------------ DIFICULTAD EXTRA ------------------------------------------------
class ManagementLibrary {
  constructor() {
    this.books = new Map()
    this.users = new Map()
    this.loans = []
  }

  addBook(title, writer, numberCopies) {
    if (this.books.has(title)) console.warn('El libro que desea agregar ya está en la biblioteca')
    else {
      this.books.set(title, {writer: writer, copies: numberCopies})
      console.log('El libro se ha agregado al catálogo de la biblioteca')
    }
  }

  addUser(idUser, name, number) {
    if (this.users.has(idUser)) console.warn('El usuario ya está registrado en la biblioteca')
    else {
      this.users.set(idUser, {name: name, number: number})
      console.log('El usuario se ha registrado correctamente en la biblioteca')
    }
  }

  loanBook(title, idUser) {
    if (!this.books.has(title)) return console.warn('El libro que desea no está en esta biblioteca')
    if (!this.users.has(idUser)) return console.warn('El usuario no esta registrado en esta biblioteca')
    const book = this.books.get(title) 
    if (book.copies > 0) {
      this.loans.push([idUser, title])
      book.copies--
      console.log('Recuerda devolver el libro cuando lo termines, gracias!')
    } else {
      console.warn('No quedan existencias del libro que desea\nPregunte nuevamente en otro momento o elija otro')
    }
  }

  returnBook(title, idUser) {
    if (this.books.has(title) && this.users.has(idUser)) {
      let booksLoanedUser = this.loans.filter((loan) => loan[0] === idUser)  // devuelde los libros retirados por el usuario
      if (booksLoanedUser.length > 0 && booksLoanedUser.map((loan) => loan[1] === title)) {  // verifica que haya libros retirado por el usuario y que coincida con el titulo ingresado
        let index = this.loans.findIndex((loan) => {return loan[0] === idUser && loan[1] === title})  // devuelve el index del array donde esta el libro retirado y el id del usuario
        this.loans.splice(index, 1)
        const book = this.books.get(title) 
        book.copies++
        console.log('Has devuelto el libro!! Gracias!!')
      } else console.warn('Id o titulo del libro incorrectos')
    }
    else {
      console.error('Datos incorrectos, vuelve a chequear que escribiste bien el nombre del libro o tu id')
    }
  }
}

const library = new ManagementLibrary()

//Creación de libros
console.log('----------------- CREACION DE LIBROS -----------------')
library.addBook('Cien años de soledad', 'Gabriel García Márquez', 5); library.addBook('1984', 'George Orwell', 7); library.addBook('Orgullo y Prejuicio', 'Jane Austen', 3); library.addBook('El Principito', 'Antoine de Saint-Exupéry', 10); library.addBook('Don Quijote de la Mancha', 'Miguel de Cervantes', 2); library.addBook('Crimen y Castigo', 'Fiódor Dostoievski', 4); library.addBook('Moby Dick', 'Herman Melville', 6); library.addBook('Ensayo sobre la ceguera', 'José Saramago', 8)

//Creación de usuarios
console.log('\n----------------- CREACION DE USUARIOS -----------------')
library.addUser(10001, 'Martina López', 987654321); library.addUser(10002, 'Javier Ríos', 912345678); library.addUser(10003, 'Sofía Giménez', 900112233); library.addUser(10004, 'Andrés Castro', 945612378); library.addUser(10005, 'Valeria Torres', 998877665); library.addUser(10006, 'Ricardo Paz', 965432101); library.addUser(10007, 'Elena Ruiz', 955544433); library.addUser(10008, 'Felipe Díaz', 933322211); library.addUser(10009, 'Carla Méndez', 977788899); library.addUser(10010, 'Pablo Núñez', 921234567); library.addUser(10011, 'Luisa Vargas', 987123456); library.addUser(10012, 'Diego Soto', 911223344); library.addUser(10013, 'Catalina Vega', 950505050); library.addUser(10014, 'Hugo Ferrer', 930303030); library.addUser(10015, 'Micaela Gil', 970707070)

// Creación de prestamos
  console.log('\n----------------- CREACION DE PRESTAMOS -----------------')
  // AGOTANDO EXISTENCIAS: 'Don Quijote de la Mancha' y 'Orgullo y Prejuicio'
  library.loanBook('Don Quijote de la Mancha', 10001); library.loanBook('Don Quijote de la Mancha', 10002)
  library.loanBook('Orgullo y Prejuicio', 10003); library.loanBook('Orgullo y Prejuicio', 10004); library.loanBook('Orgullo y Prejuicio', 10005)

  // PETICIONES EXITOSAS
  library.loanBook('1984', 10006); library.loanBook('Cien años de soledad', 10007); library.loanBook('Ensayo sobre la ceguera', 10008); library.loanBook('Moby Dick', 10009); library.loanBook('Crimen y Castigo', 10010)

  // PETICIONES FALLIDAS
    console.log('\n----------------- CREACION DE PRESTAMOS ERRONEOS -----------------')
    //Libros agotados
    library.loanBook('Don Quijote de la Mancha', 10011); library.loanBook('Orgullo y Prejuicio', 10012)
    //Libros inexistentes
    library.loanBook('El Código Da Vinci', 10013); library.loanBook('Frieren', 10014)

// Creación de devoluciones
  // Devoluciones exitosas
  console.log('\n----------------- CREACION DE DEVOLUCIONES -----------------')
  library.returnBook('Don Quijote de la Mancha', 10001); library.returnBook('Orgullo y Prejuicio', 10005); library.returnBook('1984', 10006); library.returnBook('Cien años de soledad', 10007); library.returnBook('Moby Dick', 10009)

  // Devolución con ID de usuario incorrecto (posiblemente fallida)
  console.log('\n----------------- CREACION DE DEVOLUCIONES ERRONEAS -----------------')
  library.returnBook('Crimen y Castigo', 32465)



// ---------------------------------------------------------------- REFACTORIZACION ----------------------------------------------------------------
class AddBook {
  constructor() {
    this.books = new Map()
  }

  addBook(title, writer, numberCopies) {
    if (this.books.has(title)) console.warn('El libro que desea agregar ya está en la biblioteca')
    else {
      this.books.set(title, {writer: writer, copies: numberCopies})
      console.log('El libro se ha agregado al catálogo de la biblioteca')
    }
  }
}

class AddUser {
  constructor() {
    this.users = new Map()
  }

  addUser(idUser, name, number) {
    if (this.users.has(idUser)) console.warn('El usuario ya está registrado en la biblioteca')
    else {
      this.users.set(idUser, {name: name, number: number})
      console.log('El usuario se ha registrado correctamente en la biblioteca')
    }
  }
}

class Loans {
  constructor() {
    this.loans = []
  }

  loanBook(title, idUser) {
    if (!inventory.books.has(title)) return console.warn('El libro que desea no está en esta biblioteca')
    if (!clients.users.has(idUser)) return console.warn('El usuario no esta registrado en esta biblioteca')
    const book = inventory.books.get(title) 
    if (book.copies > 0) {
      this.loans.push([idUser, title])
      book.copies--
      console.log('Recuerda devolver el libro cuando lo termines, gracias!')
    }
    else {
      console.warn('No quedan existencias del libro que desea\nPregunte nuevamente en otro momento o elija otro')
    }
  }

  returnBook(title, idUser) {
    if (inventory.books.has(title) && clients.users.has(idUser)) {
      let booksLoanedUser = this.loans.filter((loan) => loan[0] === idUser) // devuelde los libros retirados por el usuario
      if (booksLoanedUser.length > 0 && booksLoanedUser.map((loan) => loan[1] === title)) { // verifica que haya libros retirado por el usuario y que coincida con el titulo ingresado
        let index = this.loans.findIndex((loan) => {return loan[0] === idUser && loan[1] === title}) // devuelve el index del array donde esta el libro retirado y el id del usuario
        this.loans.splice(index, 1)
        const book = inventory.books.get(title) 
        book.copies++
        console.log('Has devuelto el libro!! Gracias!!')
      } else console.warn('Id o titulo del libro incorrectos')
    }
    else {
      console.error('Datos incorrectos, vuelve a chequear que escribiste bien el nombre del libro o tu id')
    }
  }
}

const inventory = new AddBook()
const clients = new AddUser()
const loans = new Loans()

//Creación de libros
console.log('----------------- CREACION DE LIBROS -----------------')
inventory.addBook('Cien años de soledad', 'Gabriel García Márquez', 5); inventory.addBook('1984', 'George Orwell', 7); inventory.addBook('Orgullo y Prejuicio', 'Jane Austen', 3); inventory.addBook('El Principito', 'Antoine de Saint-Exupéry', 10); inventory.addBook('Don Quijote de la Mancha', 'Miguel de Cervantes', 2); inventory.addBook('Crimen y Castigo', 'Fiódor Dostoievski', 4); inventory.addBook('Moby Dick', 'Herman Melville', 6); inventory.addBook('Ensayo sobre la ceguera', 'José Saramago', 8)

//Creación de usuarios
console.log('\n----------------- CREACION DE USUARIOS -----------------')
clients.addUser(10001, 'Martina López', 987654321); clients.addUser(10002, 'Javier Ríos', 912345678); clients.addUser(10003, 'Sofía Giménez', 900112233); clients.addUser(10004, 'Andrés Castro', 945612378); clients.addUser(10005, 'Valeria Torres', 998877665); clients.addUser(10006, 'Ricardo Paz', 965432101); clients.addUser(10007, 'Elena Ruiz', 955544433); clients.addUser(10008, 'Felipe Díaz', 933322211); clients.addUser(10009, 'Carla Méndez', 977788899); clients.addUser(10010, 'Pablo Núñez', 921234567); clients.addUser(10011, 'Luisa Vargas', 987123456); clients.addUser(10012, 'Diego Soto', 911223344); clients.addUser(10013, 'Catalina Vega', 950505050); clients.addUser(10014, 'Hugo Ferrer', 930303030); clients.addUser(10015, 'Micaela Gil', 970707070)

// Creación de prestamos
  console.log('\n----------------- CREACION DE PRESTAMOS -----------------')
  // AGOTANDO EXISTENCIAS: 'Don Quijote de la Mancha' y 'Orgullo y Prejuicio'
  loans.loanBook('Don Quijote de la Mancha', 10001); loans.loanBook('Don Quijote de la Mancha', 10002)
  loans.loanBook('Orgullo y Prejuicio', 10003); loans.loanBook('Orgullo y Prejuicio', 10004); loans.loanBook('Orgullo y Prejuicio', 10005)

  // PETICIONES EXITOSAS
  loans.loanBook('1984', 10006); loans.loanBook('Cien años de soledad', 10007); loans.loanBook('Ensayo sobre la ceguera', 10008); loans.loanBook('Moby Dick', 10009); loans.loanBook('Crimen y Castigo', 10010)

  // PETICIONES FALLIDAS
    console.log('\n----------------- CREACION DE PRESTAMOS ERRONEOS -----------------')
    //Libros agotados
    loans.loanBook('Don Quijote de la Mancha', 10011); loans.loanBook('Orgullo y Prejuicio', 10012)
    //Libros inexistentes
    loans.loanBook('El Código Da Vinci', 10013); loans.loanBook('Frieren', 10014)

// Creación de devoluciones
  // Devoluciones exitosas
  console.log('\n----------------- CREACION DE DEVOLUCIONES -----------------')
  loans.returnBook('Don Quijote de la Mancha', 10001); loans.returnBook('Orgullo y Prejuicio', 10005); loans.returnBook('1984', 10006); loans.returnBook('Cien años de soledad', 10007); loans.returnBook('Moby Dick', 10009)

  // Devolución con ID de usuario incorrecto (posiblemente fallida)
  console.log('\n----------------- CREACION DE DEVOLUCIONES ERRONEAS -----------------')
  loans.returnBook('Crimen y Castigo', 32465)