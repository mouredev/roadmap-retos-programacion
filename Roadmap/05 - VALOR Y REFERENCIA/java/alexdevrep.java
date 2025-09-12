package _05_Valor_y_Referencia;

import java.util.ArrayList;

public class _05_Valor_y_Referencia {
    /*
     * EJERCICIO:
     * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
     *   su tipo de dato.
     * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
     *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
     * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
     *
     * DIFICULTAD EXTRA (opcional):
     * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
     * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
     *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
     *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
     *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
     *   Comprueba también que se ha conservado el valor original en las primeras.
     */

    //Asignación de variables por valor
    static int valor1 = 10;
    static int valor2 = valor1;

    //Asignación de variables por referencia
    static ArrayList<Integer> numeros = new ArrayList<>();
    static ArrayList<Integer> numerosNew = numeros;
    //Dificultad extra
    //Programa asignación por valor
    public static void programa1(int numero1, int numero2){
         numero1 = 5;
         numero2 = 3;
         System.out.println("El valor del numero1 ahora es: "+numero1);
         System.out.println("El valor del numero2 ahora es: "+numero2);

    }
    //Programa asignación por referencia
    public static ArrayList<String> programa2 (ArrayList lista){
        ArrayList<String> listaNueva = lista;
        listaNueva.remove("Alexdevrep");
        System.out.println("Los elementos en la lista nueva son:"+ lista);
        return  listaNueva;


    }





    public static void main(String[] args){
        //Asignación de variables por valor
        valor1 = 20;
        System.out.println(valor1);
        System.out.println(valor2);

        //Asignación de variables por referencia
        //Creamos un Array
        numeros.add(1);
        numeros.add(2);
        numeros.add(3);
        numeros.add(4);
        numerosNew.remove(2);
        System.out.println(numeros);
        /*
        * Como podemos comprobar aunque hayamos quitado el número 3
        * en el arrayList numerosNew el array original numeros tambien
        * se ve afectado por esta modificacion.
        */

        //Dificultad Extra
        //Programa asignación por valor
        int numero1 =3;
        int numero2 =5;
        System.out.println("El valor original del numero1 es:"+numero1);
        System.out.println("El valor original del numero2 es:"+numero2);

        programa1 (numero1,numero2);

        //Programa asignación por referencia
        ArrayList<String> lista = new ArrayList<>();
        lista.add("Hola");
        lista.add("Alexdevrep");
        lista.add("Java");
        System.out.println("Los elementos en la lista original son:"+ lista);

        programa2(lista);

        /*
        Los valores originales no cambian despues de llamar a las funciones de intercambios
        ya que en Java los parámetros se pasan por valor incluso cuando se tratan de objetos
         */





    }
}
