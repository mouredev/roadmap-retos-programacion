import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class Worlion {


/*
 * EJERCICIO: Clases en JAVA
 */
    class Developer {
        private String name ="";
        private int age = 0;
        private List<String> languages = new ArrayList<>();

        public Developer(String name, int age, Collection<String> languages){
            this.name = name;
            this.age = age;
            this.languages.addAll(languages);
        }

        public void addLanguage(String newLanguage) {
            if(!this.languages.contains(newLanguage)) {
                this.languages.add(newLanguage);
            }
        }

        public String toString() {
            StringBuilder s = new StringBuilder("\"Developer\": {");

            s.append("\n\t\"this.name\": \"" + this.name + "\",");
            s.append("\n\t\"this.age\": \"" + this.age + "\",");
            s.append("\n\t\"this.languages\": " + this.languages );
            s.append("\n}");

            return s.toString();
        }
    }

    public static void main(String[] args) {
        new Worlion().run();
    }

    public void run() {
    
        Developer me = new Developer("Worlion", 40, List.of("Java", "Python"));
        System.out.println(me);
    }
}
