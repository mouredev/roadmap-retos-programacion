public class DomingoAndres {

    public static void main(String[] args) {

        //-------------OPERADORES----------------

        //Operadores Aritmeticos
        int a = 10; //variables para usar 
        int b = 5; //en las operaciones

        System.out.println("Suma: 10 + 5 = " + (a+b));
        System.out.println("Resta: 10 - 5 = " + (a-b));
        System.out.println("Division: 10 / 5 = " + (a/b));
        System.out.println("Modulo: 10 % 5 = " + (a%b));
        
        //Operadores de comparacion
        System.out.println("Mayor que: 10 > 5: " + (a>b));
        System.out.println("Menor que: 10 < 5: " + (a<b));
        System.out.println("Igualdad: 10 = 5: " + (a==b));
        System.out.println("Desigualdad: 10 != 5: " + (a!=b));
        System.out.println("Mayor o igual que: 10 >= 5: " + (a>=b));
        System.out.println("Menor o igual que: 10 <= 5: " + (a<=b));

        //Operadores Logicos
        System.out.println("AND &&: 10 + 5 == 15 && 10 - 5 == 5: " + (a + b == 15 && a - b == 5));
        System.out.println("OR ||: 10 + 5 == 15 && 10 - 5 == 5: " + (a + b == 15 || a - b == 5));
        System.out.println("NOT !: 10 + 3 == 14: " + (a + b != 14));

        //Operadores de asignacion
         a = 7; // Un solo signo = es asignacion
         a += 3; //suma y asinacion
         a -= 4; //resta y asgnacion
         a *= 2; //multiplicacion y asignacion
         a /= 2; //Division y asignacion
         a %= 2; //Modulo y asignacion

         //Operadores de bit
        System.out.println("AND: 10 & 5: " + (a & b));
        System.out.println("OR: 10 | 5: " + (a | b));
        System.out.println("XOR: 10 ^ 5: " + (a ^ b));
        

         //------------ESTRUCTURAS DE CONTROL--------------

         //Condicionales (IF)
        if (b > 0){
            System.out.println("Se cumplio la condicion");
        }

        // Iteracion con ciclo for
        for (int i = 0; i < b; i++){
            System.out.println("Iteracion " + i);
        }

        // Iteracion con ciclo while
        while (b < 10){
            System.out.println("Estoy dentro del ciclo");
            b ++;
        }

        //Iteracion con ciclo do-while
        do{
            System.out.println("Aca tambien estoy dentro del ciclo");
            b --;
        } while (b > 5);

        //usando switch
        switch(b){
            case 3:
                System.out.println("No me voy a ejcutar porque b vale 5");
            case 4:
                System.out.println("Tampoco me voy a ejecutar");
            case 5:
                System.out.println("Me ejecuto porque b vale 5");
        }

        //Manejo de excepciones con try-catch
        try {
            System.out.println(10 / 0);
        } catch (Exception e) {
            System.out.println("Ocurrio un error y lo controle");
        } finally{
            System.out.println("Esta parte siempre se ejecuta en el manejo de expciones.");
        }

        
        //-----------EJERCICIO DE DIFICULTAD EXTRA----------------
        for (int i = 1; i < 55; i ++){
            if (i % 2 == 0 && i != 16 && i % 3 != 0){
                System.out.println(i);
            }
        }

    }

}
