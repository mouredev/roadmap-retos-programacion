console.log('---------------------- ISP MAL HECHO ----------------------')
class WrongAnimal {
  eat() {
    console.log('Comiendo')
  }
  run() {
    console.log('Corriendo')
  }
}

class WrongDog extends WrongAnimal {}

class WrongFish extends WrongAnimal {
  run() {
    try {
      throw new Error("Un pez no puede correr")
    } catch (e) {
      console.log(e.message)
    }
  }
}

const wrongDog = new WrongDog
const wrongFish = new WrongFish

wrongDog.eat()
wrongDog.run()

wrongFish.eat()
wrongFish.run()

console.log('\n---------------------- ISP BIEN HECHO ----------------------')
const canEat = {
  eat() { console.log('Comiendo') }
}

const canRun = {
  run() { console.log('Corriendo') }
}

class Dog {
  constructor() {
    Object.assign(this, canEat, canRun)
  }
}

class Fish {
  constructor() {
    Object.assign(this, canEat)
  }
}

const dog = new Dog
const fish = new Fish

dog.eat()
dog.run()

fish.eat()

// ------------------------------------------ DIFICULTAD EXTRA ------------------------------------------
const colors = {
  ROJO: "\x1b[31m",
  VERDE: "\x1b[32m",
  AMARILLO: "\x1b[33m",
  AZUL: "\x1b[34m",
  MAGENTA: "\x1b[35m",
  CIAN: "\x1b[36m",
  RESET: "\x1b[0m"
}

const printWhiteBlack = {
  print(text) {
    console.log('Imprimiendo...')
    return new Promise(resolve => {
      setTimeout(() => {
        console.log(text)
        resolve()
      }, 1500);
    })
  }
}

const printColor = {
  print(text, color) {
    console.log('Imprimiendo...')
    return new Promise(resolve => {
      setTimeout(() => {
        switch (color) {
          case 'rojo':
            console.log(`${colors.ROJO}${text}${colors.RESET}`)
            resolve()
            break
          case 'verde':
            console.log(`${colors.VERDE}${text}${colors.RESET}`)
            resolve()
            break
          case 'amarillo':
            console.log(`${colors.AMARILLO}${text}${colors.RESET}`)
            resolve()
            break
          case 'azul':
            console.log(`${colors.AZUL}${text}${colors.RESET}`)
            resolve()
            break
          case 'magenta':
            console.log(`${colors.MAGENTA}${text}${colors.RESET}`)
            resolve()
            break
          case 'cian':
            console.log(`${colors.CIAN}${text}${colors.RESET}`)
            resolve()
            break
          default: console.warn('Ese color no esta disponible')
            resolve()
            break
        }
      }, 1500);
    })
  }
}

const hasScan = {
  scan() {
    console.log('Escaneando...')
    return new Promise(resolve => {
    setTimeout(() => {
      this.text = 'EJERCICIO:\n' +
                  'Explora el "Principio SOLID de Segregación de Interfaces\n' +
                  '(Interface Segregation Principle, ISP)", y crea un ejemplo\n' +
                  'simple donde se muestre su funcionamiento de forma correcta e incorrecta.\n' +

                  '\nDIFICULTAD EXTRA (opcional):\n' +
                  'Crea un gestor de impresoras.\n' +
                  'Requisitos:\n' +
                  '1. Algunas impresoras sólo imprimen en blanco y negro.\n' +
                  '2. Otras sólo a color.\n' +
                  '3. Otras son multifunción, pueden imprimir, escanear y enviar fax.\n' +
                  'Instrucciones:\n' +
                  '1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.\n' +
                  '2. Aplica el ISP a la implementación.\n' +
                  '3. Desarrolla un código que compruebe que se cumple el principio.'
      console.log('El scaneo a terminado')
      resolve()
    }, 2500)
    })
  }
}

const hasFax = {
  sendFax() {
    console.log('Enviando...')
    return new Promise(resolve => {
      setTimeout(() => {
        console.log('Se ha emviado el fax')
        resolve()
      }, 4000);
    })
  } 
}

class PrinterWhiteBlack {
  constructor() {
    Object.assign(this, printWhiteBlack)
  }
}

class PrinterColor {
  constructor() {
    Object.assign(this, printColor)
  }
}

class PrinterWhiteBlackScanFax {
  constructor() {
    Object.assign(this, printWhiteBlack, hasScan, hasFax)
    this.text = ''
  }
}

class PrinterColorScanFax {
  constructor() {
    Object.assign(this, printColor, hasScan, hasFax)
    this.text = ''
  }
}

const printerWhiteBlack = new PrinterWhiteBlack

const printerColor = new PrinterColor

const printerWhiteBlackScanFax = new PrinterWhiteBlackScanFax

const printerColorScanFax = new PrinterColorScanFax

async function program() {
  console.log('voy a escanear un texto con printerColorScanFax')
  await printerColorScanFax.scan()

  console.log('voy a enviar un fax con printerWhiteBlackScanFax')
  await printerWhiteBlackScanFax.sendFax('Te mando este fax desde una impresora que solo imprime en blanco y negro')

  console.log('voy a imprimir con printColor y printWhiteBlack')
  await Promise.all([printColor.print('imprimiendo en color cian', 'cian'), printWhiteBlack.print('imprimiendo en blanco y negro')]) 

  console.log('voy a imprimir el texto escaneado con printerColorScanFax')
  await printerColorScanFax.print(printerColorScanFax.text, 'magenta')
}
program()