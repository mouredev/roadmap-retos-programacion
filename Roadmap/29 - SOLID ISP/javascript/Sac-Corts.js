// Wrong way
class Device {
    turnOn() {}
    turnOff() {}
    charge() {}
    connectToInternet() {}
}

class Laptop extends Device {
    turnOn() {
        console.log("Laptop turned on");
    }

    turnOff() {
        console.log("Laptop turned off");
    }

    charge() {
        console.log("Laptop charging");
    }

    connectToInternet() {
        console.log("Laptop connected to the internet");
    }
}

class Microwave extends Device {
    turnOn() {
        console.log("Microwave turned on");
    }

    turnOff() {
        console.log("Microwave turned off");
    }

    charge() {
        throw new Error("A microwave doesn't need to be charged");
    }

    connectToInternet() {
        throw new Error("A microwave doesn't need to be connected to the internet");
    }
}

const microwave = new Microwave();
// microwave.charge();  // Error

// Correct way
class Switchable {
    turnOn() {}
    turnOff() {}
}

class Chargeable {
    charge() {}
}

class InternetConnectable {
    connectToInternet() {}
}

class Laptop2 extends Switchable {
    turnOn() {
        console.log("Laptop turned on");
    }

    turnOff() {
        console.log("Laptop turned off");
    }
}

class AdvancedLaptop extends Laptop2 {
    charge() {
        console.log("Laptop charging.");
    }

    connectToInternet() {
        console.log("Laptop connected to the internet.");
    }
}

class Microwave2 extends Switchable {
    turnOn() {
        console.log("Microwave turned on");
    }

    turnOff() {
        console.log("Microwave turned off");
    }
}

const laptop2 = new AdvancedLaptop();
laptop2.charge();
laptop2.connectToInternet();

const microwave2 = new Microwave2();
microwave2.turnOn();
microwave2.turnOff();

// Extra Exercise //
class BlackAndWhitePrintable  {
    printBlackAndWhite() {}
}

class ColorPrintable {
    printColor() {}
}

class Scannable {
    scan() {}
}

class Faxable {
    sendFax() {}
}

class BlackAndWhitePrinter extends BlackAndWhitePrintable {
    printBlackAndWhite() {
        console.log("Printing in black and white...");
    }
}

class ColorPrinter extends ColorPrintable {
    printColor() {
        console.log("Printing in color...");
    }
}

class MultiFunctionPrinter extends BlackAndWhitePrintable {
    printBlackAndWhite() {
        console.log("Printing in black and white...");
    }

    printColor() {
        console.log("Printing in color...");
    }

    scan() {
        console.log("Scanning...");
    }

    sendFax() {
        console.log("Sending fax...");
    }
}

const blackAndWhitePrinter = new BlackAndWhitePrinter();
blackAndWhitePrinter.printBlackAndWhite();

const colorPrinter = new ColorPrinter();
colorPrinter.printColor();

const multiFunctionPrinter = new MultiFunctionPrinter();
multiFunctionPrinter.printBlackAndWhite();
multiFunctionPrinter.printColor();
multiFunctionPrinter.scan();
multiFunctionPrinter.sendFax();