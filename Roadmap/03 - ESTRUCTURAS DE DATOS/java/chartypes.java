import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.InputMismatchException;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class chartypes {
    public static void main(String[] args) {
        dataStructures();
        exercise();

    }

    static void dataStructures() {
        // Arrays
        System.out.println("-------------\nArray:");
        int[] arrayNumbers = new int[3];
        arrayNumbers[0] = 1;
        arrayNumbers[1] = 2;
        arrayNumbers[2] = 3;
        System.out.println(Arrays.toString(arrayNumbers));

        // ArrayList
        System.out.println("-------------\nArrayList:");
        ArrayList<Integer> listNumbers = new ArrayList<>();
        listNumbers.add(4);
        listNumbers.add(5);
        listNumbers.add(1);
        System.out.println(listNumbers.get(0));
        listNumbers.set(1, 20);
        listNumbers.remove(2);
        listNumbers.forEach(System.out::println);

        // Sets
        System.out.println("-------------\nSets:");
        Set<Integer> setNumbers = new HashSet<>();
        setNumbers.add(5);
        setNumbers.add(12);
        setNumbers.add(8);
        setNumbers.add(12);
        setNumbers.forEach(System.out::println);

        // LinkedList
        System.out.println("-------------\nLinkedList:");
        List<String> listColors = new LinkedList<>();
        listColors.add("Red");
        listColors.add("Blue");
        listColors.add("Yellow");
        listColors.forEach(System.out::println);

        // HashMap
        System.out.println("-------------\nHasMap:");
        Map<Integer, String> mapNumbers = new HashMap<>();
        mapNumbers.put(1, "one");
        mapNumbers.put(2, "two");
        mapNumbers.put(3, "three");
        System.out.println(mapNumbers);
        mapNumbers.put(2, "five");
        System.out.println("Keys:" + mapNumbers.keySet() + "---- Values:" + mapNumbers.values());
    }

    boolean checkPhoneNumber(String phoneNumber) {
        return phoneNumber.length() >= 11;
    }

    static void exercise() {
        final String WRONG_VALUE = "You inserted a wrong value";

        Map<String, Long> contact = new HashMap<>();
        while (true) {

            System.out.println("\n-----------------------------------------------------");
            System.out.println("Select an option :\n");
            System.out.println("1. Insert a new contact");
            System.out.println("2. Show contact");
            System.out.println("3. Update a contact");
            System.out.println("4. Delete a contact");
            System.out.println("5. Exit");

            Scanner choice = new Scanner(System.in);
            switch (choice.nextInt()) {
                case 1:
                    System.out.println("Insert a name for the contact: ");
                    System.out.println("Insert a phone number for the contact: ");
                    Scanner data = new Scanner(System.in);
                    try {
                        String name = data.nextLine();
                        long phoneNumber = data.nextLong();
                        if (phoneNumber >= 10000000000L) {
                            System.out.println(WRONG_VALUE);
                            break;
                        }
                        contact.put(name, phoneNumber);
                        break;
                    } catch (InputMismatchException e) {
                        System.out.println(WRONG_VALUE);
                        break;

                    }
                case 2:
                    System.out.println("Whats the name of the contact you want to see? : ");
                    Scanner nameToShow = new Scanner(System.in);
                    Long contactValue = contact.get(nameToShow.nextLine());
                    if (contactValue instanceof Long) {
                        System.out.println(contactValue);
                    } else
                        System.out.println(WRONG_VALUE);

                    break;
                case 3:
                    System.out.println("Whats the name of the contact you want to update? : ");
                    System.out.println("Insert the new phone number to update? : ");
                    try {
                        Scanner dataToUpdate = new Scanner(System.in);
                        String nameToUpdate = dataToUpdate.nextLine();
                        long phoneNumberToUpdate = dataToUpdate.nextLong();
                        contact.put(nameToUpdate, phoneNumberToUpdate);
                        System.out.println("Contact updated correctly");

                    } catch (InputMismatchException e) {
                        System.out.println("You inserted a wrong value");
                    }
                    break;
                case 4:
                    System.out.println("Whats the name of the contact you want to delete? : ");
                    Scanner nameToDelete = new Scanner(System.in);
                    contact.remove(nameToDelete.nextLine());
                    System.out.println("Contact deleted correctly");
                    break;
                case 5:
                    return;
                default:
                    System.out.println("You inserted a wrong option ");
                    break;
            }

        }
    }
}
