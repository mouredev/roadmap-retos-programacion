public class danhingar {
    public static void main(String[] args) {
        Function function1 = new FunctionNameDecorator(new ExampleFunction("function1"));
        function1.execute();

        Function function2 = new FunctionNameDecorator(new ExampleFunction("function2"));
        function2.execute();

        Function function3 = new FunctionNameDecorator(new ExampleFunction("function3"));
        function3.execute();

        Function function4 = new FunctionCounterDecorator(new ExampleFunction("function4"));
        function4.execute();
        function4.execute();

        Function function5 = new FunctionCounterDecorator(new ExampleFunction("function5"));
        function5.execute();

        function4.execute();
        function4.execute();
        function5.execute();

        //EJEMPLO EXTRA
        BaseDecorator notifier = new SMSDecorator(new FacebookDecorator(new SlackDecorator(new basicNotifier())));

        notifier.send("HELLO!!");

        
        Notifier basicNotifier = new basicNotifier();

        Notifier smsNotifier = new SMSDecorator(basicNotifier);
        Notifier facebookNotifier = new FacebookDecorator(smsNotifier);
        Notifier slackNotifier = new SlackDecorator(facebookNotifier);

        slackNotifier.send("GOODBYE!!");
    }

}

interface Function {
    void execute();
}

class ExampleFunction implements Function {
    private String nameFunction;

    public ExampleFunction(String nameFunction) {
        this.nameFunction = nameFunction;
    }

    @Override
    public void execute() {
        System.out.println("Ejecutando la función " + this.nameFunction);
    }

    public String getNameFunction() {
        return nameFunction;
    }

}

class FunctionNameDecorator implements Function {
    private final ExampleFunction function;

    public FunctionNameDecorator(ExampleFunction function) {
        this.function = function;
    }

    @Override
    public void execute() {

        System.out.println("La función '" + function.getNameFunction() + "' ha sido llamada.");

        function.execute();

    }
}

class FunctionCounterDecorator implements Function {
    private final ExampleFunction function;
    private int callCounter = 0;

    public FunctionCounterDecorator(ExampleFunction function) {
        this.function = function;
    }

    @Override
    public void execute() {
        callCounter++;

        System.out.println("La función '" + function.getNameFunction() + "' se ha llamado " + callCounter);

        function.execute();

    }
}

interface Notifier {
    void send(String message);
}

class basicNotifier implements Notifier {

    @Override
    public void send(String message) {
        System.out.println("Enviando notificacion básica por correo:  " + message);
    }
}

abstract class BaseDecorator implements Notifier {
    protected Notifier wrapper;

    public BaseDecorator(Notifier notifier) {
        this.wrapper = notifier;
    }

    @Override
    public void send(String message) {
        wrapper.send(message);
    }
}

class SMSDecorator extends BaseDecorator {

    public SMSDecorator(Notifier wrappee) {
        super(wrappee);
    }

    @Override
    public void send(String message) {
        super.send(message);
        sendSMS(message);
    }

    private void sendSMS(String message) {
        System.out.println("Enviando notificacion mediante SMS: " + message);
    }

}

class FacebookDecorator extends BaseDecorator {

    public FacebookDecorator(Notifier wrappee) {
        super(wrappee);
    }

    @Override
    public void send(String message) {
        super.send(message);
        sendFacebook(message);
    }

    private void sendFacebook(String message) {
        System.out.println("Enviando notificación mediante Facebook: " + message);
    }

}

class SlackDecorator extends BaseDecorator {

    public SlackDecorator(Notifier wrappee) {
        super(wrappee);
    }

    @Override
    public void send(String message) {
        super.send(message);
        sendSlack(message);
    }

    private void sendSlack(String message) {
        System.out.println("Enviando notificación mediante Slack: " + message);
    }

}
