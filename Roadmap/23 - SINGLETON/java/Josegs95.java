public class Josegs95 {
    public static void main(String[] args) {
        //Ejercicio
        Singleton s1 = Singleton.getInstance("1");
        Singleton s2 = Singleton.getInstance("2");

        System.out.println("Si tienen el mismo 'id', es la misma instancia:");
        System.out.println(s1.getId());
        System.out.println(s2.getId());

        //Reto
        retoFinal();
    }

    public static void retoFinal(){
        Session session1 = Session.getInstance();
        session1.setUser("1", "Josegs95", "Jose", "user@mail.com");

        System.out.println(session1);

        Session session2 = Session.getInstance();

        System.out.println(session2);

        session2.clear();

        System.out.println(session1);
    }

    public static class Singleton{
        private static Singleton instance;
        private String id;

        private Singleton(String id){
            this.id = id;
        }

        public static Singleton getInstance(String id){
            if (instance == null)
                instance = new Singleton(id);
            return instance;
        }

        public String getId(){
            return id;
        }
    }

    public static class Session{
        private static Session session;
        private String id;
        private String username;
        private String name;
        private String email;

        private Session() {}

        public static Session getInstance(){
            if (session == null)
                session = new Session();
            return session;
        }

        public void setUser(String id, String username, String name, String email){
            this.id = id;
            this.username = username;
            this.name = name;
            this.email = email;
        }

        public String getId() {
            return id;
        }

        public String getUsername() {
            return username;
        }

        public String getName() {
            return name;
        }

        public String getEmail() {
            return email;
        }

        public void clear(){
            id = null;
            username = null;
            name = null;
            email = null;
        }

        @Override
        public String toString() {
            return "[" + id + ", " + username + ", " + name + ", " + email + "]";
        }
    }
}
