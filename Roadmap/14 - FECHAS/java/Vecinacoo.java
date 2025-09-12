import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.temporal.ChronoUnit;

public class P14 {

	public static void main(String[] args) {

		// Mostrando agnos pasados desde la fecha de nacimiento hasta ahora
		LocalDateTime fechaAhora = LocalDateTime.of(LocalDate.now(), LocalTime.now());

		LocalDateTime fechaNacimiento = LocalDateTime.of(LocalDate.of(2005, 10, 31), LocalTime.of(10, 30));

		Duration duration = Duration.between(fechaNacimiento, fechaAhora);

		long agnos = ChronoUnit.YEARS.between(LocalDateTime.now(), LocalDateTime.now().plus(duration));

		System.out.println(agnos);

		// OPCIONAL
		mostrandoFechaCumpleagnos(fechaNacimiento);

	}

	private static void mostrandoFechaCumpleagnos(LocalDateTime n) {

		System.out.println(n.getDayOfMonth() + " " + n.getMonth() + n.getYear());

		System.out.println(n.getHour() + ":" + n.getMinute() + ":" + n.getSecond());

		System.out.println("Dia " + n.getDayOfYear() + " del agno");

		System.out.println("Dia " + n.getDayOfWeek() + " de la semana");

	}

}
