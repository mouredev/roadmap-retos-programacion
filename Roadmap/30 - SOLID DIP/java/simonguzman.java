public class simonguzman {
    public static void main(String[] args) {
        exampleDIP();
        exampleNoDIP();
        adittionalExerciseNoDIP();
        adittionalExerciseDIP();
    }
    /*********************************** Ejercicio adicional con DIP ***********************************/
    static void adittionalExerciseDIP(){
        Notification emailNotification = new EmailNotification();
        NotificationService emailService = new NotificationService(emailNotification);
        emailService.sendNotification("Este es un email");

        Notification smsNotification = new SMSNotification();
        NotificationService smsService = new NotificationService(smsNotification);
        smsService.sendNotification("Este es un SMS");

        Notification pushNotification = new PushNotification();
        NotificationService pushService = new NotificationService(pushNotification);
        pushService.sendNotification("Esta es una notificación PUSH");
    }
    static interface Notification {
        void send(String message);
    }
    static class EmailNotification implements Notification {
        @Override
        public void send(String message) {
            System.out.println("Enviando email con mensaje: " + message);
        }
    }

    static class SMSNotification implements Notification {
        @Override
        public void send(String message) {
            System.out.println("Enviando SMS con mensaje: " + message);
        }
    }

    static class PushNotification implements Notification {
        @Override
        public void send(String message) {
            System.out.println("Enviando notificación PUSH con mensaje: " + message);
        }
    }

    static class NotificationService {
        private Notification notification;

        public NotificationService(Notification notification) {
            this.notification = notification;
        }

        public void sendNotification(String message) {
            notification.send(message);
        }
    }
    /*********************************** Ejercicio adicional sin DIP ***********************************/
    static void adittionalExerciseNoDIP(){
        NotificationServiceNoDIP service = new NotificationServiceNoDIP();
        service.sendEmailNotification("Este es un email");
        service.sendSMSNotification("Este es un SMS");
    }
    static class EmailNotificationNoDIP {
        public void sendEmail(String message) {
            System.out.println("Enviando email con mensaje: " + message);
        }
    }

    static class SMSNotificationNoDIP {
        public void sendSMS(String message) {
            System.out.println("Enviando SMS con mensaje: " + message);
        }
    }

    static class NotificationServiceNoDIP {
        private EmailNotificationNoDIP emailNotification = new EmailNotificationNoDIP();
        private SMSNotificationNoDIP smsNotification = new SMSNotificationNoDIP();

        public void sendEmailNotification(String message) {
            emailNotification.sendEmail(message);
        }

        public void sendSMSNotification(String message) {
            smsNotification.sendSMS(message);
        }
    }

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
        NotificationServiceNotDIP notificationService = new NotificationServiceNotDIP();
        notificationService.notifyUser("Tu cuenta ha sido activada.");
    }
    static class EmailSender {
        public void sendEmail(String message) {
            System.out.println("Enviando email: " + message);
        }
    }

    static class NotificationServiceNotDIP {
        private EmailSender emailSender = new EmailSender();  // Dependencia concreta

        public void notifyUser(String message) {
            emailSender.sendEmail(message);
        }
    }


}
