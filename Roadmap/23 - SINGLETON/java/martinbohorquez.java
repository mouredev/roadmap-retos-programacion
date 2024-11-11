public class martinbohorquez {
    public static void main(String[] args) {
        Singleton singleton = Singleton.getInstance();
        Singleton.message();
        singleton.message();
        Singleton.message();

        /*
         * DIFICULTAD EXTRA
         */

        UserSession session = UserSession.getUserInstance();
        session.assignUser("1", "Martin Bohorquez", "mbohorquez", "mbohorquez@gmail.com");
        System.out.printf("Usuario: %s, instancia Singleton: %s%n", session.getUserData(), session);
        session.deleteSession();
        System.out.printf("Usuario: %s, instancia Singleton: %s%n", session.getUserData(), session);


    }

    private static class Singleton {
        private static Singleton instance;

        private Singleton() {
        }

        public static Singleton getInstance() {
            instance = (instance == null) ? new Singleton() : instance;
            return instance;
        }

        public static void message() {
            System.out.printf("Soy un Singleton: %s%n", instance);
        }
    }

    private static class UserSession {
        private static UserSession instance;

        private String id;
        private String name;
        private String userName;
        private String email;

        private UserSession() {
        }

        public static UserSession getUserInstance() {
            instance = (instance == null) ? new UserSession() : instance;
            return instance;
        }

        public void assignUser(String id, String name, String userName, String email) {
            this.id = id;
            this.name = name;
            this.userName = userName;
            this.email = email;
        }

        public String getUserData() {
            return "{id='" + id + "', name='" + name + "', userName='" + userName + "', email='" + email + "'}";
        }

        public void deleteSession() {
            id = null;
            name = null;
            userName = null;
            email = null;
        }
    }
}
