public class AdrianNQ99 {
    public static void main(String[] chars) {
        //operadores aritmeticos
        int num1= 7;
        int num2 = 5;
        System.out.println("Operadores aritmeticos: ");
            //suma
            int suma= num1 + num2;
            System.out.println("suma= "+suma);
            //resta
            int resta= num1 - num2;
            System.out.println("resta= "+resta);
            //multiplicacion
            int multiplicacion= num1 * num2;
            System.out.println("multiplicacion= "+multiplicacion);
            //division
            int division= num1 / num2;
            System.out.println("division= "+division);
            //modulo
            int modulo= num1 % num2;
            System.out.println("resto de num1 / num2 = "+modulo);

            System.out.println("-------------------------------");

        //operadores de comparacion
            System.out.println("Operadores de comparacion: ");
            //igual que
            boolean igualQue= num1 == num2;
            System.out.println("num1 es igual que num2? "+igualQue);
            //distinto de
            boolean distintoDe= num1 != num2;
            System.out.println("num1 es distinto de num2? "+distintoDe);
            //mayor que
            boolean mayorQue= num1 > num2;
            System.out.println("num1 es mayor que num2? "+mayorQue);
            //menor que
            boolean menorQue= num1 < num2;
            System.out.println("num1 es menor que num2? "+menorQue);
            //mayor o igual que
            boolean mayorIgualQue= num1 >= num2;
            System.out.println("num1 es mayor o igual que num2? "+mayorIgualQue);
            //menor o igual que
            boolean menorIgualQue= num1 <= num2;
            System.out.println("num1 es menor o igual que num2? "+menorIgualQue);

            System.out.println("-------------------------------");

        //operadores logicos
            boolean x=true ,y=false;
            System.out.println("Operadores logicos: ");
            // AND (&&) - Devuelve true si ambas condiciones son verdaderas.
            System.out.println("And: "+(x && y));
            // OR (||) - Devuelve true si al menos una condición es verdadera.
            System.out.println("Or: "+(x || y));
            // NOT (!) - invierte el valor de una condición, es decir, cambia true a false y viceversa.
            System.out.println("Not: "+(!x));
            
            System.out.println("-------------------------------");
        
        //operadores de asignacion
            System.out.println("Operadores de asignacion: ");
            //asignacion simple
            int num3= 10;
            System.out.println("num3= "+num3);
            //asignacion con suma
            num3 += 5; //num3 = num3 + 5
            System.out.println("num3 += 5: "+num3);
            //asignacion con resta
            num3 -= 2; //num3 = num3 - 2
            System.out.println("num3 -= 2: "+num3);
            //asignacion con multiplicacion
            num3 *= 2; //num3 = num3 * 2
            System.out.println("num3 *= 2: "+num3);
            //asignacion con division
            num3 /= 4; //num3 = num3 / 4
            System.out.println("num3 /= 4: "+num3);
            //asignacion con modulo
            num3 %= 2; //num3 = num3 % 2
            System.out.println("num3 %= 2: "+num3);
            //asignacion con division
            num3 /=  2; //num3 = num3 / 2
            System.out.println("num3 /= 2: "+num3);

            System.out.println("-------------------------------");

        //operadores de binarios
            System.out.println("Operadores de binarios: ");
            int num4= 3; //00000011
            int num5= 10;  //00001010

            //AND (&) 
            int and= num1 & num2;
            System.out.println("num1 & num2: "+and);
            //OR (|) 
            int or= num1 | num2;
            System.out.println("num1 | num2: "+or);
            //XOR (^) 
            int xor= num1 ^ num2;
            System.out.println("num1 ^ num2: "+xor);
            //Complemento (~)
            int complemento= ~num1;
            System.out.println("complemento de num1: "+complemento);
            //Desplazamiento a la izquierda (<<) - Desplaza los bits a la izquierda.
            int desplazamientoIzquierda= num1 << 2;
            System.out.println("num1 << 2: "+desplazamientoIzquierda);
            //Desplazamiento a la derecha (>>) - Desplaza los bits a la derecha.
            int desplazamientoDerecha= num1 >> 2;
            System.out.println("num1 >> 2: "+desplazamientoDerecha);

            System.out.println("-------------------------------");

            // condicionales if-else
            System.out.println("Condicionales if-else: ");
            int edad= 18;
            if(edad >= 18){
                System.out.println("Eres mayor de edad.");
            }
            else if(edad == 17){
                System.out.println("Eres menor de edad, pero ya puedes tener carnet de moto.");
            }
            else{
                System.out.println("Eres menor de edad.");
            }
           
            // manejo de excepciones try-catch
            System.out.println("Manejo de excepciones try-catch: ");
            try{
                int resultado= num1 / 0; // division por cero
                System.out.println("Resultado: "+resultado);
            }catch(ArithmeticException e){
                System.out.println("Error: Division por cero.");
            }finally{
                System.out.println("Bloque finally ejecutado.");

            // extra
            for(int i=10; i<56; i++){
                if (i==16 || i%3==0){
                    continue;
                }
                System.out.println(i);
            }
    }
}}
