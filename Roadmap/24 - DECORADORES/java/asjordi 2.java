/**
 * En Java se puede implementar el concepto de decorador utilizando el patrón de diseño Decorator.
 * Decorator es un patrón de diseño estructural que permite añadir funcionalidades a objetos
 * colocando estos objetos dentro de objetos encapsuladores especiales que contienen estas funcionalidades.
 * Más información en: https://refactoring.guru/es/design-patterns/decorator
 */
public class Main {

    public static void main(String[] args) {

        Car sportsCar = new SportsCar(new BasicCar());
        sportsCar.assemble();

        BaseFunction baseFunction = new BaseFunction();
        CountingFunctionDecorator decorator = new CountingFunctionDecorator(baseFunction);
        decorator.call();
        System.out.println("Function called " + decorator.getCount() + " times");
    }

    /**
     * EJERCICIO:
     * Explora el concepto de "decorador" y muestra cómo crearlo
     * con un ejemplo genérico.
     */

    // Interfaz que define el comportamiento de un coche
    public interface Car {
        void assemble();
    }

    // Implementación básica de un coche
    public static class BasicCar implements Car {
        @Override
        public void assemble() {
            System.out.println("Basic Car!");
        }
    }

    // Decorador con referencia a un coche
    public abstract static class CarDecorator implements Car {
        protected Car car;

        protected CarDecorator(Car c){
            this.car=c;
        }

        public void assemble(){
            this.car.assemble();
        }
    }

    // Decorador que añade funcionalidades de un coche deportivo
    public static class SportsCar extends CarDecorator {
        public SportsCar(Car c) {
            super(c);
        }

        public void assemble(){
            super.assemble();
            System.out.println("Adding features of Sports Car.");
        }
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Crea un decorador que sea capaz de contabilizar cuántas veces
     * se ha llamado a una función y aplícalo a una función de tu elección.
     */

    // Interfaz para la función
    public interface Function {
        void call();
    }

    // Implementación base de la función
    public static class BaseFunction implements Function {
        @Override
        public void call() {
            System.out.println("Base function called");
        }
    }

    // Decorador que agrega la funcionalidad de contabilizar las llamadas
    public static class CountingFunctionDecorator implements Function {
        private Function baseFunction;
        private Integer count = 0;

        public CountingFunctionDecorator(Function baseFunction) {
            this.baseFunction = baseFunction;
        }

        @Override
        public void call() {
            count++;
            baseFunction.call();
        }

        public Integer getCount() {
            return this.count;
        }
    }
}
