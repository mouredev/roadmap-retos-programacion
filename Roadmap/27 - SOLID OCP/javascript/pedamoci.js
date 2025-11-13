// OCP MAL HECHO
  class DateNow {
    getDateNow(info) {
      const date = new Date
      switch (info) {
        case 'day':
          console.log(`El día es: ${date.getDay()}`)
          break;
        case 'month':
          console.log(`El mes es: ${date.getMonth()}`)
          break;
        default:
          break;
      }
    }
  }
  console.log('------------- OCP MAL HECHO -------------')
  const dateNow = new DateNow
  dateNow.getDateNow('day')
  dateNow.getDateNow('month')

  // Si necesito agregar una función tengo que modificar el switch

  class DateNow2 {
    getDateNow(info) {
      const date = new Date
      switch (info) {
        case 'day':
          console.log(`El día es: ${date.getDay()}`)
          break;
        case 'month':
          console.log(`El mes es: ${date.getMonth()}`)
          break;
        case 'year':
          console.log(`El año es: ${date.getFullYear()}`)
          break;
        default:
          break;
      }
    }
  }

  const dateNow2 = new DateNow2
  dateNow2.getDateNow('day')
  dateNow2.getDateNow('month')
  dateNow2.getDateNow('year')

// OCP BIEN HECHO
class DateNow3 {
  constructor(getDate) {
    this.getDate = getDate
  }

  getDateNow() {
    return this.getDate.getDateNow()
  }
}

class GetDateNow {
  getDateNow() {}
}

class GetDay extends GetDateNow{
  getDateNow() {
    const date = new Date
    return date.getDay()
  }
}

class GetMonth extends GetDateNow{
  getDateNow() {
    const date = new Date
    return date.getMonth()
  }
}

console.log('\n------------- OCP BIEN HECHO -------------')
const getDay = new DateNow3(new GetDay())
console.log(`El día es: ${getDay.getDateNow()}`)
const getMonth = new DateNow3(new GetMonth())
console.log(`El mes es: ${getMonth.getDateNow()}`)

// Si quiero agregar una función 
class GetYear extends GetDateNow {
  getDateNow() {
    const date = new Date
    return date.getFullYear()
  }
}

const getYear = new DateNow3(new GetYear())
console.log(`El año es: ${getYear.getDateNow()}`)

// -------------------------------------------------- EJERCICIO EXTRA --------------------------------------------------
class Calculator {
  constructor(calculation) {
    this.calculation = calculation
  }

  operation(num1, num2) {
    return this.calculation.operation(num1, num2)
  }
}

class Operations {
  operation() {}
}

class Addition extends Operations{
  operation(num1, num2) {
    return num1 + num2
  }
}

class Subtraction extends Operations{
  operation(num1, num2) {
    return num1 - num2
  }
}

class Division extends Operations{
  operation(num1, num2) {
    if (num2 === 0) return 'No se puede dividir por cero'
    return num1 / num2
  }
}

// Comprobación de que el sistema funciona
console.log('\n--------------- COMPROBACION DE FUNCIONAMIENTO ---------------')
const addition = new Calculator(new Addition())
console.log(`Suma: ${addition.operation(55, 32)}`)

const subtraction = new Calculator(new Subtraction())
console.log(`Resta: ${subtraction.operation(55, 32)}`)

const division = new Calculator(new Division())
console.log(`Divición: ${division.operation(55, 5)}`)

class Exponentiation extends Operations{
  operation(num1, num2) {
    return num1 ** num2
  }
}

console.log('\n--------------- COMPROBACION DE FUNCIONAMIENTO FINAL ---------------')
const exponentiation = new Calculator(new Exponentiation())
console.log(`Suma: ${addition.operation(5465, 3245)}`)
console.log(`Resta: ${subtraction.operation(35480, 54982)}`)
console.log(`Divición: ${division.operation(8464, 154)}`)
console.log(`Exponenciación: ${exponentiation.operation(55, 4)}`)