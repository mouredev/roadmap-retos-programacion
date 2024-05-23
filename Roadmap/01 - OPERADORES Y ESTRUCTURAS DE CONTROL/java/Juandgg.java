public class Juandgg {

    /*
         * 
         * // Operadores Aritméticos
        int suma = 10 + 5;         // Suma
        int resta = 10 - 5;        // Resta
        int multiplicacion = 10 * 5;    // Multiplicación
        int division = 10 / 5;      // División
        int modulo = 10 % 3;        // Módulo (resto de la división)
        
        // Operadores de Incremento/Decremento
        int contador = 0;
        contador++;         // Incremento
        contador--;         // Decremento
        
        // Operadores de Asignación
        int a = 10;
        a += 5;             // a = a + 5;
        a -= 3;             // a = a - 3;
        a *= 2;             // a = a * 2;
        a /= 4;             // a = a / 4;
        a %= 3;             // a = a % 3;
        a <<= 2;            // a = a << 2;
        a >>= 1;            // a = a >> 1;
        a &= 5;             // a = a & 5;
        a ^= 3;             // a = a ^ 3;
        a |= 2;             // a = a | 2;
        
        // Operadores de Relación
        boolean esIgual = (a == 10);    // Igual a
        boolean noEsIgual = (a != 10);  // No igual a
        boolean mayorQue = (a > 5);     // Mayor que
        boolean menorQue = (a < 15);    // Menor que
        boolean mayorIgualQue = (a >= 10);  // Mayor o igual que
        boolean menorIgualQue = (a <= 10);  // Menor o igual que
        
        // Operadores Lógicos
        boolean andLogico = (esIgual && mayorQue);    // AND lógico
        boolean orLogico = (esIgual || mayorQue);     // OR lógico
        boolean notLogico = !esIgual;                 // NOT lógico
        
        // Operadores de Bitwise (a nivel de bits)
        int x = 5 & 3;      // AND a nivel de bits
        int y = 5 | 3;      // OR a nivel de bits
        int z = 5 ^ 3;      // XOR a nivel de bits
        int complemento = ~5;   // NOT a nivel de bits (complemento a uno)
        int desplazamientoIzq = 5 << 2;    // Desplazamiento a la izquierda
        int desplazamientoDer = 20 >> 2;   // Desplazamiento a la derecha
        int desplazamientoDerSinSigno = 20 >>> 2;  // Desplazamiento a la derecha sin signo
        
        // Operador Ternario
        int edad = 18;
        String mensaje = (edad >= 18) ? "Es mayor de edad" : "Es menor de edad";
        
        // Otros Operadores
        String nombre = "Juan";
        boolean esInstancia = (nombre instanceof String);  // Comprueba si es una instancia de String

        //operadores de identidad

        Object miObj =new Object() ;
        //valida si un objecto es igual  a otro cuando me refiero a igual es que ocupa el mismo espacio en memmoria y demas osea que es el mismo por eso en java las cadenas no se comparan directamente asi si no que lo hacen por medio .equals(String o cadena) para el caspo de  numeros y demas esto es validp
        System.out.println(Object==Object)


         */

    //EJEMPLOS
    public static enum EnumOperacionCalculo {
        SUMA("+"),
        RESTA("-"),
        MULTIPLICACION("*"),
        DIVISION("/");
        //agregar operadores etc...
    
        private final String operador;
    
        EnumOperacionCalculo(String operador) {
            this.operador = operador;
        }
    
        public String getOperador() {
            return operador;
        }
    
        
        public static EnumOperacionCalculo validarEntrada(String text) {
            for (EnumOperacionCalculo op : EnumOperacionCalculo.values()) {
                if (op.operador.equals(text)) {
                    return op;
                }
            }

            

            throw new IllegalArgumentException("Operación no válida: " + text);
        }
    }
    

    public static int operacionCalculo(int n1, int n2 ,EnumOperacionCalculo op){
        //ejemplos basicos
        switch (op) {
            case SUMA:
                return n1 + n2;
            case RESTA:
                return n1 - n2;
            case MULTIPLICACION:
                return n1 * n2;
            case DIVISION:
                if (n2 != 0) {
                    return n1 / n2;
                } else {
                    throw new IllegalArgumentException("No se puede dividir por cero");
                }
                
        }

        //error de operacion
        return 0 ;
    }

    public static void dificultadExtra(){
        //  DIFICULTAD EXTRA (opcional):
        //  * Crea un programa que imprima por consola todos los números comprendidos
        //  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.


        for(int i =10 ;i<=55;i++ ){
            if((i % 2 ==0)&&(i!=16)&&(i % 3 !=0)){
                System.out.println(i);
            }
            
        }
    }


    public static void main(String[] args) {
        

        //Ejmplos
        //puedes agregar o intercambiar operaciones
        //int op =Juandgg.operacionCalculo(2, 2, Juandgg.EnumOperacionCalculo.SUMA);
        //System.out.println(op);


        System.out.println("\nSOLUCION EJERCICIO DIFICULTAD EXTRA\n");
        Juandgg.dificultadExtra();


    }
      

      



}
