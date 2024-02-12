public class GustavoGomez19 {
    public static void main(String[] args){
        //Punto 1: Ejemplos con operadores de Java
        //Operador de asignación (=)
        String nombre = "Gustavo";

        //Operadores aritméticos (+, -, *, /, %, ++, --, unario(+), unario(-))
        int num1 = 5;
        int num2 = 10;
        int resultado;
        boolean resultado2;
        //suma (+)
        resultado = num1 + num2;
        System.out.println("resultado = " + resultado);
        //resta (-)
        resultado = num1 - num2;
        System.out.println("resultado = " + resultado);
        //multiplicación (*)
        resultado = num1 * num2;
        System.out.println("resultado = " + resultado);
        //división (/)
        resultado = num1 / num2;
        System.out.println("resultado = " + resultado);
        //modulo (%)
        resultado = num1 % num2;
        System.out.println("resultado = " + resultado);
        //incremento (++)
        num1++;
        System.out.println("resultado = " + resultado);
        //decremento (--)
        num2--;
        //unario (+). Si el número es negativo su valor pasa a ser positivo
        int num3 = -20;
        resultado= +num3;
        System.out.println("num3 = " + num3);
        //unario (-). Si el número es positivo su valor pasa a ser negativo
        int num4 = 30;
        resultado = -num4;
        System.out.println("num4 = " + num4);

        //Operadores de comparación (==, !=, <, >, <=, >=)
        //Igualdad (==)
        resultado2 = num1 == num2;
        System.out.println("resultado2 = " + resultado2);
        //No igualdad (!=)
        resultado2 = num4 != num3;
        System.out.println("resultado2 = " + resultado2);
        //Menor que (<)
        resultado2 = num1 < num4;
        System.out.println("resultado2 = " + resultado2);
        //Mayor que >
        resultado2 = num2 > num3;
        System.out.println("resultado2 = " + resultado2);
        //Menor igual que <=
        resultado2 = num1 <= num3;
        System.out.println("resultado2 = " + resultado2);
        //Mayot igual que (>=)
        resultado2 = num2 >= num4;
        System.out.println("resultado2 = " + resultado2);

        //Operadores lógicos (&&, ||, !)
        boolean condicion1 = true;
        boolean condicion2 = false;
        boolean resultado3;
        //Operador AND (&&). Devuelve TRUE si las 2 condiciones son verdaderas
        resultado3 = condicion1 && condicion2;
        System.out.println("resultado3 = " + resultado3);
        //Operdor OR (||). Devuelve TRUE si una de las 2 condiciones es verdadera
        resultado3 = condicion1 || condicion2;
        System.out.println("resultado3 = " + resultado3);
        //Operador NOT (!). Invierte el valor de una condición
        resultado3 = !condicion2;
        System.out.println("resultado3 = " + resultado3);

        //Punto 2: Ejemplos de estructuras de control
        //Estructura de control ciclo for
        for (int i = 0; i <= 10; i++){
            System.out.println("Numero " + i);
        }
        //Estructura de control ciclo while
        int num5 = 0;
        while(num5 < 10){
            System.out.println("Numero " + num5);
            num5++;
        }
        //Estructura de control do-while
        do {
            System.out.println(num1);
            num2--;
        }while (num3 > num2);
        //Estructura de control condicional if-else
        if (num5 == num2){
            System.out.println("Los nuúmeros son iguales");
        } else {
            System.out.println("Los números son diferentes");
        }
        //Estructura de control switch case
        int diaSemana = 5;
        switch (diaSemana){
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
                System.out.println("Es un día laboral");
                break;
            case 6:
            case 7:
                System.out.println("Es un día no laboral");
                break;
            default:
                System.out.println("No es un día de la semana");
        }

        //Punto 4: Ejercicio dificultad extra
        for (int i = 10; i <= 55; i++){
            if (!(i %3 == 0) && (i %2 == 0) && (i != 16)){
                System.out.println("Número " + i);
            }
        }

    }
}
