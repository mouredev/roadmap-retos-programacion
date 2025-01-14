/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#34 ÁRBOL GENEALÓGICO DE LA CASA DEL DRAGÓN
-------------------------------------------------------
#  * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
#  * ¿Alguien se entera de todas las relaciones de parentesco
#  * entre personajes que aparecen en la saga?
#  * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
#  * Requisitos:
#  * 1. Estará formado por personas con las siguientes propiedades:
#  *    - id_entificador único (obligatorio)
#  *    - Nombre (obligatorio)
#  *    - Pareja (opcional)
#  *    - Hijos (opcional)
#  * 2. Una persona sólo puede tener una pareja (para simplificarlo).
#  * 3. Las relaciones deben valid_arse dentro de lo posible.
#  *    Ejemplo: Un hijo no puede tener tres padres.
#  * Acciones:
#  * 1. Crea un programa que permita crear y modificar el árbol.
#  *    - Añadir y eliminar personas
#  *    - Modificar pareja e hijos
#  * 2. Podrás imprimir el árbol (de la manera que consid_eres).
#  *
#  * NOTA: Ten en cuenta que la complejidad puede ser alta si
#  * se implementan todas las posibles relaciones. Intenta marcar
#  * tus propias reglas y límites para que te resulte asumible.

*/
// ________________________________________________________
// NOTE: Here is the 'people.json' file with the data if you want to test it:
//       https://pastebin.com/29kWWgPU
//       Just paste it into the base folder where file.py is located.

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

class Input {
    async inputStr(msg) {
        while (true) {
            const txt = await new Promise((resolve) => {
                rl.question(msg, (answer) => {
                    resolve(answer.trim());
                });
            });

            if (txt.length > 0) {
                return txt;
            }
            console.log("\n❌ This field cannot be empty.");
        }
    }

    async inputInt(msg) {
        while (true) {
            const txt = await this.inputStr(msg);
            if (/^\d+$/.test(txt)) {
                return parseInt(txt);
            }
            console.log("\n❌ Enter an integer.");
        }
    }
}

class Person {
    constructor(id, name) {
        this.id = id;
        this.name = name;
        this.parents = [];
        this.partners = [];
        this.children = {};
        this.deleted = false;
    }

    toJSON() {
        return {
            id: this.id,
            name: this.name,
            parents: this.parents,
            partners: this.partners,
            children: this.children,
            deleted: this.deleted
        };
    }

    static fromJSON(data) {
        const person = new Person(data.id, data.name);
        person.parents = data.parents || [];
        person.partners = data.partners || [];
        person.children = Object.fromEntries(
            Object.entries(data.children || {}).map(([k, v]) => [parseInt(k), v])
        );
        person.deleted = data.deleted || false;
        return person;
    }

    toString() {
        return `Person(id=${this.id}, name='${this.name}')`;
    }
}

class People extends Input {
    constructor(filename = "people.json") {
        super();
        this._people = [];
        this._filename = filename;
        this.loadFromJSON();
    }

    getPeople() {
        return this._people;
    }

    async loadFromJSON() {
        try {
            const fs = require('fs');
            const data = JSON.parse(fs.readFileSync(this._filename, 'utf8'));
            this._people = data.map(personData => Person.fromJSON(personData));
            console.log(`✅ The file '${this._filename}' has been successfully loaded.`);
        } catch (error) {
            console.log(`⚠️ The file '${this._filename}' not found. Starting with an empty list.`);
            this._people = [new Person(0, "unknown")];
        }
    }

    async saveToJSON() {
        try {
            const fs = require('fs');
            const data = this._people.map(person => person.toJSON());
            fs.writeFileSync(this._filename, JSON.stringify(data, null, 2));
            console.log(`✅ Data saved successfully to ${this._filename}`);
        } catch (error) {
            console.log(`❌ An error occurred while saving to '${this._filename}': ${error}. Data may not have been saved.`);
        }
    }

    printPeople() {
        console.log("_".repeat(32));
        console.log(`|${this.centerText("id", 4)}|${this.centerText("Name", 25)}|`);
        console.log("_".repeat(32));

        this._people.forEach(person => {
            if (!person.deleted) {
                console.log(`|${this.centerText(String(person.id), 4)}|${this.centerText(person.name, 25)}|`);
            }
        });

        console.log("_".repeat(32));
    }

    centerText(text, width) {
        const padding = width - text.length;
        const leftPad = Math.floor(padding / 2);
        const rightPad = padding - leftPad;
        return " ".repeat(leftPad) + text + " ".repeat(rightPad);
    }

    getPersonById(id) {
        if (id >= 0 && id < this._people.length) {
            return this._people[id];
        }
        console.log("❌ id not found.");
        return null;
    }

    async addPerson() {
        console.log("Add Person or 'x' to Exit");
        const name = await this.inputStr("Name: ");
        if (name.toLowerCase() === "x") {
            console.log("Exit");
            return;
        }

        const newId = Math.max(-1, ...this._people.map(p => p.id)) + 1;
        const newPerson = new Person(newId, name);
        this._people.push(newPerson);
        console.log(`✅ Added: ${newPerson}`);
        await this.saveToJSON();
    }

    async removePerson() {
        this.printPeople();
        console.log("\nPerson ID to mark as deleted or a letter to exit.");
        const idStr = await this.inputStr("ID: ");
        if (!/^\d+$/.test(idStr)) {
            console.log("Exit");
            return;
        }

        const person = this.getPersonById(parseInt(idStr));
        if (!person) return;

        if (person.partners.length || person.parents.length) {
            console.log("❌ You cannot delete a person who is linked to parents or partners.");
            return;
        }

        person.deleted = true;
        console.log(`✅ '${person.name}' is marked as deleted.`);
        await this.saveToJSON();
    }

    get length() {
        return this._people.length;
    }
}

class Partners extends People {
    async #add(partners, idPerson) {
        console.log("Select Partner ID");
        const idPartner = await this.inputInt("ID: ");
        const partner = this.getPersonById(idPartner);
        if (!partner || partner.deleted) {
            console.log("❌ ID not found or the person is deleted.");
            return;
        }

        if (partners.includes(idPartner)) {
            console.log("❌ This partner is already added.");
            return;
        }

        partners.push(idPartner);
        partner.partners.push(idPerson);

        console.log("✅ Partner successfully added.");
        await this.saveToJSON();
    }

    async #remove(partners, idPerson) {
        console.log("Select Partner ID to Delete");
        const id = await this.inputInt("ID: ");
        if (!partners.includes(id)) {
            console.log("❌ ID not found.");
            return;
        }

        const partner = this.getPersonById(id);
        if (!partner) {
            console.log("❌ Partner not found.");
            return;
        }

        if (Object.keys(partner.children).length > 0) {
            console.log("❌ Cannot delete a partner who has children.");
            return;
        }

        partners.splice(partners.indexOf(id), 1);
        partner.partners.splice(partner.partners.indexOf(idPerson), 1);

        console.log("✅ Partner deleted");
        await this.saveToJSON();
    }

    async #options(partners, idPerson) {
        console.log("\n1. Add partner | 2. Remove partner | 3. Exit");
        const option = await this.inputInt("\nOption: ");

        switch (option) {
            case 1:
                await this.#add(partners, idPerson);
                break;
            case 2:
                await this.#remove(partners, idPerson);
                break;
            case 3:
                return;
            default:
                console.log("❌ Invalid option.");
        }
    }

    async editPartners() {
        this.printPeople();
        console.log("\nPerson ID to edit partners or a letter to exit.");
        const idStr = await this.inputStr("ID: ");
        if (!/^\d+$/.test(idStr)) {
            console.log("Exit");
            return;
        }

        const id = parseInt(idStr);
        const person = this.getPersonById(id);
        if (!person || person.deleted) {
            console.log("❌ ID not found or the person is deleted.");
            return;
        }

        console.log(`You selected '${person.name}'`);
        const partners = person.partners;

        if (partners.length > 0) {
            console.log("Partners:");
            partners.forEach(idP => {
                const partner = this.getPersonById(idP);
                if (partner) {
                    console.log(`ID: ${partner.id} -> ${partner.name}`);
                }
            });
        } else {
            console.log("🚫 This person has no partners.");
        }

        await this.#options(partners, id);
    }
}

class Children extends Partners {
    constructor(filename = "people.json") {
        super(filename);
        this._idParent = null;
        this._children = {};
        this._idChild = null;
        this._parents = null;
        this._idPartner = null;
    }

    async #selectPartner(partners) {
        console.log("Partners:");
        partners.forEach(idP => {
            const partner = this.getPersonById(idP);
            if (partner) {
                console.log(`ID: ${partner.id} -> ${partner.name}`);
            }
        });

        console.log("Select the ID of the partner with whom you have the child.");
        const idPartner = await this.inputInt("ID: ");
        const partner = this.getPersonById(idPartner);
        if (!partners.includes(idPartner) || !partner || partner.deleted) {
            console.log("❌ ID not found or the person is deleted.");
            return null;
        }

        return idPartner;
    }

    async #updateChildParent() {
        console.log("Select Child ID");
        const idChild = await this.inputInt("ID: ");
        const child = this.getPersonById(idChild);
        if (!child) {
            console.log("❌ ID not found.");
            return null;
        }

        if (child.parents.length) {
            console.log("❌ This person already has parents.");
            return null;
        }

        const idPartner = this._idPartner;
        if (this._children[idPartner]) {
            if (!this._children[idPartner].includes(idChild)) {
                this._children[idPartner].push(idChild);
            }
        } else {
            this._children[idPartner] = [idChild];
        }

        const parent = this.getPersonById(this._idParent);
        if (parent) {
            parent.children = this._children;
        }

        child.parents = [this._idParent, idPartner];

        return idChild;
    }

    #updateChildPartner(partner) {
        if (this._idParent in partner.children) {
            if (!partner.children[this._idParent].includes(this._idChild)) {
                partner.children[this._idParent].push(this._idChild);
            }
        } else {
            partner.children[this._idParent] = [this._idChild];
        }
    }

    async #add() {
        const parent = this.getPersonById(this._idParent);
        if (!parent) {
            console.log("❌ Parent not found.");
            return;
        }

        const partners = parent.partners;
        if (!partners.length) {
            console.log("❌ This person does not have a partner with whom to have children.");
            return;
        }

        const idPartner = await this.#selectPartner(partners);
        if (!idPartner) return;

        const partner = this.getPersonById(idPartner);
        if (!partner) {
            console.log("❌ Partner not found.");
            return;
        }

        this._idPartner = idPartner;
        const idChild = await this.#updateChildParent();
        if (idChild === null) return;

        this._idChild = idChild;
        this.#updateChildPartner(partner);

        console.log("✅ Child successfully added.");
        await this.saveToJSON();
    }

    async #removeAndUpdate(idParent, idPartner) {
        const parent = this.getPersonById(idParent);
        if (!parent) {
            console.log("❌ Parent not found.");
            return;
        }

        const childrenWithPartner = parent.children[idPartner] || [];
        if (childrenWithPartner.includes(this._idChild)) {
            const index = childrenWithPartner.indexOf(this._idChild);
            childrenWithPartner.splice(index, 1);
            if (childrenWithPartner.length === 0) {
                delete parent.children[idPartner];
            } else {
                parent.children[idPartner] = childrenWithPartner;
            }
        }

        const child = this.getPersonById(this._idChild);
        if (child) {
            const index = child.parents.indexOf(idParent);
            if (index !== -1) {
                child.parents.splice(index, 1);
            }
        }
    }

    async #remove() {
        console.log("Select Child ID to Delete");
        const idChild = await this.inputInt("ID: ");
        const child = this.getPersonById(idChild);
        if (!child) {
            console.log("❌ Child not found.");
            return;
        }

        const parents = child.parents;
        if (parents.length !== 2) {
            console.log("❌ Child does not have two parents.");
            return;
        }

        this._idChild = idChild;
        this._parents = parents;
        const [idP1, idP2] = parents;
        await this.#removeAndUpdate(idP1, idP2);
        await this.#removeAndUpdate(idP2, idP1);

        console.log("✅ Child deleted");
        await this.saveToJSON();
    }

    async #options() {
        console.log("\n1. Add child | 2. Remove child | 3. Exit");
        const option = await this.inputInt("\nOption: ");

        switch (option) {
            case 1:
                await this.#add();
                break;
            case 2:
                await this.#remove();
                break;
            case 3:
                return;
            default:
                console.log("❌ Invalid option.");
        }
    }

    async editChildren() {
        this.printPeople();
        console.log("\nPerson ID to edit Children or a letter to exit.");
        const idStr = await this.inputStr("ID: ");
        if (!/^\d+$/.test(idStr)) {
            console.log("Exit");
            return;
        }

        const id = parseInt(idStr);
        const parent = this.getPersonById(id);
        if (!parent || parent.deleted) {
            console.log("❌ ID not found or the person is deleted.");
            return;
        }

        console.log(`You selected '${parent.name}'`);
        const children = parent.children;
        if (Object.keys(children).length > 0) {
            console.log("Children:");
            for (const [partnerId, childIds] of Object.entries(children)) {
                const partner = this.getPersonById(parseInt(partnerId));
                const partnerName = partner ? partner.name : "Unknown";
                console.log(`With ID: ${partnerId} -> '${partnerName}':`);
                childIds.forEach(childId => {
                    const child = this.getPersonById(childId);
                    const childName = child ? child.name : "Unknown";
                    console.log(`    ID: ${childId} -> '${childName}'`);
                });
            }
        } else {
            console.log("🚫 This person has no children.");
        }

        this._idParent = id;
        this._children = children;
        await this.#options();
    }
}

class Tree extends Children {
    #filteredGrandparents() {
        const grandparents = [];
        const noPartner = [];

        for (const person of this.getPeople()) {
            if (
                !person.parents.length &&
                !person.deleted &&
                person.name !== "unknown"
            ) {
                const partners = person.partners;
                if (!partners.length) {
                    noPartner.push(person);
                    continue;
                }

                let hasGrandparentPartner = false;
                for (const partnerId of partners) {
                    const partner = this.getPersonById(partnerId);
                    if (partner && grandparents.includes(partner)) {
                        hasGrandparentPartner = true;
                        break;
                    }
                }

                if (!hasGrandparentPartner) {
                    grandparents.push(person);
                }
            }
        }

        return [grandparents, noPartner];
    }

    #printChild(children, px, isLast, isRoot) {
        children.forEach((childId, j) => {
            const isLastChild = j === children.length - 1;
            let newPrefix = px;
            if (!isRoot) {
                newPrefix = px.slice(0, -4) + (isLast ? "    " : "│   ");
            }

            this.#printFamily(
                childId,
                newPrefix + (isLastChild ? "└── " : "├── "),
                isLastChild,
                false
            );
        });
    }

    #printParents(id, partners, px, isLast, isRoot) {
        partners.forEach(partnerId => {
            const partner = this.getPersonById(partnerId);
            if (partner) {
                console.log(`${px}💑 With: ${partner.name} (ID: ${partner.id})`);
                const children = partner.children[id] || [];
                if (children.length) {
                    this.#printChild(children, px, isLast, isRoot);
                } else {
                    console.log(`${px}└── 🚫 Without children`);
                }
            }
        });
    }

    #printFamily(id, px = "", isLast = false, isRoot = true) {
        const person = this.getPersonById(id);
        if (!person) return;

        console.log(`${px}🙂 ${person.name} (ID: ${person.id})`);

        const partners = person.partners;
        if (Array.isArray(partners) && partners.length) {
            if (!isRoot) {
                px = px.slice(0, -4) + (isLast ? "    " : "│   ");
            }

            this.#printParents(id, partners, px, isLast, isRoot);
            if (!isLast) {
                console.log(px);
            }
        }
    }

    printTree() {
        const [grandparents, noPartner] = this.#filteredGrandparents();

        if (!grandparents.length && !noPartner.length) {
            console.log("⚠️ No users are registered.");
            return;
        }

        if (noPartner.length) {
            console.log("__________\nParents unknown, without descendants and without a partner:");
            noPartner.forEach(p => {
                console.log(`😐 ${p.name}`);
            });
        }

        console.log();
        grandparents.forEach((person, i) => {
            console.log(`__________\nFamily #${i + 1}`);
            this.#printFamily(person.id);
        });
    }
}

class Program extends Tree {
    static MENU = `
  ---------------------------------------------
  | 1. Add person     | 4. Edit children      |  
  | 2. Remove person  | 5. Print tree         |
  | 3. Edit partners  | 6. Exit               |
  ---------------------------------------------`;

    async run() {
        while (true) {
            console.log(Program.MENU);
            const option = await this.inputInt("\nOption: ");

            switch (option) {
                case 1:
                    await this.addPerson();
                    break;
                case 2:
                    await this.removePerson();
                    break;
                case 3:
                    await this.editPartners();
                    break;
                case 4:
                    await this.editChildren();
                    break;
                case 5:
                    this.printTree();
                    break;
                case 6:
                    console.log("Bye");
                    rl.close();
                    return;
                default:
                    console.log("❌ Invalid option.");
            }
        }
    }
}

const program = new Program();
program.run().catch(console.error);
