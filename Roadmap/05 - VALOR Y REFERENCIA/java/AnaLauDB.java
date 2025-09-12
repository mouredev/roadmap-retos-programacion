public class AnaLauraDB {
    public static void main(String[] args) {
        System.out.println("AnaLauraDB está lista para usarse.\n");

        // Ejemplo de asignación por valor (tipos primitivos)
        int a = 5;
        int b = a; // b recibe el valor de a
        b = 10; // modificar b no afecta a
        System.out.println("Por valor:");
        System.out.println("a = " + a); // 5
        System.out.println("b = " + b); // 10

        System.out.println();

        // Ejemplo de asignación por referencia (objetos)
        int[] arr1 = { 1, 2, 3 };
        int[] arr2 = arr1; // arr2 referencia el mismo arreglo que arr1
        arr2[0] = 99; // modificar arr2 afecta a arr1
        System.out.println("Por referencia:");
        System.out.print("arr1 = ");
        imprimirArreglo(arr1); // 99, 2, 3
        System.out.print("arr2 = ");
        imprimirArreglo(arr2); // 99, 2, 3

        System.out.println();

        // Función con variable por valor
        int x = 20;
        modificarPorValor(x);
        System.out.println("Después de modificarPorValor(x): x = " + x); // sigue siendo 20

        System.out.println();

        // Función con variable por referencia
        int[] valores = { 7, 8, 9 };
        modificarPorReferencia(valores);
        System.out.print("Después de modificarPorReferencia(valores): valores = ");
        imprimirArreglo(valores); // primer elemento cambiado a 100

        // EXTRA:

        System.out.println("\nEXTRA: Intercambio de valores");
        // Intercambio por valor (tipos primitivos)
        int val1 = 100;
        int val2 = 200;
        int[] nuevosValores = intercambiarPorValor(val1, val2);
        System.out.println("\nIntercambio por valor:");
        System.out.println("Originales: val1 = " + val1 + ", val2 = " + val2);
        System.out.println("Nuevos:     val1 = " + nuevosValores[0] + ", val2 = " + nuevosValores[1]);

        // Intercambio por referencia (arreglos)
        int[] ref1 = { 1, 2, 3 };
        int[] ref2 = { 4, 5, 6 };
        int[][] nuevosRefs = intercambiarPorReferencia(ref1, ref2);
        System.out.println("\nIntercambio por referencia:");
        System.out.print("Originales: ref1 = ");
        imprimirArreglo(ref1);
        System.out.print("            ref2 = ");
        imprimirArreglo(ref2);
        System.out.print("Nuevos:     ref1 = ");
        imprimirArreglo(nuevosRefs[0]);
        System.out.print("            ref2 = ");
        imprimirArreglo(nuevosRefs[1]);
    }

    // Función que recibe un int (por valor)
    public static void modificarPorValor(int n) {
        n = 50;
    }

    // Función que recibe un arreglo (por referencia)
    public static void modificarPorReferencia(int[] arr) {
        arr[0] = 100;
    }

    // Utilidad para imprimir arreglos
    public static void imprimirArreglo(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1)
                System.out.print(", ");
        }
        System.out.println();

    }

    // Intercambio por valor
    public static int[] intercambiarPorValor(int a, int b) {
        int temp = a;
        a = b;
        b = temp;
        return new int[] { a, b };
    }

    // Intercambio por referencia
    public static int[][] intercambiarPorReferencia(int[] arr1, int[] arr2) {
        int[] temp = arr1.clone();
        arr1 = arr2.clone();
        arr2 = temp;
        return new int[][] { arr1, arr2 };
    }
}
