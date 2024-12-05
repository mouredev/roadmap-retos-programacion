public class Josegs95 {
    public static void main(String[] args) {
        //Ejericio
        //Forma incorrecta
        WrongLaptop laptop1 = new WrongLaptop(new ExternalBattery());
        laptop1.charge();

        //Forma correcta
        Laptop laptop2 = new Laptop(new ExternalBattery());
        laptop2.charge();

        laptop2 = new Laptop(new InternalBattery());
        laptop2.charge();

        //Reto
        new Josegs95().retoFinal();
    }

    public void retoFinal(){
        Notification notification = new Notification();
        notification.sendNotification("Jose", "Hola", new Email());
        notification.sendNotification("Laura", "Buenas tardes", new PUSH());
        notification.sendNotification("Yolanda", "Adios", new SMS());
    }

    //Forma incorrecta
    public static class WrongLaptop {
        private ExternalBattery battery;
        public WrongLaptop(ExternalBattery battery){
            this.battery = battery;
        }

        public void charge(){
            battery.charge();
        }
    }
    //Forma correcta
    public interface Battery{
        public void charge();
    }
    public static class ExternalBattery implements Battery{
        @Override
        public void charge(){
            System.out.println("La batería se carga mediante un transformador");
        }
    }
    public static class InternalBattery implements Battery{

        @Override
        public void charge() {
            System.out.println("La batería se carga sin necesidad de un transformador");
        }
    }
    public static class Laptop{
        private Battery battery;

        public Laptop(Battery battery){
            this.battery = battery;
        }

        public void charge(){
            battery.charge();
        }
    }
    //Reto
    public interface MessageSender{
        public void send(String recipient, String text);
    }
    public class Email implements MessageSender{
        @Override
        public void send(String recipient, String text) {
            System.out.println("\"" + text + "\" enviado por email a " + recipient);
        }
    }
    public class PUSH implements MessageSender{
        @Override
        public void send(String recipient, String text) {
            System.out.println("\"" + text + "\" enviado por push a " + recipient);
        }
    }
    public class SMS implements MessageSender{
        @Override
        public void send(String recipient, String text) {
            System.out.println("\"" + text + "\" enviado por SMS a " + recipient);
        }
    }
    public class Notification{
        public void sendNotification(String recipient, String text, MessageSender sender){
            sender.send(recipient, text);
        }
    }
}
