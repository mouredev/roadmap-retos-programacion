
import java.util.*;

public class RodrigoGit87 {
    public static void main(String[] args) {
        /*
         *
         * DIFICULTAD EXTRA (opcional):
         * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
         * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
         *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
         *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
         *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
         *   Comprueba también que se ha conservado el valor original en las primeras.
         */

        //tipos de variables POR VALOR (son los primitivos y la 'copia' no afecta ala variable original ya q son independientes (cada una se almacena en una ubicacion diferente en
        // memoria 'Stack')
        float producto = 100;
        float descuento = (15 * 100 / 100); // <- 15 %
        float productoCon15Descuento = producto - descuento; // <- 85
        IO.println("\nproducto con descuento: " + productoCon15Descuento);
        IO.println(" pero producto sigue teniendo el valor original asignado : " + producto);

        // variables POR REFERENCIA ( Clases, Objetos, Strings, ARRays.. ) Lo q se 'copia' es la 'referencia en memoria', por tanto, ambas variables 'apuntan' al mismo sitio en memoria 'Heap'. Y cambiar algo
        //en el 'mismo sitio', altera el valor de lo que hay en el sitio, y como ambas variables apuntan al 'mismo sitio' ambas se modifican.

        int[] myArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        IO.println(Arrays.toString(myArray));

        int[] anotherArray = myArray; // <- anotherArray 'apunta' al mismo sitio en memoria que myArray.
        IO.println(Arrays.toString(anotherArray));

        anotherArray[9] = 69; // <- Cambiar una posicion en este array, tambien modificará la misma posicion en el array original, ya que ambos apuntan al mismo 'Heap'
        IO.println("\nmyArray: ");
        IO.print(Arrays.toString(myArray));

        IO.println("\nanotherArray: ");
        IO.print(Arrays.toString(anotherArray));

        IO.println("");

        //llamada metodo de funcion por valor
        int numA = 10;
        modificarInt(numA); // el metodo siempre imprimirá 30 por que -> ver metodo modificarInt
        IO.println(" comprobamos q numA sigue valiendo 10, numA = "+numA+" después de usarlo como parametro del metodo");

        //llamada metodo de funcion por referencia
        var lista1 = new ArrayList<Integer>();
        for (int i=1; i<= 10; i++) lista1.add(i); // añado numeros a la lista con ciclo for

        funcionReferencia(lista1); // lista1 y listaParametro 'apuntan' al mismo sitio en memoria (Heap)
        IO.println("comprobamos q lista1 ( el original )  ha cambiado tras usar el metodo: " + lista1); // si fuese por valor, (imposible si no es primitivo), hubiese impreso el valor original (del 1 al 10)

        // -----
        // EXTRA
        // -----
        int d = 10;
        int e = 20;

        int[] retornoFuncion = changeValue(d,e);

        IO.println(d);
        IO.println(e);
        IO.println(" valores  invertidos : " + Arrays.toString(retornoFuncion));

    }

        //Funcion con datos por Valor
        public static void modificarInt (int num){  //el valor q usemos en la llamada, se asignará a la nueva variable creada 'num'
        IO.println(num); // <-- Imprimirá 10, q es el valor de numA  ( num es una copia de numA )
        num= 30;  // <- Ahora la copia tiene asignado el valor 30
        IO.println(num);  // <-  Imprime 30
        }


        //Funcion por Referencia
        public static void funcionReferencia (ArrayList<Integer> listaParametro){
            listaParametro.add(55);
            IO.println("lista parametro: " + listaParametro );
        }
        // -----
        // EXTRA
        // -----
        public static int[] changeValue(int valueA, int valueB) { // a= 10 b = 20
            int temp = valueA; // temp 10
            valueA = valueB; // a = 20
            valueB = temp; // b = 10
            return new int[] {valueA,valueB};
        }


}
