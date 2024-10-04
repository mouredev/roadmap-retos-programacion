public class simonguzman {
    public static void main(String[] args) {
        exampleDIP();
    }
    /*********************************** Ejercicio adicional sin DIP ***********************************/

    /*********************************** Ejercicio adicional sin DIP ***********************************/

    /*********************************** Ejemplo con DIP ***********************************/
    static void exampleDIP(){
        MessageSender emailSender = new EmailSender();
        NotificationService notificationService = new NotificationService(emailSender);
        notificationService.notifyUser("Tu cuenta ha sido activada.");

        MessageSender smsSender = new SMSSender();
        notificationService = new NotificationService(smsSender);
        notificationService.notifyUser("Tu código de verificación es 1234.");
    }
    static interface MessageSender {
        void sendMessage(String message);
    }

    static class EmailSender implements MessageSender {
        @Override
        public void sendMessage(String message) {
            System.out.println("Enviando email: " + message);
        }
    }

    static class SMSSender implements MessageSender {
        @Override
        public void sendMessage(String message) {
            System.out.println("Enviando SMS: " + message);
        }
    }

    static class NotificationService {
        private MessageSender messageSender;

        public NotificationService(MessageSender messageSender) {
            this.messageSender = messageSender;
        }

        public void notifyUser(String message) {
            messageSender.sendMessage(message);
        }
    }

    /*********************************** Ejemplo sin DIP ***********************************/
}
