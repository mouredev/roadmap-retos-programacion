public class hernanR {
    public static void main(String[] args) {
        // Por valor: tipos primitivos
        int a = 10;
        int b = a;
        b = 20;
        System.out.println("Por valor - a: " + a);
        System.out.println("Por valor - b: " + b);

        // Por referencia: objetos
        int[] c = { 1, 2, 3 };
        int[] d = c;
        d[0] = 10;
        System.out.println("Por referencia - c[0]: " + c[0]);
        System.out.println("Por referencia - d[0]: " + d[0]);

        // DIFICULTAD EXTRA (opcional):
        int[] valores = { 10, 20 };
        intercambiarPorReferencia(valores);
        int nuevoX = valores[0];
        int nuevoY = valores[1];
        System.out.println("Intercambio por referencia - nuevoX: " + nuevoX);
        System.out.println("Intercambio por referencia - nuevoY: " + nuevoY);
    }

    // Por valor
    public static void porValor(int a, int b) {
        a = 20;
        b = 30;
    }

    // Por referencia
    public static void porReferencia(int[] c, int[] d) {
        c[0] = 10;
        d[0] = 20;
    }

    public static void intercambiarPorReferencia(int[] arr) {
        int temp = arr[0];
        arr[0] = arr[1];
        arr[1] = temp;
    }
}
