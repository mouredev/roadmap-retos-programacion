//Operadores aritméticos
        int a = 5;
        int b = 3;
        System.out.println("OPERADORES LÓGICOS:");
        System.out.println("Suma: a + b = " + (a + b));
        System.out.println("Resta: a - b = " + (a - b));
        System.out.println("Multiplicación: a * b = " + (a * b));
        System.out.println("División: a / b = " + (a / b));
        System.out.println("Modulo: a % b = " + (a % b));
        System.out.println("Incremento: b++ = " + b++);
        System.out.println("Decremento: a-- = " + a--);

//Operadores de asignación
        System.out.println("OPERADORES DE ASIGNACIÓN");
        int c = 3;
        c += 3;
        System.out.println("con suma: " + " c+=3 " + c);
        c -= 2;
        System.out.println("con resta: " + " c-=2 " + c);
        c *= 2;
        System.out.println("multiplicación: " + " c*=2 " + c);
        c /= 5;
        System.out.println("división: " + " c/=5 " + c);
        c %= 2;
        System.out.println("modulo: " + " c%=2 " + c);

//Operadores de comparación
        System.out.println("OPERADORES DE COMPARACIÓN: ");
        System.out.println("Igualdad: a == b");
        System.out.println("Desigualdad: a!= b");
        System.out.println("Mayor que : a>b");
        System.out.println("Menor que : b<a");
        System.out.println("Mayor o igual: a>=3");
        System.out.println("Menor o igual: b<= 6");

//Operadores lógicos
        System.out.println("OPERADORES LÓGICOS:");
        System.out.println("And = &&");
        System.out.println("Or = || ");
        System.out.println("Not = !");
//Operadores por bits

//CONDICIONALES:
        System.out.println("CONDICIONALES:");
        if (c >= b) {
            System.out.println("C es mayor o igual que b");
        } else {
            System.out.println("C es menor que b");
        }
//ITERATIVAS:
        System.out.println("ITERATIVAS:");
        System.out.println("FOR");
        for (int i = 0; b <= 7; b++) {
            System.out.println("i");
        }

        System.out.println("SWITCH");

        int dia = 2;
        switch (dia) {
            case 1:
                System.out.println("Lunes");
                break;
            case 2:
                System.out.println("Martes");
                break;
            case 3:
                System.out.println("Miércoles");
                break;
            case 4:
                System.out.println("Jueves");
                break;
            case 5:
                System.out.println("Viernes");
                break;
            case 6:
                System.out.println("Sábado");
                break;
            case 7:
                System.out.println("Domingo");
                break;
        }
        System.out.println("WHILE");
        int f = 0;
        while (f < 10) {
            System.out.println("El valor es menor de 10");
            f++;
        }
        System.out.println("Do-While");
        int num = 0;
        do {
            System.out.println("El valor es menor de 10");
            num++;
        } while (num < 10);
        
        //EXCEPCIONES:
        System.out.println("EXCEPTION");
        
        try {
            int h = 2/0;
        }
        catch (ArithmeticException ex) {
            System.out.println("División por 0");
        }

        //El Bucle while, primero comprueba la condición y luego ejecuta la orden. Puede no ejecutarse ninguna vez.
        //El bucle Do-While primero ejecuta la orden y luego comprueba la condición, por ello siempre se ejecutará, al menos, 1 vez.
        //------EXTRA-------
        for (int x = 10; x <= 55; x++) {
            if ((x%2==0) && !(x==16) && !(x%3 ==0)){
            System.out.println(x);
        }
        }
    }

}
