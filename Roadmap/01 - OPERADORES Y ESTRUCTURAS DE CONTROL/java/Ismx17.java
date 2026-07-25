public class Ismx17 {
    public static void main(String[] args) {
        
        //Operadores Aritmeticos
        int num1 = 5;
        int num2 = 2;

        System.out.println("Operadores Aritmeticos");
        System.out.println("Suma: " + (num1 + num2));
        System.out.println("Resta: " + (num1 - num2));
        System.out.println("Multiplicacion: " + (num1 * num2));
        System.out.println("Division: " + (num1 / num2));
        System.out.println("Modulo: " + (num1 % num2));
        System.out.println("Incremento: " + (++num1));
        System.out.println("Decremento: " + (--num2));
        System.out.println();

        //Operadores Logicos
        boolean a = true;
        boolean b = false;

        System.out.println("Operadores Logicos");
        System.out.println("AND: " + (a&&b));
        System.out.println("OR: " + (a||b));
        System.out.println("NOT: " + (!a));
        System.out.println();

        //Operadores de Comparacion
        System.out.println("Operadores de Comparacion");
        System.out.println("Igualdad: " + (num1 == num2));
        System.out.println("Desigualdad: " + (num1 != num2));
        System.out.println("Mayor que: " + (num1 > num2));
        System.out.println("Menor que:" + (num1 < num2));
        System.out.println("Mayor o igual que: " + (num1 >= num2));
        System.out.println("Menor o igual que: " + (num1 <= num2));
        System.out.println();

        //Operadores de Asignacion
        System.out.println("Operadores de Asignacion");
        System.out.println("Asignacion: " + (num1 = num2));
        System.out.println("Suma y asignacion: " + (num1 += num2));
        System.out.println("Resta y asignacion: " + (num1 -= num2));
        System.out.println("Multiplicacion y asignacion: " + (num1 *= num2));
        System.out.println("Division y asignacion: " + (num1 /= num2));
        System.out.println("Modulo y asignacion: " + (num1 %= num2));
        System.out.println();

        //Ejemplos de estructuras de control
        System.out.println("Ejemplos de estructuras de control");

        //IF - ELSE IF - ELSE
        if (num1 < num2) {
            System.out.println("El numero es mayor");
        } else if (num1 > num2){
            System.out.println("El numero es menor");
        } else {
            System.out.println("El numero es igual");
        }
        System.out.println();

        // DO - WHILE
        int i = 0;
        do {
            System.out.println("Iteracion" + i);
            i++;
        } while (i < 5);
        System.out.println();

        //WHILE
        int j = 5;
        while (j <= 5 && j > 0) {
            System.out.println("Iteracion " + i);
            i--;
        }

        //EJERCICIO EXTRA
        System.out.println("EJERCICIO EXTRA");
        for (int k = 10; k <= 55; k++) {
            if (k != 16 && k % 3 != 0 && k % 2 == 0) {
                System.out.println(k);
            }
            if (k == 55) {
                break;
            }
            else {
                System.out.println(k);
            }
        }
    }
}
