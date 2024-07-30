/*
  EJERCICIO:
  Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
  y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
*/

console.log("+++++++++ FORMA INCORRECTA +++++++++");

class ProductProof {
  getDetails() {
    console.log("Obtener detalles del producto físico.");
  }

  saveToDb() {
    console.log("Guardar producto físico en la base de datos.");
  }
}

class DigitalProductProof extends ProductProof {
  getDetails() {
    console.log("Obtener detalles del producto digital.");
  }

  saveToDb() {
    console.log("Guardar producto digital en la base de datos.");
  }
}

const productProof = new ProductProof();
const digitalProductProof = new DigitalProductProof();

productProof.getDetails();
productProof.saveToDb();
digitalProductProof.getDetails();
digitalProductProof.saveToDb();

console.log("\n+++++++++ FORMA CORRECTA +++++++++");

class Product {
  getDetails() {
    console.error("Primero se debe definir si los detalles a obtener son de un producto físico o dígital.");
  }
}

class PhysicalProduct extends Product {
  getDetails() {
    console.log("Obtener detalles del producto físico.");
  }
}

class DigitalProduct extends Product {
  getDetails() {
    console.log("Obtener detalles del producto digital.");
  }

  saveToDb() {
    console.log("Guardar producto digital en la base de datos.");
  }
}

const product = new Product();
const physicalProduct = new PhysicalProduct();
const digitalProduct = new DigitalProduct();

product.getDetails();
physicalProduct.getDetails();
digitalProduct.getDetails();
digitalProduct.saveToDb();

/*
  DIFICULTAD EXTRA (opcional):
  Crea un gestor de impresoras.
  Requisitos:
  1. Algunas impresoras sólo imprimen en blanco y negro.
  2. Otras sólo a color.
  3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
  Instrucciones:
  1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
  2. Aplica el ISP a la implementación.
  3. Desarrolla un código que compruebe que se cumple el principio.
*/

console.log("\n+++++++++ GESTOR DE IMPRESORAS +++++++++");

class BlackAndWhiteInterface {
  print(document) {
    console.error(`El documento ${document} no se puede imprimir a blanco y negro desde la interfaz.`);
  }
}

class ColorInterface {
  colorPrint(document) {
    console.error(`El documento ${document} no se puede imprimir a color desde la interfaz.`);
  }
}

class ScannerInterface {
  scan(document) {
    console.error(`El documento ${document} no se puede escanear desde la interfaz.`);
  }
}

class FaxInterface {
  fax(document) {
    console.error(`El documento ${document} no se puede enviar por fax desde la interfaz.`);
  }
}

class BlackAndWhitePrinter extends BlackAndWhiteInterface {
  print(document) {
    console.log(`Imprimiendo el documento "${document}" a blanco y negro.`);
  }
}

class ColorPrinter extends ColorInterface {
  colorPrint(document) {
    console.log(`Imprimiendo el documento "${document}" a color.`);
  }
}

class MultifunctionPrinter extends (BlackAndWhiteInterface, ColorInterface, ScannerInterface, FaxInterface) {
  print(document) {
    console.log(`Imprimiendo el documento "${document}" a blanco y negro.`);
  }

  colorPrint(document) {
    console.log(`Imprimiendo el documento "${document}" a color.`);
  }

  scan(document) {
    console.log(`Escaneando el documento "${document}".`);
  }

  fax(document) {
    console.log(`Enviando por el documento "${document}" por fax.`);
  }
}

function testingPrinters() {
  const doc = "tenencia-2024.pdf"

  const blackAndWhiteInterface = new BlackAndWhiteInterface();
  const colorInterface = new ColorInterface();
  const scannerInterface = new ScannerInterface();
  const faxInterface = new FaxInterface();

  const blackAndWhitePrinter = new BlackAndWhitePrinter();
  const colorPrinter = new ColorPrinter();
  const multifunctionPrinter = new MultifunctionPrinter();

  blackAndWhiteInterface.print(doc);
  colorInterface.colorPrint(doc);
  scannerInterface.scan(doc);
  faxInterface.fax(doc);

  blackAndWhitePrinter.print(doc);
  colorPrinter.colorPrint(doc);
  multifunctionPrinter.print(doc);
  multifunctionPrinter.colorPrint(doc);
  multifunctionPrinter.scan(doc);
  multifunctionPrinter.fax(doc);
}

testingPrinters();
