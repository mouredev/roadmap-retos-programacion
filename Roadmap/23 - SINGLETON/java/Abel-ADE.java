public class Main {                                                                                                                                               
                                                                                                                                                                  
    /**                                                                                                                                                           
     * Singleton es un patrón de diseño creacional que permite tener una instancia de una clase o variable,                                                       
     * al tiempo que proporciona un punto de acceso global a esta instancia.                                                                                      
     */                                                                                                                                                           
                                                                                                                                                                  
    //Tenemos una variable global, que para acceder a ella se deberá usar el método get.                                                                          
    private static String singleton;                                                                                                                               
                                                                                                                                                                  
    //Crea una instancia si no existe y funciona cómo punto de acceso global.                                                                                     
    public static String getSingleton() {                                                                                                                          
        if (singleton == null) {                                                                                                                                  
            singleton = "singleton";                                                                                                                              
        }                                                                                                                                                         
        return singleton;                                                                                                                                         
    }                                                                                                                                                             
                                                                                                                                                                  
    public static void main(String[] args) {                                                                                                                      
        //Usamos nuestro singleton.                                                                                                                               
        System.out.println(getSingleton()+"\n");                                                                                                                  
                                                                                                                                                                  
        //DIFICULTAD EXTRA (opcional):                                                                                                                            
        User sesionUser = Sesion.getUser();                                                                                                                       
                                                                                                                                                                  
        System.out.println("Iniciando sesión...\n");                                                                                                              
                                                                                                                                                                  
        System.out.println("ID: "+ sesionUser.getId());                                                                                                           
        System.out.println("Nombre de usuario: "+ sesionUser.getUserName());                                                                                      
        System.out.println("Nombre: "+ sesionUser.getName());                                                                                                     
        System.out.println("Correo: "+ sesionUser.getEmail());                                                                                                    
                                                                                                                                                                  
        Sesion.removeUser();                                                                                                                                      
                                                                                                                                                                  
        System.out.println("\nSesión eliminada");                                                                                                                 
    }                                                                                                                                                             
}                                                                                                                                                                 
                                                                                                                                                                  
class Sesion {                                                                                                                                                     
    //Atributo singleton                                                                                                                                          
    private static User user;                                                                                                                                      
                                                                                                                                                                  
    //Método que nos devuelve una instancia única                                                                                                                 
    public static User getUser() {                                                                                                                                 
        if (user == null) {                                                                                                                                       
            user = new User(1, "Abel-ADE", "Abel", "Abel-ADE@correo.es");                                                                                         
        }                                                                                                                                                         
        return user;                                                                                                                                              
    }                                                                                                                                                             
                                                                                                                                                                  
    // Método que elimina los datos de la sesión                                                                                                                  
    public static void removeUser() {                                                                                                                              
        if (user != null) {                                                                                                                                       
            user = null;                                                                                                                                          
        }                                                                                                                                                         
    }                                                                                                                                                             
}                                                                                                                                                                 
                                                                                                                                                                  
class User {                                                                                                                                                       
    //Atributos de un usuario                                                                                                                                     
    private int id;                                                                                                                                                
    private String userName;                                                                                                                                       
    private String name;                                                                                                                                           
    private String email;                                                                                                                                          
                                                                                                                                                                  
    //Métodos get y set para sus atributos                                                                                                                        
    public int getId() {                                                                                                                                           
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
                                                                                                                                                                  
    //Constructor                                                                                                                                                 
    public User(int id, String userName, String name, String email) {                                                                                              
        this.id = id;                                                                                                                                             
        this.userName = userName;                                                                                                                                 
        this.name = name;                                                                                                                                         
        this.email = email;                                                                                                                                       
    }                                                                                                                                                             
}                                                                                                                                                                 
