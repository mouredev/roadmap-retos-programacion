public class AnaLauDB {
    public static class AnaLauDBException extends Exception {
        public AnaLauDBException(String message) {
            super(message);
        }
    }

    public static void main(String[] args) throws AnaLauDB.AnaLauDBException {
        System.out.println("Manejo de excepciones en AnaLauDB");

        try {
            System.out.println("1.-Division de 9 entre 0");
            int resultado = 9 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Error: Division por cero no permitida.");
            System.out.println("Tipo: " + e.getClass().getSimpleName());
            System.out.println("Mensaje: " + e.getMessage() + "\n");
        }

        try {
            System.out.println("2.- Accediendo a indice fuera de rango");
            int[] datos = { 7, 8, 9 };
            System.out.println(datos[5]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Error: Indice fuera de rango.");
            System.out.println("Tipo: " + e.getClass().getSimpleName());
            System.out.println("Mensaje: " + e.getMessage() + "\n");
        }

        System.out.println("3.- Probando 'procesar (int a)' con varios casos:");
        procesar(5);
        procesar(-1);
        procesar(0);
        procesar(10);
    }

    // EXTRA
    public static int procesar(int a) throws AnaLauDBException {
        // 1) Validación de negocio
        if (a < 0) {
            throw new IllegalArgumentException("El parámetro no puede ser negativo.");
        }
        // 2) Regla de negocio: valor prohibido
        if (a == 10) {
            throw new AnaLauDBException("El 10 está prohibido por política interna.");
        }
        // 3) Operación que puede causar ArithmeticException si a == 0
        int resultado = 100 / a; // Si a == 0, lanza ArithmeticException
        return resultado;
    }

    public static void probarProcesar(int a) {
        System.out.println("-> Llamando procesar(" + a + ")");
        try {
            int r = procesar(a);
            System.out.println("Resultado: " + r);
            System.out.println("No se ha producido ningún error.");
        } catch (AnaLauDBException | IllegalArgumentException | ArithmeticException e) {
            System.out.println("Tipo de error: " + e.getClass().getSimpleName());
            System.out.println("Mensaje: " + e.getMessage());
        } finally {
            System.out.println("Ejecución finalizada.\n");
        }
    }
}
