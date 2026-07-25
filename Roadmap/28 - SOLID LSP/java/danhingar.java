public class danhingar {

    public static void main(String[] args) throws Exception {
        /*
         * Bird bird = new Bird();
         * bird.fly();
         * Chicken chicken = new Chicken();
         * chicken.fly();
         */

        Bird1 bird1 = new Bird1();
        bird1.move();
        bird1 = new Chicken1();
        bird1.move();

        Bird1 chicken1 = new Chicken1();
        chicken1.move();
        chicken1 = new Bird1();
        chicken1.move();

        // Extra
        Motorbike motorbike = new Motorbike();
        Car car = new Car();
        Bike bicycle = new Bike();

        Vehicle.test(motorbike);
        Vehicle.test(car);
        Vehicle.test(bicycle);

        
    }

}

// Incorrecto
class Bird {
    public void fly() throws Exception {
        System.out.println("Flying");
    }
}

class Chicken extends Bird {
    @Override
    public void fly() throws Exception {
        throw new Exception("Los pollos no vuelan");
    }
}

class Bird1 {

    public void move() {
        System.out.println("Moving");
    }

}

class Chicken1 extends Bird1 {

    public void move() {
        System.out.println("Walking");
    }
}

// EXTRA

class Vehicle {
    private Integer speed = 0;

    public Vehicle() {
    }

    public void accelerate(Integer increment) {
        speed = speed + increment;
        System.out.printf("Velocidad: %d Km/h\n", speed);
    }

    public void brake(Integer decrement) {
        speed = speed - decrement;
        if (speed < 0)
            speed = 0;
        System.out.printf("Velocidad: %d Km/h\n", speed);
    }

    public static void test(Vehicle vehicle){
        vehicle.accelerate(5);
        vehicle.brake(1);
    }

}

class Motorbike extends Vehicle {


    @Override
    public void accelerate(Integer increment) {
        System.out.println("La moto está acelerando");
        super.accelerate(increment);
    }

    @Override
    public void brake(Integer decrement) {
        System.out.println("La moto está frenando");
        super.brake(decrement);
    }

}

class Bike extends Vehicle {

    @Override
    public void accelerate(Integer increment) {
        System.out.println("La bicicleta está acelerando");
        super.accelerate(increment);
    }

    @Override
    public void brake(Integer decrement) {
        System.out.println("La bicicleta está frenando");
        super.brake(decrement);
    }

}

class Car extends Vehicle {

    @Override
    public void accelerate(Integer increment) {
        System.out.println("El coche está acelerando");
        super.accelerate(increment);
    }

    @Override
    public void brake(Integer decrement) {
        System.out.println("El coche está frenando");
        super.brake(decrement);
    }

}