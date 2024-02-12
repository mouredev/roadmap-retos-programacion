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

        // CONDICIONAL - IF
        if (num1 < num2) {
            System.out.println( num1 + " es mayor que " + num2);
        }
        else if (num1 > num2) {
            System.out.println(num1 + " es menor que " + num2);
        }
        else {
            System.out.println(num1 + " es igual que " + num2);
        }

        // CONDICIONAL - SWITCH
        String diasDeLaSemana = "Martes";
        switch (diasDeLaSemana) {
            case "Lunes":
                System.out.println("Hoy es Lunes");
                break;
            case "Martes":
                System.out.println("Hoy es Martes");
                break;
            case "Miercoles":
                System.out.println("Hoy es Miércoles");
                break;
            case "Jueves":
                System.out.println("Hoy es Jueves");
                break;
            case "Viernes":
                System.out.println("Hoy es Viernes");
                break;
            default:
                System.out.println("Hoy es fin de semana");
                break;
        }

        // BUCLE -  DOWHILE
        int contador1 = 10;
        do {
            System.out.println(contador1);
            contador1 --;
        } while (contador1 >= 0);

        // BUCLE WHILE
        int contador2 = 1;
        while (contador2 >= 10) {
            System.out.println(contador2);
            contador2++;
        }

        // BUCLE FOR
        int contador3;
        for (contador3 = 0; contador3 <= 10; contador3++) {
            System.out.println(contador3);
        }

        // DIFICULTAD EXTRA (OPCIONAL)
        int var;
        for (var = 10; var <= 55; var++ ) {
            if (var % 2 == 0 && var != 16 && var % 3 == 1) {
                System.out.println(var);
            }
        }
    }
}