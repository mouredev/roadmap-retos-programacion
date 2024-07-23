import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class YellowDev {
    public static void main(String[] args) {
        int value = 1;
        //Operadores

        //Sufijo
        value++;
        System.out.println(value); //Ahora vale dos
        value--;
        System.out.println(value); //Vuelve a valer uno
        //Unario
        value = -value;
        System.out.println(value); //Como solamente se aplica a un valor no es una resta sino una negacion, negar 1 es igual a -1
        value = +value;
        System.out.println(value); //No cambiara su valor debido a que si seguimos las leyes de los signos negativo mas positivo es negativo
        value = --value;
        System.out.println(value); //Ahora si relaiza el decremento pero solamente en uno dando como resultado -2
        value = ++value;
        System.out.println(value); //Ahora se realiza el aumento en uno
        value = ~value;
        System.out.println(value); //Como este valor utiliza los bits del valor qu3 en este caso es -1 al invertirlos se obtiene el 0 en binario.Por ello muestra 0

        //Multiplicativo

        value = 2;
        //Multiplicacion
        value = value * value;
        System.out.println(value); //Se obtiene 4 de multiplicar 2 * 2
        //Division
        value = value / value;
        System.out.println(value); //Se obtiene 1 de dividir 1 / 1
        //Modulo
        value = value % value;
        System.out.println(value); //Se obtiene 0 ya que es el resto de dividir 1/1

        //Aditivo

        int value2 = 5;
        //Suma
        int result = value2 + value;
        System.out.println(result); //Se obtiene 5 de sumar 0 de value y 5 de value2
        //Resta
        result = result - 3;
        System.out.println(result); //Se obtiene 2 de restarle 3 a 5

        //Cambio

        value = 2; //El valor en binario de 2 es 0000 0010
        value = value << 2;
        System.out.println(value); //En este caso el valor binario se recorre hacia la izquierda dos veces, dando como resultado 0000 1000 que es 8
        value = value >> 3;
        System.out.println(value); //Ahora recorrimos 3 a la derecha entonces es 0000 0001 que es 1
        //En caso del signo >>> la diferencia resalta en que se recorre la n cantidad de veces y llena de 0 a la izquierda

        //Relacional

        //Mayor que
        int value1 = 5;
        value2 = 8;
        System.out.println(value1 > value2); //Hace la comparacion de los valores y devuelve un valor booleanos, en este caso es false porque 5 no es mayor que 8
        //Menor que
        System.out.println(value1 < value2); //En este caso si es true debido a que 5 si es menor que 8
        int value3 = 5;
        //Menor igual
        System.out.println(value1 <= value3); //Aqui se hace una verificacion doble en donde verifica si el primer valor es menor o igual que el segundo valor, en este caso no es menor pero si es igual
        //Mayor igual
        System.out.println(value2 >= value3); //Y aqui aunque no son igual el value2 si es mayor que value3
        //Intanceof, en este caso se puede usar para comparar instancias de diferentes objetos, nos devuelve valores booleanos con respecto si una isntancia se encuentra o no

        //Igualdad

        System.out.println(value == value2); //value=1, value2=8, como no son iguales devuelve un valor false
        System.out.println(value != value2); //Devuelve un valor true ya que si son valores diferentes
        //AND bit a bit
        int value4 = 5;
        int value5 = 8;
        System.out.println(value5 & value4);
        //Imprime 0 porque no hay ninguna coincidencia del numero 1 en la misma posicion
        /*Lo que pasa en esta ocasion es que compara todos los digitos del numero binario
          entonces si ambos son 1 el resultado sera 1 pero si hay un 0 el resultado sera sero, al final se saca
          el valor generado de la comparacion de los binarios y surge un nuevo binario y ese es el resultado, solamente
          se hace la conversion*/
        //OR exclusivo bit a bit
        System.out.println(value5 ^ value4); //Lo mismo que el anterior pero si hay al menos un numero entonces el valor es 1, dando como resultado 13
        //OR inclusivo |
        System.out.println(value5 | value4); //Retorna un 1 si y solo si uno de los valores en 1, pero si ambos son 1 devuelve un 0, en este caso imprime 13 nuevamente
        //Y logico
        //Su uso mas comun en las condicionales en donde el valor debe de cumplir una serie de reglas para que sea verdadera la condicional y sesguir con el flujo del codigo
        if (value2 < 2 && value3 > 5) {
            System.out.println("Yiyi");
        } else {
            System.out.println("No yiyi");
        }
        //OR logico
        //Este es como el Y logico pero la diferencia radica en que si al menos un valor es verdadera la condicional se vuelve true
        if (value2 < 2 || value3 > 5) {
            System.out.println("Siu yiyi");
        } else {
            System.out.println("Nou yiyi");
        }

        /*
         * Ternario
         * EL uso de este se asemeja a la condicional if, donde se evalua una condicion y en base a si es true o false se brinda un resultado:
         * */

        boolean seraTrue = false;
        value = 1;
        value1 = 2;
        result = seraTrue ? value : value1;
        System.out.println(result);

        //Asignacion

        //igual
        int newValue = 52;
        System.out.println(newValue);
        //Mas igual
        newValue += 52;
        System.out.println(newValue); //Le suma la cantidad y luego le agrega el valor si lo ponemos al reves no se refleja el cambio debido a que la suma no ocurre
        //Menos igual
        newValue -= 2;
        System.out.println(newValue); //Le resta la cantidad y luego le asigna el valor
        //Multiplicar igual
        newValue *= 2;
        System.out.println(newValue); //Le multiplica y asigna el valor
        //Dividir igual
        newValue /= 4;
        System.out.println(newValue); //Le divide y asigna el valor
        //Modulo igual
        newValue %= 4;
        System.out.println(newValue); //Le saca el modulo y asigna el valor
        //&=, ^=, |=, <<=, >>=, >>>= estos operadores usan los ejemplos anteriores con los bits, entonces hace la funcion y asigna valor en una sola accion

        //Estructuras de control
        //Selectivas de seleccion o condicionales
        //if
        boolean moving = false;
        if (moving) {
            System.out.println("Stop");  //Selectiva simple
        } else if (moving == false) {    //Selectiva doble
            System.out.println("god");
        } else {
            System.out.println("God job");
        }
        //Iterativas, de iteracion, de repeticion o repetitivas
        //while
        int contador = 5;
        while (contador <= 8) {
            System.out.println("Si");
            contador++;
        }

        //Do while
        contador = 3;
        do {
            System.out.println("Yiyi");
            contador++;
        } while (contador <= 5);

        //for
        int result10 = 1;
        for (int i = 0; i < 10; i++) {
            result10++;
            System.out.println(result10); //Dato curioso se pueden hacer un ciclo infinito si se dejan los parametros del for vacios
        }

        //for each
        int[] numbers = {1, 2, 3, 4, 5};
        for (int numeber : numbers) {
            System.out.println(numeber);
        }
        //Declaracion Break
        int MyVariable = 6;
        for (int i = 0; i < 10; i++) {
            if (i != MyVariable) {
                System.out.println(i);
            } else {
                break; //Terminar bucles
            }
        }
        //Declaracion continue
        int MyVariable2 = 6;
        for (int i = 0; i < 10; i++) {
            if (i != MyVariable2) {
                System.out.println(i);
            } else {
                continue;  //Saltar el flujo en el punto que sea 6
            }
        }
        //Declaracion return
       /*
       *  int Myvariable3 = 5;
        if (Myvariable3 < 10) {
            return Myvariable3 + 3;
        }
        System.out.println(Myvariable3);
        return 0;
       * */

        //Declaracion yield
        String weekDay = "Thursday";
        int dayNumber = switch (weekDay) {
            case "MONDAY", "FRIDAY", "SUNDAY" -> 1;
            case "TUESDAY" -> 2;
            case "THURSDAY", "SATURDAY" -> {
                System.out.println("It's either Thursday or Saturday!");
                yield 3; // Usamos yield para devolver un valor después de ejecutar más instrucciones
            }
            case "WEDNESDAY" -> 4;
            default -> {
                System.out.println("Invalid day: " + weekDay);
                yield -1; // Usamos yield para devolver un valor predeterminado en caso de un día no válido
            }
        };
        System.out.println(dayNumber);
        //Switch case
        String subject = "Maths";
        switch (subject) {
            case "Maths" -> System.out.println("Maths");
            case "Sunny" -> System.out.println("Sunny");
            case "Algebraic" -> System.out.println("Algebraic");
        }
        //Try catch
        PrintWriter out = null;
/*
        try {
            System.out.println("Entering" + " try statement");

            out = new PrintWriter(new FileWriter("OutFile.txt"));
            for (int i = 0; i < SIZE; i++) {
                out.println("Value at: " + i + " = " + list.get(i));
            }
        } catch (IndexOutOfBoundsException e) {
            System.err.println("Caught IndexOutOfBoundsException: "
                    +  e.getMessage());

        } catch (IOException e) {
            System.err.println("Caught IOException: " +  e.getMessage());

        } finally {
            if (out != null) {
                System.out.println("Closing PrintWriter");
                out.close();
            }
            else {
                System.out.println("PrintWriter not open");
            }
        }

 */
        //Ejercicio extra
        for (int i = 10; i <=  55; i++) {
            if (i == 16 || (i % 3 == 0)) {
                continue;
            }
            System.out.println(i);
        }
    }
}
