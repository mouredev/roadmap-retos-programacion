public class miguelex {

    public static void saludo() {
        System.out.println("Hola, soy Miguel");
    }

    public static void lenguaje(String lenguaje) {
        System.out.println("Este ejercicio esta hecho en el lenguaje " + lenguaje);
    }

    public static int suma(int a, int b) {
        return a + b;
    }

    public static int extra(String a, String b) {
        int count = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 15 == 0) {
                System.out.println(a + b);
            } else if (i % 3 == 0) {
                System.out.println(a);
            } else if (i % 5 == 0) {
                System.out.println(b);
            } else {
                System.out.println(i);
                count ++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        saludo();
        lenguaje("Java");
        System.out.println("La suma de 5 y 3 es " + suma(5, 3));
        System.out.println("Ejemplo de uso de funcion del sistema --> Longitud de una cadena de texto (Hola, Mundo!): " + "Hola, Mundo!".length());
        System.out.println("Ejercicio extra");
        System.out.println("Se ha imprimido " + extra("Fizz", "Buzz") + " veces");
    }
}
