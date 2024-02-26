public class KingSaul22 {
    public static void main(String[] args) {


        //DIFICULTAD EXTRA
        String a = "Sal", b = "Azúcar";
        System.out.println("\nNúmeros impresos: " + dificultadExtra(a, b));
    }

    private static int dificultadExtra(String cadena1, String cadena2) {
        int contNumero = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 5 == 0 && i % 3 == 0) {
                System.out.println(cadena1 + " y " + cadena2);
            } else if (i % 3 == 0) {
                System.out.println(cadena1);
            } else if (i % 5 == 0) {
                System.out.println(cadena2);
            } else {
                System.out.println(i);
                contNumero++;
            }
        }

        return contNumero;
    }
}
