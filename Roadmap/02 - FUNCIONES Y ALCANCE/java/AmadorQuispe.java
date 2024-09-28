import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class AmadorQuispe {
    // Esto es una variable GLOBAL, accesible desde toda la clase.
    static String user;

    public static void main(String[] args) {
        welcomeSystem();
        // Esto es una variable LOCAL solo es accesible desde el método main
        Scanner sc = new Scanner(System.in);
        printQuestion("Ingresa tu nombre :");
        user = sc.next();
        String greeting = greeting(user);
        printMessage(greeting);
        printMessage("El sistema puede hacer estos trabajos");
        printMessage("[A] Operación simple (+,-,* y / de dos números) ");
        printMessage("[B] Operación multiple (+, - y * de varios números) ");
        printMessage("[C] Factorial de un número");
        printQuestion("Ingresa la opción :");
        String job = sc.next();
        printMessage("Seleccionaste la opción " + jobSelected(job));
        if (job.equalsIgnoreCase("A")) {
            printMessage("Dentro de las operaciones simples tenemos :");
            printMessage("(1) Suma");
            printMessage("(2) Resta");
            printMessage("(3) Multiplicación");
            printMessage("(4) División");
            printMessage("(5) Potencia");
            printQuestion("Digita el número de la operación :");
            String selected = sc.next();
            printMessage("Haz seleccionado " + operationSelected(selected) + ", ahora ingresa los números.");
            printQuestion("Ingresa el número 1 :");
            double number1 = sc.nextDouble();
            printQuestion("Ingresa el número 2 :");
            double number2 = sc.nextDouble();
            double result = operation(selected, number1, number2);
            printMessage("El resultado de la operación " + operationSelected(selected) + " :");
            printMessage("" + number1 + " y " + number2 + " es: " + result);
        } else if (job.equalsIgnoreCase("B")) {
            printMessage("Dentro de las operaciones multiples tenemos :");
            printMessage("(1) Suma");
            printMessage("(2) Resta");
            printMessage("(3) Multiplicación");
            printQuestion("Digita el número de la operación :");
            String selected = sc.next();
            printMessage("Haz seleccionado " + operationSelected(selected) + ", ahora ingresa los números.");
            printQuestion("Ingresa los números separado por una coma (,) ejemplo 1,2,3 :  ");
            String input = sc.next();
            Double[] numbers = stringToArray(input);
            double result = operationsMultipleNumbers(selected, numbers);
            printMessage("El resultado de la operación " + operationSelected(selected) + " :");
            printMessage("" + input + " es: " + result);
        } else if (job.equalsIgnoreCase("C")) {
            printMessage("Factorial de un número :");
            printQuestion("Ingresa el número positivo :");
            int number = sc.nextInt();
            long result = factorial(number);
            printMessage("El factorial de " + number + " es " + result);
        } else {
            printMessage("La opción que seleccionaste no existe");
        }

        sc.close();
        printMessage(exitSystem());

    }

    /*
     * Función sin parametro ni retorno.
     */
    static void welcomeSystem() {
        System.out.println("------------------------------");
        System.out.println("----Bienvenido al sistema-----");
        System.out.println("------------------------------");
    }

    /*
     * Función que recibe un parametro pero no retorna ningún valor.
     */
    static void printMessage(String message) {
        System.out.println(message);
    }

    static void printQuestion(String question) {
        System.out.print(question);
    }

    /*
     * Función sin parametro y con retorno.
     */
    static String exitSystem() {
        return "Gracias por usar el sistema " + user + " regresa pronto.";
    }

    static String greeting(String name) {
        return "Hola, bienvenido " + name;
    }

    /*
     * Función que recibe un parametro y retorna un valor.
     * 
     * @Return: Double[]
     */
    static Double[] stringToArray(String sNumbers) {
        List<Double> numbers = new ArrayList<>();
        String[] numbersSplit = sNumbers.split(",");
        for (int i = 0; i < numbersSplit.length; i++) {
            numbers.add(Double.parseDouble(numbersSplit[i]));
        }
        return numbers.toArray(new Double[0]);
    }

    /*
     * Función que recibe un parametro y retorna un valor.
     */
    static String jobSelected(String input) {
        return switch (input) {
            case "A":
                yield "[A] Operación simple";
            case "B":
                yield "[B] Operación multiple";
            case "C":
                yield "[C] Factorial";
            default:
                yield "No soportado";
        };
    }

    /*
     * Función que recibe un parametro y retorna un valor.
     */
    static String operationSelected(String input) {
        String operation = switch (input) {
            case "1":
                yield "(1) Suma";
            case "2":
                yield "(2) Resta";
            case "3":
                yield "(3) Multiplicación";
            case "4":
                yield "(4) División";
            case "5":
                yield "(5) Potencia";

            default:
                yield "No soportado";
        };
        return operation;
    }

    /*
     * Función que recibe varios parametros y retorna un valor.
     */
    static double operation(String operator, double number1, double number2) {
        switch (operator) {
            case "1":
                return number1 + number2;
            case "2":
                return number1 - number2;
            case "3":
                return number1 * number2;
            case "4":
                return number1 / number2;
            case "5":
                // Aquí usamos una función propio del lenguaje
                return Math.pow(number1, number2);

            default:
                throw new RuntimeException("Operación no soportada");
        }
    }

    /*
     * Función que recibe un parametro de tipo cadena y un varargs (o argumentos
     * variables) de tipo Double
     * y retorna un valor
     */
    static double operationsMultipleNumbers(String operator, Double... numbers) {
        // Esto es una variable local, es accesible solo dentro del scope metodo.
        double total = 0;
        switch (operator) {
            case "1":
                for (int i = 0; i < numbers.length; i++) {
                    total += numbers[i];
                }
                break;
            case "2":
                for (int i = 0; i < numbers.length; i++) {
                    total -= numbers[i];
                }
                break;
            case "3":
                total = 1;
                for (int i = 0; i < numbers.length; i++) {
                    total *= numbers[i];
                }
                break;

            default:

                break;
        }

        return total;
    }

    /*
     * Función recursivo: Una función recursiva es una función que se llama a sí
     * misma durante su ejecución
     */
    static long factorial(int num) {
        if (num == 0) {
            return 1;
        } else {
            return num * factorial(num - 1);
        }
    }

    // Eercicio extra
    static int fizzBuzz(String fizz, String buzz) {
        int count = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0) {
                System.out.println(fizz);
            } else if (i % 5 == 0) {
                System.out.println(buzz);
            } else if (i % 5 == 0 && i % 3 == 0) {
                System.out.println(fizz + buzz);
            } else {
                System.out.println(i);
                count++;
            }
        }
        return count;
    }

}
