import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.temporal.TemporalAdjusters;
import java.util.LinkedList;
import java.util.List;
import java.util.Random;

public class Main {

    public static void main(String[] args) {
        calculateBatmanDay();
        batcaveSecuritySystem();
    }

    /*
        RETO 1:
        Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta su 100 aniversario.
        El Batman Day se celebra el tercer sábado de septiembre de cada año.
     */
    public static void calculateBatmanDay() {
        List<LocalDate> batmanDayAnniversary = new LinkedList<>();
        int year = 1939;

        for (int i = 0; i < 100; i++) {
            LocalDate firstDayOfSeptember = LocalDate.of(year, 9, 1);
            LocalDate firstSaturday = firstDayOfSeptember.with(TemporalAdjusters.firstInMonth(DayOfWeek.SATURDAY));
            LocalDate thirdSaturday = firstSaturday.plusWeeks(2);
            batmanDayAnniversary.add(thirdSaturday);
            year++;
        }

        batmanDayAnniversary.forEach(day -> System.out.println("El sábado de la tercera semana de septiembre de " + day.getYear() + " es el día " + day.getDayOfMonth()));
    }

    /*
        Reto 2:
     */
    public static void batcaveSecuritySystem() {
        Sensor[][] grid = new Sensor[20][20];
        Random random = new Random();

        for (int x = 0; x < 20; x++) {
            for (int y = 0; y < 20; y++) {
                grid[x][y] = new Sensor(x, y, random.nextInt(11));
            }
        }

        int centerX = 0, centerY = 0, maxSum = 0;

        for (int x = 0; x <= 17; x++) {
            for (int y = 0; y <= 17; y++) {
                int currSum = calculateSum(grid, x, y);
                if (currSum > maxSum) {
                    maxSum = currSum;
                    centerX = x + 1;
                    centerY = y + 1;
                }
            }
        }

        int distanceToBatcave = Math.abs(centerX) + Math.abs(centerY);

        System.out.println("Most intense area is at (" + centerX + ", " + centerY + ") with a sum of " + maxSum);
        System.out.println("Distance to Batcave: " + distanceToBatcave);
        System.out.println("Security protocol should be activated? " + ((maxSum > 20) ? "YES" : "NO"));
    }

    private static int calculateSum(Sensor[][] grid, int x, int y) {
        int sum = 0;
        for (int i = x; i < x + 3; i++) {
            for (int j = y; j < y + 3; j++) {
                sum += grid[i][j].level;
            }
        }
        return sum;
    }

    record Sensor(int x, int y, int level) {}
}
