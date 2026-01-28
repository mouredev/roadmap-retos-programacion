public class LogicaJava01 {
    
    public static void main(String[] args) {
    
        // 1.
        int a = 10; // Asignación
        a += 2; // Asignación (se puede combinar con cualquier operador aritmético)
        int b = 3;
        
        System.out.println(a + b); // suma
        System.out.println(a - b); // resta
        System.out.println(a * b); // multiplicación
        System.out.println(a / b); // división
        System.out.println(a % b); // módulo
        
        System.out.println(a == b);
        System.out.println(a != b);
        System.out.println(a > b);
        System.out.println(a < b);
        System.out.println(a >= b);
        System.out.println(a <= b);
        
        boolean t = true;
        boolean f = false;
        
        System.out.println(t && f); // AND
        System.out.println(t || f); // OR
        System.out.println(!t);     // NOT
        
        String s1 = "Java";
        String s2 = "Java";
        
        System.out.println(a == b);        // false (distintas referencias)
        System.out.println(s1.equals(s2));   // true (mismo contenido)
        
        Object obj = "Hola";
        
        System.out.println(obj instanceof String);
        System.out.println(obj instanceof Integer);
        
        int m = 5;  // 0101
        int n = 3;  // 0011

        System.out.println(m & n);  // AND
        System.out.println(m | n);  // OR
        System.out.println(m ^ n);  // XOR
        System.out.println(m << 1); // desplazamiento izquierda
        System.out.println(m >> 1); // desplazamiento derecha
        
        // 2.
        if (a > b) {
            System.out.println("a es mayor que b");
        } else {
            System.out.println("b es mayor o igual que a");
        }

        int dia = 2;
        switch (dia) {
            case 1 -> System.out.println("Lunes");
            case 2 -> System.out.println("Martes");
            default -> System.out.println("Otro día");
        }

        for (int i = 0; i < 3; i++) {
            System.out.println(i);
        }

        int contador = 0;
        while (contador < 3) {
            System.out.println(contador);
            contador++;
        }
        
        // EXTRA
        for (int i=10;i<56;i++) {
            if (i%2==0 && i!=16 && i%3!=0) {
                System.out.println(i);
            }
        }
    }
}
