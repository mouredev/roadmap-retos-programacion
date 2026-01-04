import java.util.Calendar;

public class FranDev200 {

    static Calendar calendar = Calendar.getInstance();
    static int currentYear = calendar.get(Calendar.YEAR);

    static void main() {
        /*
            - Crea ejemplos de funciones básicas que representen las diferentes
            posibilidades del lenguaje:
            Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
         */

        welcome();
        System.out.println("Este año, cumples " + age(2005) + " años.");
        info("Franciso", 20, "Desarrollador de Software");
        payRise("Fran", 2000, 15);

        /*
            DIFICULTAD EXTRA (opcional):
            Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
            - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
            - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
            - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
            - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
            - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

         */

        System.out.println("Numero de veces que se ha impreso solo el numero: " + printNumber("Hola Java", "Adios Java"));

    }

        /*
            - Crea ejemplos de funciones básicas que representen las diferentes
            posibilidades del lenguaje:
            Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
         */

    public static void welcome(){
        System.out.println("Bienvenido a los retos de programación");
    }

    public static int age (int yearOfBirth){

        int age = FranDev200.currentYear - yearOfBirth;
        return age;
    }

    public static void info(String name, int age, String work){
        System.out.println(name + " tiene " + age + " años y su trabajo es ser " + work);
    }

    public static void payRise(String name, double actualSalary, int ageExperience){

        double newSalary = actualSalary + (actualSalary * percentageIncrease(ageExperience) / 100);

        System.out.println(name + " ha pasado de cobrar " + actualSalary + "€, a cobrar "  + newSalary + "€." );
        System.out.println("Esto es gracias a sus " + ageExperience + " años de experiencia en el sector.");

    }

    private static double percentageIncrease(int ageExperience){

        int percentage = 0;

        if(ageExperience == 0){
            percentage = 0;
        }else if(ageExperience == 1){
            percentage = 10;
        } else if (ageExperience < 5) {
            percentage = 20;
        }else if(ageExperience < 10){
            percentage = 30;
        }else if(ageExperience >= 10){
            percentage = 40;
        }

        return percentage;
    }

        /*
            DIFICULTAD EXTRA (opcional):
            Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
            - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
            - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
            - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
            - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
            - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

         */

    public static int printNumber(String text1, String text2){

        int onlyNumberPrint = 0;

        for (int i = 1; i <= 100; i++){

            if( (i % 3) == 0 && (i % 5) == 0){
                System.out.println(text1 + "  ||  " + text2);

            }else if( (i % 3) == 0){
                System.out.println(text1);
            }else if( (i % 5) == 0){
                System.out.println(text2);
            }else{
                System.out.println(i);
                onlyNumberPrint++;
            }

        }

        return onlyNumberPrint;

    }

}
