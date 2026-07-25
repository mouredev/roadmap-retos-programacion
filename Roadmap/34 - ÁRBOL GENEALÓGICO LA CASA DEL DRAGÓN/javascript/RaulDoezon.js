/*
 * EJERCICIO:
 * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026! 
 * ¿Alguien se entera de todas las relaciones de parentesco
 * entre personajes que aparecen en la saga?
 * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 * Requisitos:
 * 1. Estará formado por personas con las siguientes propiedades:
 *    - Identificador único (obligatorio)
 *    - Nombre (obligatorio)
 *    - Pareja (opcional)
 *    - Hijos (opcional)
 * 2. Una persona sólo puede tener una pareja (para simplificarlo).
 * 3. Las relaciones deben validarse dentro de lo posible.
 *    Ejemplo: Un hijo no puede tener tres padres.
 * Acciones:
 * 1. Crea un programa que permita crear y modificar el árbol.
 *    - Añadir y eliminar personas
 *    - Modificar pareja e hijos
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 * 
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
*/

class Person {
  constructor(id, name) {
    this.id = id;
    this.name = name;
    this.partner = null;
    this.children = [];
    this.has_parents = false;
  }

  addPartner(partner) {
    if (this.partner !== null) {
      console.log(`${this.name} ya tiene pareja: ${this.partner.name}.`);
    } else {
      this.partner = partner;
      partner.partner = this;

      console.log(`${this.name} es pareja de ${partner.name}.`);
    }
  }

  addChild(child) {
    if (!this.children.includes(child)) {
      this.children.push(child);

      console.log(`${child.name} es hijo/a de ${this.name}`);
    } else {
      console.log(`${child.name} es hijo/a de ${this.name}.`);
    }
  }
}

class FamilyTree {
  constructor() {
    this.people = {};
  }

  addPerson(id, name) {
    if (id in this.people) {
      console.log(`La persona con ID: ${id} ya existe.`);
    } else {
      const person = new Person(id, name);

      this.people[id] = person;

      console.log(`${name} (ID: ${id}) se agregó al árbol.`);
    }
  }

  removePerson(id) {
    if (id in this.people) {
      const person = this.people[id];

      delete this.people[id];

      console.log(`${person.name} (ID: ${id}) se eliminó del árbol.`);
    } else {
      console.log(`La persona con ID: ${id} no existe en el árbol.`);
    }
  }

  setPartner(id1, id2) {
    if (id1 in this.people && id2 in this.people) {
      const person1 = this.people[id1];
      const person2 = this.people[id2];

      person1.addPartner(person2);
    } else {
      console.log("Algún ID no existe en el árbol.");
    }
  }

  addChild(parent_id, child_id) {
    if (parent_id in this.people && child_id in this.people) {
      if (parent_id === child_id) {
        console.log("Los ID no pueden ser iguales a la hora de asignar un hijo.");
      } else {
        const parent = this.people[parent_id];

        if (parent.partner === null) {
          console.log("Se necesita una pareja para poder tener un hijo.");
        } else {
          const child = this.people[child_id];

          if (child.has_parents) {
            console.log(`${child.name} (ID: ${child.id}) ya tiene padres.`);
          } else {
            child.has_parents = true;
            parent.addChild(child);
            parent.partner.addChild(child);
          }
        }
      }
    } else {
      console.log("Algún ID no existe en el árbol.");
    }
  }

  printTree() {
    const visited = new Set();
    const printPerson = (person, level = 0) => {
      if (visited.has(person.id)) {
        return;
      }

      visited.add(person.id);

      const indent = "\t".repeat(level);

      console.log(`${indent} - ${person.name} (ID: ${person.id})`);

      if (person.partner) {
        visited.add(person.partner.id);

        console.log(`${indent}   Pareja: ${person.partner.name} (ID: ${person.partner.id})`);
      }

      if (person.children.length > 0) {
        console.log(`${indent}   Hijos:`);

        for (const child of person.children) {
          printPerson(child, level + 1);
        }
      }
    };

    for (const person of Object.values(this.people)) {
      const is_child = person.has_parents;

      if (!is_child) {
        printPerson(person);
      }
    }
  }
}

let tree = new FamilyTree();

tree.addPerson(0, "Raditz");
tree.addPerson(1, "Goku");
tree.addPerson(2, "Milk");
tree.addPerson(3, "Gohan");
tree.addPerson(4, "Goten");
tree.addPerson(5, "Videl");
tree.addPerson(6, "Pan");

tree.removePerson(0);

tree.setPartner(1, 2);
tree.setPartner(3, 5);

tree.addChild(1, 3);
tree.addChild(1, 4);
tree.addChild(3, 6);

tree.printTree();
