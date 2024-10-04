public class simonguzman {
    public static void main(String[] args) {
        exampleDIP();
        exampleNoDIP();
    }
    /*********************************** Ejercicio adicional sin DIP ***********************************/

    /*********************************** Ejercicio adicional sin DIP ***********************************/

    /*********************************** Ejemplo con DIP ***********************************/
    static void exampleDIP(){
        MessageSender emailSender = new EmailSenderDIP();
        NotificationServiceDIP notificationService = new NotificationServiceDIP(emailSender);
        notificationService.notifyUser("Tu cuenta ha sido activada.");

        MessageSender smsSender = new SMSSenderDIP();
        notificationService = new NotificationServiceDIP(smsSender);
        notificationService.notifyUser("Tu código de verificación es 1234.");
    }
    static interface MessageSender {
        void sendMessage(String message);
    }

    static class EmailSenderDIP implements MessageSender {
        @Override
        public void sendMessage(String message) {
            System.out.println("Enviando email: " + message);
        }
    }

    static class SMSSenderDIP implements MessageSender {
        @Override
        public void sendMessage(String message) {
            System.out.println("Enviando SMS: " + message);
        }
    }

    static class NotificationServiceDIP {
        private MessageSender messageSender;

        public NotificationServiceDIP(MessageSender messageSender) {
            this.messageSender = messageSender;
        }

        public void notifyUser(String message) {
            messageSender.sendMessage(message);
        }
    }

    /*********************************** Ejemplo sin DIP ***********************************/
    static void exampleNoDIP(){
        NotificationService notificationService = new NotificationService();
        notificationService.notifyUser("Tu cuenta ha sido activada.");
    }
    static class EmailSender {
        public void sendEmail(String message) {
            System.out.println("Enviando email: " + message);
        }
    }

    static class NotificationService {
        private EmailSender emailSender = new EmailSender();  // Dependencia concreta

        public void notifyUser(String message) {
            emailSender.sendEmail(message);
        }
    }


}
