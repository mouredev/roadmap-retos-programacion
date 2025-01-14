public class eulogioep {
    public static void main(String[] args) {
        // Ejemplos de asignación por valor (tipos primitivos)
        int a = 5;
        int b = a; // b es una copia del valor de a
        b = 10; // Cambiar b no afecta a a
        System.out.println("a: " + a + ", b: " + b); // a: 5, b: 10

        // Ejemplos de asignación por referencia (objetos)
        int[] arr1 = {1, 2, 3};
        int[] arr2 = arr1; // arr2 apunta al mismo array que arr1
        arr2[0] = 100; // Cambiar arr2 afecta a arr1
        System.out.println("arr1[0]: " + arr1[0] + ", arr2[0]: " + arr2[0]); // arr1[0]: 100, arr2[0]: 100

        // Ejemplo de función con parámetro por valor
        int x = 5;
        modificarValor(x);
        System.out.println("x después de modificarValor: " + x); // x no cambia

        // Ejemplo de función con parámetro por referencia
        int[] array = {1, 2, 3};
        modificarReferencia(array);
        System.out.println("array[0] después de modificarReferencia: " + array[0]); // array[0] cambia

        // DIFICULTAD EXTRA
        // Programa 1: Intercambio por valor
        int num1 = 10, num2 = 20;
        System.out.println("Antes del intercambio por valor: num1 = " + num1 + ", num2 = " + num2);
        int[] resultadoValor = intercambioPorValor(num1, num2);
        int nuevoNum1 = resultadoValor[0], nuevoNum2 = resultadoValor[1];
        System.out.println("Después del intercambio por valor:");
        System.out.println("Variables originales: num1 = " + num1 + ", num2 = " + num2);
        System.out.println("Nuevas variables: nuevoNum1 = " + nuevoNum1 + ", nuevoNum2 = " + nuevoNum2);

        // Programa 2: Intercambio por referencia
        Integer ref1 = 30, ref2 = 40;
        System.out.println("\nAntes del intercambio por referencia: ref1 = " + ref1 + ", ref2 = " + ref2);
        Integer[] resultadoReferencia = intercambioPorReferencia(ref1, ref2);
        Integer nuevoRef1 = resultadoReferencia[0], nuevoRef2 = resultadoReferencia[1];
        System.out.println("Después del intercambio por referencia:");
        System.out.println("Variables originales: ref1 = " + ref1 + ", ref2 = " + ref2);
        System.out.println("Nuevas variables: nuevoRef1 = " + nuevoRef1 + ", nuevoRef2 = " + nuevoRef2);
    }

    // Función que recibe un parámetro por valor
    public static void modificarValor(int n) {
        n = 100; // Este cambio no afecta a la variable original
    }

    // Función que recibe un parámetro por referencia
    public static void modificarReferencia(int[] arr) {
        arr[0] = 100; // Este cambio afecta al array original
    }

    // Función para intercambio por valor
    public static int[] intercambioPorValor(int a, int b) {
        int temp = a;
        a = b;
        b = temp;
        return new int[]{a, b};
    }

    // Función para intercambio por referencia
    public static Integer[] intercambioPorReferencia(Integer a, Integer b) {
        Integer temp = new Integer(a);
        a = new Integer(b);
        b = new Integer(temp);
        return new Integer[]{a, b};
    }
}