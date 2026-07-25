// Wrong way
class Device {
    turnOn(): void {}
    turnOff(): void {}
    charge(): void {}
    connectToInternet(): void {}
}

class Laptop extends Device {
    turnOn(): void {
        console.log("Laptop turned on");
    }

    turnOff(): void {
        console.log("Laptop turned off");
    }

    charge(): void {
        console.log("Laptop charging");
    }

    connectToInternet(): void {
        console.log("Laptop connected to the internet");
    }
}

class Microwave extends Device {
    turnOn(): void {
        console.log("Microwave turned on");
    }

    turnOff(): void {
        console.log("Microwave turned off");
    }

    charge(): void {
        throw new Error("A microwave doesn't need to be charged");
    }

    connectToInternet(): void {
        throw new Error("A microwave doesn't need to be connected to the internet");
    }
}

const microwave = new Microwave();
// microwave.charge();  // Error

// Correct way
class Switchable {
    turnOn(): void {}
    turnOff(): void {}
}

class Chargeable {
    charge(): void {}
}

class InternetConnectable {
    connectToInternet(): void {}
}

class Laptop2 extends Switchable {
    turnOn(): void {
        console.log("Laptop turned on");
    }

    turnOff(): void {
        console.log("Laptop turned off");
    }
}

class AdvancedLaptop extends Laptop2 implements Chargeable, InternetConnectable {
    charge(): void {
        console.log("Laptop charging.");
    }

    connectToInternet(): void {
        console.log("Laptop connected to the internet.");
    }
}

class Microwave2 extends Switchable {
    turnOn(): void {
        console.log("Microwave turned on");
    }

    turnOff(): void {
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
class BlackAndWhitePrintable {
    printBlackAndWhite(): void {}
}

class ColorPrintable {
    printColor(): void {}
}

class Scannable {
    scan(): void {}
}

class Faxable {
    sendFax(): void {}
}

class BlackAndWhitePrinter extends BlackAndWhitePrintable {
    printBlackAndWhite(): void {
        console.log("Printing in black and white...");
    }
}

class ColorPrinter extends ColorPrintable {
    printColor(): void {
        console.log("Printing in color...");
    }
}

class MultiFunctionPrinter extends BlackAndWhitePrintable implements ColorPrintable, Scannable, Faxable {
    printBlackAndWhite(): void {
        console.log("Printing in black and white...");
    }

    printColor(): void {
        console.log("Printing in color...");
    }

    scan(): void {
        console.log("Scanning...");
    }

    sendFax(): void {
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
