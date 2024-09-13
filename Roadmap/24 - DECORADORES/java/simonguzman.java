
import java.util.HashMap;
import java.util.Map;



public class simonguzman {
    public  static void main(String[] args) {
        genericExample();
        example();
        adittionalExercise();
    }

    /***************************** Ejercicio adicional*****************************/

    static void adittionalExercise(){
        ComponentExtra componente = new ConcreteComponentExtra();
        CountDecorator contadorDecorador = new CountDecorator(componente);

        contadorDecorador.operation();  
        contadorDecorador.operation();  
        contadorDecorador.operation();  

        System.out.println("Total de invocaciones: " + contadorDecorador.getContador());
    }
    static interface ComponentExtra{
        void operation();
    }

    //Componente concreto
    static class ConcreteComponentExtra implements ComponentExtra{
        @Override
        public void operation() {
            System.out.println("Ejecutando operacion base...");
        }
    }

    //Decorador abstracto
    static abstract class DecoratorExtra implements ComponentExtra{
        protected ComponentExtra component;

        public DecoratorExtra(ComponentExtra component){
            this.component = component;
        }

        public void operation() {
            this.component.operation();
        }
    }
    // Decorador concreto que cuenta las veces que se llama a la operación
    static class CountDecorator extends DecoratorExtra {
        private int contador = 0;
    
        public CountDecorator(ComponentExtra component) {
            super(component);
        }
    
        @Override
        public void operation() {
            contador++;
            System.out.println("La operación se ha llamado " + contador + " veces.");
            super.operation();
        }
    
        public int getContador() {
            return contador;
        }
    }

    /***************************** Ejemplo de implemetacion mas complejo *****************************/
    /*Se realizo un ejemplo adicional para mostrar mejor y poner en practica la sintaxis
     * del patron decorador, en el cual se busco simular lo que seria un login de una cuenta
     * de un usuario, con sus respectivas validaciones
     */
    static void example(){

        //Simulacion de inicio de sesion.
        UserService userService = new LoginAttemptsDecorator(new BasicUserService(), 3);
        userService.login("user1", "password");
        userService.login("user1", "wrongpassword");
        userService.login("user1", "wrongpassword");
        userService.login("user1", "wrongpassword");
        userService.login("user1", "wrongpassword");
    }
    //Interfaz base del servicio de usuario
    static interface UserService{
        boolean login(String username, String password);
    }

    //implementacion basica del servicio de usuario
    static class BasicUserService implements UserService{
        private Map<String, String> userDatabase = new HashMap<>();

        public BasicUserService(){
            //Simulacion de una base de datos de usuarios
            userDatabase.put("user1", "password");
            userDatabase.put("user2", "12345");
        }

        @Override
        public boolean login(String username, String password){
            String storedPassword = userDatabase.get(username);
            if(storedPassword != null && storedPassword.equals(password)){
                System.out.println("Inicio de sesion exitoso para "+username);
                return true;
            }else{
                System.out.println("Credenciales incorrectas para "+username);
                return false;
            }
        }
    }

    //Decorador para contar los intentos de inicio de sesion
    static class LoginAttemptsDecorator implements UserService{
        private UserService userService;
        private Map<String, Integer> loginAttempts;
        private int maxAttempts;

        public LoginAttemptsDecorator(UserService userService, int maxAttempts) {
            this.userService = userService;
            this.maxAttempts = maxAttempts;
            this.loginAttempts = new HashMap<>();
        }

        @Override
        public boolean login(String username, String password) {
            if(loginAttempts.getOrDefault(username, 0) >= maxAttempts){
                System.out.println("Cuenta bloqueada para "+username+" por exceder los intentos permitidos");
                return false;
            }

            boolean success = userService.login(username, password);
            if(!success){
                loginAttempts.put(username, loginAttempts.getOrDefault(username, 0)+1);
                System.out.println("Intentos fallidos para "+username+":" + loginAttempts.get(username));
            }else{
                loginAttempts.put(username, 0);
            }
            return success;
        }
        
    }

    /***************************** Ejemplo generico *****************************/
    static void genericExample(){
        Component component = new ConcreteComponent();
        Component decorated = new ConcreteDecorator(component);
        decorated.operation();
    }
    
    //Interfaz base
    static interface Component{
        void operation();
    }

    //Componente concreto
    static class ConcreteComponent implements Component{
        @Override
        public void operation() {
            System.out.println("Ejecutando operacion base...");
        }
    }

    //Decorador abstracto
    static abstract class Decorator implements Component{
        protected Component component;

        public Decorator(Component component){
            this.component = component;
        }

        public void operation() {
            this.component.operation();
        }
    }

    //Decorador concreto que añade funcionalidad
    static class ConcreteDecorator extends Decorator{
        public ConcreteDecorator(Component component){
            super(component);
        }

        @Override
        public void operation() {
            super.operation();
            addFunctionality();
        }

        private void addFunctionality(){
            System.out.println("Funcionalidad adicional del decorador.");
        }
    }
}
