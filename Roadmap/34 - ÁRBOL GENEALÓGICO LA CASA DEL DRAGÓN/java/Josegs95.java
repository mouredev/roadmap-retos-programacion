import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().houseOfDragons();
    }

    private int idCounter = 1;

    private List<Person> personList;

    final private Scanner sc = new Scanner(System.in);

    public void houseOfDragons(){
        personList = new ArrayList<>();

        try(sc){
            app: while(true){
                printOptions();
                String option = askOptionToUser();
                switch (option){
                    case "1":
                        addPerson();
                        break;
                    case "2":
                        deletePerson();
                        break;
                    case "3":
                        addPartner();
                        break;
                    case "4":
                        addChild();
                        break;
                    case "5":
                        printFamilyTree();
                        break;
                    case "6":
                        break app;
                }
                System.out.println();
            }
        }

        System.out.println("Saliendo de la aplicación");
    }

    private String askOptionToUser(){
        boolean validOption = false;
        String option = null;
        while(!validOption){
            System.out.print("Seleccione la opción que desee (1-6): ");
            option = sc.nextLine();
            switch (option){
                case "1": case "2": case "3": case "4": case "5": case "6":
                    validOption = true;
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
        }
        System.out.println();

        return option;
    }

    private void addPerson(){
        System.out.print("Introduzca el nombre de la persona: ");
        String name = sc.nextLine();

        personList.add(new Person(idCounter++, name));
        System.out.println(name + " añadido/a correctamente.");
    }

    private void deletePerson(){
        printPeople();
        try{
            Person person = getPersonByIDFromUser("Introduzca el 'id' de la persona que quiere borrar o '0' para cancelar: ");

            Person partner = person.getPartner();
            if(partner != null)
                partner.setPartner(null);
            Person father = person.getFather();
            if(father != null)
                father.getChildren().remove(person);
            Person mother = person.getMother();
            if(mother != null)
                mother.getChildren().remove(person);

            personList.remove(person);
            System.out.println(person.getName() + " borrada correctamente.");
        } catch (SafeCancelException e) {
            System.out.println("Abortando operación...");
        }
    }

    private void addPartner(){
        printPeople();

        try {
            Person person1 = getPersonByIDFromUser("Introduzca el 'id' de la persona que a la que quiere " +
                    "añadir una pareja o '0' para cancelar: ");
            if (person1.getPartner() != null){
                System.out.println(person1.getName() + " ya tiene pareja");
                return;
            }

            Person person2 = getPersonByIDFromUser("Introduzca el 'id' de la persona que quiere " +
                    "añadir como pareja de " + person1 + " o '0' para cancelar: ");
            if (person2.getPartner() != null){
                System.out.println(person2.getName() + " ya tiene pareja");
                return;
            }
            if (person1 == person2){
                System.out.println("No puede seleccionar a la misma persona como pareja");
                return;
            }

            person1.setPartner(person2);
            person2.setPartner(person1);
        } catch (SafeCancelException e) {
            System.out.println("Abortando operación...");
        }
    }

    private void addChild(){
        printPeople();

        try{
            Person child = getPersonByIDFromUser("Introduzca el 'id' del hijo/a; o '0' para cancelar: ");

            if (child.getFather() != null)
                System.out.println("Esta persona ya tiene un padre");
            else {
                Person father = getPersonByIDFromUser("Introduzca el 'id' del padre; o '0' para cancelar: ");
                if (child == father){
                    System.out.println("No puede elegir a la misma persona como padre");
                }
                father.addChild(child);
                child.setFather(father);
            }
            if (child.getMother() != null)
                System.out.println("Esta persona ya tiene una madre");
            else{
                Person mother = getPersonByIDFromUser("Introduzca el 'id' de la madre; o '0' para cancelar: ");
                if (child == mother){
                    System.out.println("No puede elegir a la misma persona como madre");
                }
                mother.addChild(child);
                child.setMother(mother);
            }
        } catch (SafeCancelException e) {
            System.out.println("Abortando operación...");
        }
    }

    private void printFamilyTree(){
        List<Person> printedPeople = new ArrayList<>();
        for(Person person : personList){
            if (printedPeople.contains(person))
                continue; //Ya está pintado
            if (person.hasParents())
                continue; //Tiene personas por encima en el árbol

            if (person.getPartner() != null){
                if (person.getPartner().hasParents())
                    continue;
            }

            printPersonTree(printedPeople, person, "");
            System.out.println();
        }
    }

    private void printPersonTree(List<Person> printedPeople, Person person, String indent){
        System.out.print(person.getName());
        printedPeople.add(person);

        if (person.getPartner() != null){
            System.out.println("/" + person.getPartner().getName());
            printedPeople.add(person.getPartner());
        } else
            System.out.println();

        for (Person child : person.getChildren()){
            System.out.print(indent + "|_> ");
            printPersonTree(printedPeople, child, indent.concat("\t\t"));
        }
    }

    private Person getPersonByIDFromUser(String message) throws SafeCancelException {
        Integer idPerson = askIDToUser(message);
        if (idPerson == 0)
            throw new SafeCancelException();

        Person person = searchPersonByID(idPerson);
        if (person == null){
            System.out.println("No hay nadie registrado con ese 'id'");
            throw new SafeCancelException();
        }

        return person;
    }

    private Integer askIDToUser(String message){
        Integer id = null;
        while(id == null){
            System.out.print(message);
            try{
                id = Integer.parseInt(sc.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Error. Debe introducir un número");
            }
        }

        return id;
    }

    private Person searchPersonByID(int idPerson){
        for (Person person : personList){
            if (person.getID() == idPerson)
                return person;
        }

        return null;
    }

    private void printOptions(){
        System.out.println("---Opciones---");
        System.out.println("1. Añadir persona");
        System.out.println("2. Borrar persona");
        System.out.println("3. Añadir pareja de persona");
        System.out.println("4. Añadir hijo/s de persona");
        System.out.println("5. Imprimir árbol genealógico");
        System.out.println("6. Salir del programa");
        System.out.println("----------------------");
    }

    private void printPeople(){
        for (Person p : personList)
            System.out.println(p);
    }

    public class Person {
        final private Integer ID;
        final private String NAME;
        private Person partner;
        private Person mother;
        private Person father;
        private List<Person> children;

        public Person(Integer ID, String name) {
            this.ID = ID;
            this.NAME = name;
            children = new ArrayList<>();
        }

        public Integer getID() {
            return ID;
        }

        public String getName() {
            return NAME;
        }

        public Person getPartner() {
            return partner;
        }

        public void setPartner(Person partner) {
            this.partner = partner;
        }

        public List<Person> getChildren() {
            return children;
        }

        public boolean addChild(Person child){
            if (!children.contains(child))
                return children.add(child);
            else
                return false;
        }

        public Person getMother() {
            return mother;
        }

        public void setMother(Person mother) {
            this.mother = mother;
        }

        public Person getFather() {
            return father;
        }

        public void setFather(Person father) {
            this.father = father;
        }

        public boolean hasParents(){
            return father != null || mother != null;
        }

        @Override
        public String toString() {
            return NAME + "[id:" + ID + "]";
        }
    }

    public class SafeCancelException extends Exception{}
}
