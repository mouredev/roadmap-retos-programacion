package MauroDevRetos;

public class reto_1 {
    
        public static void main(String[] args) {
            // Operadores Aritméticos
            int a = 10;
            int b = 3;
            System.out.println("Suma: " + (a + b));
            System.out.println("Resta: " + (a - b));
            System.out.println("Multiplicación: " + (a * b));
            System.out.println("División: " + (a / b));
            System.out.println("Módulo: " + (a % b));

            // Operadores Lógicos
            boolean x = true;
            boolean y = false;
            System.out.println("AND lógico: " + (x && y));
            System.out.println("OR lógico: " + (x || y));
            System.out.println("NOT lógico: " + (!x));

            // Operadores de Comparación
            System.out.println("Igual: " + (a == b));
            System.out.println("No igual: " + (a != b));
            System.out.println("Mayor que: " + (a > b));
            System.out.println("Menor que: " + (a < b));
            System.out.println("Mayor o igual que: " + (a >= b));
            System.out.println("Menor o igual que: " + (a <= b));

            // Operadores de Asignación
            int c = 5;
            c += 3; // c = c + 3
            System.out.println("Suma asignación: " + c);
            c -= 2; // c = c - 2
            System.out.println("Resta asignación: " + c);
            c *= 4; // c = c * 4
            System.out.println("Multiplicación asignación: " + c);
            c /= 3; // c = c / 3
            System.out.println("División asignación: " + c);
            c %= 3; // c = c % 3
            System.out.println("Módulo asignación: " + c);

            // Operadores de Identidad
            Integer d = Integer.valueOf(5);
            Integer e = Integer.valueOf(5);
            System.out.println("Igualdad de referencia: " + (d == e)); // false
            System.out.println("Igualdad de valor: " + (d.equals(e))); // true

            // Operadores a Nivel de Bits
            int f = 5; // 0101 en binario
            int g = 3; // 0011 en binario
            System.out.println("AND a nivel de bits: " + (f & g)); // 0001
            System.out.println("OR a nivel de bits: " + (f | g)); // 0111
            System.out.println("XOR a nivel de bits: " + (f ^ g)); // 0110
            System.out.println("Complemento a nivel de bits: " + (~f)); // 1010 (en complemento a dos)
            System.out.println("Desplazamiento a la izquierda: " + (f << 1)); // 1010
            System.out.println("Desplazamiento a la derecha: " + (f >> 1)); // 0010
            System.out.println("Desplazamiento a la derecha sin signo: " + (f >>> 1)); // 0010

            // Estructuras Condicionales
            if (a > b) {
                System.out.println("a es mayor que b");
            } else {
                System.out.println("a no es mayor que b");
            }

            int dia = 3;
            switch (dia) {
                case 1:
                    System.out.println("Lunes");
                    break;
                case 2:
                    System.out.println("Martes");
                    break;
                case 3:
                    System.out.println("Miércoles");
                    break;
                case 4:
                    System.out.println("Jueves");
                    break;
                case 5:
                    System.out.println("Viernes");
                    break;
                case 6:
                    System.out.println("Sábado");
                    break;
                case 7:
                    System.out.println("Domingo");
                    break;
                default:
                    System.out.println("Día inválido");
                    break;
            }

            // Estructuras Iterativas
            // for loop
            for (int i = 0; i < 5; i++) {
                System.out.println("for loop: " + i);
            }

            // while loop
            int j = 0;
            while (j < 5) {
                System.out.println("while loop: " + j);
                j++;
            }

            // do-while loop
            int k = 0;
            do {
                System.out.println("do-while loop: " + k);
                k++;
            } while (k < 5);

            // foreach loop
            int[] array = { 1, 2, 3, 4, 5 };
            for (int num : array) {
                System.out.println("foreach loop: " + num);
            }

            // Manejo de Excepciones
            try {
                int resultado = 10 / 0;
                System.out.println("Resultado: " + resultado);
            } catch (ArithmeticException i) {
                System.out.println("Error: División por cero");
            } finally {
                System.out.println("Bloque finally ejecutado");
            }
            /*
             * Crea un programa que imprima por consola todos los números comprendidos
             * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
             */

            for (int i = 10; i <= 55; i++) {
                if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                    System.out.println("numero" + i);
                }

            }
        }
    }

