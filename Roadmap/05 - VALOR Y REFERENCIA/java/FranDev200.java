
public class FranDev200 {

    /*
     * EJERCICIO:
     * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
     *   su tipo de dato.
     * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
     *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
     * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
     *
     * DIFICULTAD EXTRA (opcional):
     * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
     * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
     *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
     *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
     *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
     *   Comprueba también que se ha conservado el valor original en las primeras.
     */

    static void main() {

        System.out.println("Asignacion por valor");
        System.out.println("====================");
        int x = 10;
        System.out.println("Antes de modificar el valor de x=" + x);
        modificarPorValor(x);
        System.out.println("Después de modificar el valor de x=" + x);
        System.out.println("=====================================");
        System.out.println("Asignacion por referencia");
        System.out.println("=========================");
        Animal animal = new Animal("Rubi");
        System.out.println("Antes de modificar el nombre: " + animal.name);
        modificarPorReferencia(animal);
        System.out.println("Después de modificar el nombre: " + animal.name);
        System.out.println("====================================");

        System.out.println("\nEJERCICIO EXTRA");
        System.out.println("===============");
        System.out.println("Intercambios por valor");
        int a = 20;
        int b = 10;
        System.out.println("======================");
        System.out.println("Antes de intercambiarlos");
        System.out.println("------------------------");
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println("========================");
        int[] changeNumbers = intercambiarPorValor(a, b);
        int c = changeNumbers[0];
        int d = changeNumbers[1];
        System.out.println("Después de intercambiarlos");
        System.out.println("--------------------------");
        System.out.println("a = " + c);
        System.out.println("b = " + d);
        System.out.println("==========================");
        System.out.println("Intercambios por referencia");
        Animal animal1 = new Animal("Perro");
        Animal animal2 = new Animal("Gato");
        System.out.println("======================");
        System.out.println("Antes de intercambiarlos");
        System.out.println("------------------------");
        System.out.println("Nombre animal1 = " + animal1.name);
        System.out.println("Nombre animal2 = " + animal2.name);
        System.out.println("========================");
        Animal[] animals = intercambiarPorReferencia(animal1, animal2);
        System.out.println("Después de intercambiarlos");
        System.out.println("--------------------------");
        System.out.println("Nombre animal1 = " + animal1.name);
        System.out.println("Nombre animal2 = " + animal2.name);
        System.out.println("==========================");
    }

    public static void modificarPorValor(int x){
        x = 20; // x vale 20 solamente en la funcion, fuera de ella vale otra cosa
    }

    public static void modificarPorReferencia(Animal animal){
        animal.name = "Indi";
    }

    public static int[] intercambiarPorValor(int a, int b){
        int c = a;
        a = b;
        b = c;
        int[] result = {a, b};
        return result;
    }

    public static Animal[] intercambiarPorReferencia(Animal a, Animal b){
        Animal animal = new Animal(a.name);
        a.name = b.name;
        b.name = animal.name;
        Animal[] result = {a, b};
        return result;
    }

    static class Animal{
        String name;

        public Animal(String name){
            this.name = name;
        }
    }

}






