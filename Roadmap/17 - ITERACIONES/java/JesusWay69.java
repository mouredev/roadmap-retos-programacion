package roadmap.ejercicio_17;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
public class JesusWay69 {
    public static void main(String[] args) {
        iterator1();
        iterator2();
        iterator3();
        iterator4();
        iterator5();
        iterator6();
        iterator7();
        iterator8();
        iterator9(0);
        iterator10();
        iterator11();
        iterator12();
        iterator13();
        iterator14();
        iterator15();
    }

    /*FUNCIÓN FOR CON CONDICIÓN DE INICIO,PARADA Y PASO*/
    private static void iterator1() {
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + " ");
        }
        System.out.print(" --> Método 1");
        System.out.println("");
    }

    /*FUNCIÓN WHILE CON CONDICIÓN DE PARADA Y PASO*/
    private static void iterator2() {
        int i = 1;
        while (i <= 10) {
            System.out.print(i + " ");
            i++;
        }
        System.out.print(" --> Método 2");
        System.out.println("");
    }

    /*FUNCIÓN DO-WHILE CON CONDICIÓN DE PASO Y PARADA*/
    private static void iterator3() {
        int i = 1;
        do {
            System.out.print(i + " ");
            i++;
        } while (i <= 10);
        System.out.print(" --> Método 3");
        System.out.println("");
    }

    /*FUNCIÓN FOR CON DOS ÍNDICES DE CONTROL (PARES-IMPARES) MEDIANTE PASO DE 2 EN 2*/
    private static void iterator4() {
        for (int i = 1, j = 2; i < 10 && j <= 10; i += 2, j += 2) {
            System.out.print(i + " " + j + " ");
        }
        System.out.print(" --> Método 4");
        System.out.println("");
    }

    /*FUNCIÓN FOR CON DOS ÍNDICES DE CONTROL (PARES-IMPARES) MEDIANTE CONDICIÓN DE SU MÓDULO*/
    private static void iterator5() {
        for (int i = 1, j = 2; i < 10 && j <= 10; i++, j++) {
            if (i % 2 != 0 || j % 2 == 0) {
                System.out.print(i + " " + j + " ");
            }
        }
        System.out.print(" --> Método 5");
        System.out.println("");
    }

    /*FUNCIÓN CON 2 FOR CONCATENADOS , EL SEGUNDO RECIBE EL ÍNDICE DONDE TERMINA EL ANTERIOR Y COMPLETA LA ITERACIÓN*/
    private static void iterator6() {
        int i;
        for (i = 1; i <= 5; i++) {
            if (i <= 5) {
                System.out.print(i + " ");
            }
        }
        for (int j = i; j <= 10; j++) {
            System.out.print(j + " ");
        }
        System.out.print(" --> Método 6");
        System.out.println("");
    }

    /*FUNCIÓN FOR CON CONDICIÓN DE INICIO Y PASO FUERA DE SU CONSTRUCCIÓN Y CON CONDICIÓN DE PARADA BOOLEANA */
    private static void iterator7() {
        int i = 1;
        for (; true;) {
            if (i <= 10) {
                System.out.print(i + " ");
                i++;
            } else {
                System.out.print(" --> Método 7");
                System.out.println("");
                break;
            }

        }
    }

    /*FUNCIÓN CON FOR ANIDADOS CON CONDICIÓN DE INICIO,PARADA Y PASO, EL PRIMERO IMPRIME LOS IMPARES Y EL SEGUNDO LOS PARES */
    private static void iterator8() {
        int i;
        for (i = 1; i <= 10; i += 2) {
            System.out.print(i + " ");
            for (int j = 0; j < 1; j++) {
                if (i < 10) {
                    System.out.print(i + 1 + " ");
                }
            }
        }
        System.out.print(" --> Método 8");
        System.out.println("");
    }

    /*FUNCIÓN CON CONDICIÓN DE PARADA, INCREMENTO Y RECURSIVIDAD QUE RECIBE UN 0 COMO PARÁMETRO Y HACE EL INCREMETO
    PREVIO EN LA PROPIA FUNCIÓN PRINT*/
    private static void iterator9(int i) {
        if (i < 10) {
            System.out.print(++i + " ");
            iterator9(i);
        } else {
            System.out.print(" --> Método 9");
            System.out.println("");
        }
    }

    /*FUNCIÓN QUE CONSTRUYE UN STRINGBUILDER , SE LLENA CON LA SECUENCIA NUMÉRICA Y LUEGO SE RECORRE EXTRAYÉNDOLOS COMO CHAR,
    COMO CADA CHAR ES INPENDIENTE "TRUCAMOS" LA IMPRESIÓN PARA QUE IMPRIMA UN 10 Y NO UN 1 Y UN 0 AL FINAL*/
    private static void iterator10() {
        StringBuilder nums = new StringBuilder();
        for (int i = 1; i <= 10; i++) {
            nums.append(i);
        }
        for (int j = 0; j <= nums.length() - 1; j++) {
            if (nums.charAt(j) == '0') {
                System.out.print("\b0 ");
            } else {
                System.out.print(nums.charAt(j) + " ");
            }
        }
        System.out.print(" --> Método 10");
        System.out.println("");
    }

    /*FUNCIÓN CON GENERACIÓN DE NÚMEROS ALEATORIOS QUE SE AÑADEN A UN TREESET HASTA QUE ESTE CUMPLA LA CONDICIÓN DE LONGITUD 10
    MEDIANTE UN CICLO DO-WHILE Y SE EXTRAEN CON UN CICLO FOR-EACH*/
    private static void iterator11() {
        Set<Integer> mySet = new TreeSet<>();
        do {
            int num = (int) (Math.random() * 10 + 1);
            mySet.add(num);
        } while (mySet.size() <= 9);

        for (Integer value : mySet) {
            System.out.print(value + " ");
        }
        System.out.print(" --> Método 11");
        System.out.println("");
    }

    /*FUNCIÓN DONDE DECLARAMOS UN ARRAY CON LOS CARACTERES CORRESPONDIENTES A LOS CÓDIGO ASCII DEL 51 AL 60,
    DESPUES LOS RECORREMOS CON UN FOR-EACH DECLARANDO LOS ELEMENTOS COMO NUMÉRICOS Y RESTÁNDOLES 50 */
    private static void iterator12() {
        char[] myList = {'3', '4', '5', '6', '7', '8', '9', ':', ';', '<'};

        for (int myCode : myList) {
            System.out.print((myCode - 50) + " ");
        }
        System.out.print(" --> Método 12");
        System.out.println("");
    }

    /*FUNCIÓN CON 5 WHILES ANIDADOS CON CONDICIONES DE PARADA IDÉNTICAS PARA COMPROBAR QUE CADA UNO SOLO ITERA
    UNA VEZ SIEMPRE QUE HAYA OTRO POR DEBAJO, EL ULTIMO (EL 5º) ES EL QUE COMPLETA LA SECUENCIA DEL 5 AL 10
    Y VA VOLVIENDO UNO POR UNO A LOS ANTERIORES COMPROBANDO SI LA CONDICIÓN DE PARADA SE CUMPLE EN TODOS Y COMO
    ES ASÍ LA EJECUCIÓN TERMINA, EN UN CASO DE FOR ANIDADOS OCURRE EXACTAMENTE LO MISMO*/

    private static void iterator13() {
        int i = 0;
        while (i < 10) {
            i++;
            System.out.print(i + " ");
            while (i < 10) {
                i++;
                System.out.print(i + " ");
                while (i < 10) {
                    i++;
                    System.out.print(i + " ");
                    while (i < 10) {
                        i++;
                        System.out.print(i + " ");
                        while (i < 10) {
                            i++;
                            System.out.print(i + " ");
                        }
                    }
                }
            }
        }
        System.out.print(" --> Método 13");
        System.out.println("");
    }

    /*FUNCIÓN DONDE SE DECLARAN 2 VARIABLES ORIGINALES Y EN BASE A ESTAS SE DECLARAN 7 MÁS CON CÁLCULOS BASADOS EN ELLAS
    QUE TERMINAN REPRESENTANDO LA SECUENCIA POR PAREJAS (EXCEPTO EL 9), SE AÑADEN A UN ARRAYLIST Y SE RECORREN CON UN FOR PARA 
    EXTRAER LOS ELEMENTOS (PAREJAS DE NÚMEROS) Y UN FOR-EACH ANIDADO DENTRO QUE SEPARA CADA PAREJA EN 2 CHAR INDEPENDIENTES
    (EXCEPTO EL 10)*/
    private static void iterator14() {
        List<String> myList = new ArrayList<>();
        int a = 1, b = 11, c = b + a, d = b * 2, e = c + d, f = e + d, g = f + d, h = g / 2 - 30, i = (g + d) / 10;
        myList.add(c + "");
        myList.add(e + "");
        myList.add(f + "");
        myList.add(g + "");
        myList.add(h + "");
        myList.add(i + "");

        for (String element : myList) {
            for (int j = 0; j < element.length(); j++) {
                if (element.charAt(j) == '0') {
                    System.out.print("\b");
                }
                System.out.print(element.charAt(j) + " ");
            }
        }
        System.out.print(" --> Método 14");
        System.out.println("");
    }

    /*FUNCIÓN CON WHILE CUYA CONDICIÓN ES UN TIPO BOOLEAN DECLARADO PREVIAMENTE CON INCREMENTO, IMPRESIÓN CON
    IF TERNARIO Y CONDICIÓN DE SALIDA CON EL PROPIO ELEMENTO BOOLEANO*/
    private static void iterator15() {
        boolean num = true;
        int i = 0;
        while (num) {
            ++i;
            num = (i <= 10);
            System.out.print(num ? i + " " : " --> Método 15\n");
            if (!num) break;      
        }

    }
}
