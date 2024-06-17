import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class FreedAInew {

    private static final int TERMINAL_WIDTH = 80;  // Width of the terminal for centering text
    private static int totalCakesBaked = 0;  // Simulated global variable to keep track of total cakes baked

    public static void main(String[] args) {
        // BASIC FUNCTIONS
        // Demonstrating basic Java functionality
        printCurrentDate();  // Without parameters and without return

        LocalDate currentDate = getCurrentDate();  // Without parameters and with return
        System.out.println("Current date (returned): " + currentDate);

        printDate(LocalDate.of(2023, 5, 31));  // With parameters and without return

        String formattedDate = formatDate(LocalDate.of(2024, 5, 31));  // With parameters and with return
        System.out.println(formattedDate);

        // FUNCTIONS WITHIN FUNCTIONS
        ScarsToYourBeautiful();  // Centered text output

        // FUNCTION ALREADY CREATED IN THE LANGUAGE
        // Display anime titles and release dates
        displayAnimeList();  // Example of functions already created in the language

        // VARIABLE LOCAL y GLOBAL.
        // Demonstrate local and global variables
        bakeCakes("Benjamin", 5); // Benjamin bakes 5 cakes
        bakeCakes("Benjamin", 3); // Benjamin bakes 3 more cakes
        bakeCakes("Itamar", 7); // Itamar bakes 7 cakes

        // Print total cakes baked in the bakery (simulated global result)
        System.out.println("Total cakes baked in the bakery: " + totalCakesBaked);

        // Print numbers from 1 to 100 with specific conditions
        String text1 = "M(3)";
        String text2 = "M(5)";
        int count = printNumbersWithTexts(text1, text2);
        System.out.println("Total numbers printed: " + count);
    }

    // Demonstrating basic Java functionality

    // Function without parameters and without return
    private static void printCurrentDate() {
        LocalDate date = LocalDate.now();
        System.out.println("Current date: " + date);
    }

    // Function without parameters with return
    private static LocalDate getCurrentDate() {
        return LocalDate.now();
    }

    // Function with parameters and without return
    private static void printDate(LocalDate date) {
        System.out.println("Provided date: " + date);
    }

    // Function with parameters and with return
    private static String formatDate(LocalDate date) {
        return "Formatted date: " + date;
    }

    // Function demonstrating the use of inner classes and lambda expressions
    private static void ScarsToYourBeautiful() {
        System.out.println(centerText("She just wants to be"));

        // Define an anonymous inner class
        Runnable runnable1 = new Runnable() {
            @Override
            public void run() {
                System.out.println(centerText("beautiful She goes"));
            }
        };

        // Call the run method of the anonymous inner class
        runnable1.run();

        // Define a lambda expression
        Runnable runnable2 = () -> {
            System.out.println(centerText("unnoticed, she knows no limits She craves"));
        };

        // Call the run method of the lambda expression
        runnable2.run();
    }

    // Method to center text in the terminal
    private static String centerText(String text) {
        int padding = (TERMINAL_WIDTH - text.length()) / 2;
        StringBuilder paddedText = new StringBuilder();
        for (int i = 0; i < padding; i++) {
            paddedText.append(" ");
        }
        paddedText.append(text);
        return paddedText.toString();
    }

    // Demonstrate local and global variables
    // Method to add cakes to the total count (simulated global update)
    private static void addCakesToTotal(int cakes) {
        totalCakesBaked += cakes;
    }

    // Method for a baker to bake cakes
    private static void bakeCakes(String name, int cakes) {
        // Local variable to keep track of cakes baked by this baker in this method call
        int cakesBakedByThisBaker = cakes;

        // Simulate the baker baking cakes
        System.out.println(name + " baked " + cakesBakedByThisBaker + " cakes.");

        // Update the global-like total cakes baked
        addCakesToTotal(cakesBakedByThisBaker);
    }

    // Method to display a list of anime titles and their release dates
    private static void displayAnimeList() {
        // Create a list of anime titles and release dates
        List<String[]> animeList = new ArrayList<>();
        animeList.add(new String[]{"Tensei Shitara Dai Nana", "June 6, 2024"});
        animeList.add(new String[]{"KonoSuba: God’s Blessing on This Wonderful World!", "June 06, 2024"});
        animeList.add(new String[]{"Kaiju No. 8", "June 06, 2024"});
        animeList.add(new String[]{"Ranger Reject", "June 06, 2024"}); // Note: Release date is in July, but included for demonstration purposes.

        // Display the anime list
        System.out.println("Popular Anime of June 2024:");
        for (String[] anime : animeList) {
            System.out.println("- " + anime[0] + " (" + anime[1] + ")");
        }
    }

    // Method to print numbers from 1 to 100 with specific conditions
    private static int printNumbersWithTexts(String text1, String text2) {
        int count = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(text1 + text2);
            } else if (i % 3 == 0) {
                System.out.println(text1);
            } else if (i % 5 == 0) {
                System.out.println(text2);
            } else {
                System.out.println(i);
                count++;
            }
        }
        return count;
    }
}
