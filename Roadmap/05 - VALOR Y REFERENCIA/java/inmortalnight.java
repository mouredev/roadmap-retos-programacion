// 05 - VALOR Y REFERENCIA

public class inmortalnight {
    public static void main(String[] args) {
        //Variables por valor, tipos primitivos
        int a = 5;
        int b = a;
        b = 10;
        System.out.println(a + " " + b); 
        //Variables por referencia, tipos compuestos
        int[] c = {5};
        int[] d = c;
        d[0] = 10;
        System.out.println(c[0] + " " + d[0]);


        //EXTRA
        //Por valor
        int valor1 = 10;
        int valor2 = 20;
        int valor3 = (intercambiaValor(valor1, valor2))[0];
        int valor4 = ((intercambiaValor(valor1, valor2))[1]);
        System.out.println("original: " + valor1 + " " + valor2);
        System.out.println("después: " + valor3 + " " + valor4);
        
        //Por referencia
        int[] valor1_1 = {10, 20};
        int[] valor2_2 = {30, 40};
        int[] valor3_3 = (intercambiaReferencia(valor1_1, valor2_2))[0];
        int[] valor4_4 = (intercambiaReferencia(valor1_1, valor2_2))[1];
        System.out.println("original: " );
        printArray(valor1_1);
        printArray(valor2_2);
        System.out.println("después: " );
        printArray(valor3_3);
        printArray(valor4_4);
    }
    public static int[] intercambiaValor(int a, int b){
        int temp = a;
        a = b;
        b = temp;
        int[] n = {a, b};
        return n;
    } 
    public static int[][] intercambiaReferencia(int[] a, int[] b){
        int[] temp = a;
        a = b;
        b = temp;
        int[][] n = {a, b};
        return n;
    }
    
    public static void printArray(int[] array) {
        for (int i : array) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}