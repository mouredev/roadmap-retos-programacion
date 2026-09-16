
import java.util.*;

public class DennisGD94 {
    public static void main(String[] args) {

        System.out.println("ESTRUCTURAS DE DATOS");

        System.out.println("Array");

        int[] numbers = new int[5];
        System.out.println("Inserción");
        numbers[0] = 2;
        numbers[1] = 7;
        numbers[2] = 10;
        numbers[3] = 3;
        numbers[4] = 5;

        System.out.println("Actualización");
        System.out.println(numbers[1]);
        numbers[1] = 20;
        System.out.println(numbers[1]);

        System.out.println("Ordenación");
        Arrays.sort(numbers);
        System.out.println(Arrays.toString(numbers));

        System.out.println("Borrado: " + "Los Arrays no permiten borrado, ya que su tamaño es fijo");


        System.out.println("ArrayList");
        ArrayList<String> names = new ArrayList<>();
        System.out.println("Inserción");
        names.add("Dennis");
        names.add("Juan");
        names.add("Valentina");
        names.add("Diana");
        names.add("Jhon");

        System.out.println("Borrado");

        for(String name : names){
            System.out.println(name);
        }
        System.out.println("________");

        names.remove("Juan");
        for(String name : names){
            System.out.println(name);

        }
        System.out.println("________");

        System.out.println("Actualización");
        System.out.println(names.get(2));
        names.set(2, "Fabio");
        System.out.println(names.get(2));
        System.out.println("______");

        System.out.println("Ordenación");
        names.sort(Comparator.naturalOrder());
        for (String name : names){
            System.out.println(name);
        }


        System.out.println("LinkedList");
        LinkedList<Character> characters = new LinkedList<>();
        System.out.println("Inserción");
        characters.add('a');
        characters.add('c');
        characters.add('d');
        characters.add('r');
        characters.add('v');
        for (Character character : characters){
            System.out.println(character);
        }
        System.out.println("_________");
        System.out.println("Actualización");
        System.out.println(characters.get(1));
        characters.set(1, 'f');
        System.out.println(characters.get(1));

        System.out.println("Borrado");
        characters.remove(characters.get(3));
        for (Character character : characters){
            System.out.println(character);
        }

        System.out.println("Ordenaciçon");
        characters.sort(Comparator.naturalOrder());
        for (Character character : characters){
            System.out.println(character);

        }


        System.out.println("HashSet");

        HashSet<Integer> list = new HashSet<>();
        System.out.println("Inserción");
        list.add(55);
        list.add(30);
        list.add(45);
        list.add(11);
        list.add(20);
        for (int i : list){
            System.out.println(i);
        }
        System.out.println("Borrado");
        list.remove(30);
        for (int i : list){
            System.out.println(i);
        }
        System.out.println("Actualizar");


        System.out.println("Ordenar: " + "Los HashSets no mantienen un orden");

        System.out.println("HashMap");
        HashMap<String, Integer> ages = new HashMap<>();
        System.out.println("Inserción");
        ages.put("Dennis", 32);
        ages.put("Fabio", 3);
        ages.put("Lola", 24);
        ages.put("Carlos", 17);
        for(Map.Entry<String, Integer> age : ages.entrySet()){
            System.out.println(age);
        }

        System.out.println("Actualización");
        System.out.println(ages.get("Carlos"));
        ages.replace("Carlos", 17, 21);
        System.out.println(ages.get("Carlos"));

        System.out.println("Borrado");
        ages.remove("Carlos");
        for(Map.Entry<String, Integer> age : ages.entrySet()){
            System.out.println(age);
        }

        System.out.println("--------------------");
        System.out.println("Contact book");
        System.out.println("____________________");

        Contact contact = new Contact();

        contact.showMenu();


    }

    public static class Contact{

        private HashMap<String, String> contacts;

        public Contact(){
            contacts = new HashMap<>();
        }

        public void showMenu() {
            Scanner scanner = new Scanner(System.in);

            boolean flag = true;
            while (flag) {

                System.out.println("1. Add contact");
                System.out.println("2. Update contact");
                System.out.println("3. Remove contact");
                System.out.println("4. Search contact");
                System.out.println("5. Show contacts");
                System.out.println("6. Exit");

                int menu = scanner.nextInt();
                scanner.nextLine();


                switch (menu) {
                    case 1 -> {
                        System.out.println("Enter contact name:");
                           String name = scanner.nextLine();
                        System.out.println("Enter phone number:");
                           String phone = scanner.nextLine();
                           addContact(name, phone);
                    }
                    case 2 -> {
                        System.out.println("Enter contact name:");
                            String name = scanner.nextLine();
                        System.out.println("Enter new phone number");
                            String newPhone = scanner.nextLine();
                            updateContact(name, newPhone);
                    }
                    case 3 -> {
                        System.out.println("Enter contact name:");
                        String name = scanner.nextLine();
                            removeContact(name);
                    }
                    case 4 -> {
                        System.out.println("Enter contact name:");
                            String name = scanner.nextLine();
                            String phone = searchContact(name);
                            if(phone == null) {
                                System.out.println("Contact not found");
                            }else {
                                System.out.println("Contact found:");
                                System.out.println(name + ":" + phone);
                            }
                    }
                    case 5 -> {
                          showContacts();
                    }
                    case 6 -> {
                        System.out.println("Contact book closed");
                            flag = false;
                    }
                    default -> System.out.println("Invalid option");

                }
            }
        }


        public String searchContact(String name){
            if(contacts.containsKey(name)){
                return contacts.get(name);
            }
            return null;
        }

        public void addContact(String name, String phone){
            if(!isValidPhone(phone)){
                System.out.println("Invalid phone number");
                return;
            }
            if (searchContact(name) != null) {
                    System.out.println("Contact already exist");
                    return;
                }
            contacts.put(name, phone);
            System.out.println("Contact added");
        }

        public void showContacts() {
            if (contacts.isEmpty()) {
                System.out.println("No contact found");
            }else {
                for (Map.Entry<String, String> entry : contacts.entrySet()) {
                    System.out.println(entry.getKey() + ": " + entry.getValue());
                }
            }
        }

        public void updateContact(String name, String newPhone){
            if(!isValidPhone(newPhone)){
                System.out.println("Invalid phone number");
                return;
            }
            if(searchContact(name) == null){
                System.out.println("Contact not found");
                return;
            }
            contacts.replace(name, newPhone);
            System.out.println("Updated contact");
        }

        public void removeContact(String name){
            if(searchContact(name) == null){
                System.out.println("Contact not found");
            }else{
                contacts.remove(name);
                System.out.println("Removed contact");
            }
        }

        public boolean isValidPhone(String phone){
            if(phone.isEmpty()){
                return false;
            }
            if (phone.length() > 11) {
                return false;
            }
            for (int i = 0; i < phone.length(); i++){
                    if(!Character.isDigit(phone.charAt(i))){
                        return false;
                    }
                }
            return true;
        }
    }





}
