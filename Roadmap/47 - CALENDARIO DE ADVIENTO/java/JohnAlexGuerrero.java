package org.example;

import java.util.Scanner;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
        // * - El calendario mostrará los días del 1 al 24 repartidos
        // *   en 6 columnas a modo de cuadrícula.
        //- Cada cuadrícula correspondiente a un día tendrá un tamaño
        // *   de 4x3 caracteres, y sus bordes serán asteríscos.
        //* Ejemplo de cuadrículas:
        //* **** **** ****
        //* *01* *02* *03* ...
        //* **** **** ****
    static int [][] calendar = {
            {1,2,3,4,5,6}, {7,8,9,10,11,12}, {13,14,15,16,17,18}, {19,20,21,22,23,24}
    };

    public static void showCalendar(){
        for(int[] row: calendar){
            System.out.println("**** **** **** **** **** **** ");
            for(int i: row){
                String day = (i < 10)? "0"+i : ""+i;
                if(i == 0){
                    day = "**";
                }
                System.out.printf("*"+day+"* ");
            }
            System.out.println();
        }
        System.out.println("**** **** **** **** **** **** ");
        System.out.println();
    }

    public static boolean avalableDay(int d){
        for (int i = 0; i < calendar.length; i++){
            for (int j = 0; j < calendar[i].length; j++){
                if(calendar[i][j] == d){
                    selectDayInCalendar(i,j);
                    return true;
                }
            }
        }
        return false;
    }

    public static void selectDayInCalendar(int indexX, int indexY){
        // *   cubierta de asteríscos (sin mostrar el día).
        // * Ejemplo de selección del día 1
        // * **** **** ****
        // * **** *02* *03* ...
        // * **** **** ****
        calendar[indexX][indexY] = 0;
    }

    public static void main(String[] args) {
        // Press Alt+Intro with your caret at the highlighted text to see how
        Scanner scanner = new Scanner(System.in);
        boolean flag = true;

        while(flag){
            showCalendar();
            //* - El usuario seleccioná qué día quiere descubrir.
            System.out.println("select one day or exit: ");
            String selectDay = scanner.nextLine();

            if(selectDay.equals("exit")){
                flag = false;
            }

            try{
                int selectedDay = Integer.parseInt(selectDay);

                //Si está sin descubrir, se le dirá que ha abierto ese día
                if(avalableDay(selectedDay)){
                    System.out.println("This day is avalable.");
                }else{
                    //* - Si se selecciona un número ya descubierto, se le notifica
                    // *   al usuario.
                    System.out.println("Day is not avalable.");
                }

            }catch(NumberFormatException ex){
                System.out.println("select on number.");
            }
        }

        // *   y se mostrará de nuevo el calendario con esa cuadrícula

    }
}