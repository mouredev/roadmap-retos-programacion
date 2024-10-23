import java.util.ArrayList;
import java.util.List;

public class danhingar {

    public static void main(String[] args) {

        int numero1 = 2;
        int numero2 = 6;
        float numero3 = 8.5f;
        byte numero4 = 3;

        // OPERADORAS ARITMÉTICOS
        int suma = numero1 + numero2;
        System.out.println("Resultado suma: " + suma);
        int resta = numero4 - numero1;
        System.out.println("Resultado resta: " + resta);
        float multiplicacion = numero3 * numero1;
        System.out.println("Resultado multiplicacion: " + multiplicacion);
        double division = numero3 / numero1;
        System.out.println("Resultado division: " + division);
        int divisionEntera = (int) (numero3 / numero1);
        System.out.println("Resultado divisionEntera: " + divisionEntera);
        int modulo = numero2 % numero1;
        System.out.println("Resultado modulo: " + modulo);
        double exponente = Math.pow(numero1, 2);
        System.out.println("Resultado exponente: " + exponente);

        // OPERADORES COMPARACIÓN
        boolean esIgual = numero1 == numero2;
        System.out.println("Igualdad: " + esIgual);
        boolean noIgual = numero2 != numero3;
        System.out.println("Desigualdad: " + noIgual);
        boolean mayorQue = numero1 > numero2;
        System.out.println("Mayor que: " + mayorQue);
        boolean menorQue = numero2 < numero3;
        System.out.println("Menor que: " + menorQue);
        boolean mayorIgualQue = numero4 >= numero1;
        System.out.println("Mayor o igual que: " + mayorIgualQue);
        boolean menorIgualQue = numero2 <= numero1;
        System.out.println("Menor o igual que: " + menorIgualQue);

        // OPERADORES LÓGICOS
        boolean and = numero1 > numero2 && numero2 < numero3;
        System.out.println("Operador &&: " + and);
        boolean or = numero1 > numero2 || numero2 < numero3;
        System.out.println("Operador ||: " + or);
        boolean negacion = !or;
        System.out.println("Negacion !: " + negacion);

        // OPERADORES DE ASIGNACIÓN
        int myNumber = 10;
        System.out.println("myNumber " + myNumber);
        myNumber += 3;
        System.out.println("myNumber " + myNumber);
        myNumber -= 1;
        System.out.println("myNumber " + myNumber);
        myNumber *= 4;
        System.out.println("myNumber " + myNumber);
        myNumber /= 8;
        System.out.println("myNumber " + myNumber);
        myNumber ^= 7;
        System.out.println("myNumber " + myNumber);
        myNumber %= 1;
        System.out.println("myNumber " + myNumber);
        myNumber >>= 1;
        System.out.println("myNumber " + myNumber);
        myNumber <<= 1;
        System.out.println("myNumber " + myNumber);
        myNumber |= 1;
        System.out.println("myNumber " + myNumber);
        myNumber &= 1;
        System.out.println("myNumber " + myNumber);

        // Condicionales
        String nombre = "Daniel";
        if (nombre == "Daniel") {
            System.out.println("nombre es 'Daniel'");
        } else if (nombre == "Pepe") {
            System.out.println("nombre es 'Pepe'");
        } else {
            System.out.println("nombre es indefinido");
        }

        switch (nombre) {
            case "Daniel":
                System.out.println("Hola Daniel");
                break;
            case "Pepe":
                System.out.println("Hola Pepe");
                break;
            default:
                System.out.println("Hola desconocido");
        }

        String saludo = nombre.equals("Daniel") ? "Hola Daniel" : "Hola desconocido";
        System.out.println(saludo);

        // Iterativas
        for (int i = 0; i < 12; i++) {
            System.out.println(i);
        }

        List<String> names = List.of("Daniel", "Paco", "Pepe", "Luis");
        // Itera todas una colección
        for (String name : names) {
            System.out.println(name);
        }

        while (numero2 > 1) {
            System.out.println(numero2);
            numero2--;
        }

        // Excepciones
        try {
            int divisionError = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Error aritmetico");
        } finally {
            System.out.println("Finalizado el manejo de excepciones");
        }

        // EJERCICIO EXTRA
        for (int j = 10; j < 56; j++) {
            if (j != 16 && j % 2 == 0 && j % 3 != 0) {
                System.out.println(j);
            }
        }
    }
}
