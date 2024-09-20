public class Rubioj17 {
    public static void main(String[] args) {
        /*
         * EJERCICIO:
         * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
         *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
         *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
         * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
         *   que representen todos los tipos de estructuras de control que existan
         *   en tu lenguaje:
         *   Condicionales, iterativas, excepciones...
         * - Debes hacer print por consola del resultado de todos los ejemplos.
         *
         * DIFICULTAD EXTRA (opcional):
         * Crea un programa que imprima por consola todos los números comprendidos
         * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
         *
         * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
         */

        //Operadores Aritméticos
        System.out.println("* * Operadores Aritmeticos * *");
        System.out.println("Suma: 6+2=" + (6+2));
        System.out.println("Resta: 6-2=" + (6-2));
        System.out.println("Multiplicación: 6*2=" + (6*2));
        System.out.println("Division: 6/2=" + (6/2));
        System.out.println("Residuo: 6%2=" + (6%2));
        System.out.println();

        //Operadores de Comparación
        System.out.println("* * Operadores de Comparación * *");
        System.out.println("Igual que: 6==2 " + (6==2));
        System.out.println("Diferente a: 6!=2 " + (6!=2));
        System.out.println("Mayor que: 6>2 " + (6>2));
        System.out.println("Menor que: 6<2 " + (6<2));
        System.out.println("Mayor igual que: 6>=2 " + (6>=2));
        System.out.println("Menor igual que: 6<=2 " + (6<=2));
        System.out.println();

        //Operadores Logicos
        System.out.println("* * Operadores Logicos * *");
        System.out.println("And &&: 5+5 == 2*5 && 10+5 == 25*5 " + (5+5 == 2*5 && 10+5 == 25*5));
        System.out.println("Or ||: 5+5 == 2*5 || 10+5 == 25*5 " + (5+5 == 2*5 || 10+5 == 25*5));
        System.out.println("Not !: 5+5 == 2*5 && 10-5 == 25/5 " + !(5+5 == 2*5 && 10-5 == 25/5));
        System.out.println();

        //Operadores de Asignación
        int a = 10;
        System.out.println("* * Operadorres de Asignación * *");
        System.out.println("+=: a+=5 " + (a+=5));
        System.out.println("-=: a-=5 " + (a-=5));
        System.out.println("*=: a*=5 " + (a*=5));
        System.out.println("/=: a/=5 " + (a/=5));
        System.out.println();

        //Operadores Ternarios
        System.out.println("* * Operadores Ternarios * *");
        System.out.println("Condición ? true : false ejemplo: 5>2 " + (5>2 ? "Mayor" : "Menor"));
        System.out.println();

        //Estructura de Control
        System.out.println("* * Estructura de Control * *");
        //Condicionales
        System.out.println("* * Condicionales * *");
        int n1 = 2, n2 = 4;
        if (n1 > n2) {
            System.out.println(n1 + " Es Mayor que " + n2);
        }else{
            System.out.println(n1 + " No es Mayor que " + n2);
        }
        System.out.println();

        //Iterativas
        System.out.println("* * Iterativas * *");
        System.out.println("* Usando For *");
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + ",");
        }
        System.out.println("\b");
        System.out.println("* Usando While *");
        int c = 1;
        while (c<=10) {
            System.out.print(c + ",");
            c++;
        }
        System.out.println("\b");
        System.out.println();

        //Excepciones
        System.out.println("* * Excepciones * *");
        try {
            System.out.println("Dividir 2/0 " + (2/0));
        }catch (Exception e) {
            System.out.println("No se puede Dividir por 0 " + e.getMessage());
        }finally {
            System.out.println();
        }

        //Dificultad Extra
        System.out.println("* * Dificultad Extra * *");
        for (int i = 10; i <= 35; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.print(i + ",");
            }
        }
        System.out.println("\b");
    }
}
