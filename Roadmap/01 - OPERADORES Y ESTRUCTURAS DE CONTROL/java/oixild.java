
/*
*   Suma + o +=
*   Resta - o -=
*   Multiplicación * o *=
*   División / o /=
*   Módulo % o %=
*   Incremento ++
*   Decremento --
*   Igual a ==
*   Distinto de !=
*   Mayor que >
*   Menor que <
*   Mayor o igual a >=
*   Menor o igual a <=
*   Y &&
*   O ||
*/

public class oixild {
    public static void main(String[] args) {

        int num1 = 10, num2 = 10, num3 = 5, num4 = 15;

        System.out.println(num1 + num2);
        System.out.println(num1 - num3);
        System.out.println(num1 * num2);
        System.out.println(num1 / num2);

        System.out.println(num1 % num4 + "\n");

        ++num1;
        --num2;
        System.out.println(num1);
        System.out.println(num2 + "\n");

        int num5 = 10, num6 = 10;

        if (num5 == num6)
            System.out.println("num5 y num6 son iguales");
        if (num5 != num1)
            System.out.println("num5 y num1 son diferentes");
        if (num5 > num1)
            System.out.println("num5 es mayor que num1");
        if (num1 < num5)
            System.out.println("num1 es menor que num5");
        if (num5 >= num6)
            System.out.println("num5 es mayor o igual num6");
        if (num6 <= num5)
            System.out.println("num6 es menor o igual num5\n");
        if (num1 == 11 && num5 == 10)
            System.out.println("num1 es igual a 11 y num5 es igual a 10");
        if (num1 != 13 && num5 != 13)
            System.out.println("num1 no es igual a 13 y num5 no es igual a 13\n");

        for (int i = 0; i <= 5; i++)
            System.out.println("i = " + i);
        System.out.println("\n");

        // DIFICULTAD EXTRA (OPCIONAL)

        int start = 10, end = 55;

        while (start < end && start >= 10) {
            if (start == 16 || start % 3 == 0)
                ++start;
            if (start <= end)
                System.out.println(start);
            ++start;
        }
    }
}