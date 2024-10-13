
// EJERCICIO #01: OPERADORES Y ESTRUCTURAS DE CONTROL

public class zemanue {
    public static void main(String[] args) {
        
        int a = 10, b = 2;
        System.out.println("Variables: a = " + a + ", b = " + b);

        System.out.println("OPERADORES ARITMÉTICOS/ALGEBRAICOS:");
        System.out.println("- Suma: a + b = " + (a + b));
        System.out.println("- Resta: a - b = " + (a - b));
        System.out.println("- Multiplicación: a * b = " + (a * b));
        System.out.println("- División: a / b = " + (a / b));
        System.out.println("- Módulo/resto: a % b = " + (a % b));

        System.out.println("OPERADORES DE INCREMENTO y DECREMENTO:");
        a++;
        System.out.println("- Incremento: a++ = " + a);
        a--;
        System.out.println("- Decremento: a-- = " + a);

        System.out.println("OPERADORES DE ASIGNACIÓN:");
        b = 5;
        System.out.println("- Asignación: b = 5 --> b = " + b);
        b += 10;
        System.out.println("- Suma y asignación: b += 10 --> b = " + b);
        b -= 3;
        System.out.println("- Resta y asignación: b -= 3 --> b = " + b);
        b *= 2;
        System.out.println("- Multiplicación y asignación: b *= 2 --> b = " + b);
        b /= 8;
        System.out.println("- División y asignación: b /= 8 --> b = " + b);

        System.out.println("OPERADORES RELACIONALES/DE COMPARACIÓN:");
        System.out.println("- Igualdad: a == b = " + (a == b));
        System.out.println("- Desigualdad: a!= b = " + (a != b));
        System.out.println("- Mayor que : a > b = " + (a > b));
        System.out.println("- Menor que : b < a = " + (a < b));
        System.out.println("- Mayor o igual a: a >= 11 = " + (a >= 11));
        System.out.println("- Menor o igual a: b <= 3 = "+ (b <= 3));

        System.out.println("OPERADORES LÓGICOS:");
        System.out.println("- && (AND): (a < 100 && a > 1) = " + (a < 100 && a > 1));
        System.out.println("- || (OR): (a < 10 || b > 1) = " + (a < 10 || b > 1));
        System.out.println("- ! (NOT): !(b == 30) = " + !(b == 30));

        System.out.println("OPERADOR TERNARIO: \"?\" y \":\" ");
        int mayor = (a > b) ? a : b;
        System.out.println("int mayor = (a > b) ? a : b --> " + mayor);


        System.out.println("ESTRUCTURAS DE CONTROL");
        System.out.println("CONDICIONALES");
        System.out.println("- IF-ELSE: ");
        String resultado;
        if (a > b) {
            resultado = "a es mayor que b";
        } else if (a < b) {
            resultado = "b es mayor que a";
        } else {
            resultado = "a y b son iguales";
        }
        System.out.println(resultado);
        
        System.out.println("ITERATIVAS (BUCLES)");
        System.out.println("- FOR:");
        for (int i = 0; i < 10; i++) {
            System.out.print(i);
        }
        System.out.println("");

        System.out.println("- FOR EACH:");
        String[] cuatroLetras = new String[] {"a", "b", "c", "d"};
        for (String string : cuatroLetras) {
            System.out.print(string);
        }
        System.out.println("");

        System.out.println("- WHILE:");
        int c = 15;
        while (c > a) {
            System.out.print(c + "-");
            c--;
        }
        System.out.println("");

        System.out.println("- DO WHILE: ");
        do {
            System.out.println("Se imprime al menos una vez");
        } while (a < b);

        System.out.println("EXCEPCIONES: ");
        System.out.println("Try-catch:");
        try {
            c /= 0;
        } catch (ArithmeticException divisionEntre0) {
            System.out.println("No se puede dividir entre 0");
        }

        System.out.println("EJERCICIO OPCIONAL:");
        for (int i = 10; i < 56; i++) {
            if ((i % 2 != 0)
                    && i != 16
                    && i % 3 != 0) {
                System.out.println(i);
            }
        }
    }
}
