import java.util.Arrays;

public class LucasAG01 {
    public static void main(String[] args) {
        /*
    Operaciones
     */

        String s1 = "hola";
        String s2 = "Java";


        //concatenacion

        System.out.println(s1+", "+s2);

        String s3= s1.concat(" ").concat(s2); //hola java

        //Longitud

        int length=s2.length();
        System.out.println("Longitud: "+length);

        //Acceder a un caracter específico

        char ch=s2.charAt(1); //'a'

        //Comparacion de cadenas

        String compas2="Java";
        boolean iguales = s1.equals(compas2); //false  Conque falle una mayuscula, dará false

        boolean iguales2 = s2.equalsIgnoreCase(compas2); //true


        //Subcadenas

        String substr1= s1.substring(0,4); //hola
        String substr2= s2.substring(0,2); //Ja

        //Reemplazar

        String replace=s1.replace('a','4');
        String replace2=s2.replace("Java","Python");

        //Dividir cadenas

        String divi = "Java,Python,C++,Socorro";

        String[] langua =divi.split(","); //Se dividem por la coma, se crea una lista.

        //Mayusculas y minusculas

        String upper = s1.toUpperCase();
        String lower = s2.toLowerCase();

        //Eliminar espacios en blanco

        String espacios= "    Hola java   ";
        String trimmed = espacios.trim(); // "Hola Java";

        //Verificar si empieza y termina

        boolean empiezapor= s1.startsWith("H"); //false
        boolean terminapor =s2.endsWith("a"); //true


        //Conversion

        int num = 12345678;
        String nums = "12345678";

        String numString= String.valueOf(num);
        String empiezapor2=String.valueOf(empiezapor); //"false" en cadena

        int nums2=Integer.parseInt(nums);




        //Buscar dentro de una cadena

        int index1=s1.indexOf('a'); //solo dirá la posicion del 1º char que encuentre.

        //invertir cadena

        String reverse = new StringBuilder(s1).reverse().toString();

        //Ver s hay cosas en blanco
        boolean blanco= s1.isEmpty();


        //StringBuilder y StringBuffer

        /*
        clases usadas para la manipulaciuon de cadenas de carcteres.

        StringBuilder
        No es seguro para hilos: No es sincronizado, lo que lo hace más rápido para uso en un solo hilo.
        Eficiente en rendimiento: Ideal para manipular cadenas cuando se hacen muchas modificaciones.
        Mutable: Permite cambiar el contenido de la cadena sin crear nuevos objetos en memoria.
        Métodos comunes: append() "añadir texto al final", insert(5, "java "), delete(), reverse(), replace()


        StringBuffer
        Seguro para hilos: Sus métodos están sincronizados, lo que lo hace adecuado para entornos multihilo.
        Menos eficiente que StringBuilder: Debido a la sincronización, las operaciones pueden ser más lentas en comparación con StringBuilder.
        Mutable: Al igual que StringBuilder, permite modificar el contenido de la cadena sin crear nuevos objetos.
        Métodos comunes: Al igual que StringBuilder, ofrece métodos como append(), insert(), delete(), reverse(), replace().

         */




    }

    public static void check (String uno, String dos){

        //Palidromo Se lee igual hacia adelante y hacia atrás.

        System.out.println(uno.equals(new StringBuilder(uno).reverse().toString()) ? "ES PALI" :"NO ES PALI");
        System.out.println(uno.equals(new StringBuilder(dos).reverse().toString()) ? "ES PALI" :"NO ES PALI");

        /*
        uno.equals(...):

        uno: Es la cadena original que quieres verificar.
        uno.equals(...): El método equals() compara si la cadena original (uno) es igual a la cadena que se pasa como argumento. Si son iguales, devolverá true; de lo contrario, devolverá false.

        new StringBuilder(uno):
        Aquí creas un nuevo objeto de tipo StringBuilder, que es una clase en Java que permite manipular eficientemente cadenas de texto (a diferencia de String, que es inmutable).
        Pasas la cadena uno como argumento al constructor para que el StringBuilder contenga la misma secuencia de caracteres que uno.

        .reverse():
        El método reverse() invierte el contenido del StringBuilder. Es decir, cambia el orden de los caracteres.


        .toString():
        El método toString() convierte el StringBuilder (que tiene la cadena invertida) de vuelta a un objeto de tipo String.



        El uso de ? y : en Java es parte del operador ternario, que es una forma abreviada de la estructura if-else.
        condición: Una expresión booleana que se evalúa. Si es true, se elige el valor a la izquierda de :, si es false, se elige el valor a la derecha.
        valor_si_true: El valor que se devolverá si la condición es true.
        valor_si_false: El valor que se devolverá si la condición es false.
        */


        //Anagrama  Palabra o frase formada al reorganizar las letras de otra.

        //Vamos a convertir un sitrng a una cadena de carcteres, la ordenamos y revisamos
        char[] cadena1 =uno.toCharArray();
        char[] cadena2 =dos.toCharArray();

        //Metodos de arrays con cada clase, puede haber centenares de metodosd
        Arrays.sort(cadena1);
        Arrays.sort(cadena2);

        System.out.println(Arrays.equals(cadena1,cadena2) ? "Son anagrama" : "No son anagrama");

        //Isograma: Palabra o frase donde ninguna letra se repite.

        System.out.println(uno.length()==uno.chars().distinct().count() ? "Es isosgrama" : "No lo es");
        System.out.println(dos.length()==dos.chars().distinct().count() ? "Es isosgrama" : "No lo es");

        /*
        uno.length: longitud

        uno.chars: Este método devuelve un Stream de int que representa los códigos de los caracteres en la cadena uno.
                   Cada carácter de la cadena se convierte en su valor Unicode (código de carácter).

        disatinc: revisa si son diferentes, eliminado los duplicados

        count: contea los carcteres depues de la eliminacion de carcters

        Resumen:  Esta es la condición que se está evaluando.
                  Compara la longitud original de la cadena (uno.length()) con la cantidad de caracteres únicos en la cadena (uno.chars().distinct().count()).
                  Si ambos valores son iguales, significa que ningún carácter se repite en la cadena, lo que indica que la cadena es un isograma.
                  Si son diferentes, significa que hay al menos un carácter repetido, lo que indica que no es un isograma.

         */

    }




}
