import java.util.*;

public class Sniker1223 {

  private Map<String, String> contacts;

  public Sniker1223() {
    contacts = new HashMap<>();
  }

  public void addContact(String name, String phone) {
    contacts.put(name, phone);
    System.out.println("Contact added: " + name);
  }

  public void listContacts() {
    if (contacts.isEmpty()) {
      System.out.println("Agent is empty.");
      return;
    }
    System.out.println("Contacts:");
    for (Map.Entry<String, String> entry : contacts.entrySet()) {
      System.out.println("Name: " + entry.getKey() + ", Phone: " + entry.getValue());
    }
  }

  public void searchContacts(String name) {
    String phone = contacts.get(name);
    if (phone != null) {
      System.out.println("Contact found: " + name + ", Phone: " + phone);
    } else {
      System.out.println("Contact not found: " + name);
    }
  }

  public static void main(String[] args) {
    getExampleArray(new int[] { 10, 2, 67, 4, 5 });
    getExampleArrayList();
    getExampleHashMap();

    // Run with: javac Sniker1223.java then java Sniker1223
    Scanner scanner = new Scanner(System.in);
    Sniker1223 sniker = new Sniker1223();

    while (true) {
      System.out.println("\nOptions:");
      System.out.println("1. Add contact");
      System.out.println("2. List contacts");
      System.out.println("3. Search contact");
      System.out.println("4. Exit");
      System.out.println("Select an option");

      int choice = scanner.nextInt();
      scanner.nextLine();

      switch (choice) {
        case 1:
          System.out.println("Name: ");
          String name = scanner.nextLine();
          System.out.println("Phone: ");
          String phone = scanner.nextLine();
          sniker.addContact(name, phone);
          break;
        case 2:
          sniker.listContacts();
          break;
        case 3:
          System.out.println("Name to search for: ");
          String searchName = scanner.nextLine();
          sniker.searchContacts(searchName);
          break;
        case 4:
          System.out.println("Quit... ");
          scanner.close();
          return;
        default:
          System.out.println("Invalid choice. Try again. ");
      }
    }
  }

  static void getExampleArray(int[] array) {
    // sort elements
    Arrays.sort(array);

    // Print Array
    for (int numOfarray : array) {
      System.out.println(numOfarray);
    }

    // Get element
    System.out.println(array[3]);

    // Update an element
    for (int i = 0, j = 0; i < array.length; i++, j++) {
      array[i] = j;
    }

    for (int numOfarray : array) {
      System.out.println(numOfarray);
    }
  }

  static void getExampleArrayList() {
    ArrayList<String> names = new ArrayList<>();
    // Add elements
    names.add("Juan");
    names.add("Ana");
    // Print elements
    System.out.println(names);

    // Sort elements
    Collections.sort(names);
    System.out.println(names);
    // Update elements
    names.set(1, "Cesar");
    // Get element
    System.out.println(names.get(1));
    // Delete element
    names.remove(1);
    System.out.println(names);
  }

  static void getExampleHashMap() {
    HashMap<String, Integer> studentsAge = new HashMap<>();
    // Add elements
    studentsAge.put("Lili", 12);
    studentsAge.put("Lore", 8);
    studentsAge.put("Lucy", 2);
    System.out.println(studentsAge);

    // get elements
    System.out.println(studentsAge.get("Lili"));

    // sort by Key
    TreeMap<String, Integer> sortedByKey = new TreeMap<>();
    sortedByKey.putAll(studentsAge);
    System.out.println(sortedByKey + " ordered by key");

    // sort by value
    // Hashmap to List
    List<Map.Entry<String, Integer>> entryList = new ArrayList<>(studentsAge.entrySet());
    // sort by value
    entryList.sort(Map.Entry.comparingByValue());
    // Create LinkedHashMap
    LinkedHashMap<String, Integer> sortedMap = new LinkedHashMap<>();
    for (Map.Entry<String, Integer> entry : entryList) {
      sortedMap.put(entry.getKey(), entry.getValue());
    }
    System.out.println(sortedMap + " ordered by value");

    // update element
    studentsAge.put("Lucy", 20);
    System.out.println(studentsAge);

    // Delete element
    studentsAge.remove("Lore");
    studentsAge.remove("Lili");
    System.out.println(studentsAge);
  }

}
