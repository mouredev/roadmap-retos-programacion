<?php

// Ejemplo de código que viola el principio de inversión de dependencias

class CreditCardPayment {
    public function process($amount) {

        echo "Procesando pago de $amount con tarjeta de crédito\n";
    }
}

class PaymentProcessor {
    private $paymentMethod;

    public function __construct() {
        $this->paymentMethod = new CreditCardPayment();
    }

    public function processPayment($amount) {
        $this->paymentMethod->process($amount);
    }
}

// Uso
echo "\n\nEjemplo de mala implementacion\n\n";
$paymentProcessor = new PaymentProcessor();
$paymentProcessor->processPayment(100);

?>


<?php

// Ejemplo de codigo que cumple el principio de inversion de dependencias
interface PaymentMethodInterface {
    public function process($amount);
}

// Implementación concreta de la interfaz
class CreditCardPayment2 implements PaymentMethodInterface {
    public function process($amount) {

        echo "Procesando pago de $amount con tarjeta de crédito\n";
    }
}

class PayPalPayment implements PaymentMethodInterface {
    public function process($amount) {
        // Lógica para procesar el pago con PayPal
        echo "Procesando pago de $amount con PayPal\n";
    }
}

class PaymentProcessor2 {
    private $paymentMethod;

    public function __construct(PaymentMethodInterface $paymentMethod) {
        $this->paymentMethod = $paymentMethod;
    }

    public function processPayment($amount) {
        $this->paymentMethod->process($amount);
    }
}

echo "\n\nEjemplo correcto\n\n";
$creditCardPayment = new CreditCardPayment2();
$paymentProcessor = new PaymentProcessor2($creditCardPayment);
$paymentProcessor->processPayment(100);

echo "\n\nAhora probemos usando paypal\n\n";
$paypalPayment = new PayPalPayment();
$paymentProcessor = new PaymentProcessor2($paypalPayment);
$paymentProcessor->processPayment(200);

// Ejercicio extra

interface NotificationInterface {
    public function send($message, $recipient);
}

class EmailNotification implements NotificationInterface {
    public function send($message, $recipient) {
        // Lógica para enviar un correo electrónico
        echo "Enviando email a $recipient: $message\n";
    }
}

class PushNotification implements NotificationInterface {
    public function send($message, $recipient) {
        // Lógica para enviar una notificación push
        echo "Enviando notificación push a $recipient: $message\n";
    }
}

class SMSNotification implements NotificationInterface {
    public function send($message, $recipient) {
        // Lógica para enviar un SMS
        echo "Enviando SMS a $recipient: $message\n";
    }
}

class NotificationService {
    private $notificationMethod;

    // Inyección de la dependencia a través del constructor
    public function __construct(NotificationInterface $notificationMethod) {
        $this->notificationMethod = $notificationMethod;
    }

    public function notify($message, $recipient) {
        $this->notificationMethod->send($message, $recipient);
    }
}

echo "\n\nEjercicio extra\n\n";

$emailNotification = new EmailNotification();
$pushNotification = new PushNotification();
$smsNotification = new SMSNotification();

// Crear el servicio de notificaciones con diferentes métodos
$emailService = new NotificationService($emailNotification);
$pushService = new NotificationService($pushNotification);
$smsService = new NotificationService($smsNotification);

// Enviar notificaciones utilizando el servicio
$emailService->notify("Hola, mundo!", "usuario@example.com");
$pushService->notify("Tienes una nueva actualización", "usuario123");
$smsService->notify("Tu código de verificación es 123456", "666666666");
