
import java.util.Scanner;


public class simonguzman {
 
    public static void main(String[] args) {
        firstExercise();
    }

    public enum Days{
        LUNES,
        MARTES,
        MIERCOLES,
        JUEVES,
        VIERNES,
        SABADO,
        DOMINGO     
    }

    static void firstExercise(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese un dia de la semana");
        int n = scanner.nextInt();

        System.out.println("El dia "+n+" corresponde al dia: "+getDay(n));
    }

    static Days getDay(int n){
        Days day = weekDays(n);
        return day;
    }

    static Days weekDays(int n){
        switch (n) {
            case 1: return Days.LUNES;
            case 2: return Days.MARTES;
            case 3: return Days.MIERCOLES;
            case 4: return Days.JUEVES;
            case 5: return Days.VIERNES;
            case 6: return Days.SABADO;
            case 7: return Days.DOMINGO;
            default:
                throw new IllegalArgumentException("ERROR: Numero incorrecto.");
        }
    }
}
