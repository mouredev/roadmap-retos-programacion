public class JerrySantana {
    public static void main(String[] args) {
        unarios(10);
        aritmeticos(5, 8);
        cambioShift(-8, 2);
        relacionales(7, 2);
        bitAbit();
        logicos();
        System.out.println(ternario(true));
        System.out.println(ternario(false));
        asignacion();
        System.out.println("------> Extra <------");
        extra();
    }

    public static void unarios(int value) {
        // Operadores unarios
        System.out.println("------ Operadores unarios.");
        System.out.println("El valor es: " + value);
        System.out.println("valor++: " + value++); // imprime el valor y después le suma 1 (posfijo)
        System.out.println("++valor: " + ++value); // le suma 1 al valor y después lo imprime (prefijo)
        System.out.println("~valor: " + ~value); // si el valor es positivo, le resta el valor a 0, si es negativo lo suma a 0
    }

    public static void aritmeticos(int a, int b) {
        // Operadores aritmeticos
        System.out.println("------ Operadores aritmeticos.");
        System.out.println("a: " + a + ", b: " + b);
        System.out.println("a + b = " + (a + b)); // realizar la suma a + b
        System.out.println("a - b = " + (a - b)); // realiza la resta a - b
        System.out.println("a * b = " + (a * b)); // realiza la multiplicacion a * b
        System.out.println("a / b = " + (a / b)); // realiza la division a / b
        System.out.println("a % b = " + (a % b)); // realiza la operación módulo a % b
    }

    public static void cambioShift(int value, int power) {
        // Operadores de shift o cambio
        System.out.println("------ Operadores shift o de cambio.");
        System.out.println("Valor: " + value + ", potencia: " + power);
        System.out.println("valor << potencia: " + (value << power)); // multiplica el valor por 2 elveado a la potencia
        System.out.println("valor >> potencia: " + (value >> power)); // divide el valor entre 2 elveado a la potencia
        System.out.println("valor >>> potencia: " + (value >>> power)); // divide el valor entre 2 elveado a la potencia, sin considerar el signo
    }

    public static void relacionales(int a, int b) {
        // Operadores relacionales de comparación
        System.out.println("------ Operadores relacionales.");
        System.out.println("a: " + a + ", b: " + b);
        System.out.println("¿a < b? " + (a < b)); // Verifica si el valor a es menor que el valor b
        System.out.println("¿a > b? " + (a > b)); // Verifica si el valor a es mayor que el valor b
        System.out.println("¿a <= b? " + (a <= b)); // Verifica si el valor a es menor o igual al valor b
        System.out.println("¿a >= b? " + (a >= b)); // Verifica si el valor a es mayor o igual al valor b
        String cadena = "Esto es un objeto, instancia de la clase String.";
        System.out.println("cadena: " + cadena);
        System.out.println("¿cadena es una instancia de la clase String? " + (cadena instanceof String)); // Verifica si el objeto es una instancia de cierta clase
        // Operadores relacionales de igualdad
        System.out.println("¿a == b? " + (a == b)); // Verifica si el valor a es igual al valor b
        System.out.println("¿a != b? " + (a != b)); // Verifica si el valor a es diferente al valor b
    }

    public static void bitAbit() {
        // Operadores bitwise
        System.out.println("------ Operadores bitwise.");
        System.out.println("false & true : " + (false&true)); // Bitwise And, verifica ambos valores sin importar si el primer valor es falso o verdadero
        System.out.println("true | true : " + (true|true)); // Bitwise Or inclusivo, verifica ambos valores sin importar si el primer valor es falso o verdadero
        System.out.println("true ^ false : " + (true^false)); // Bitwise Or exclusivo o XOR, verifica si los valores son diferentes
    }

    public static void logicos() {
        // Operadores lógicos
        System.out.println("------ Operadores logicos.");
        System.out.println("false && true: " + (false&&true)); // Logic And, si el primer valor es falso ya no comprueba el segundo valor
        System.out.println("true || false: " + (true||false)); // Logic Or, si el primer valor es verdadero ya no comprueba el segundo valor
    }

    public static String ternario(boolean bool) {
        // Operador ternario
        System.out.println("------ Operador ternario.");
        String verdadero = "Este es el resultado verdadero de un operador ternario.";
        String falso = "Este es el resultado falso de un operador ternario.";
        return bool?verdadero:falso; // Es una forma simplificada de un condicional if - else
        // Se evalua la condición a la izquierda del signo de interrogación
        // Si se cumple la condición se ejecuta el código a la izquierda de los dos puntos
        // Si no se cumple la condición se ejcuta el código a la derecha de los dos puntos
    }

    public static void asignacion() {
        // Operadores de asignación
        System.out.println("-> Operadores de asignacion.");
        int a;
        boolean b;
        System.out.println("a = 5, a = " + (a = 5)); // Le asigna el valor de 5 a la variable a
        System.out.println("a += 2, a = " + (a += 2)); // Le suma 2 a la variable a y el resultado lo asigna a si misma
        System.out.println("a -= 10, a = " + (a -= 10)); // Le resta 10 a la variable a y el resultado lo asigna a si misma
        System.out.println("a *= 4, a = " + (a *= 4)); // Multiplica por 4 a la variable a y el resultado lo asigna a si misma
        System.out.println("a /= 3, a = " + (a /= 3)); // Divide entre 3 a la variable a y el resultado lo asigna a si misma
        System.out.println("a %= 6, a = " + (a %= 6)); // Realiza la operación módulo de a módulo 6 y el resultado lo asigna a si misma
        System.out.println("a <<= 2, a = " + (a<<=2)); // Multiplica a por 2 elevado a la 2 y el resultado lo asigna a si misma
        System.out.println("a >>= 2, a = " + (a>>=2)); // Divide a entre 2 elevado a la 2 y el resultado lo asigna a si misma
        System.out.println("a >>>= 2, a = " + (a>>>=2)); // Divide a entre 2 elevado a la 2, sin tener en cuenta el signo, y el resultado lo asigna a si misma
        System.out.println("b = true " + (b = true)); // Asigna el valor true a la variable b
        System.out.println("b &= b, b = " + (b &= b)); // Verifica el valor de b & b, y el resultado lo asigna a si misma
        System.out.println("b ^= b, b = " + (b ^= b)); // Verifica el valor de b ^ b, y el resultado lo asigna a si misma
        System.out.println("b |= b, b = " + (b |= b)); // Verifica el valor de b | b, y el resultado lo asigna a si misma
    }
    
    public static void extra() {
        for(int i = 10; i < 56; i++) {
            if((i != 16) && (i % 3 != 0) && (i % 2 == 0)) {
                System.out.println(i);
            }
        }
    }
}