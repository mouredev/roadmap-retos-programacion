public class AmadorQuispe {
    public static void main(String[] args) {
        // En java esta definido dos tipos de excepción
        // Checked Exceptions, es obligatoria su manejo ya sea declarando en la firma
        // del método o usando try-catch

        // Unchecked Exceptions, no es obligatorio su manejo y ocurren en tiempo de
        // ejecución

        try {
            // Código que puede generar una excepción
            int result = 10 / 0; // Esto generará una excepción de división por cero (ArithmeticException)
            System.out.println(result);
        } catch (ArithmeticException e) {
            // Captura de la excepción específica
            System.out.println("Ocurrió una excepción: " + e.getMessage());
        }

        try {
            List<Integer> numbers = new ArrayList<>();
            numbers.add(2);
            numbers.add(4);
            numbers.add(6);
            numbers.add(8);
            // intentamos acceder al indice 4, como no tenemos lanza una excepción
            System.out.println(numbers.get(4));
        } catch (IndexOutOfBoundsException e) {
            System.out.println(e.getMessage());
        }
        // ArithmeticException y IndexOutOfBoundsException son unchecked exception, no
        // obliga a manejarlo

        File file = new File("not_existing_file.txt"); // intentamos acceder a un archivo
        try {
            FileInputStream stream = new FileInputStream(file);
        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }
        // FileNotFoundException es checked exception, por lo cual estamos obligados a
        // manejarlo

        // EXTRA

        System.out.println("Ingresa los números a dividir");
        try (Scanner sc = new Scanner(System.in)) {
            do {

                System.out.print("Ingresa el numerado :");
                int n1 = sc.nextInt();
                System.out.print("Ingresa el denominador :");
                int n2 = sc.nextInt();

                try {
                    double res = divisionPositive(n1, n2);
                    System.out.println(String.format("El resultado de %d / %d es %s", n1, n2, res));
                } catch (NumberNegativeException ne) {
                    System.out.println(ne.getMessage());
                } catch (ArithmeticException ae) {
                    System.out.println(ae.getMessage());
                } catch (Exception e) {
                    System.out.println(e.getMessage());
                } finally {
                    System.out.println("-------------------");
                }

            } while (true);
        }
    }

    private static double divisionPositive(int numerator, int denominator) {
        if (numerator < 0 || denominator < 0) {
            throw new NumberNegativeException("No negativos");
        }
        double result = numerator / denominator;
        return result;

    }

    public static class NumberNegativeException extends RuntimeException {

        public NumberNegativeException(String message) {
            super(message);
        }
    }

}
