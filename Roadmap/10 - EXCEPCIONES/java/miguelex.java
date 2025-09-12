public class miguelex {
    public static void main(String[] args) {
        try {
            int a = 5;
            int b = 0;
            int c = a / b;
            System.out.println(c);
        } catch (ArithmeticException e) {
            System.out.println("No se puede dividir por cero");
        }

        // excepcion por indice fuera de rango

        try {
            int[] array = new int[5];
            array[10] = 10;
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Indice fuera de rango");
        }

        try {
            //System.out.println(extra("Java", 10, "Miguel"));
            // System.out.println(extra("Java", 10));
            // System.out.println(extra("", 10, "Miguel"));
            // System.out.println(extra("Java", -10, "Miguel"));
            System.out.println(extra("Java", 10, "Mouredev"));
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public static String extra(String lenguaje, int reto, String usuario) {
        // Comprobación de cantidad de parámetros
        if (lenguaje == null || reto < 0 || usuario == null) {
            throw new IllegalArgumentException("Se deben proporcionar 3 parámetros");
        }
        // Comprobación de primer parámetro
        if (lenguaje.isEmpty()) {
            throw new IllegalArgumentException("El primer parámetro no puede estar vacío");
        }
        // Comprobación de segundo parámetro
        if (reto < 0) {
            throw new IllegalArgumentException("El segundo parámetro debe ser un entero no negativo");
        }
        // Comprobación de tercer parámetro
        if (usuario.equals("Mouredev")) {
            throw new IllegalArgumentException("El tercer parámetro no puede ser 'Mouredev'");
        }
        // Concatenación con formato
        return "Reto #" + reto + " - " + lenguaje + " enviado por " + usuario;
    }
}