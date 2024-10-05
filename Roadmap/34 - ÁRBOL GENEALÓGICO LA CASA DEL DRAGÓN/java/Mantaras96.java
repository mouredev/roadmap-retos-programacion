package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class Mantaras96 {

    public static void main(String[] args) {

        // Crear personas
        Person person1 = new Person("Meri");
        Person person2 = new Person("John");
        Person child1 = new Person("Tom");
        Person child2 = new Person("Anna");

        // Establecer relaciones
        person1.setPartner(person2);

        // Añadir hijos
        person1.addChild(child1);
        person1.addChild(child2);

        // Imprimir la familia de person1
        printFamily(person1);
        System.out.println("####################### Persona2 #######################");
        printFamily(person2);

    }

    public static class Person {

        private final String identifier;
        private Person partner;
        private final String name;
        private List<Person> children;

        public Person(String name) {
            this.identifier = UUID.randomUUID().toString();
            this.name = name;
            this.children = new ArrayList<Person>(); // Initialize the list
        }

        public String getIdentifier() {
            return identifier;
        }

        public Person getPartner() {
            return partner;
        }

        public void setPartner(Person partner) {
            if (this.partner != partner) {
                this.partner = partner;
                if (partner != null && partner.getPartner() != this) {
                    partner.setPartner(this);
                }
            }
        }

        public String getName() {
            return name;
        }

        public List<Person> getChildren() {
            return children;
        }

        public void setChildren(List<Person> children) {
            this.children = children;
        }

        public void addChild(Person child) {
            if (!this.children.contains(child)) {
                this.children.add(child);
                if (this.partner != null && !this.partner.getChildren().contains(child)) {
                    this.partner.getChildren().add(child);
                }
            }
        }

        @Override
        public String toString() {
            return "My name is " + this.name;
        }

    }

    private static void printFamily(Person persona) {
        String info = persona.toString();
        if (persona.getPartner() != null) {
            info += " y mi pareja es " + persona.getPartner().getName();
        } else {
            info += " y no tengo pareja";
        }
        System.out.println(info);
    
        if (persona.getChildren().size() > 0) {
            System.out.println("----------- Hijos ----------");
            for (Person child : persona.getChildren()) {
                System.out.println("Soy el hijo de " + persona.getName() + " y mi nombre es " + child.getName());
                printFamily(child);
            }
        } else {
            System.out.println(" No tengo hijos ");
        }
    }
    

}
