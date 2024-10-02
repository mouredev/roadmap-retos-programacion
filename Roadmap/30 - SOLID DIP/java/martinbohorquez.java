/**
 * #30 SOLID: PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS (DIP)
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    public static void main(String[] args) {
        incorrectDIP();
        correctDIP();
        /*
         * DIFICULTAD EXTRA
         */
        notificationDIP();
    }

    private static void incorrectDIP() {
        Lampara lampara = new Lampara();
        lampara.operate("on");
        lampara.operate("off");
    }

    private static void correctDIP() {
        Lamp lamp = new Lamp(new LampSwitch());
        lamp.operate("on");
        lamp.operate("off");
    }

    private static void notificationDIP() {
        var service = new NotificationService(new EmailNotifier());
        service.notify("Mensaje 1");
        service = new NotificationService(new PushNotifier());
        service.notify("Mensaje 2");
        service = new NotificationService(new SmsNotifier());
        service.notify("Mensaje 3");
    }
}

class Interruptor {
    protected void turnOn() {
        System.out.println("Enciende la lámpara!");
    }

    protected void turnOff() {
        System.out.println("Apaga la lámpara!");
    }
}

class Lampara {
    private final Interruptor aSwitch;

    public Lampara() {
        aSwitch = new Interruptor();
    }

    protected void operate(String command) {
        if ("on".equals(command)) aSwitch.turnOn();
        else if ("off".equals(command)) aSwitch.turnOff();
    }
}

interface Switch {
    void turnOn();

    void turnOff();
}

class LampSwitch implements Switch {
    @Override
    public void turnOn() {
        System.out.println("Enciende la lámpara!");
    }

    @Override
    public void turnOff() {
        System.out.println("Apaga la lámpara!");
    }
}

class Lamp {
    private final Switch aSwitch;

    public Lamp(Switch aSwitch) {
        this.aSwitch = aSwitch;
    } // Desacoplar la clase para poder usar cualquier clase implementa Switch (ejem. LampSwitch)

    protected void operate(String command) {
        if ("on".equals(command)) aSwitch.turnOn();
        else if ("off".equals(command)) aSwitch.turnOff();
    }
}

interface Notifier {
    void send(String message);
}

class EmailNotifier implements Notifier {
    @Override
    public void send(String message) {
        System.out.printf("Enviando email con texto: %s%n", message);
    }
}

class PushNotifier implements Notifier {
    @Override
    public void send(String message) {
        System.out.printf("Enviando PUSH con texto: %s%n", message);
    }
}

class SmsNotifier implements Notifier {
    @Override
    public void send(String message) {
        System.out.printf("Enviando SMS con texto: %s%n", message);
    }
}

class NotificationService {
    private final Notifier notifier;

    public NotificationService(Notifier notifier) {
        this.notifier = notifier;
    }

    void notify(String message) {
        notifier.send(message);
    }
}