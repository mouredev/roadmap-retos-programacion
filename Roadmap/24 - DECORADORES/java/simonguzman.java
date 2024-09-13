

public class simonguzman {
    public  static void main(String[] args) {
        genericExample();
    }


    /***************************** Ejemplo generico *****************************/

    static void genericExample(){
        Component component = new ConcreteComponent();
        Component decorated = new ConcreteDecorator(component);
        decorated.operation();
    }
    static interface Component{
        void operation();
    }

    static class ConcreteComponent implements Component{
        @Override
        public void operation() {
            System.out.println("Ejecutando operacion base...");
        }
    }

    static abstract class Decorator implements Component{
        protected Component component;

        public Decorator(Component component){
            this.component = component;
        }

        public void operation() {
            this.component.operation();
        }
    }

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
