class Person {
    constructor(id, name) {
        this.id = id;
        this.name = name;
        this.partner = null;
        this.children = [];
    }

    setPartner(partner) {
        this.partner = partner;
    }

    addChild(child) {
        this.children.push(child);
    }
}

class FamilyTree {
    constructor() {
        this.people = {};
    }

    addPerson(id, name) {
        this.people[id] = new Person(id, name);
    }

    removePerson(id) {
        delete this.people[id];
    }

    setPartner(id1, id2) {
        if (this.people[id1] && this.people[id2]) {
            this.people[id1].setPartner(this.people[id2]);
            this.people[id2].setPartner(this.people[id1]);
        }
    }

    addChild(parentId, childId) {
        if (this.people[parentId] && this.people[childId]) {
            this.people[parentId].addChild(this.people[childId]);
        }
    }

    printTree() {
        Object.values(this.people).forEach(person => {
            if (!this.hasParents(person)) {
                this.printSubTree(person);
                console.log("");
            }
        });
    }

    printSubTree(person, indent = 0) {
        console.log(" ".repeat(indent) + person.name + (person.partner ? " ⟷ " + person.partner.name : ""));
        person.children.forEach(child => {
            this.printSubTree(child, indent + 4);
        });
    }

    hasParents(person) {
        return Object.values(this.people).some(other => other.children.includes(person));
    }
}

let tree = new FamilyTree();
tree.addPerson(1, "Aegon I Targaryen");
tree.addPerson(2, "Rhaenys Targaryen");
tree.addPerson(3, "Visenya Targaryen");

tree.addPerson(4, "Aenys I Targaryen");
tree.addPerson(5, "Maegor I Targaryen");

tree.addPerson(6, "Jaehaerys I Targaryen");
tree.addPerson(7, "Alysanne Targaryen");

tree.addPerson(8, "Aegon II Targaryen");
tree.addPerson(9, "Helaena Targaryen");

tree.addPerson(10, "Viserys II Targaryen");

tree.addPerson(11, "Rhaenyra Targaryen");
tree.addPerson(12, "Daemon Targaryen");

tree.setPartner(1, 2); // Aegon I y Rhaenys
tree.setPartner(1, 3); // Aegon I y Visenya
tree.setPartner(4, 7); // Jaehaerys I y Alysanne
tree.setPartner(8, 9); // Aegon II y Helaena
tree.setPartner(11, 12); // Rhaenyra y Daemon

tree.addChild(1, 4); // Aenys I hijo de Aegon I y Rhaenys
tree.addChild(1, 5); // Maegor I hijo de Aegon I y Visenya

tree.addChild(4, 6); // Jaehaerys I hijo de Aenys I
tree.addChild(4, 11); // Rhaenyra hija de Aenys I

tree.addChild(6, 8); // Aegon II hijo de Jaehaerys I
tree.addChild(6, 10); // Viserys II hijo de Jaehaerys I

tree.printTree();
