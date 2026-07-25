public class Josegs95 {
    public static void main(String[] args) {
        //Ejercicio
        //En java es un poco engorroso los decoradores porque necesitas muchas clases
        //e interfaces para implementar el patrón de diseño
        Interface instance1 = new DefaultImplClass();
        System.out.println(instance1.getString());

        Interface instance2 = new Decorator(new DefaultImplClass());
        System.out.println(instance2.getString());

        //Reto
        retoFinal();
    }

    public static void retoFinal(){
        //Voy a reutilizar la interfaz y las clases usadas en el ejercicio para evitar
        //crear demasiado código "dummy"
        Interface instance = new ChallengeDecorator(new DefaultImplClass());

        System.out.println("Veces que se ha llamado a 'getString()': " + ((ChallengeDecorator)instance).getCounter());
        instance.getString();
        instance.getString();
        instance.getString();
        System.out.println("Veces que se ha llamado a 'getString()': " + ((ChallengeDecorator)instance).getCounter());
    }

    public interface Interface{
        String getString();
    }

    public static class DefaultImplClass implements Interface{
        @Override
        public String getString() {
            return "Cadena por defecto";
        }
    }

    public static abstract class BaseDecorator implements Interface{
        private Interface interfaceInstance;

        public BaseDecorator(Interface interfaceInstance) {
            this.interfaceInstance = interfaceInstance;
        }

        @Override
        public String getString() {
            return interfaceInstance.getString();
        }
    }

    public static class Decorator extends BaseDecorator{
        public Decorator(Interface interfaceInstance) {
            super(interfaceInstance);
        }

        @Override
        public String getString() {
            return super.getString() + ", mas la cadena del decorador";
        }
    }

    public static class ChallengeDecorator extends BaseDecorator{

        private int counter;

        public ChallengeDecorator(Interface interfaceInstance) {
            super(interfaceInstance);
            counter = 0;
        }

        @Override
        public String getString() {
            counter++;
            return super.getString();
        }

        public int getCounter() {
            return counter;
        }
    }
}
