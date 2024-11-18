import java.util.*;

/**
 * #34 ÁRBOL GENEALÓGICO DE LA CASA DEL DRAGÓN
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    public static void main(String[] args) {
        FamilyTree tree = new FamilyTree();

        tree.addPerson(1, "Jocelyn", Gender.FEMALE);
        tree.addPerson(2, "Aemon", Gender.MALE);

        tree.setPartner(1, 2);

        tree.addPerson(3, "Rhaenys", Gender.FEMALE);

        tree.addChild(1, 3);

        tree.addPerson(4, "Corlys", Gender.MALE);

        tree.setPartner(3, 4);

        tree.addPerson(5, "Laena", Gender.FEMALE);
        tree.addPerson(6, "Laenor", Gender.MALE);

        tree.addChild(3, 5);
        tree.addChild(3, 6);

        tree.addPerson(7, "Baelon", Gender.MALE);
        tree.addPerson(8, "Alyssa", Gender.FEMALE);

        tree.setPartner(7, 8);

        tree.addPerson(9, "Viserys I", Gender.MALE);
        tree.addPerson(10, "Daemon", Gender.MALE);

        tree.addChild(7, 9);
        tree.addChild(8, 10);

        tree.addPerson(11, "Aemma", Gender.FEMALE);

        tree.setPartner(9, 11);

        tree.addPerson(12, "Rhaenyra", Gender.FEMALE);

        tree.addChild(9, 12);

        tree.setPartner(10, 12);

        tree.addPerson(13, "Aegon", Gender.MALE);
        tree.addPerson(14, "Viserys", Gender.MALE);

        tree.addChild(12, 13);
        tree.addChild(12, 14);

        tree.displayTree();
    }

    static class Person implements Comparable<Person> {
        private Integer id;
        private String name;
        private Integer level;
        private Gender gender;
        private Person partner;
        private Person father;
        private Person mother;
        private Set<Person> children;

        public Person(Integer id, String name, Gender gender) {
            this.id = id;
            this.name = name;
            this.level = 0;
            this.gender = gender;
            this.partner = null;
            this.father = null;
            this.mother = null;
            children = new TreeSet<>();
        }

        public Integer getId() {
            return id;
        }

        public void setId(Integer id) {
            this.id = id;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public Integer getLevel() {
            return level;
        }

        public void setLevel(Integer level) {
            this.level = level;
        }

        public Gender getGender() {
            return gender;
        }

        public void setGender(Gender gender) {
            this.gender = gender;
        }

        public Person getPartner() {
            return partner;
        }

        public void setPartner(Person partner) {
            this.partner = partner;
        }

        public Person getFather() {
            return father;
        }

        public void setFather(Person father) {
            if (getFather() == null) {
                if (father != null) {
                    father.addChild(this);
                    this.father = father;
                    System.out.printf("A %s se le ha asignado un padre: %s.%n", getName(), father.getName());
                } else System.out.printf("%s aún no tiene asignado un padre.%n", getName());
            } else System.out.printf("%s ya tiene un padre con nombre %s.%n", getName(), getFather().getName());
        }

        public Person getMother() {
            return mother;
        }

        public void setMother(Person mother) {
            if (getMother() == null) {
                if (mother != null) {
                    mother.addChild(this);
                    this.mother = mother;
                    System.out.printf("A %s se le ha asignado una madre: %s.%n", getName(), mother.getName());
                } else System.out.printf("%s aún no tiene asignado un padre.%n", getName());
            } else System.out.printf("%s ya tiene una madre con nombre %s.%n", getName(), getMother().getName());
        }

        public Set<Person> getChildren() {
            return children;
        }

        public void setChildren(Set<Person> children) {
            this.children = children;
        }

        private void addPartner(Person partner) {
            if (getPartner() != null) System.out.printf("%s ya está emparejado con %s.%n", getName(), getPartner());
            else if (partner.getPartner() != null) System.out.printf("%s ya está emparejado con %s.%n",
                    partner.getName(), partner.getPartner());
            else {
                setPartner(partner);
                partner.setPartner(this);
                System.out.printf("%s es pareja de %s.%n", getName(), partner.getName());
            }
        }

        private Person addChild(Person child) {
            if (getChildren().contains(child)) {
                if (child.getGender() == Gender.MALE)
                    System.out.printf("%s ya es hijo de %s.%n", child.getName(), getName());
                if (child.getGender() == Gender.FEMALE)
                    System.out.printf("%s ya es hija de %s.%n", child.getName(), getName());
            } else if (child.getFather() != null && child.getMother() != null)
                System.out.printf("%s tiene como padres a: %s y %s.%n",
                        child.getName(), child.getFather().getName(), child.getMother().getName());
            else {
                getChildren().add(child);
                if (child.getGender() == Gender.MALE)
                    System.out.printf("A %s se le ha asignado un hijo: %s.%n", getName(), child.getName());
                if (child.getGender() == Gender.FEMALE)
                    System.out.printf("A %s se le ha asignado una hija: %s.%n", getName(), child.getName());
                if (getGender() == Gender.MALE) {
                    child.setFather(this);
                    if (child.getMother() == null) child.setMother(getPartner());
                    else System.out.printf("%s tiene como padres a: %s y %s.%n",
                            child.getName(), child.getFather().getName(), child.getMother().getName());
                }
                if (getGender() == Gender.FEMALE) {
                    child.setMother(this);
                    if (child.getFather() == null) child.setFather(getPartner());
                    else System.out.printf("%s tiene como padres a: %s y %s.%n",
                            child.getName(), child.getFather().getName(), child.getMother().getName());
                }
            }
            return this;
        }

        @Override
        public int compareTo(Person other) {
            return this.id.compareTo(other.id);
        }
    }

    public enum Gender {
        MALE("Hombre"),
        FEMALE("Mujer");

        private final String displayName;

        // Constructor to initialize the display name
        Gender(String displayName) {
            this.displayName = displayName;
        }

        @Override
        public String toString() {
            return displayName;
        }
    }

    static class FamilyTree {
        private Map<Integer, Person> people;
        private int nivel;

        public FamilyTree() {
            people = new LinkedHashMap<>();
        }

        private void addPerson(Integer id, String name, Gender gender) {
            if (people.containsKey(id)) System.out.printf("La persona con ID: %d ya existe!%n", id);
            else {
                Person person = new Person(id, name, gender);
                people.put(id, person);
                System.out.printf("La persona con nombre %s [ID: %d] ha sido añadida al árbol.%n", name, id);
            }
        }

        private void removePerson(Integer id) {
            if (people.containsKey(id)) {
                Person person = people.get(id);
                people.remove(id);
                System.out.printf("La persona con nombre %s [ID: %d] ha sido removida del árbol.%n",
                        person.getName(), id);
            }
        }

        private void setPartner(Integer id1, Integer id2) {
            if (people.containsKey(id1)) {
                if (people.containsKey(id2)) people.get(id1).addPartner(people.get(id2));
                else System.out.printf("El ID: %d no existe en el árbol!%n", id2);
            } else System.out.printf("El ID: %d no existe en el árbol!%n", id1);
        }

        private void addChild(Integer parentId, Integer childId) {
            if (parentId.equals(childId)) System.out.printf("Los IDs: %d y %d no pueden ser iguales!%n",
                    parentId, childId);
            if (people.containsKey(parentId)) {
                Person parent = people.get(parentId);
                if (parent.getPartner() == null)
                    System.out.printf("%s no tiene pareja. Se necesita una pareja para poder tener un hijo.%n",
                            parent.getName());
                else if (people.containsKey(childId)) {
                    parent.addChild(people.get(childId));
                } else System.out.printf("El ID: %d del niño no existe en el árbol!%n", childId);
            } else System.out.printf("El ID: %d del padre/madre no existe en el árbol!%n", parentId);
        }

        private void displayTree() {
            Set<Integer> visited = new LinkedHashSet<>();
            int level = 0;
            nivel = 0;
            people.values().forEach(person -> {
                if (person.getFather() == null && person.getMother() == null) {
                    displayPerson(person, level, visited);
                }
            });
        }

        private void displayPerson(Person person, int level, Set<Integer> visited) {
            if (visited.contains(person.getId()) && level == person.getLevel()) return;
            if (level == 0) {
                System.out.println("-".repeat(60));
                System.out.printf("Árbol #%d:%n", ++nivel);
            }
            visited.add(person.getId());
            person.setLevel(level);
            String indent1 = "\t".repeat(level) + "└> ";
            String indent2 = "\t".repeat(level) + "   ";
            System.out.printf("%s%s [ID: %d]%n", indent1, person.getName(), person.getId());
            Person partner = person.getPartner();
            Set<Person> children = person.getChildren();
            if (partner != null) {
                visited.add(person.getPartner().getId());
                System.out.printf("%sPareja: %s [ID: %d]%n", indent2, partner.getName(), partner.getId());
            }
            if (!person.getChildren().isEmpty()) {
                System.out.printf("%sHijos:%n", indent2);
                children.forEach(child -> {
                    child.setLevel(level);
                    displayPerson(child, level + 1, visited);
                });
            }
        }
    }
}
