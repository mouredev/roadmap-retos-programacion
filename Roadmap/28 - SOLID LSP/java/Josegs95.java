import java.util.Random;

public class Josegs95 {
    public static void main(String[] args) {
        //Ejercicio
        //Forma incorrecta
        WrongAnimal animal1 = new WrongAnimal();
        WrongAnimal snake1 = new WrongSnake();
        WrongAnimal tiger1 = new WrongTiger();

        animal1.putEggs();
        snake1.putEggs();
        tiger1.putEggs();
        //Forma correcta
        OviparousAnimal animal2 = new OviparousAnimal();
        OviparousAnimal snake2 = new Snake();
        MammalAnimal animal3 = new MammalAnimal();
        MammalAnimal tiger2 = new Tiger();

        animal2.putEggs();
        snake2.putEggs();
        animal3.breastfeed();
        tiger2.breastfeed();

        //Reto
        new Josegs95().retoFinal();
    }

    public void retoFinal(){
        Random rnd = new Random();
        Vehicle vehicle1 = new Car(50);
        Vehicle vehicle2 = new Train(100);
        Vehicle vehicle3 = new Plane(150);
        Vehicle[] vehicles = {vehicle1, vehicle2, vehicle3};

        for (int i = 0; i < 50; i++){
            if (rnd.nextBoolean())
                vehicles[rnd.nextInt(vehicles.length)].accelerate();
            else
                vehicles[rnd.nextInt(vehicles.length)].brake();
        }
    }

    //Clases incorrectas
    public static class WrongAnimal{
        public void putEggs(){
            System.out.println("El animal pone huevos");
        }
    }
    public static class WrongSnake extends WrongAnimal{
        @Override
        public void putEggs() {
            System.out.println("La serpiente pone huevos");
        }
    }
    public static class WrongTiger extends WrongAnimal{
        @Override
        public void putEggs() {
            //throw new UnsupportedOperationException("Los tigres no ponen huevos");
        }
    }
    //Clases correctas
    public static class Animal{}
    public static class OviparousAnimal extends Animal{
        public void putEggs() {
            System.out.println("El animal ovíparo pone huevos");
        }
    }
    public static class MammalAnimal extends Animal{
        public void breastfeed() {
            System.out.println("El animal mamífero da de mamar");
        }
    }
    public static class Snake extends OviparousAnimal{
        @Override
        public void putEggs() {
            System.out.println("La serpiente pone huevos");
        }
    }
    public static class Tiger extends MammalAnimal{
        @Override
        public void breastfeed() {
            System.out.println("El tigre da de mamar");
        }
    }
    //Reto
    public class Vehicle{
        private double speed;

        public Vehicle(double speed){
            this.speed = speed;
        }

        public void accelerate(){
            ++speed;
        }
        public void brake(){
            if (speed > 0)
                --speed;
        }

        public double getSpeed() {
            return speed;
        }
    }
    public class Car extends Vehicle{

        public Car(double speed) {
            super(speed);
        }

        @Override
        public void accelerate() {
            super.accelerate();
            System.out.println("El coche acelera y su velocidad es de " + super.getSpeed() + "Km/h");
        }

        @Override
        public void brake() {
            super.brake();
            System.out.println("El coche frena y su velocidad es de " + super.getSpeed() + "Km/h");
        }
    }
    public class Train extends Vehicle{
        public Train(double speed) {
            super(speed);
        }

        @Override
        public void accelerate() {
            super.accelerate();
            System.out.println("El tren acelera y su velocidad es de " + super.getSpeed() + "Km/h");
        }

        @Override
        public void brake() {
            super.brake();
            System.out.println("El tren frena y su velocidad es de " + super.getSpeed() + "Km/h");
        }
    }
    public class Plane extends Vehicle{
        public Plane(double speed) {
            super(speed);
        }

        @Override
        public void accelerate() {
            super.accelerate();
            System.out.println("El avión acelera y su velocidad es de " + super.getSpeed() + "Km/h");
        }

        @Override
        public void brake() {
            super.brake();
            System.out.println("El avión frena y su velocidad es de " + super.getSpeed() + "Km/h");
        }
    }
}
