import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Calendar;
import java.util.Locale;

public class JimsimroDev {
  private final static DateTimeFormatter FORMATO = DateTimeFormatter.ISO_LOCAL_DATE;

  /**
   * @param args
   */
  public static void main(String[] args) {

    //API de java con la clase Calendar
    Calendar fecha = Calendar.getInstance();
    int year = fecha.get(Calendar.YEAR);
    int month = fecha.get(Calendar.MONTH) + 1; // Los meses empiezan desde 0
    int day = fecha.get(Calendar.DATE);
    int hour = fecha.get(Calendar.HOUR_OF_DAY);
    int minute = fecha.get(Calendar.MINUTE);
    int second = fecha.get(Calendar.SECOND);
    System.out.printf("Fecha y hora actual: %d:%d:%d %02d:%02d:%02d%n", year, month, day, hour, minute, second);

    // Fecha actual: con la clase LocalDateTime
    LocalDateTime fechaActual = LocalDateTime.now();
    System.out.println("Fecha actual: " + fechaActual);

    LocalDate fechaNacimiento = LocalDate.of(1995, 07, 28);//Mi fecha de nacimiento con LocalDate
    System.out.println("Fecha de nacimiento: " + fechaNacimiento);
    // Calcular la edad con LocalDate
    int anoNacimiento = fechaNacimiento.getYear();
    var anosTranscurridos = year - anoNacimiento;
    if (month < fechaNacimiento.getMonthValue()) {
      anosTranscurridos--;
    } else if (month == fechaNacimiento.getMonthValue() && day < fechaNacimiento.getDayOfMonth()) {
      anosTranscurridos--;
    }
    System.out.println(String.format("Tengo %s años.", anosTranscurridos));

    // Calcular la edad con Calendar
    fecha.add(Calendar.YEAR,- fechaNacimiento.getYear());
    System.out.printf("Edad actual: %d%n ",fecha.get(Calendar.YEAR));

    //Extra
    DateTimeFormatter formatearFechas = DateTimeFormatter.ofPattern("dd/MM/yyyy");// Formato dd/MM/yyyy  -> 28/07/1995
    DateTimeFormatter formatearFechas1 = DateTimeFormatter.ofPattern("D-MM-Y");// Formato D-MM-Y -> 209-07-1995
    DateTimeFormatter formatearFechas2 = DateTimeFormatter.ofPattern("dd-MMMM-y"); // Formato dd-MMMM-y -> 28-julio-1995
    DateTimeFormatter formatearFechas3 = DateTimeFormatter.ofPattern("dd-MMM-y");// Formato dd-MMM-y -> 28-jul-1995
    DateTimeFormatter formatearFechas4 = DateTimeFormatter.ofPattern("E-MMM-y");// Formato dd-MMM-y -> Fri-jul-1995
    DateTimeFormatter formatearFechas5 = DateTimeFormatter.ofPattern("EEEE-MMM-y");// Formato dd-MMM-y -> Friday-jul-1995
    DateTimeFormatter formatearFechas6 = DateTimeFormatter.ofPattern("EEEE-MMMM-y");// Formato dd-MMM-y -> Friday-julio-1995
    DateTimeFormatter formatearFechas7 = DateTimeFormatter.ofPattern("EEEE-MMMM-d-y");// Formato dd-MMM-y -> Friday-julio-28-1995
    DateTimeFormatter formatearFechas8 = DateTimeFormatter.ofPattern("EEEE-MMMM-w-d-y");// Formato EEEE-MMMM-w-d-y -> Friday-julio-30-28-1995
    DateTimeFormatter formatearFechas9 = DateTimeFormatter.ofPattern("w-d");// Formato w-d muestra la semana y el día del mes -> 30-28
    DateTimeFormatter formatearFechas10 = DateTimeFormatter.ofPattern("Q");// Formato Q muestra el trimestre del año -> 3
    DateTimeFormatter personalizado = DateTimeFormatter.ofPattern("dd 'de' MMMM 'de' yyyy", new Locale("es", "CO"));// Formato personalizado en español -> 28 de julio de 1995
    System.out.println("Fecha de nacimiento con formato ISO: " + fechaNacimiento.format(FORMATO));// formato ISO -> 1995-07-28
    System.out.println("Fecha de nacimiento: " + fechaNacimiento.format(formatearFechas));
    System.out.println("Fecha de nacimiento con formato bonito: " + fechaNacimiento.format(formatearFechas1));
    System.out.println("Fecha de nacimiento con formato bonito: " + fechaNacimiento.format(formatearFechas2));
    System.out.println("Fecha de nacimiento con formato bonito: " + fechaNacimiento.format(formatearFechas3));
    System.out.println("Fecha de nacimiento con formato bonito: " + fechaNacimiento.format(formatearFechas4));
    System.out.println("Fecha de nacimiento con formato bonito: " + fechaNacimiento.format(formatearFechas5));
    System.out.println("Fecha de nacimiento con formato bonito: " + fechaNacimiento.format(formatearFechas6));
    System.out.println("Fecha de nacimiento con formato bonito: " + fechaNacimiento.format(formatearFechas7));
    System.out.println("Fecha de nacimiento con formato bonito: " + fechaNacimiento.format(formatearFechas8));
    System.out.println("Fecha de nacimiento con formato bonito: " + fechaNacimiento.format(formatearFechas9));
    System.out.println("Fecha de nacimiento con formato bonito: " + fechaNacimiento.format(formatearFechas10));
    System.out.println("Fecha de nacimiento con formato bonito: " + fechaNacimiento.format(personalizado));


  }
}
