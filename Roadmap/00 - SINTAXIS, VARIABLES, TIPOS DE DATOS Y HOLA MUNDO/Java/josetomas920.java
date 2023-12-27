import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class josetomas09 {

// Esta es una introduccion al lenguaje de Java.
// es posible que le falten elementos, lo estoy aprendiendo :D

// Link de la web oficial: https://www.oracle.com/es/java/

//      ### Estructura Basica ###

    //      ==== Declaracion de una clase ====
    public class josetomas09 { // public hace referencia a que la "class(clase) Introduccion" se puede acceder desde cualquier otra clase.

        public static void main(String[] args) { // "static" refiere a que es una clase estatica, "void" quiere decir que no devuelve nada, "main" es la clase "principal" donde se ejecuta todo el codigo.

            //      === Hola mundo! ===
            System.out.println("Hola, Java!");


            //      === Variables ===

            // Enteros
            int entero = 10;            // int = Valores unicamente enteros, es decir, sin coma.
            long largo = 1000000L;      // long = Es identico a int pero con mas espacio en memoria para almacenar mas digitos.

            // Decimales
            float decimal = 3.14f;      // float = Valores decimales, es decir, numeros con coma.
            double doble = 2.71828;     // double = Tiene un rango mucho mayor y puede representar numeros en un mayor rango.

            // Caracteres y Cadenas
            char caracter = 'A';                // char = character(caracter) es solamente una letra, se suele representar con comillas simples ''.
            String cadena = "Hola, Mundo!";     // String = cadena de caracteres, es decir, varias char unidas, se suele representar con comillas dobles " :) ".

            // Booleanos
            boolean verdadero = true;       // boolean = booleano, variables con unicamente dos estados TRUE(verdadero) y FALSE(falso)
            boolean falso = false;          // Generalmente es para representar estados, ej: si o no, 1 o 0, V o F, etc.


            //      === Operaciones Simples ===

            //Operaciones con Strings.
            String myString = "Esto es una cadena de texto";
            System.out.println("myString");
            myString = "Aquí cambio el valor de la cadena de texto";
            System.out.println(myString);

            // Operaciones con Enteros(int).
            Integer myInt = 7;
            System.out.println(myInt);
            myInt = myInt + 4;
            System.out.println("myInt = myInt + 4 es igual a " + myInt);    // Se pueden concatenar o juntar Strings y variables u otras Strings para imprimirlos por pantalla.
            System.out.println(myInt - 1);                                  // Se pueden hacer operaciones simples dentro del Print.

            // Decimales.
            Double myDouble = 6.5;
            System.out.println(myDouble);
            Float myFloat = 6.5f;
            System.out.println(myFloat);

            // Concatenacion de distintos tipos de datos.

            System.out.println(myDouble + " " + myString + " " + myFloat + " " + myInt);

            // Booleanos.
            Boolean myBoolean = true;
            myBoolean = false;
            System.out.println(myBoolean);
            myBoolean = null;
            System.out.println(myBoolean);

            //      === Constantes ===

            final String myConstant = "Esto es una cadena de texto constante";  // "final" indica constante, "String" indica el tipo de dato(puede ser otro), las constantes no varian con el tiempo.

            //      === Control de flujo ===

            if (Condicion1){
                // Se ejecuta el codigo si "Condicion1" es TRUE(verdadero)
            } else if (Condicion2) {
                // Se ejecuta el codigo si "Condicion2" es TRUE(verdadero)
            } else {
                // Se ejecuta si ninguna de las condiciones es verdadera
            }
    /*
                    #### Operadores ####

        === Operadores Aritmeticos ===
            + (suma)
            - (resta)
            * (multiplicación)
            / (división)
            % (módulo, devuelve el resto de la división)


        === Operadores de Asignacion ===
            = (asignación)
            +=, -=, *=, /=, %= (operadores de asignación compuesta)
            Ejemplo:
            int x = 10;
            x += 5; // x ahora es 15 (equivalente a x = x + 5)


        === Operadores de Incremento/Decremento ===
            ++ (incremento) // Incrementa en 1.
            -- (decremento) // Decrementa en 1.
            Ejemplo:
            int contador = 0;
            contador++; // incrementa contador en 1


        === Operador Ternario ===
            "? :" (operador ternario) // Es "parecido" al if pero mas simple o resumido, si la condicion es TRUE se ejecuta lo que esta a la Izquierda de los ":" de lo contrario se ejecuta lo otro.
            Ejemplo:
            int edad = 20;
            String mensaje = (edad >= 18) ? "Mayor de edad" : "Menor de edad";


        === Igualdad ===
            ==  : Comprueba si dos valores son iguales.
            !=  : Comprueba si dos valores no son iguales.


        === Comparación ===
            <   : Menor que.
            >   : Mayor que.
            <=  : Menor o igual que.
            >=  : Mayor o igual que.


        === Operadores lógicos ===
            &&  :   AND   lógico (también conocido como "y" lógico). Devuelve true si ambas expresiones son true.
            ||  :   OR    lógico (también conocido como "o" lógico). Devuelve true si al menos una de las expresiones es true.
            !   :   NOT   lógico (también conocido como "no" lógico). Invierte el valor de una expresión booleana.


        === Comparación de objetos ===
            equals():    Método utilizado para comparar si dos objetos son iguales en términos de contenido. Se usa comúnmente con objetos de la clase String.
    */

            //      === Operaciones Simples ===

            myFloat = null;
            if (myFloat != null) {
                System.out.println(myFloat + 10);
                System.out.println("My Float es distinto de nulo");
            } else {
                System.out.println("My Float es nulo");
            }

            if (myInt == 11) {
                System.out.println("myInt == 11");
            } else if (myInt == 12) {
                System.out.println("myInt == 12");
            } else {
                System.out.println("El valor no es ni 11 ni 12");
            }

            //      === Switches ===
            switch (expresion) {
                case valor1:
                    // Código a ejecutar si la expresion es igual a valor1.
                    break;
                case valor2:
                    // Código a ejecutar si la expresion es igual a valor2.
                    break;
                // Puedes tener más casos según sea necesario.
                default:
                    // Código a ejecutar si ninguno de los casos anteriores coincide.
            }
            // Ejemplo:

            int diaDeLaSemana = 3;

            switch (diaDeLaSemana) {
                case 1:
                    System.out.println("Lunes");
                    break;
                case 2:
                    System.out.println("Martes");
                    break;
                case 3:
                    System.out.println("Miércoles");
                    break;
                // Otros casos según sea necesario
                default:
                    System.out.println("Día no válido");
            }


            //      === Listas/Arrays ===

            List<String> myList = new ArrayList();
            myList.add(myString);
            myList.add(myInt.toString());
            System.out.println(myList);

            //      === Mapas ===

            Map<String, String> myMap = new HashMap();
            myMap.put("string", myString);
            myMap.put("int", myInt.toString());
            System.out.println(myMap);
            System.out.println(myMap.get("int"));

            //      === Bucles ===

            // "FOR": El bucle for es útil cuando conoces la cantidad exacta de veces que deseas que se repita el código.

            for (inicialización; condición; actualización) {
                // Código a repetir
            }

            // Ejemplo:
            for (int i = 0; i < 5; i++) {
                System.out.println("Iteración " + i);
            }

            // "WHILE": El bucle while se utiliza cuando no conoces de antemano cuántas veces se ejecutará el código y la repetición depende de una condición booleana.

            while (condición) {
                // Código a repetir
            }

            // Ejemplo:
            int contador = 0;
            while (contador < 5) {
                System.out.println("Iteración " + contador);
                contador++;
            }

            // "DO-WHILE": El bucle do-while es similar al while, pero garantiza que el código dentro del bucle se ejecute al menos una vez, ya que la condición se evalúa después de la primera ejecución.

            do {
                // Código a repetir
            } while (condición);

            // Ejemplo:
            int contador = 0;
            do {
                System.out.println("Iteración " + contador);
                contador++;
            } while (contador < 5);


            //      === Clases ===

            chuleta myMain = new chuleta();
            System.out.println(myMain.myFunction(5, 2));
            System.out.println(myMain.myFunction(3, 126389));
        }
    }
}
