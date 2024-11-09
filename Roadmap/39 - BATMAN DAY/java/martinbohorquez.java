import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.TemporalAdjusters;
import java.util.*;
import java.util.concurrent.atomic.AtomicReference;

import static java.time.DayOfWeek.*;

public class martinbohorquez {
    public static void main(String[] args) {
        // RETO 1
        System.out.println("La fechas de celebración para el día de Batman hasta su  100 aniversario:");
        getBatmanDay100().forEach(map -> System.out.printf("Batman day %s (%s aniversario): %s%n",
                map.get("year"), map.get("aniversaryYear"), map.get("aniversaryDate")));

        // RETO 2
        List<Sensor> sensor = getGothamMap(25, 30, 5);

        batCaveSecuritySystem(sensor);

    }

    private static List<Map<String, String>> getBatmanDay100() {
        int initialYear = 1939;
        int month = 9;
        int dayOfMonth = 1;
        List<Map<String, String>> batmanDayAnniversaryDates = new ArrayList<>();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        for (int i = 85; i <= 100; i++) {
            LocalDate date = LocalDate.of(initialYear + i, month, dayOfMonth)
                    .with(TemporalAdjusters.dayOfWeekInMonth(3, SATURDAY));
            batmanDayAnniversaryDates.add(Map.of("year", String.valueOf(initialYear + i),
                    "aniversaryYear", String.valueOf(i),
                    "aniversaryDate", date.format(formatter)));
        }
        return batmanDayAnniversaryDates;
    }

    private static List<Sensor> getGothamMap(int x, int y, int threatMaxLevel) {
        List<Sensor> sensores = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < x; i++)
            for (int j = 0; j < y; j++) {
                Sensor sensor = new Sensor(i, j, random.nextInt(0, threatMaxLevel + 1));
                sensores.add(sensor);
            }
        return sensores;
    }

    private static void batCaveSecuritySystem(List<Sensor> sensores) {
        int x = Sensor.getxMax();
        int y = Sensor.getyMax();
        int maxAlertLevel = 0;
        Sensor sensor = null;
        for (int i = 1; i < x - 1; i++) {
            for (int j = 1; j < y - 1; j++) {
                int sum = 0;
                Sensor candidateSensor = null;
                for (Sensor s : sensores) {
                    if (Math.abs(s.getX() - i) <= 1 && Math.abs(s.getY() - j) <= 1) {
                        sum += s.getThreatLevel();
                        if (s.getX() == i && s.getY() == j) candidateSensor = s;
                    }
                }

                if (sum > maxAlertLevel && candidateSensor != null) {
                    maxAlertLevel = sum;
                    sensor = candidateSensor;
                }
            }
        }
        if (sensor != null) {
            System.out.printf("El centro de cuadrícula (3x3) más amenazada es: (%d, %d)%n",
                    sensor.getX(), sensor.getY());
            System.out.printf("La suma de las amenazas dentro de la cuadrícula es: %d%n",
                    maxAlertLevel);
            System.out.printf("La distancia entre la Batcueva (0,0) y el centro de la cuadrícula más amenazada: %s%n",
                    sensor.getX() + sensor.getY());
            System.out.printf("Se activó el protocolo de seguridad: %s%n", maxAlertLevel > 20 ? "Sí" : "No");
        }
    }

    private static class Sensor {
        private Integer x;
        private Integer y;
        private Integer threatLevel;
        private static Integer xMax = 0;
        private static Integer yMax = 0;

        public Sensor() {
        }

        public Sensor(Integer xPosition, Integer yPosition, Integer threatLevel) {
            this.x = xPosition;
            this.y = yPosition;
            this.threatLevel = threatLevel;
            xMax++;
            yMax++;
        }

        public Integer getX() {
            return x;
        }

        public Integer getY() {
            return y;
        }

        public Integer getThreatLevel() {
            return threatLevel;
        }

        public static Integer getxMax() {
            return xMax;
        }

        public static Integer getyMax() {
            return yMax;
        }

        @Override
        public String toString() {
            return "Sensor{" +
                    "xPosition=" + x +
                    ", yPosition=" + y +
                    ", threatLevel=" + threatLevel +
                    '}';
        }
    }
}
