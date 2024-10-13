package com.amsoft.roadmap.example28;

/*
El Principio de Substitución de Liskov es uno de los principios SOLID y hace referencia a cómo usamos
la herencia de forma adecuada. El principio dice algo como lo siguiente si S es un subtipo de T ,
T puede ser reemplazado con objetos de tipo S sin alterar el comportamiento esperado en el programa.
* */
public class Example28 {
    public static void main(String[] args) {
        Person person = new Child("Juan","2233 3333 3333 5555");
        Payable citizen = new Citizen("Amador","1111 2222 3333 4444");
        citizen.pay();

        //EXTRA
        Vehicle car = new Car();
        Vehicle motorbike = new Motorbike();
        Vehicle truck = new Truck();
        TestVehicle testVehicle = new TestVehicle();
        testVehicle.accelerate(car);
        testVehicle.accelerate(motorbike);
        testVehicle.accelerate(truck);

        testVehicle.brake(car);
        testVehicle.brake(motorbike);
        testVehicle.brake(truck);
    }
}
/*
La clase Person, se viola el Principio de Sustitución de Liskov porque la subclase Child hereda el método pay()
de Person, lo que permite que un objeto Child realice pagos, aunque lógicamente un niño no debería poder hacerlo.
La solución propuesta introduce una interfaz Payable que define el método pay(), y solo la subclase Citizen
implementa esta interfaz, mientras que Child no.
Esto garantiza que solo los objetos de Citizen puedan realizar pagos, respetando así el LSP y asegurando que los
objetos de Child no se comporten de manera inapropiada al sustituir objetos de la clase base Person.
 */
class Person {
    private String name;
    private String bankAccount;

    public Person(String name, String bankAccount) {
        this.name = name;
        this.bankAccount = bankAccount;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getBankAccount() {
        return bankAccount;
    }

    public void setBankAccount(String bankAccount) {
        this.bankAccount = bankAccount;
    }
}
interface  Payable {
    void pay();
}
class Child extends Person {
    public Child(String name, String bankAccount) {
        super(name, bankAccount);
    }
}
class Citizen extends Person implements Payable {
    public Citizen(String name, String bankAccount) {
        super(name, bankAccount);
    }

    @Override
    public void pay() {
        System.out.println(this.getName() + " pay with number account bank number " + this.getBankAccount());
    }
}

/*VIOLA LSP*/
/* class Person {
    private String name;
    private String bankAccount;

    public Person(String name, String bankAccount) {
        this.name = name;
        this.bankAccount = bankAccount;
    }

    public void pay(){
        System.out.println(name + " pay with number account bank number " + bankAccount);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getBankAccount() {
        return bankAccount;
    }

    public void setBankAccount(String bankAccount) {
        this.bankAccount = bankAccount;
    }
}
class Child extends Person {

    public Child(String name, String bankAccount) {
        super(name, bankAccount);
    }

    @Override
    public void pay() {
        throw new UnsupportedOperationException("Cannot pay");
    }
}
class Citizen extends Person {
    public Citizen(String name, String bankAccount) {
        super(name, bankAccount);
    }
}*/

/*EXTRA*/
class TestVehicle {
    public void accelerate(Vehicle vehicle){
        vehicle.accelerate();
    }
    public void brake(Vehicle vehicle){
        vehicle.brake();
    }
}
abstract class Vehicle {
    abstract void accelerate();
    abstract void brake();
}

class Car extends Vehicle {

    @Override
    void accelerate() {
        System.out.println("Acelerando el coche");
    }

    @Override
    void brake() {
        System.out.println("Frenando el coche");
    }
}

class Motorbike extends Vehicle{

    @Override
    void accelerate() {
        System.out.println("Acelerando la motocicleta");
    }

    @Override
    void brake() {
        System.out.println("Frenando la motocicleta");
    }
}

class Truck extends Vehicle {

    @Override
    void accelerate() {
        System.out.println("Acelerando el camión");
    }

    @Override
    void brake() {
        System.out.println("Frenando el camión");
    }
}

