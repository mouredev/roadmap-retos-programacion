public class francescvm8 {
    public static void main(String[] args) {
        int a=10,b=5;
        // Operadores aritméticos
        System.out.println("Operadores aritméticos");
        System.out.println("Suma: "+(a+b)); 
        System.out.println("Resta: "+(a-b));
        System.out.println("Multiplicación: "+(a*b));
        System.out.println("División: "+(a/b)); 
        System.out.println("Módulo: "+(a%b));
        System.out.println("Incremento: "+(++a));
        System.out.println("Decremento: "+(--b));
        System.out.println("Negación: "+(-a));
        System.out.println("Complemento a 1: "+(~a));
        System.out.println("Desplazamiento a la izquierda: "+(a<<1));
        System.out.println("Desplazamiento a la derecha: "+(a>>1));
        System.out.println("Desplazamiento a la derecha sin signo: "+(a>>>1));
        System.out.println("AND: "+(a&b));
        System.out.println("OR: "+(a|b));
        System.out.println("XOR: "+(a^b));

        // Operadores de comparación
        System.out.println("\nOperadores de comparación");
        System.out.println("Igualdad: "+(a==b));
        System.out.println("Desigualdad: "+(a!=b));
        System.out.println("Mayor que: "+(a>b));
        System.out.println("Menor que: "+(a<b));
        System.out.println("Mayor o igual que: "+(a>=b));
        System.out.println("Menor o igual que: "+(a<=b));

        // Operadores lógicos
        System.out.println("\nOperadores lógicos");
        System.out.println("AND lógico: "+(a>b && a<b));
        System.out.println("OR lógico: "+(a>b || a<b));
        System.out.println("NOT lógico: "+!(a>b));

        // Operadores de asignación
        System.out.println("\nOperadores de asignación");
        System.out.println("Asignación: "+(a=b));
        System.out.println("Suma y asignación: "+(a+=b));
        System.out.println("Resta y asignación: "+(a-=b));
        System.out.println("Multiplicación y asignación: "+(a*=b));
        System.out.println("División y asignación: "+(a/=b));
        System.out.println("Módulo y asignación: "+(a%=b));
        System.out.println("Desplazamiento a la izquierda y asignación: "+(a<<=b));
        System.out.println("Desplazamiento a la derecha y asignación: "+(a>>=b));
        System.out.println("Desplazamiento a la derecha sin signo y asignación: "+(a>>>=b));
        System.out.println("AND y asignación: "+(a&=b));
        System.out.println("OR y asignación: "+(a|=b));
        System.out.println("XOR y asignación: "+(a^=b));

        // Operadores de identidad
        System.out.println("\nOperadores de identidad");
        System.out.println("Igualdad de objetos: "+(a==b));
        System.out.println("Desigualdad de objetos: "+(a!=b));

        // Operadores de pertenencia
        System.out.println("\nOperadores de pertenencia");
        System.out.println("Pertenece: "+(a instanceof Integer));
        
        // Estructuras de control
        System.out.println("\nEstructuras de control");
        
        // Condicionales
        if(a>b) {
            System.out.println("a es mayor que b");
        } else {
            System.out.println("a es menor que b");
        }
        
        // Iterativas
        for(int i=0;i<5;i++) {
            System.out.println("Iteración "+i);
        }

        // Excepciones
        try {
            int c = a/0;
        } catch(ArithmeticException e) {
            System.out.println("No se puede dividir por 0");
        }
        
        // Números entre 10 y 55, pares y no múltiplos de 3 ni 16
        System.out.println("\nNúmeros entre 10 y 55, pares y no múltiplos de 3 ni 16");
        for(int i=10;i<=55;i++) {
            if(i%2==0 && i!=16 && i%3!=0) {
                System.out.println(i);
            }
            
        }
    }
}