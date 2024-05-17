public class Worlion {

    /*
    * EJERCICIO: Herencia
    */
    abstract class Animal {
        String name;
        String family;
        String sound;
        String icon;

        abstract String doSound();
    }

    class Dog extends Animal {
        String family = "Canidae";
        String sound = "guau";
        String icon = "🐶";

        public Dog(String name){
            this.name = name;
        }
        
        public String doSound() {
            StringBuilder s = new StringBuilder("Los perros ladran asi: ");
            s.append(this.sound);
            s.append(this.icon);
            s.append(", y este se llama "+this.name);

            return s.toString();
        }
    }

    class Cat extends Animal {
        String family = "Felidae";
        String sound = "miau";
        String icon = "🐱";

        public Cat(String name){
            this.name = name;
        }
        
        public String doSound() {
            StringBuilder s = new StringBuilder("Los gatos maullan asi: ");
            s.append(this.sound);
            s.append(this.icon);
            s.append(", y este se llama "+this.name);

            return s.toString();
        }
    }
    

    public static void main(String[] args) {
        new Worlion().run();
    }

    public void run(){
        Animal perro = new Dog("Juanito");
        System.out.println(perro.doSound());

        Animal cat = new Cat("Botitas");
        System.out.println(cat.doSound());
    }
}

