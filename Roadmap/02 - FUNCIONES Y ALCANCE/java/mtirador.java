public class mtirador {
    public static void main(String[] args) {
        

       
        int num= 7;

        Saludo();
        Saludo2("Hola a todos");
        combinacion("Este es el numero de la suerte", num);
        System.out.println(suma(num, num)); 
        System.out.println(random());
        extra("multiplo de 3", "multiplo de 5");

    }

    /*Sin parámetros ni retorno */
    private static void Saludo(){
        System.out.println("Hola Mundo");
    }
    
    /*con un parámetro y sin retorno */
    private static void Saludo2(String frase){
        System.out.println(frase);
    }

    /*Con dos parámetros y sin retorno */
    private static void combinacion(String frase,int num){

        System.out.println(frase+num); 
    }

    /*función con retorno y dos parámetros */

    private static int suma(int num1,int num2){ 
        int resultado=num1+num2;
        System.out.println("El resultado de la suma entre "+ num1+ " y "+ num2+ " = ");
       
        return resultado;
    }

    /*función dentro de función */

    private static int random(){
        int ale = (int) (Math.random()*25+1);
        System.out.println("El número aleatorio entre 1 y 25 es: ");

        return ale;
        
    }

    /*Ejercicio Extra */
    /*
 
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

    private static int extra(String text1,String text2){

        int cont=0;
        System.out.println(" ");
        System.out.println("Ejercicio Extra: ");
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(text1 + " y "+text2);
            } else if (i % 3 == 0) {
                System.out.println(text1);
            } else if (i % 5 == 0) {
                System.out.println(text2);
            } else {
                System.out.println(i);
                cont++;
            }
        }
        return cont;
    }



}
