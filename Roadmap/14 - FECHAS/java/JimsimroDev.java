import java.time.LocalDate;
import java.util.Calendar;

public class JimsimroDev {
  public static void main(String[] args) {
    Calendar fecha = Calendar.getInstance();
    int year = fecha.get(Calendar.YEAR);
    int month = fecha.get(Calendar.MONTH) + 1; // Los meses empiezan desde 0
    int day = fecha.get(Calendar.DATE);
    System.out.println("Fecha actual: " + year + "-" + (month) + "-" + day);

    LocalDate fechaNacimiento = LocalDate.of(1995, 07, 28);
    int anoNacimiento = fechaNacimiento.getYear();
    var anosTranscurridos = year - anoNacimiento;
    if (month < fechaNacimiento.getMonthValue()) {
      anosTranscurridos--;
    } else if (month == fechaNacimiento.getMonthValue() && day < fechaNacimiento.getDayOfMonth()) {
      anosTranscurridos--;
    }
    System.out.println(String.format("Tengo %s años.", anosTranscurridos));
  }
}
