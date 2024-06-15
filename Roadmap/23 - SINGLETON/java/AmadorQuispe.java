

public class Main {
    public static void main(String[] args) {
        String singleton1 = Singleton.getInstance();
        String singleton2 = Singleton.getInstance();
        //Hace refencia a la misma memoria
        System.out.println(singleton1 == singleton2);

        Thread thread1 = new Thread(()->{
            SessionUser sessionUser1 = SessionUser.getInstance("0001","user1","user1","user1@gmail.com");
            System.out.println(sessionUser1.getEmail());
        });
        thread1.start();

        //main thread
        SessionUser sessionUser = SessionUser.getInstance("0002","aquispe","Amador","aquispe@gmail.com");
        System.out.println(sessionUser.getEmail());

        Thread thread2 = new Thread(()->{
            SessionUser sessionUser1 = SessionUser.getInstance("0003","user3","user3","user3@gmail.com");
            System.out.println(sessionUser1.getEmail());
        });
        thread2.start();

    }
}

class Singleton {
    private static String name;

    private Singleton(){
        name = "clase singleton";
    }

    public static String getInstance(){
        return name == null ? "clase singleton" : name;
    }
}

class SessionUser{
    private final String id;
    private final String userName;
    private final String name;
    private final String email;
    private static SessionUser instance;

    private SessionUser(String id, String username, String name, String email) {
         this.id = id;
         this.userName = username;
         this.name = name;
         this.email = email;
    }

    //Synchronized, sincroniza la creación en concurrente.
    public static synchronized SessionUser getInstance(String id, String username, String name, String email) {
        if (instance == null) instance = new SessionUser(id, username, name, email);
        return instance;
    }

    public String getId() {
        return id;
    }

    public String getUserName() {
        return userName;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }
}
