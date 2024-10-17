package com.amsoft.roadmap.example34;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Example34 {
    public static void main(String[] args) {
        FamilyTree tree = new FamilyTree();

        Person p1 = new Person("Persona 01");
        Person p2 = new Person("Persona 02");
        Person p3 = new Person("Persona 03");
        Person p4 = new Person("Persona 04");
        Person p5 = new Person("Persona 05");

        p1.setPartner(p2);
        p2.setPartner(p1);

        p1.addChildren(p3, p4);
        p2.addChildren(p3, p4);

        p3.addChild(p5);

        tree.addPeople(p1, p2, p3, p4, p5);

        tree.printTree();
    }

    static class Person {
        private final UUID id = UUID.randomUUID();
        private final String name;
        private Person partner;
        private List<Person> children;

        public Person(String name) {
            this.name = name;
            this.children = new ArrayList<>();
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
            Optional.ofNullable(this.partner)
                    .ifPresentOrElse(p -> System.out.println("Error: " + this.name + " ya tiene pareja."),
                            () -> this.partner = partner);
        }

        public List<Person> getChildren() {
            return children;
        }

        public void addChild(Person child) {
            if (children.stream().noneMatch(c -> c.equals(child))) {
                children = Stream.concat(children.stream(), Stream.of(child))
                        .collect(Collectors.toList());
            } else {
                System.out.println("Error: El hijo " + child.getName() + " ya existe.");
            }
        }


        public void addChildren(Person... children) {
            Arrays.stream(children)
                    .forEach(this::addChild);
        }
    }

    static class FamilyTree {
        private List<Person> people;

        public FamilyTree() {
            this.people = new ArrayList<>();
        }

        public void addPeople(Person... persons) {
            people = Stream.concat(people.stream(), Arrays.stream(persons))
                    .distinct()
                    .collect(Collectors.toList());
        }

        public void removePerson(Person person) {
            Optional.of(people.remove(person))
                    .ifPresentOrElse(p -> System.out.println(person.getName() + " eliminado."),
                            () -> System.out.println("Error: Persona no encontrada."));
        }

        public void printTree() {
            people.forEach(person -> {
                System.out.println("ID: " + person.getId() + ", Name: " + person.getName());
                Optional.ofNullable(person.getPartner())
                        .ifPresent(p -> System.out.println("  Pareja: " + p.getName()));
                if (!person.getChildren().isEmpty()) {
                    System.out.println("  Hijos: " + person.getChildren()
                            .stream()
                            .map(Person::getName)
                            .collect(Collectors.joining(", ")));
                }
            });
        }
    }
}
