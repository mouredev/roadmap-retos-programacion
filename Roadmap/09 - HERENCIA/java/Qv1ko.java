public class Qv1ko {

    public static void main(String[] args) {

        Dog dog = new Dog();
        dog.setName("Rex");
        
        Cat cat = new Cat();
        cat.setName("Whiskers");

        animalSound(dog);
        animalSound(cat);

    }

    public static void animalSound(Animal animal) {
        System.out.println(animal.getName() + " makes the sound: ");
        animal.makeSound();
    }

}

class Animal {

    String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void makeSound() {
        System.out.println("Unknown sound");
    }

    @Override
    public String toString() {
        return name;
    }

}

class Dog extends Animal {

    @Override
    public void makeSound() {
        System.out.println("Guau Guau");
    }

}

class Cat extends Animal {

    @Override
    public void makeSound() {
        System.out.println("Miau Miau");
    }

}
