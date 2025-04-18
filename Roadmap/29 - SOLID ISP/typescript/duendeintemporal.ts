//#29 { retosparaprogramadores } - Principio SOLID de Segregación de Interfaces (Interface Segregation Principle (ISP))
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
 */
//Bibliografy: The Web Development Glossary (Jens Oliver Meiert) (Z-Library)
//GPT

/* Interface Segregation Principle
The principle that no client should be forced to depend on methods it does
not use. ISP splits interfaces that are very large into smaller and more
specific ones so that clients will only have to know about the methods that
are of interest to them. Such shrunken interfaces are also called role
interfaces. ISP is intended to keep a system decoupled and thus easier to
refactor, change, and redeploy.  */

let log = console.log;

// Check if running in a browser environment
const isBrowser = typeof window !== 'undefined';

// Conditional check for browser environment
if (isBrowser) {
    window.addEventListener('load', () => {
        const body: HTMLBodyElement | null = document.querySelector('body');
        const title = document.createElement('h1');

        body?.style.setProperty('background', '#000');
        body?.style.setProperty('text-align', 'center');

        title.textContent = 'Retosparaprogramadores #29.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '100vh');

        body?.appendChild(title);

        setTimeout(() => {
            alert('Retosparaprogramadores #29. Please open the Browser Developer Tools.');
        }, 2000);
        log('Retosparaprogramadores #29');
    });
} else {
    log('This code is designed to run in a browser environment. Skipping window-related code.');
    log('Retosparaprogramadores #29');
}

// Incorrect Example
class PaymentService {
    processCreditCardPayment(amount: number): void {}
    processPayPalPayment(amount: number): void {}
    processBitcoinPayment(amount: number): void {}
}

class CreditCardPayment extends PaymentService {
    processCreditCardPayment(amount: number): void {
        log(`Processing credit card payment of ${amount}`);
    }
    
    processPayPalPayment(amount: number): void {
        throw new Error("This payment method does not support PayPal payments");
    }
    
    processBitcoinPayment(amount: number): void {
        throw new Error("This payment method does not support Bitcoin payments");
    }
}

class PayPalPayment extends PaymentService {
    processCreditCardPayment(amount: number): void {
        throw new Error("This payment method does not support credit card payments");
    }
    
    processPayPalPayment(amount: number): void {
        log(`Processing PayPal payment of ${amount}`);
    }
    
    processBitcoinPayment(amount: number): void {
        throw new Error("This payment method does not support Bitcoin payments");
    }
}

class BitcoinPayment extends PaymentService {
    processCreditCardPayment(amount: number): void {
        throw new Error("This payment method does not support credit card payments");
    }
    
    processPayPalPayment(amount: number): void {
        throw new Error("This payment method does not support PayPal payments");
    }
    
    processBitcoinPayment(amount: number): void {
        log(`Processing Bitcoin payment of ${amount}`);
    }
}


const creditCardPayment = new CreditCardPayment();
creditCardPayment.processCreditCardPayment(250); // Processing credit card payment of 250
//creditCardPayment.processPayPalPayment(87); // This will throw an error
//Error: This payment method does not support PayPal payments at CreditCardPayment.processPayPalPayment

// Correct Example
class CreditCardPaymentService {
    processCreditCardPayment(amount: number): void {
        log(`Processing credit card payment of ${amount}`);
    }
}

class PayPalPaymentService {
    processPayPalPayment(amount: number): void {
        log(`Processing PayPal payment of ${amount}`);
    }
}

class BitcoinPaymentService {
    processBitcoinPayment(amount: number): void {
        log(`Processing Bitcoin payment of ${amount}`);
    }
}


const creditCardPayment1 = new CreditCardPaymentService();
creditCardPayment1.processCreditCardPayment(400); // Processing credit card payment of 400

const payPalPayment = new PayPalPaymentService();
payPalPayment.processPayPalPayment(130); // Processing PayPal payment of 130

const bitcoinPayment = new BitcoinPaymentService();
bitcoinPayment.processBitcoinPayment(0.020); // Processing Bitcoin payment of 0.02


//Extra Dificulty Exercise

class BlackAndWhitePrinter{
    print(doc: string): void{
        log(`Printing: ${doc} in Black & White`);
    }
}

class ColorPrinter{
    print(doc: string): void{
        log(`Printing: ${doc} in Color`);
    }
}

class MultiFunctionPrinter{

    printInBlackAndWhite(doc: string): void{
        log(`Printing: ${doc} in Black & White`);
    }

    print(doc: string): void{
        log(`Printing: ${doc} in Color`);
    }

    fax(doc: string): void{
        log(`Faxing: ${doc}`);
    }

    scan(doc: string): void{
        log(`Scanning: ${doc}`);
    }
}

let book = 'vuelointemporal.odt';

const bw_printer = new BlackAndWhitePrinter();
bw_printer.print(book); // Printing: vuelointemporal.odt in Black & White

const c_printer = new ColorPrinter();
c_printer.print(book); // vuelointemporal.odt in Color

const m_printer = new MultiFunctionPrinter();
m_printer.printInBlackAndWhite(book); // vuelointemporal.odt in Black & White
m_printer.print(book); // Printing: vuelointemporal.odt in Color
m_printer.fax(book); // Faxing: vuelointemporal.odt
m_printer.scan(book); // Scanning: vuelointemporal.odt