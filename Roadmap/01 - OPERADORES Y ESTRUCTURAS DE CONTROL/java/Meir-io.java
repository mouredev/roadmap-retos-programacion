public class Meir {
    public static void main(String[] args) {
        // Operadores aritmeticos
        int suma = 10 + 5;
        int resta = 10 - 5;
        int multiplicacion = 10 * 5;
        int division = 10 / 5;
        int modulo = 10 % 5;

        //Operadores de comparacion
        boolean esMayor = 10 > 5;
        boolean esMenor = 10 < 5;
        boolean esIgual = 10 == 5;
        boolean esDiferente = 10 != 5;
        boolean esMayorIgual = 10 >= 5;
        boolean esMenorIgual = 10 <= 5;

        //Operadores logicos
        boolean y = true && true;
        boolean o = true || false;
        boolean no = !true;

        //Operadores de asignacion
        int x = 10;
        x += 5;
        x -= 1;
        x *= 2;
        x /= 2;
        x %= 2;
        x++;
        x--;

        for (int i = 10; i <= 55; i++){
            if (i % 2 == 0 && i != 16 && i % 3 == 0){
                System.out.println(i);
            }
        }


    }
}
