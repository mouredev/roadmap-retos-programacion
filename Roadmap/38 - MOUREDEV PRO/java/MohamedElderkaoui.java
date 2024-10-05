import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.stream.Collectors;

public class MohamedElderkaoui {

    public static void main(String[] args) {
        String filePath = "participants.csv"; // Path to your CSV file
        
        List<Participant> activeParticipants = new ArrayList<>();

        // Step 1: Read the CSV file and filter "activo" participants
        try (BufferedReader br = Files.newBufferedReader(Paths.get(filePath))) {
            String line;
            // Skip the first line (header)
            br.readLine();
            
            while ((line = br.readLine()) != null) {
                String[] data = line.split(","); // Assuming CSV is comma-separated
                int id = Integer.parseInt(data[0].trim());
                String email = data[1].trim();
                String status = data[2].trim();
                
                // Only consider "activo" participants
                if (status.equalsIgnoreCase("activo")) {
                    activeParticipants.add(new Participant(id, email));
                }
            }
        } catch (IOException e) {
            System.out.println("Error reading the file: " + e.getMessage());
        }

        // Step 2: Randomly select winners if there are enough participants
        if (activeParticipants.size() >= 3) {
            Collections.shuffle(activeParticipants); // Randomize the list

            // Select three unique winners
            Participant subscriptionWinner = activeParticipants.get(0);
            Participant discountWinner = activeParticipants.get(1);
            Participant bookWinner = activeParticipants.get(2);

            // Step 3: Display the winners
            System.out.println("Winners:");
            System.out.println("Subscription Winner: " + subscriptionWinner);
            System.out.println("Discount Winner: " + discountWinner);
            System.out.println("Book Winner: " + bookWinner);
        } else {
            System.out.println("Not enough active participants to select winners.");
        }
    }

    // Helper class to represent a participant
    static class Participant {
        int id;
        String email;

        Participant(int id, String email) {
            this.id = id;
            this.email = email;
        }

        @Override
        public String toString() {
            return "ID: " + id + ", Email: " + email;
        }
    }
}
