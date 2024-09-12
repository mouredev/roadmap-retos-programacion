

/** #09 - Java -> Jesus Antonio Escamilla */

public class JesusAntonioEEscamilla {
    public static void main(String[] args) {
    //---EJERCIÓ---
        Animal perro = new Perro();
        Animal gato = new Gato();
        Animal pajaro = new Pajaro();

        System.out.println("Herencia");
        imprimirSonido(perro);
        imprimirSonido(gato);
        imprimirSonido(pajaro);

        System.out.println("\n");

        System.out.println("Extra Métodos");
        // Extra: Mostrar acciones adicionales
        ((Perro) perro).correr();
        ((Gato) gato).cazar();
        ((Pajaro) pajaro).volar();
    //---EXTRA---
        // Pendiente
    }

    //---EJERCIÓ---
    // Superclase Animal
    static class Animal {
        public void hacerSonido(){
            System.out.println("El animal hace ruido");
        }
    }

    // Subclases Perro
    static class Perro extends Animal {
        @Override
        public void hacerSonido(){
            System.out.println("El perro ladra: ¡Guau Guau!");
        }

        // Método adicional para perro
        public void correr(){
            System.out.println("Esta corriendo felizmente");
        }
    }

    // Subclases Gato
    static class Gato extends Animal {
        @Override
        public void hacerSonido(){
            System.out.println("El gato maúlla: ¡Miau Miau!");
        }

        // Método adicional para gato
        public void cazar(){
            System.out.println("Esta cazando un ratón");
        }
    }

    // Nueva Subclases Pájaro
    static class Pajaro extends Animal {
        @Override
        public void hacerSonido(){
            System.out.println("El pájaro canta: ¡Pio Pio!");
        }

        // Método adicional para gato
        public void volar(){
            System.out.println("Esta volando alto en el cielo");
        }
    }

    // Función que recibe un objeto de tipo Animal y llama a su método hacerSonido
    public static void imprimirSonido(Animal animal){
        animal.hacerSonido();
    }



    /**-----DIFICULTAD EXTRA-----*/

    // Pendientes

    /**-----DIFICULTAD EXTRA-----*/
}