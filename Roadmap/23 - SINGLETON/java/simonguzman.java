public class simonguzman {
    public static void main(String[] args) {
        genericSingleton();
    }

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
