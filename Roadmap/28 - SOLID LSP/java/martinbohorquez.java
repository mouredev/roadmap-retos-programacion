import java.util.Random;

public class martinbohorquez {

    public static void main(String[] args) {
//        incorrectLSP();
        correctLSP();
        /*
         * DIFICULTAD EXTRA
         */
        vehicleLSP();

    }

    /*
    private static void incorrectLSP() {
        Bird sparrow = new Sparrow();
        makeBirdFly(sparrow); // Funciona correctamente

        Bird ostrich = new Ostrich();
        makeBirdFly(ostrich); // Lanza excepción, lo cual es un error de LSP
    }

    public static void makeBirdFly(Bird bird) {
        bird.fly();
    }
    */

    private static void correctLSP() {
        FlyingBird sparrow = new Sparrow();
        makeBirdFly(sparrow); // Funciona correctamente

        // Ostrich no puede ser pasado a makeBirdFly, ya que no implementa FlyingBird.
    }

    private static void makeBirdFly(FlyingBird bird) {
        bird.fly();
    }

    private static void vehicleAccelerateBrake(Vehicule vehicule) {
        Random random = new Random();
        vehicule.accelerate(random.nextInt(10));
        vehicule.brake(random.nextInt(5));
    }

    private static void vehicleLSP() {
        Vehicule car = new Car(60);
        vehicleAccelerateBrake(car);
        Vehicule bicycle = new Bicycle(0);
        vehicleAccelerateBrake(bicycle);
        Vehicule motorcycle = new Motorcycle(40);
        vehicleAccelerateBrake(motorcycle);

    }
}

/*
// Clase base
class Bird {
    public void fly() {
        System.out.println("El pájaro vuela.");
    }
}

// Clase derivada
class Sparrow extends Bird {
    @Override
    public void fly() {
        System.out.println("El gorrión vuela.");
    }
}

// Clase derivada que no vuela
class Ostrich extends Bird {
    @Override
    public void fly() {
        throw new UnsupportedOperationException("El avestruz no puede volar.");
    }
}*/

// Interfaz base
interface Bird {
    // Métodos comunes
}

interface FlyingBird extends Bird {
    void fly();
}

class Sparrow implements FlyingBird {
    @Override
    public void fly() {
        System.out.println("El gorrión vuela.");
    }
}

class Ostrich implements Bird {
    // No implementa fly()
}

abstract class Vehicule {
    private Integer speed;

    protected Vehicule() {
        this(0);
    }

    protected Vehicule(Integer speed) {
        this.speed = speed;
        System.out.printf("Se crea un %s un con velocidad %d.%n", getClass().getSimpleName(), speed);
    }

    void accelerate(Integer increment) {
        speed += increment;
        System.out.printf("Velocidad: %d Km/h.%n", speed);
    }

    void brake(Integer decrement) {
        speed -= decrement;
        if (speed < 0) speed = 0;
        System.out.printf("Velocidad: %d Km/h.%n", speed);
    }
}

class Car extends Vehicule {
    protected Car() {
        super();
    }

    protected Car(Integer speed) {
        super(speed);
    }

    @Override
    void accelerate(Integer increment) {
        System.out.printf("El auto está acelerando en %d.%n", increment);
        super.accelerate(increment);
    }

    @Override
    void brake(Integer decrement) {
        System.out.printf("El auto está frenando en %d.%n", decrement);
        super.brake(decrement);
    }
}

class Bicycle extends Vehicule {
    protected Bicycle() {
        super();
    }

    protected Bicycle(Integer speed) {
        super(speed);
    }

    @Override
    void accelerate(Integer increment) {
        System.out.printf("La bicicleta está acelerando en %d.%n", increment);
        super.accelerate(increment);
    }

    @Override
    void brake(Integer decrement) {
        System.out.printf("La bicicleta está frenando en %d.%n", decrement);
        super.brake(decrement);
    }
}

class Motorcycle extends Vehicule {
    protected Motorcycle() {
        super();
    }

    protected Motorcycle(Integer speed) {
        super(speed);
    }

    @Override
    void accelerate(Integer increment) {
        System.out.printf("La moto está acelerando en %d.%n", increment);
        super.accelerate(increment);
    }

    @Override
    void brake(Integer decrement) {
        System.out.printf("La moto está frenando en %d.%n", decrement);
        super.brake(decrement);
    }
}
