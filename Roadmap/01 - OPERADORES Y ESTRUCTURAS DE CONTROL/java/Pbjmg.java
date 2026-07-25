public class Pbjmg {
    public static void main(String[] args){

        // Operadores aritmeticos
        int suma = 24 + 5;  //29
        double resta = 3.2 - 1.1;   //2.1
        double division = 5 / 2;    //2.5
        int modulo = 6 % 2;     //0
        int multiplicacion = 10 * 2;    //20

        // Operadores logicos
        boolean andLogico = (5 > 3 && 8 > 4);   //true
        boolean notLogico = !(8>2);     //false

        // Operadores de asignacion
        int x = 8; //8
        x += 2;     //10
        x -= 5;     //5
        x *= 4;     //20
        x /= 2;     //10
        x %= 2;     //0

        // Operadores de comparacion
        boolean esIgual = (5 == 5); //true
        boolean esDiferente = (5 != 3); //true
        boolean mayor = (4 > 2);  //true
        boolean menor = (1 < 6); //true
        boolean mayorIgual = (9 >= 9); //true
        boolean menorIgual = (8<=8); //true

        // Operadores de incremento y decremento
        int a =  5; 
        a ++; //6
        int b = 4;
        b--; //3
        int preIncremento = ++a + --b; //9 (incrementa o decrece el valor antes de devolverlo)
        System.out.println(a);
        System.out.println(b);
        System.out.println(preIncremento);

        // Operador ternario
        int edad = 38;
        String mensaje = (edad >= 25) ? "Viejo" : "Joven"; //Viejo
        System.out.println(mensaje);
        //------------------------------------------------

        // Estructuras Condicionales
        //if-else
        edad = 18;
        if (edad>=18) {
            System.out.println("Eres mayor de edad");
        }else {
            System.out.println("Eres menor de edad");
        }

        //if-else if-else
        int nota = 75;
        if(nota>=90) {
            System.out.println("Sobresaliente");
        }else if(nota>=70){
            System.out.println("Notable");
        }else {
            System.out.println("Aprobado");
        }

        //Switch
        int dia = 5;
        String resultado = switch (dia) {
            case 1 -> "Lunes";
            case 2 -> "Martes";
            case 3 -> "Miercoles";
            case 4 -> "Jueves";
            case 5 -> "Viernes";
            case 6 -> "Sabado";
            case 7 -> "Domingo";
            default -> "No valido";
        };
        System.out.println(resultado);

        //Estructuras repetitivas, Bucles
        //While
        int i = 0;
        while(i <= 5) {
            System.out.println(i);
            i++;
        }

        //do-while
        int j = 0;
        do {
            System.out.println(j);
            j++;
        }while(j<=5);

        //for
        for(int k = 0; k <=5; k++) {
            System.out.println("Iteracion: " + k);
        }

        //for-each
        int[] lista = {1,2,3,4,5};
        for(int num : lista) {
            System.out.print(num);
        }

        // Estructuras de control, interrupcion
        //break
        for(i = 0; i < 10; i++) {
            if(i == 5) { 
                break; // Se detiene la iteracion en 5
            }
            System.out.println(i);
        }

        //continue
        for(i = 0; i < 10; i++) {
            if(i == 5) {
                continue; // Se salta el numero 5
            }
            System.out.println(i);
        }

        //return
        System.out.println(sumar(10,25));
        System.out.println();
        
        //------------------ Opcional
        /*
        Imprimimos por pantalla los numeros comprendidos del 10 al 55 incluidos
        que sean pares, saltandonos el 16 y que no sean multiplos de 3
         */ 
        for(i = 10; i <= 55; i++) {
            if(i%2==0 && i != 16 && i %3 != 0){
                System.out.println(i);
            }
        }

        
    }

    //return
    public static int sumar (int num1,int num2) {
        return num1 + num2;
    }
}
