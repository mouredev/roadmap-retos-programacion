public class danhingar {

    public static void main(String[] args) {
        // Definición de singleton como clase
        SinglentonClass singlentonClass1 = SinglentonClass.getInstance();
        System.out.println(singlentonClass1.hashCode());

        SinglentonClass singlentonClass2 = SinglentonClass.getInstance();
        System.out.println(singlentonClass2.hashCode());

        System.out.println(singlentonClass1 == singlentonClass2);

        // Definición de singleton como enumerado
        SinglentonEnum singlentonEnum1 = SinglentonEnum.INSTANCE.getInstance();
        System.out.println(singlentonEnum1.hashCode());

        SinglentonEnum singlentonEnum2 = SinglentonEnum.INSTANCE.getInstance();
        System.out.println(singlentonEnum2.hashCode());

        System.out.println(singlentonEnum1 == singlentonEnum2);

        // Extra
        UserSession userSession1 = UserSession.getInstance();
        userSession1.login(1, "user1", "Pepe", "pepe@gmail.com");
        System.out.println(userSession1.toString());

        UserSession userSession2 = UserSession.getInstance();
        System.out.println(userSession2.toString());

        UserSession userSession3 = UserSession.getInstance();
        userSession3.logout();
        System.out.println(userSession3.toString());
        System.out.println(userSession2.toString());
        System.out.println(userSession1.toString());

        UserSessionEnum userSession4 = UserSessionEnum.INSTANCE.getInstance();
        userSession4.login(2, "user2", "Juan", "juan@gmail.com");

        System.out.println("Session 4"+userSession4.toString());

        UserSessionEnum userSession5 = UserSessionEnum.INSTANCE.getInstance();
        userSession4.login(3, "user3", "Mateo", "mateo@gmail.com");
        System.out.println("Session 4"+userSession4.toString());
        System.out.println("Session 5"+userSession5.toString());

        UserSessionEnum userSession6 = UserSessionEnum.INSTANCE.getInstance();
        userSession6.logout();
        System.out.println("Session 4"+userSession4.toString());
        System.out.println("Session 5"+userSession5.toString());
        System.out.println("Session 6"+userSession6.toString());
    }

}

class SinglentonClass {

    private static SinglentonClass INSTANCE;

    private SinglentonClass() {

    }

    public static SinglentonClass getInstance() {
        if (INSTANCE == null) {
            INSTANCE = new SinglentonClass();
        }

        return INSTANCE;
    }
}

enum SinglentonEnum {
    INSTANCE();

    public SinglentonEnum getInstance() {
        return INSTANCE;
    }

    private SinglentonEnum() {
    }

}

// EXTRA
class UserSession {
    private static UserSession INSTANCE;
    private Integer id;
    private String username;
    private String name;
    private String email;

    private UserSession() {
    }

    public static UserSession getInstance() {
        if (INSTANCE == null) {
            INSTANCE = new UserSession();
        }

        return INSTANCE;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void login(Integer id, String username, String name, String email) {
        this.id = id;
        this.username = username;
        this.name = name;
        this.email = email;
    }

    @Override
    public String toString() {
        return "Session [id=" + id + ", username=" + username + ", name=" + name + ", email=" + email + "]";
    }

    public void logout() {
        this.id = null;
        this.username = null;
        this.name = null;
        this.email = null;
    }

}

enum UserSessionEnum {
    INSTANCE();

    private Integer id;
    private String username;
    private String name;
    private String email;

    public UserSessionEnum getInstance() {
        return INSTANCE;
    }

    private UserSessionEnum() {
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String toString() {
        return " [id=" + id + ", username=" + username + ", name=" + name + ", email=" + email + "]";
    }
    
    public void logout() {
        this.id = null;
        this.username = null;
        this.name = null;
        this.email = null;
    }

    public void login(Integer id, String username, String name, String email) {
        this.id = id;
        this.username = username;
        this.name = name;
        this.email = email;
    }

}