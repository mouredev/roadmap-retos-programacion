import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Set;
import java.util.TreeSet;

public class Qv1ko {

    public static void main(String[] args) {

        arrayStructure();

        listStructure();

        setStructure();

        mapStructure();

        schedule();
        
    }

    private static void arrayStructure() {
        
        String[] array = new String[6];

        array[0] = "A";

        array[0] = null;

        array[0] = "A";

        array[0] += " - Updated";

        array[1] = "B";

        String aux = "";

        aux = array[0];
        array[0] = array[1];
        array[1] = aux;
        
    }
    
    private static void listStructure() {
        
        ArrayList<Integer> list = new ArrayList<Integer>();

        list.add(0);

        list.set(0, 3);

        list.remove(0);

        list.add(5);

        list.add(4);
        
        list.add(3);

        Collections.sort(list);

    }
    
    private static void setStructure() {
        
        Set<String> set = new TreeSet<>();

        set.add("B");

        set.add("C");

        set.add("A");

        set.remove("B");

    }
    
    private static void mapStructure() {
        
        HashMap<Integer, String> map = new HashMap<Integer, String>();

        map.put(0, "A");
        map.put(1, "B");
        map.put(2, "C");

        map.remove(1);

        map.replace(2, "B");

    }

    private static void schedule() {

        System.out.println("\nS C H E D U L E");

        HashMap<String, String> contacts = new HashMap<String, String>();
        boolean exit = false;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String option = "", option2 = "";

        while (!exit) {

            options();
            try {
                System.out.print(">> ");
                option = br.readLine();
                switch (option) {
                    case "1":
                        if (contacts.size() != 0) {
                            System.out.println("\nType the name of the contact to search for");
                            System.out.print(">> ");
                            option = br.readLine();
                            if (contacts.containsKey(option)) {
                                System.out.println("Contact " + option + " - " + contacts.get(option));
                            } else {
                                System.out.println("\n>> contact not found");
                            }
                        } else {
                            System.out.println("\n>> you have no contacts");
                        }
                        break;

                    case "2":
                        System.out.println("\nEnter the name of the new contact");
                        System.out.print(">> ");
                        option = br.readLine();
                        if (contacts.containsKey(option)) {
                            System.out.println("\n>> the contact already exists");
                        } else {
                            do {
                                System.out.println("\nEnter the phone number of the new contact");
                                System.out.print(">> ");
                                option2 = br.readLine();
                            } while (!option2.matches("\\d{9,11}"));
                            contacts.put(option, option2);
                            System.out.println("\nUser " + option + " with phone (" + option2 + ") successfully added");
                        }
                        break;

                    case "3":
                        System.out.println("\nEnter the name of the contact");
                        System.out.print(">> ");
                        option = br.readLine();
                        if (contacts.containsKey(option)) {
                            do {
                                System.out.println("\nEnter the phone number");
                                System.out.print(">> ");
                                option2 = br.readLine();
                            } while (!option2.matches("\\d{9,11}"));
                            contacts.replace(option, option2);
                            System.out.println("\nUser " + option + " with phone (" + option2 + ") successfully added");
                        } else {
                            System.out.println("\n>> contact not found");
                        }
                        break;

                    case "4":
                        if (contacts.size() != 0) {
                            System.out.println("\nEnter the name of the contact you wish to delete");
                            System.out.print(">> ");
                            option = br.readLine();
                            if (contacts.containsKey(option)) {
                                contacts.remove(option);
                                System.out.println("\nUser " + option + " was successfully deleted");
                            } else {
                                System.out.println("\n>> contact not found");
                            }
                        } else {
                            System.out.println("\n>> you have no contacts");
                        }
                        break;

                    case "0":
                        exit = true;
                        System.out.println("\n>> leaving...\n");
                        break;

                    default:
                        throw new Exception();

                }
            } catch (Exception exc) {
                System.out.println("\n>> error when selecting the option\n");
            }
            
        }

    }

    private static void options() {
        System.out.println("\nOptions:");
        System.out.println("-----");
        System.out.println("1) Search contact");
        System.out.println("2) Create contact");
        System.out.println("3) Update contact");
        System.out.println("4) Delete contact");
        System.out.println("0) Exit");
        System.out.println("-----");
    }

}
