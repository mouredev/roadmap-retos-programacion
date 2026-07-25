import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().adventCalendar();
    }

    final private Scanner sc = new Scanner(System.in);
    private List<Integer> calendar;

    public void adventCalendar(){
        initCalendar();

        try(sc){
            while(true){
                printCalendar();
                int option = askDayToUser();
                if (option == 0) {
                    System.out.println("Saliendo de la aplicación...");
                    break;
                }

                openDay(option);
                System.out.println();
            }
        }
    }

    private Integer askDayToUser(){
        boolean validDay = false;
        Integer option = 0;
        do{
            try{
                System.out.print("Selecciona un día del calendario (0 para salir): ");
                option = Integer.parseInt(sc.nextLine());
                if (option < 0 || option > 24)
                    System.out.println("Debe elegir un número del 1-24");
                else
                    validDay = true;
            } catch (NumberFormatException e) {
                System.out.println("Introduzca un número entero por favor");
            }
        }while(!validDay);

        return option;
    }

    private void openDay(Integer day){
        if (!calendar.contains(day)){
            System.out.println("El día " + day + " ya se ha descubierto");
        }

        calendar.remove(day);
    }

    private void initCalendar(){
        calendar = new ArrayList<>();

        for (Integer i = 1; i < 25; i++){
            calendar.add(i);
        }
    }

    private void printCalendar(){
        int dayCount = 1;
        for (int row = 0; row < 4; row++){
            for (int aux = 0; aux < 3; aux++){
                for (int column = 0; column < 6; column++){
                    if (aux % 2 == 0)
                        System.out.print("**** ");
                    else{
                        if (calendar.contains(dayCount))
                            System.out.print("*" + getFormattedDay(dayCount++) + "* ");
                        else{
                            System.out.print("**** ");
                            dayCount++;
                        }
                    }

                }
                System.out.println();
            }
            System.out.println();
        }
    }

    private String getFormattedDay(int day){
        return String.format("%02d", day);
    }
}