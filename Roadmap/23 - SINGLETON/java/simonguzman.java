
public class simonguzman {
    public static void main(String[] args) {
        genericSingleton();
        additionalExercise();
    }
    /**************************** Ejercicio adicional ****************************/
    public static void additionalExercise(){
        UserSession session = UserSession.getUserInstance();
        session.assignUser("001", "Simon Guzman", "sguzman", "sguzman@hotmail.com");
        System.out.println(session.getUserData());
        session.deleteSession();
        System.out.println(session.getClass());
    }

    public static class UserSession{
        private static UserSession instance;

        private String id;
        private String name;
        private String userName;
        private String email;

        private UserSession(){

        }

        public static UserSession getUserInstance(){
            if(instance == null){
                instance = new UserSession();
            }
            return instance;
        }

        public void assignUser(String id, String name, String userName, String email){
            this.id = id;
            this.name = name;
            this.userName = userName;
            this.email = email;
        }

        public String getUserData(){
            if (id == null){
                return "No hay usuarios en la sesion";
            }
            return "ID: "+id+" ,username: " + userName + " ,name: " + name + " ,email: " + email;
        }

        public void deleteSession(){
            id = null;
            name = null;
            userName = null;
            email = null;
        }
    }

    /**************************** Ejemplo de singleton ****************************/
    public static void genericSingleton(){
        Singleton singleton = Singleton.getInstance();
        singleton.showMessage();
    }

    public static class Singleton{
        private static Singleton instance;

        private Singleton(){

        }

        public static Singleton getInstance(){
            if(instance == null){
                instance = new Singleton();
            }
            return instance;
        }

        public static void showMessage(){
            System.out.println("Soy un Singleton.");
        }
    }
}
