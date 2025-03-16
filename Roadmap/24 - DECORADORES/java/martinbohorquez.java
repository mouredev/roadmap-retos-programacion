/*
 * #24 PATRONES DE DISEÑO: DECORADORES
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    public static void main(String[] args) {
        Component component = new ConcreteComponent();
        Component smsConcreteDecorated = new SmsDecorator(component);
        Component facebookConcreteDecorated = new FacebookDecorator(component);
        component.notification();
        smsConcreteDecorated.notification();
        facebookConcreteDecorated.notification();

        /*
         * DIFICULTAD EXTRA
         */
        ComponentExtra componente = new ConcreteComponentExtra();
        CountDecorator contadorDecorador = new CountDecorator(componente);

        contadorDecorador.operation();
        contadorDecorador.operation();
        contadorDecorador.operation();

        System.out.printf("Total de invocaciones: %s%n", contadorDecorador.getContador());
    }

    //Interfaz base
    interface Component {
        void notification();
    }

    //Componente concreto
    static class ConcreteComponent implements Component {
        @Override
        public void notification() {
            System.out.println("Notificación por defecto!");
        }
    }

    //Decorador abstracto
    abstract static class Decorator implements Component {
        private final Component component;

        private Decorator(Component component) {
            this.component = component;
        }

        public void notification() {
            this.component.notification();
            System.out.printf("Notificación por %s!%n", this.getClass().getSimpleName());
        }
    }

    //Decorador concreto que añade funcionalidad
    static class SmsDecorator extends Decorator {
        private SmsDecorator(Component component) {
            super(component);
        }

        @Override
        public void notification() {
            super.notification();
            addFunctionality();
        }

        private void addFunctionality() {
            System.out.printf("Funcionalidad adicional de %s!%n", this.getClass().getSimpleName());
        }
    }

    //Decorador concreto que añade funcionalidad
    static class FacebookDecorator extends Decorator {
        private FacebookDecorator(Component component) {
            super(component);
        }

        @Override
        public void notification() {
            super.notification();
            addFunctionality();
        }

        private void addFunctionality() {
            System.out.printf("Funcionalidad adicional de %s!%n", this.getClass().getSimpleName());
        }
    }

    // DIFICULTAD EXTRA
    interface ComponentExtra {
        void operation();
    }

    //Componente concreto
    static class ConcreteComponentExtra implements ComponentExtra {
        @Override
        public void operation() {
            System.out.println("Ejecutando operación base!");
        }
    }

    //Decorador abstracto
    abstract static class DecoratorExtra implements ComponentExtra {
        private final ComponentExtra component;

        private DecoratorExtra(ComponentExtra component) {
            this.component = component;
        }

        public void operation() {
            this.component.operation();
        }
    }

    // Decorador concreto que cuenta las veces que se llama a la operación
    static class CountDecorator extends DecoratorExtra {
        private int contador = 0;

        private CountDecorator(ComponentExtra component) {
            super(component);
        }

        @Override
        public void operation() {
            System.out.println("La operación se ha llamado " + ++contador + " vez/veces.");
            super.operation();
        }

        private int getContador() {
            return contador;
        }
    }
}




