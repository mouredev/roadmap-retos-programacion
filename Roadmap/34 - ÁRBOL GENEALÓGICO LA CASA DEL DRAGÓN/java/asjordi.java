import java.util.LinkedList;
import java.util.List;
import java.util.UUID;

public class asjordi {

    public static void main(String[] args) {
        FamilyTree tree = new FamilyTree();

        Person john = new Person("John");
        Person jane = new Person("Jane");
        Person jack = new Person("Jack");
        Person jill = new Person("Jill");
        Person jenny = new Person("Jenny");

        john.setPartner(jane);
        jane.setPartner(john);

        john.addChild(jack);
        john.addChild(jill);
        jane.addChild(jack);
        jane.addChild(jill);

        jack.addChild(jenny);

        tree.addPerson(john);
        tree.addPerson(jane);

        tree.printTree();

    }

    static class Person {
        private final UUID id = UUID.randomUUID();
        private String name;
        private Person partner;
        private List<Person> children;

        public Person(String name) {
            this.name = name;
            this.children = new LinkedList<>();
        }

        public UUID getId() {
            return id;
        }

        public String getName() {
            return name;
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

        public void addChild(Person child) {
            this.children.add(child);
        }

        public void removeChild(Person child) {
            this.children.remove(child);
        }
    }

    static class FamilyTree {
        private List<Person> people;

        public FamilyTree() {
            this.people = new LinkedList<>();
        }

        public void addPerson(Person person) {
            this.people.add(person);
        }

        public void removePerson(Person person) {
            this.people.remove(person);
        }

        public void printTree() {
            for (Person person : people) {
                System.out.println("ID: " + person.getId() + ", Name: " + person.getName());
                if (person.getPartner() != null) System.out.println("  Partner: " + person.getPartner().getName());
                if (!person.getChildren().isEmpty()) {
                    System.out.println("  Children: ");
                    for (Person child : person.getChildren()) {
                        System.out.println("    - " + child.getName());
                    }
                }
            }
        }
    }

}
