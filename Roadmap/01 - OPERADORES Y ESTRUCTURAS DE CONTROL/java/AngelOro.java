public class AngelOro {

    public static void cicloFor(){
        System.out.println("Números par del 0 al 300");
        for (int i = 0; i <= 300; i+=2){
            System.out.println(i);
        }
    }

    public static void cicloWhile(int a){
        System.out.println("Ciclo while");
        while (a > 0){
            System.out.println(a);
            a--;
        }
    }

    public static void main(String[] args) {
        /*
         * Operadores aritméticos
         */
        int num1 = 20;
        int num2 = 9;

        System.out.println("Operadores aritméticos");
        //Suma
        int resultado = num1 + num2;
        System.out.println(num1 + " + " + num2 + " = " + resultado );

        //Resta
        resultado = num1 - num2;
        System.out.println(num1 + " - " + num2 + " = " + resultado);

        //Multiplicación
        resultado = num1 * num2;
        System.out.println(num1 + " * " + num2 + " = " + resultado);

        //División
        resultado = num1 / num2;
        System.out.println(num1 + " / " + num2 + " = " + resultado);

        //Residuo
        resultado = num1 % num2;
        System.out.println(num1 + " % " + num2 + " = " + resultado);

        /*
         *Operadores combinados
         */


        System.out.println("Operadores combinados");
        //num1 = num1 + num2
        num1+=num2;
        System.out.println(num1);

        //num1 = num1 - num2
        num1-=num2;
        System.out.println(num1);

        //num1 = num1 * num2
        num1*=num2;
        System.out.println(num1);

        //num1 = num1 / num2
        num1/=num2;
        System.out.println(num1);

        //num1 = num1 % num2
        num1%=num2;
        System.out.println(num1);

        /*
         * Operadores de relación
         */

        System.out.println("Operadores de relación");
        //Igual que
        boolean relacion = num1 == num2;
        System.out.println(num1+" == "+num2+" = "+relacion);

        //Distinto que
        relacion = num1 != num2;
        System.out.println(num1+" != "+num2+" = "+relacion);

        //Menor que
        relacion = num1 < num2;
        System.out.println(num1+" < "+num2+" = "+relacion);

        //Mayor que
        relacion = num1 > num2;
        System.out.println(num1+" > "+num2+" = "+relacion);

        //Menor o Igual que
        relacion = num1 <= num2;
        System.out.println(num1+" <= "+num2+" = "+relacion);

        //Mayor o Igual que
        relacion = num1 >= num2;
        System.out.println(num1+" >= "+num2+" = "+relacion);

        /*
         * Operadore lógicos
         */

        System.out.println("Operadores lógicos");
        //Negación NOT
        relacion = !(num1 == num2);
        System.out.println("!("+num1+" == "+num2+") = "+relacion);

        //OR
        relacion = (num1 < num2) | (num1 == num2);
        System.out.println("("+num1+" < "+num2+") | ( "+num1+" == "+num2+") = "+relacion);

        //XOR
        relacion = (num1 > num2) ^ (num1 == num2);
        System.out.println("("+num1+" > "+num2+") ^ ( "+num1+" == "+num2+") = "+relacion);

        //AND
        relacion = (num1 < num2) & (num1 != num2);
        System.out.println("("+num1+" < "+num2+") & ( "+num1+" != "+num2+") = "+relacion);

        //||
        relacion = (num1 <= num2) || (num1 == num2);
        System.out.println("("+num1+" <= "+num2+") || ( "+num1+" == "+num2+") = "+relacion);

        //&&
        relacion = (num1 <= num2) && (num1 == num2);
        System.out.println("("+num1+" <= "+num2+") && ( "+num1+" == "+num2+") = "+relacion);

        /*
         * Operadores de bit
         */

        System.out.println("Operadores bit");
        num1 = 14;
        num2 = 18;
        //~ : Negación
        System.out.println("~"+num1 + " = " + ~num1 );

        //| : Suma lógica binaria
        System.out.println(num1 + " | " + num2 +" = " + (num1|num2) );

        //^ : Suma lógica exclusiva
        System.out.println(num1 + " ^ " + num2 +" = " + (num1^num2) );

        //& : Producto lógico binario
        System.out.println(num1 + " & " + num2 +" = " + (num1&num2) );

        //<<:
        System.out.println(num1 + " << " + num2 +" = " + (num1<<num2) );

        //>>:
        System.out.println(num1 + " >> " + num2 +" = " + (num1>>num2) );

        //Ciclos
        cicloFor();
        cicloWhile(10);

    }
}