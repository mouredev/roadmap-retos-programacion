// Autor: Héctor Adán 
// GitHub: https://github.com/hectorio23

class Person {
    constructor(id, name, partner = null) {
        this.id = id;  // Unique identifier
        this.name = name;  // Person's name
        this.partner = partner;  // Optional partner
        this.children = [];  // List of children
    }

    addChild(child) {
        if (this.getParents(child).length < 2) {
            this.children.push(child);
        } else {
            throw new Error(`${child.name} already has two parents.`);
        }
    }

    setPartner(partner) {
        if (!this.partner) {
            this.partner = partner;
            partner.partner = this;  // Mutual partnership
        } else {
            throw new Error(`${this.name} already has a partner.`);
        }
    }

    getParents(person) {
        // Find parents by checking who has this person as a child
        return Person.allInstances.filter(p => p.children.includes(person));
    }

    static displayTree(person, level = 0) {
        if (person.partner ) {
            console.log("  ".repeat(level) + person.partner.name);
        }
        console.log("  ".repeat(level) + person.name);
        person.children.forEach(child => {
            Person.displayTree(child, level + 1);
        });
    }
}

// Keep track of all instances
Person.allInstances = [];

// Sample usage
const alice = new Person(1, "Andrea");
Person.allInstances.push(alice);
const bob = new Person(2, "Adan");
Person.allInstances.push(bob);
alice.setPartner(bob);
const charlie = new Person(3, "Alejandro");
Person.allInstances.push(charlie);
alice.addChild(charlie);
Person.displayTree(alice);

