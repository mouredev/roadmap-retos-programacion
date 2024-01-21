class pguill02{

    public static void main(String[] args) {
        //En java encontramos los operadores aritméticos y booleanos básicos

        //Operadores aritméticos

        int a = 10;
        int b = 23;

        System.out.println("Suma: " + (a+b));
        System.out.println("Resta: " + (a-b));
        System.out.println("Multiplicación: " + (a*b));
        System.out.println("División: " + (a/b));
        System.out.println("Resto: " + (a%b));

        //Operadores booleanos

        boolean t = true;
        boolean f = false;

        System.out.println("AND: " + (t && f));
        System.out.println("OR: " + (t || f));
        System.out.println("NOT: " + (!t));

        //Operadores de comparación

        System.out.println("Igual: " + (a == b));
        System.out.println("Distinto: " + (a != b));
        System.out.println("Mayor: " + (a > b));
        System.out.println("Menor: " + (a < b));
        System.out.println("Mayor o igual: " + (a >= b));
        System.out.println("Menor o igual: " + (a <= b));
        
        //Operadores de asignación

        System.out.println("Asignación: " + (a = b));
        System.out.println("Suma y asignación: " + (a += b));
        System.out.println("Resta y asignación: " + (a -= b));
        System.out.println("Multiplicación y asignación: " + (a *= b));
        System.out.println("División y asignación: " + (a /= b));
        System.out.println("Resto y asignación: " + (a %= b));
        System.out.println("AND y asignación: " + (a &= b));
        System.out.println("OR y asignación: " + (a |= b));
        System.out.println("XOR y asignación: " + (a ^= b));
        System.out.println("Desplazamiento a la izquierda y asignación: " + (a <<= b));
        System.out.println("Desplazamiento a la derecha y asignación: " + (a >>= b));
        System.out.println("Desplazamiento a la derecha sin signo y asignación: " + (a >>>= b));

        //Operadores de incremento y decremento

        System.out.println("Pre-incremento: " + (++a));
        System.out.println("Post-incremento: " + (a++));
        System.out.println("Pre-decremento: " + (--a));
        System.out.println("Post-decremento: " + (a--));
        
        //Operadores ternarios

        System.out.println("Ternario: " + (a > b ? a : b));
        
        //Estructuras de control

        //Estructura if

        if(a > b){
            System.out.println("a es mayor que b");
        }else if(a < b){
            System.out.println("a es menor que b");
        }else{
            System.out.println("a es igual que b");
        }

        //Bucle for


        for(int i = 0; i < 10; i++){
            System.out.println("i vale: " + i);
        }

        //Bucle while

        int i = 0;

        while(i < 10){
            System.out.println("i vale: " + i);
            i++;
        }

        for (int j = 10; j <= 55; j++) {
            if(j % 2 == 0){
                if(j%3 == 0){
                    if (j != 16){
                        System.out.println(j);
                    }
            }
        }
    }
}
}