public class danhingar {

    public static void main(String[] args) {
        Lamp lamp1 = new Lamp();
        lamp1.operate("on");
        lamp1.operate("off");

        //Con DIP
        Lamp1 lamp2 = new Lamp1(new LampSwitchInterface());
        lamp2.operate("on");
        lamp2.operate("off");

        //Extra
        NotificationManager manager1 = new NotificationManager(new EmailNotifier());
        manager1.notify("Hello");

        NotificationManager manager2 = new NotificationManager(new PushNotifier());
        manager2.notify("Hello");

        NotificationManager manager3 = new NotificationManager(new SMSNotifier());
        manager3.notify("Hello");
    }

}

// SIN DIP
class Switch {

    public void turnOn() {
        System.out.println("Enciende la lámpara");
    }

    public void turnOff() {
        System.out.println("Apaga la lámpara");
    }

}

class Lamp {

    private Switch switch1;

    public Lamp() {
        this.switch1 = new Switch();
    }

    public void operate(String command) {
        if (command.equals("on")) {
            switch1.turnOn();
        } else if (command.equals("off")) {
            switch1.turnOff();
        }
    }

}

// CON DIP
interface SwitchInterface {
    void turnOn();

    void turnOff();
}

class LampSwitchInterface implements SwitchInterface {

    @Override
    public void turnOn() {
        System.out.println("Enciende la lámpara");
    }

    @Override
    public void turnOff() {
        System.out.println("Apaga la lámpara");
    }

}

class Lamp1 {

    private SwitchInterface switchInterface;

    public Lamp1(SwitchInterface switchInterface) {
        this.switchInterface = switchInterface;
    }

    public void operate(String command) {
        if (command.equals("on")) {
            switchInterface.turnOn();
        } else if (command.equals("off")) {
            switchInterface.turnOff();
        }
    }
    
}


//EXTRA
interface NotifierInterface{
    void sendNotification(String msg);
}

class EmailNotifier implements NotifierInterface{

    @Override
    public void sendNotification(String msg) {
        System.out.printf("Enviando email con texto %s.\n",msg);
    }

}

class PushNotifier implements NotifierInterface{

    @Override
    public void sendNotification(String msg) {
        System.out.printf("Enviando PUSH con texto %s.\n",msg);
    }

}

class SMSNotifier implements NotifierInterface{

    @Override
    public void sendNotification(String msg) {
        System.out.printf("Enviando SMS con texto %s.\n",msg);
    }
}

class NotificationManager {

    private NotifierInterface notifierInterface;

    public NotificationManager(NotifierInterface notifierInterface) {
        this.notifierInterface = notifierInterface;
    }

    public void notify(String msg){
        notifierInterface.sendNotification(msg);
    }
    
}