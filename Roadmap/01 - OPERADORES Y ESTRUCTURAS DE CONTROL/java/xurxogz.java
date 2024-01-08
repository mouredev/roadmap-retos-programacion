public class xurxogz {
    public static void main(String[] args) {
        // #01 OPERADORES Y ESTRUCTURAS DE CONTROL

        // ASIGNACION
        int num1 = 10;
        System.out.println(num1);

        int num2 = 5;
        System.out.println(num2);

        int num3 = num1 += num2;
        System.out.println(num3);

        int num4 = num1 -= num2;
        System.out.println(num4);

        int num5 = num1 *= num2;
        System.out.println(num5);

        int num6 = num1 /= num2;
        System.out.println(num6);

        int num7 = num1 %= num2;
        System.out.println(num7);

        // ARITMETICOS
        int suma = num1 + num2;
        System.out.println(suma);

        int resta = num1 - num2;
        System.out.println(resta);

        int multiplicacion = num1 * num2;
        System.out.println(multiplicacion);

        int division = num1 / num2;
        System.out.println(division);

        int modulo = num1 % num2;
        System.out.println(modulo);

        // COMPARACION E IDENTIDAD
        boolean resultado1 = num1 > num2;
        System.out.println(resultado1);

        boolean resultado2 = num1 >= num2;
        System.out.println(resultado2);

        boolean resultado3 = num1 < num2;
        System.out.println(resultado3);

        boolean resultado4 = num1 <= num2;
        System.out.println(resultado4);

        boolean resultado5 = num1 == num2;
        System.out.println(resultado5);

        boolean resultado6 = num1 != num2;
        System.out.println(resultado6);

        // LOGICOS
        int edad = 15;
        boolean esMayorDeEdad = edad == 18 || edad > 18;
        System.out.println(esMayorDeEdad);

        boolean esMenorDeEdad = edad < 18 && esMayorDeEdad == false;
        System.out.println(esMenorDeEdad);

        boolean esVerdadero = true;
        boolean esFalso = !esVerdadero;
        System.out.println(esFalso);

        // DIFICULTAD EXTRA (OPCIONAL)
        int var;
        for (var = 10; var <= 55; var++ ) {
            if (var % 2 == 0 && var != 16 && var % 3 == 1) {
                System.out.println(var);
            }
        }
    }
}
