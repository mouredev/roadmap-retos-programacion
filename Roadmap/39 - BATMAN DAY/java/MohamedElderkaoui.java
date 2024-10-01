import java.util.*;

public class MohamedElderkaoui {

    public static void main(String[] args) {
        // Challenge 1: Batman Day calculation until 100th anniversary using Calendar
        int currentYear = 2024;
        int batmanAge = 85;
        System.out.println("Batman Day until 100th Anniversary:");
        calculateBatmanDayUsingCalendar(currentYear, batmanAge);

        // Challenge 2: Batcave Security System
        System.out.println("\nBatcave Security System:");
        // Sample sensor data: (x, y, threat level)
        List<int[]> sensors = List.of(
            new int[]{3, 3, 5},
            new int[]{4, 4, 8},
            new int[]{5, 5, 2},
            new int[]{10, 10, 9},
            new int[]{11, 11, 3},
            new int[]{12, 12, 7}
        );
        batcaveSecuritySystem(sensors);
    }

    // CHALLENGE 1: Calculate Batman Day until his 100th anniversary using Calendar
    public static void calculateBatmanDayUsingCalendar(int currentYear, int batmanAge) {
        int yearsLeft = 100 - batmanAge;
        for (int i = 0; i <= yearsLeft; i++) {
            int year = currentYear + i;
            Calendar thirdSaturday = getThirdSaturdayOfSeptember(year);
            System.out.printf("Batman Day in %d: %tF\n", year, thirdSaturday.getTime());
        }
    }

    // Get the third Saturday of September using Calendar
    private static Calendar getThirdSaturdayOfSeptember(int year) {
        // Create a calendar instance set to September 1st of the given year
        Calendar calendar = Calendar.getInstance();
        calendar.set(year, Calendar.SEPTEMBER, 1);

        // Find the first Saturday of September
        while (calendar.get(Calendar.DAY_OF_WEEK) != Calendar.SATURDAY) {
            calendar.add(Calendar.DAY_OF_MONTH, 1);
        }

        // Move to the third Saturday
        calendar.add(Calendar.DAY_OF_MONTH, 14); // Add 2 more weeks

        return calendar;
    }

    // CHALLENGE 2: Batcave Security System
    public static void batcaveSecuritySystem(List<int[]> sensors) {
        // 20x20 grid of Gotham
        int[][] gothamGrid = new int[20][20];

        // Fill the grid with the threat levels from the sensor data
        for (int[] sensor : sensors) {
            int x = sensor[0];
            int y = sensor[1];
            int threatLevel = sensor[2];
            gothamGrid[x][y] = threatLevel;
        }

        int maxThreatSum = 0;
        int centerX = 0, centerY = 0;

        // Find the 3x3 grid with the maximum threat level
        for (int i = 0; i <= 17; i++) {
            for (int j = 0; j <= 17; j++) {
                int threatSum = calculateThreatSum(gothamGrid, i, j);
                if (threatSum > maxThreatSum) {
                    maxThreatSum = threatSum;
                    centerX = i + 1;
                    centerY = j + 1;
                }
            }
        }

        // Calculate the distance from Batcave (0, 0) to the center of the most threatened grid
        int distanceToBatcave = Math.abs(centerX) + Math.abs(centerY);

        // Display the results
        System.out.println("Most threatened 3x3 grid center: (" + centerX + ", " + centerY + ")");
        System.out.println("Sum of threats: " + maxThreatSum);
        System.out.println("Distance to Batcave: " + distanceToBatcave);

        // Check if the security protocol should be activated
        if (maxThreatSum > 20) {
            System.out.println("Security Protocol Activated!");
        } else {
            System.out.println("Security Protocol NOT Activated.");
        }
    }

    // Helper function to calculate the sum of threats in a 3x3 grid starting from (x, y)
    private static int calculateThreatSum(int[][] grid, int x, int y) {
        int sum = 0;
        for (int i = x; i < x + 3; i++) {
            for (int j = y; j < y + 3; j++) {
                sum += grid[i][j];
            }
        }
        return sum;
    }
}
