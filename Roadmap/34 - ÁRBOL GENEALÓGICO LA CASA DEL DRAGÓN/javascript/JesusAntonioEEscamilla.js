/** #34 - JavaScript -> Jesus Antonio Escamilla */

/**
 * ÁRBOL GENEALÓGICO DE LA CASA DEL DRAGÓN.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

class Persona {
    constructor(id, name) {
        this.id = id;
        this.name = name;
        this.partner = null;
        this.children = [];
        this.parents = [];
    }
}

class ArbolGenealogico {
    constructor() {
        this.people = new Map(); // Almacenamos personas usando un Map para un acceso rápido
    }
    
    addPersona(id, name) {
        if (this.people.has(id)) {
            console.log(`La persona con id ${id} ya existe.`);
            return;
        }
        const person = new Persona(id, name);
        this.people.set(id, person);
        console.log(`Persona ${name} añadida con id ${id}.`);
    }
    
    removePersona(id) {
        if (!this.people.has(id)) {
            console.log(`La persona con id ${id} no existe.`);
            return;
        }
        const person = this.people.get(id);
        
        // Quitar la relación de pareja
        if (person.partner) {
            const partner = this.people.get(person.partner);
            partner.partner = null;
        }
        
        // Quitar la relación de hijos
        person.children.forEach(childId => {
            const child = this.people.get(childId);
            child.parents = child.parents.filter(parentId => parentId !== id);
        });
        
        this.people.delete(id);
        console.log(`Persona con id ${id} eliminada.`);
    }
    
    assignPareja(id1, id2) {
        if (!this.people.has(id1) || !this.people.has(id2)) {
            console.log('Una o ambas personas no existen.');
            return;
        }
        
        const person1 = this.people.get(id1);
        const person2 = this.people.get(id2);
    
        if (person1.partner || person2.partner) {
            console.log('Una de las personas ya tiene pareja.');
            return;
        }
    
        person1.partner = id2;
        person2.partner = id1;
        console.log(`${person1.name} y ${person2.name} ahora son pareja.`);
    }
    
    addHijo(parentId, childId) {
        if (!this.people.has(parentId) || !this.people.has(childId)) {
            console.log('El padre o el hijo no existen.');
            return;
        }
    
        const parent = this.people.get(parentId);
        const child = this.people.get(childId);
    
        if (child.parents && child.parents.length >= 2) {
            console.log(`${child.name} ya tiene dos padres.`);
            return;
        }
    
        parent.children.push(childId);
        if (!child.parents) {
            child.parents = [];
        }
        child.parents.push(parentId);
        console.log(`${child.name} añadido como hijo de ${parent.name}.`);
    }
    
    removeHijo(parentId, childId) {
        if (!this.people.has(parentId) || !this.people.has(childId)) {
            console.log('El padre o el hijo no existen.');
            return;
        }
    
        const parent = this.people.get(parentId);
        parent.children = parent.children.filter(id => id !== childId);
        const child = this.people.get(childId);
        child.parents = child.parents.filter(id => id !== parentId);
    
        console.log(`${child.name} eliminado como hijo de ${parent.name}.`);
    }

    imprimirArbol() {
        const visited = new Set();
    
        const printPerson = (person, level = 0) => {
            if (visited.has(person.id)) {
                return; // Evita ciclos
            }

            visited.add(person.id);
            
            const indent = '\t'.repeat(level);
            console.log(`${indent}- ${person.name} [ID: ${person.id}]`);
            
            if (person.partner) {
                const partner = this.people.get(person.partner);
                if (partner) {
                    visited.add(partner.id);
                    console.log(`${indent}  Pareja: ${partner.name} [ID: ${partner.id}]`);
                }
            }
            
            if (person.children.length > 0) {
                console.log(`${indent}  Hijos:`);
                person.children.forEach(childId => {
                const child = this.people.get(childId);
                if (child) {
                    printPerson(child, level + 1);
                }
                });
            }
        };
        
        // Iniciar impresión para cada persona que no sea hijo (raíz)
        this.people.forEach(person => {
        const isChild = person.parents.length > 0;
        if (!isChild) {
            printPerson(person);
        }
        });
    }

}

// Ejemplo de uso
const arbol = new ArbolGenealogico();

arbol.addPersona(1, "Jocelyn");
arbol.addPersona(2, "Aemon");

arbol.assignPareja(1, 2);

arbol.addPersona(3, "Rhaenys");

arbol.addHijo(1, 3);

arbol.addPersona(4, "Corlys");

arbol.assignPareja(3, 4);

arbol.addPersona(5, "Laena");
arbol.addPersona(6, "Laenor");

arbol.addHijo(3, 5);
arbol.addHijo(3, 6);

arbol.addPersona(7, "Baelon");
arbol.addPersona(8, "Alyssa");

arbol.assignPareja(7, 8);

arbol.addPersona(9, "Viserys I");
arbol.addPersona(10, "Daemon");

arbol.addHijo(7, 9);
arbol.addHijo(8, 10);

arbol.addPersona(11, "Aemma");

arbol.assignPareja(9, 11);

arbol.addPersona(12, "Rhaenyra");

arbol.addHijo(9, 12);

arbol.assignPareja(10, 12);

arbol.addPersona(13, "Aegon");
arbol.addPersona(14, "Viserys");

arbol.addHijo(12, 13);
arbol.addHijo(12, 14);

arbol.imprimirArbol();