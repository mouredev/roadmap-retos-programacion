public class Davidr1594 {
    public static void main(String[] args) {
        int a = 10, b=5;
        System.out.println("------Operadores de aritmeticas--------");

        System.out.println("suma");
        System.out.println(a+b);

        System.out.println("Resta");
        System.out.println(a-b);

        System.out.println("Multiplicación");
        System.out.println(a * b);
        
        System.out.println("Division");
        System.out.println(a/b);

        System.out.println("Operadores de asignacion");
        // se utiliza el =
        //a vale 10 pero le asignaremos el valor de b
        a = b;
        //ahora a vale 5

        System.out.println("operador de asignacion simple");
        
        System.out.println("+=");
        a += 5;
        System.out.println(a);

        System.out.println("--------Operadores de Comparacion---------");

        System.out.println("Comparacion: == compara si son iguales");
        System.out.println("!= Pregunta si es distinto a: ");
        System.out.println("<  > menor y mayor que:");
        

        System.out.println("---------Operadores Logicos--------");
        System.out.println("AND o &&");
        if(a > b && a> 0){
            System.out.println(a);
        }else System.out.println(b);

        System.out.println("|| OR");
        if((a>b) || a> 0 ){
            System.out.println(a);
        }else System.out.println(b);

        System.out.println("! NOT");
        if (a != b) {
        System.out.println(a);    
        } else {System.out.println(b);
            
        }

        System.out.println("--------Operadores de incremento y decremento--------");

        System.out.println("++ y -- aumenta el valor de 1 en 1 o lo decrementa");

        System.out.println("----------Operador Ternario-------");
        System.out.println("String mensaje = (edad >= 18) ? \"Eres mayor de edad\" : \"Eres menor de edad\"");
        int resultado = ((a>b)? a:b);

        /*
         Operadores de bits
        Los operadores de bits se utilizan para realizar operaciones a nivel de bits en valores enteros.
        Estos operadores permiten manipular datos binarios y realizar operaciones de desplazamiento de bits. 
        Ejemplos de operadores de bits incluyen & (AND a nivel de bits), | (OR a nivel de bits), ^ (XOR a nivel de bits), 
        << (desplazamiento a la izquierda) y >> (desplazamiento a la derecha).
         */

        //Ejercicio Extra

        System.out.println("ejercicio Extra");
        for (int i = 10; i < 55; i++) {
            if(i != 16 && (i%3 != 0)){
                System.out.print(i+",");
            }
            
        }
    }
}
