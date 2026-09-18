public class DennisGD94 {
    public static void main(String[] args) {





        int a = 5;
        int b = 8;
        int c = 2;
        System.out.println("OPERADORES ARITMÉTICOS: ");

        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (b - c));
        System.out.println("Multiplicación: " + (a * c));
        System.out.println("División: " + (b / c));

        System.out.println("OPERADORES DE COMPARACIÓN: ");

        System.out.println("Igual que: " + (a==b));
        System.out.println("Distinto de: " + (b != c));
        System.out.println("Menor que: " + (c < a));
        System.out.println("Mayor que: " + (c > a));
        System.out.println("Mayor igual que: " + (c >= a));
        System.out.println("Menor igual que: " + (c <= a));

        System.out.println("OPERADORES DE ASIGNACIÓN: ");
        a = 5;
        System.out.println(a);
        a += 4;
        System.out.println(a);
        a -= 3;
        System.out.println(a);
        a /= 2;
        System.out.println(a);
        a *= 4;
        System.out.println(a);
        a %= 2;
        System.out.println(a);


        System.out.println("OPERADORES LÓGICOS: ");

        System.out.println((a > b) && (c > a));
        System.out.println((b < a) && (a > c));
        System.out.println((c < b) || (a == c));
        System.out.println(!(a <= b) && (c < b));

        System.out.println("OPERADORES DE INCREMENTO Y DECREMENTO: ");
        System.out.println("(++)" + "(--)");
        a++;
        System.out.println(a);
        c--;
        System.out.println(c);



        System.out.println("ESTRUCTURAS DE CONTROL: ");
        System.out.println("(if/else)" + "(else-if)" + "(switch)" + "(while)" + "(for)" + "(do-while)" + "(for-each)");
        if(a > b){
            System.out.println("a es mayor que b");
        } else if (a == b) {
            System.out.println("a es igual a b");
        }else{
            System.out.println("a es menor que b");
        }


        String[] list = {"Dennis", "Diana", "Valentina", "Fabio"};
        for(String listNames: list){
            System.out.println(listNames);
        }


        int dia = 3;
        switch (dia){
            case 1 -> System.out.println("Lunes");
            case 2 -> System.out.println("Martes");
            default -> System.out.println("Miercoles");
        }


        System.out.println(b);
        System.out.println(c);

        while (b >= c){
            c++;
            System.out.println("Valor de b: " + (b) + ", " + "Valor de c: " + (c));
        }

        do{
            System.out.println("Valor de c: " + (c));
            b++;
        }while (c < b);

        System.out.println("OPERADOR TERNARIO");
        String resultado = (dia == 3) ? "Es miércoles" : "No es miércoles";
        System.out.println(resultado);




        for(int i = 10; i <= 55; i++){
            if((i % 2 == 0) && (i != 16) && (i % 3 != 0)){
                System.out.println(i);
            }
        }



    }


}
