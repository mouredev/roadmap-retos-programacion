public class CurtoBrull {

    // Variable global
    static String globalText = "Hello World! Variable global";

    public static void main(String[] args) {
        // Crear diferentes tipos de funciones sin parámetros ni retorno, con uno o varios parámetros, con retorno...
        printText();
        printText("Hello World! Con parámetro sin retorno");
        System.out.println(returnText());
        System.out.println(returnText("Hello World! Con parámetro y con retorno"));
        System.out.println(returnText(globalText, "Múltiples Parámetros con retorno!"));
        printText2();
        printTextRec(3);
        System.out.println("Veces que se ha impreso un número: " + extraExercice(100, "Pim", "Pam"));
    }

    public static void printText() {
        // Variable local
        String localText = "Hello World! Variable local. Función sin parámetros ni retorno";
        System.out.println(localText);
    }

    public static void printText(String text) {
        System.out.println(text);
    }

    public static String returnText() {
        return "Hello World! Sin parámetros y con retorno";
    }

    public static String returnText(String text) {
        return text;
    }

    public static String returnText(String text, String text2) {
        return text + " " + text2;
    }

    // Funcion dentro de otra funcion
    public static void printText2() {
        System.out.println("Hello World! Llamada de función dentro de función");
        printText();
    }

    // Funcion recursiva
    public static void printTextRec(int n) {
        if (n == 0) {
            return;
        }
        System.out.println("Hello World! Función recursiva");
        printTextRec(n - 1);
    }

/*
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

    public static int extraExercice(int n, String text1, String text2) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(text1 + text2);
            } else if (i % 3 == 0) {
                System.out.println(text1);
            } else if (i % 5 == 0) {
                System.out.println(text2);
            } else {
                System.out.println(i);
                count++;
            }
        }
        return count;
    }


}
