public class Meir {
    public static void main(String[] args) {
        int variableGlobal = 2;
        sinParametro();
        conParametro(variableGlobal);
        System.out.println(conRetorno("Hola"));
        variableLocal();
        System.out.println(funcionExtra("Hola", "Mundo"));

    }

    static void sinParametro() {
        System.out.println("Sin parametros");
    }

    static void conParametro(int a) {
        System.out.println("Con parametro: " + a);
    }

    static String conRetorno(String a) {
        return a;
    }

    static void variableLocal() {
        int a = 10;
        System.out.println(a);
    }

    static int funcionExtra(String a, String b) {
        int contador = 0;
        for (int i = 1; i < 100; i++) {
            if (i % 3 == 0) {
                System.out.println(a);
            }
            else if (i % 5 == 0) {
                System.out.println(b);
            }
            else if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(a + b);
            }
            else {
                System.out.println(i);
                contador++;
            }
        }
    return contador;
    }

}
