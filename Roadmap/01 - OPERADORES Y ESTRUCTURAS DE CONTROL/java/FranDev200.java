import java.sql.SQLOutput;
import java.util.HashMap;
import java.util.Map;

public class FranDev200 {

    static void main() {

        /*
           - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
           Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
           (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
        */

        int a = 3;
        int b = 4;

        // OPERADORES ARITMÉTICOS
        // - Suma
        System.out.println(a + b);

        // - Resta
        System.out.println(a - b);

        // - Multiplicación
        System.out.println(a * b);

        // - División
        System.out.println(a / b);

        // - Módulo
        System.out.println(a % b);

        // OPERADORES DE ASIGNACIÓN
        // - Igualación
        System.out.println(a = 7);

        // - Igualación con suma
        System.out.println(a += 3);

        // - Igualación con resta
        System.out.println(a -= 1);

        // - Igualación con multiplicación
        System.out.println(a *= 5);

        // - Igualación con división
        System.out.println(a /= 6);

        // - Igualación con módulo
        System.out.println(a %= 9);

        // OPERADORES DE COMPARACIÓN
        // - Igual que
        System.out.println(a == b);

        // - Distinto que
        System.out.println(a != b);

        // - Mayor que
        System.out.println(a > b);

        // - Menor que
        System.out.println(a < b);

        // - Mayor o igual que
        System.out.println(a >= b);

        // - Menos o igual que
        System.out.println(a <= b);

        // OPERADORES LÓGICOS
        // - AND
        System.out.println(true && true);
        System.out.println(true && false);
        System.out.println(false && true);
        System.out.println(false && false);

        // - OR
        System.out.println(true || true);
        System.out.println(true || false);
        System.out.println(false || true);
        System.out.println(false || false);

        // - NOT
        System.out.println(!true);
        System.out.println(!false);

        // Mix de los tres operadores
        System.out.println(!(true && false) || (false || !true));

        // OPERADORES UNARIOS
        System.out.println(-b);

        System.out.println(--a);

        System.out.println(a--);
        System.out.println(a);

        System.out.println(++b);

        System.out.println(b++);
        System.out.println(b);


        //OPERADOR DE CONCATENACIÓN
        System.out.println("El valor de la variable 'a' es: " + a + ". Y el valor de la variable 'b' es: " + b);


        /*
            - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
            que representen todos los tipos de estructuras de control que existan en tu lenguaje:
            Condicionales, iterativas, excepciones...
         */

        if(a >= b){
            System.out.println("El valor de a es mayor al de b");
        }else if(a <= b){
            System.out.println("El valor de a es menor al de b");
        }else if(a == b){
            System.out.println("a y b tienen el mismo valor");
        }

        for(int i = 0; i <= (a + b); i++){
            System.out.println(i);
        }

        System.out.println("Resultados del bucle while");
        int c = 1;
        while( c > 0 && c <= 10){
            System.out.println(c);
            c = 1;
            c = (int) (Math.random() * 20 ) + 1;
        }

        int numRand = 0;
        do{
            if(numRand < 7){
                System.out.println("Hola Java");
            }else{
                break;
            }
            numRand = (int) (Math.random() * 10 ) + 1;
        }while (true);

        HashMap<String, Double> examResults = new HashMap<>();
        examResults.put("Pedro", 3.5);
        examResults.put("Alicia", 4.7);
        examResults.put("Jose", 8.3);
        examResults.put("Inma", 9.1);
        examResults.put("David", 6.8);
        examResults.put("Alba", 1.0);
        examResults.put("Fran", 5.0);

        System.out.println("Notas del examen de programación");
        System.out.println("================================");
        for (Map.Entry<String, Double> map: examResults.entrySet()){
            System.out.print(map.getKey() + " -> " + map.getValue());

           if(map.getValue() < 5 ){
               System.out.println(" SUSPENDIDO");
           }else{
               System.out.println(" APROBADO");
           }
        }

        int[] months = {5, 2, 1, 2, 5, 1, 7, 8, 9, 5, 8, 10, 12, 11, 1, 13, 20, 1};

        for(int month: months){
            switch (month){
                case 1:
                    System.out.println("Enero");
                    break;
                case 2:
                    System.out.println("Febrero");
                    break;
                case 3:
                    System.out.println("Marzo");
                    break;
                case 4:
                    System.out.println("Abril");
                    break;
                case 5:
                    System.out.println("Mayo");
                    break;
                case 6:
                    System.out.println("Junio");
                    break;
                case 7:
                    System.out.println("Julio");
                    break;
                case 8:
                    System.out.println("Agosto");
                    break;
                case 9:
                    System.out.println("Septiembre");
                    break;
                case 10:
                    System.out.println("Octurbe");
                    break;
                case 11:
                    System.out.println("Noviembre");
                    break;
                case 12:
                    System.out.println("Diciembre");
                    break;
                default:
                    System.out.println("Ese mes no existe.");
            }
        }

        /*
            - DIFICULTAD EXTRA (opcional):
            Crea un programa que imprima por consola todos los números comprendidos
            entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
         */

        System.out.println("EJERCICIO EXTRA");
        System.out.println("===============");
        for(int i = 10; i >= 10 && i <= 55; i++){

            if(i == 16 || (i % 2) != 0 || (i % 3) == 0){
                continue;
            }

            System.out.println(i);
        }

    }

}
