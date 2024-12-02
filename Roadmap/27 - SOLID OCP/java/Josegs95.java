public class Josegs95 {
    public static void main(String[] args) {
        //Ejercicio
        //Forma incorrecta
        Object object1 = new WrongHuman();
        if (object1 instanceof WrongHuman)
            System.out.println("Los humanos se mueven a dos patas");
        else if (object1 instanceof WrongCat)
            System.out.println("Los gatos se mueven a cuatro patas");
        else if (object1 instanceof WrongPigeon)
            System.out.println("Las palomas se mueven por el aire volando");
        else
            System.out.println("Animal desconocido");

        //Forma correcta
        Object object2 = new Cat();
        if (object2 instanceof Animal)
            ((Animal) object2).move();
        else
            System.out.println("Animal desconocido");

        //Reto
        retoFinal();
    }

    public static void retoFinal(){
        double result = Calculator.calculate(Calculator.Operations.SUMAR, 7, 8);
        System.out.println("7 + 8 = " + result);

        result = Calculator.calculate(Calculator.Operations.RESTAR, 1, 2.5);
        System.out.println("1 - 2.5 = " + result);

        result = Calculator.calculate(Calculator.Operations.MULTIPLICAR, 1.3, 4.6);
        System.out.println("1.3 * 4.6 = " + result);

        result = Calculator.calculate(Calculator.Operations.DIVIDIR, 2, 1.5);
        System.out.println("2 / 1.5 = " + result);

        result = Calculator.calculate(Calculator.Operations.POTENCIA, 5, 5);
        System.out.println("5 ^ 5 = " + result);
    }

    public static class WrongHuman{}
    public static class WrongCat{}
    public static class WrongPigeon {}

    public interface Animal{
        public void move();
    }
    public static class Human implements Animal{
        public void move(){
            System.out.println("Los humanos se mueven a dos patas");
        }
    }
    public static class Cat implements Animal{
        public void move(){
            System.out.println("Los gatos se mueven a cuatro patas");
        }
    }
    public static class Pigeon implements Animal{
        public void move(){
            System.out.println("Las palomas se mueven por el aire volando");
        }
    }

    public class Calculator{
        public enum Operations{
            SUMAR(new Sum()),
            RESTAR(new Subtract()),
            MULTIPLICAR(new Multiply()),
            DIVIDIR(new Divide()),
            POTENCIA(new Power());

            private Operation operation;

            Operations (Operation operation){
                this.operation = operation;
            }

            public Operation getOperation(){
                return operation;
            }

        }

        public static double calculate(Operations operation, double n1, double n2){
            return operation.getOperation().execute(n1, n2);
        }

    }
    public interface Operation{
        public double execute(double n1, double n2);
    }
    public static class Sum implements Operation{

        public double execute(double n1, double n2) {
            return n1 + n2;
        }
    }
    public static class Subtract implements Operation{

        @Override
        public double execute(double n1, double n2) {
            return n1 - n2;
        }
    }
    public static class Multiply implements Operation{

        @Override
        public double execute(double n1, double n2) {
            return n1 * n2;
        }
    }
    public static class Divide implements Operation{

        @Override
        public double execute(double n1, double n2) {
            return n1 / n2;
        }
    }
    public static class Power implements Operation{

        @Override
        public double execute(double n1, double n2) {
            double result = 1;
            for (int i = 0; i < n2; i++)
                result *= n1;
            return result;
        }
    }
}
