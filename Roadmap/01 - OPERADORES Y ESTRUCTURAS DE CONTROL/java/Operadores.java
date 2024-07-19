public class RoadRamp02 {
    public static void main(String[] args) {

//        /*Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
//         Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
//          (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
//          */
//        int a=15;
//        int b=8;
//
//        System.out.println("Suma :" + (a + b));
//        System.out.println("resta :" + (a - b));
//        System.out.println("multiplicacion :" + (a * b));
//        System.out.println("modulo :" + (a % b));
//        System.out.println("Division :" + (a / b));
//
////Operadores de comparacion
//        int c = 5;
//        int d = 7;
//
//        boolean igual = (c == d); // Comprueba si a es igual a b (igual será false).
//        boolean noIgual = (c != d); // Comprueba si a no es igual a b (noIgual será true).
//        boolean mayorQue = (c > d); // Comprueba si a es mayor que b (mayorQue será false).
//        boolean menorIgual = (c <= d); // Comprueba si a es menor o igual que b (menorIgual será true).
//
////operadores de asignacion
//        int x=10;
//        x=10;
//        x-=10;
//        x+=10;
//        x%=10;
//        x/=10;
//
//        //Operadores logicos
////        boolean z = true;
////        boolean r= false;
////        boolean result=z && r;
////        boolean result=z || r;
////        //boolean result=z !=r;
//
//        /*
//        Utilizando las operaciones con operadores que tú quieras, crea ejemplos
// *   que representen todos los tipos de estructuras de control que existan
// *   en tu lenguaje:
// *   Condicionales, iterativas, excepciones...
// * - Debes hacer print por consola del resultado de todos los ejemplos.
//         */
//
//        int f=5;
//        int o=9;
//        boolean igual2 = (f == o);
//        boolean noIgual2 = (f != o);
//        boolean mayorQue2 = (f > o);
//        boolean menorIgual2 = (f <= o);
//
//        System.out.println(igual2);
//        System.out.println(noIgual2);
//        System.out.println(mayorQue2);
//        System.out.println(menorIgual2);
//
//
//
//        int a2=15;
//        int b2=8;
//
//        System.out.println("Suma :" + (a2 + b2));
//        System.out.println("resta :" + (a2 - b2));
//        System.out.println("multiplicacion :" + (a2 * b2));
//        System.out.println("modulo :" + (a2 % b2));
//        System.out.println("Division :" + (a2 / b2));
//
//        /*
//        DIFICULTAD EXTRA (opcional):
// * Crea un programa que imprima por consola todos los números comprendidos
// * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
//         */
//
        for (int i = 10; i <= 55; i++) {
int numero=i;
            if (numero==16){
                continue;
            }else if(numero %3==0) {
                continue;
            }else if(numero %2 !=0) {
                continue;
            }

            System.out.println("numero : " + i);
            }

    }
}
