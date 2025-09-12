<?php

// Ejemplo basico sin ISP

interface PaymentInterface {
    public function payOnline($amount);
    public function payInCash($amount);
}

class OnlinePayment implements PaymentInterface {
    public function payOnline($amount) {
        echo "Procesando el pago online de " . $amount . " €\n";
    }

    public function payInCash($amount) {
        throw new Exception("El pago Online no admite el pago en efectivo");
    }
}

class CashPayment implements PaymentInterface {
    public function payOnline($amount) {
        throw new Exception("El pago en efectivo no permite el pago por medios online");
    }

    public function payInCash($amount) {
        echo "Procesando el pago en efectivo de " . $amount. " €\n";
    }
}

echo "\n Ejemplo basico sin ISP\n";
$onlinePayment = new OnlinePayment();
$cashPayment = new CashPayment();

$onlinePayment->payOnline(100);
//$onlinePayment->payInCash(100); 

//$cashPayment->payOnline(100); 
$cashPayment->payInCash(100);

// Ejemplo basico aplicando ISP

interface OnlinePaymentInterface {
    public function payOnline($amount);
}

interface CashPaymentInterface {
    public function payInCash($amount);
}

class OnlinePayment2 implements OnlinePaymentInterface {
    public function payOnline($amount) {
        echo "Procesando el pago online de " . $amount. " €\n";
    }
}

class CashPayment2 implements CashPaymentInterface {
    public function payInCash($amount) {
        echo "Procesando el pago en efectivo de " . $amount. " €\n";
    }
}

echo "\n Ejemplo basico con ISP\n";
$onlinePayment = new OnlinePayment2();
$cashPayment = new CashPayment2();

$onlinePayment->payOnline(100);

$cashPayment->payInCash(100);

// Extra

interface BlackAndWhitePrintInterface {
    public function printBlackAndWhite($document);
}

interface ColorPrintInterface {
    public function printColor($document);
}

interface ScanInterface {
    public function scan($document);
}

interface FaxInterface {
    public function sendFax($document);
}

class BlackAndWhitePrinter implements BlackAndWhitePrintInterface {
    public function printBlackAndWhite($document) {
        echo "Imprimiendo el documento " . $document . " en ByN\n";
    }
}

class ColorPrinter implements ColorPrintInterface {
    public function printColor($document) {
        echo "Imprimiendo el documento " . $document . " en color\n";
    }
}

class MultifunctionPrinter implements BlackAndWhitePrintInterface, ColorPrintInterface, ScanInterface, FaxInterface {
    public function printBlackAndWhite($document) {
        echo "Imprimiendo el documento " . $document . " en ByN\n";
    }

    public function printColor($document) {
        echo "Imprimiendo el documento " . $document . " en color\n";
    }

    public function scan($document) {
        echo "Escaneando el documento " . $document . "\n";
    }

    public function sendFax($document) {
        echo "Mandando por fax el documento ". $document . "\n";
    }
}

function testPrinter(BlackAndWhitePrintInterface $bwPrinter = null, ColorPrintInterface $colorPrinter = null, ScanInterface $scanner = null, FaxInterface $faxMachine = null) {
    $document = "Test_Document.doc";

    if ($bwPrinter !== null) {
        $bwPrinter->printBlackAndWhite($document);
    }

    if ($colorPrinter !== null) {
        $colorPrinter->printColor($document);
    }

    if ($scanner !== null) {
        $scanner->scan($document);
    }

    if ($faxMachine !== null) {
        $faxMachine->sendFax($document);
    }
}

$bwPrinter = new BlackAndWhitePrinter();
$colorPrinter = new ColorPrinter();
$multifunctionPrinter = new MultifunctionPrinter();

echo "\nExtra\n";
echo "Probando impresora ByN:\n";
testPrinter($bwPrinter);

echo "\nProbanco impresora color:\n";
testPrinter(null, $colorPrinter);

echo "\nProbando impresora multifunción:\n";
testPrinter($multifunctionPrinter, $multifunctionPrinter, $multifunctionPrinter, $multifunctionPrinter);