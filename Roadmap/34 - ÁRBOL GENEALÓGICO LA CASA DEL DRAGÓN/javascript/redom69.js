class Person {
    constructor(id, name, couple = null, children = []) {
        this.id = id
        this.name=name
        this.couple = couple
        this.children= children
    }

    addChild(child){
        this.children.push(child)
    }

    modifyCouple(couple){
        this.couple = couple
    }

    toString(){
        const coupleName = this.couple ? this.couple.name : "None";
        return `Person(id=${this.id}, name=${this.name}, couple=${coupleName}, children=${this.children.length})`;
    }
}

class FamilyTree{

    constructor(person){
        this.root = person
        this.people = {};
        this.people[person.id] = person;
    }

    addPerson(person){
        if (!(person.id in this.people)) {
            this.people[person.id] = person
        }else{
            console.log('Ya existe')
        }
    }

    deletePerson(person_id){
        if (id in this.people) {
            delete this.people[person_id];
        }else{
            console.log('No existe')
        }
    }

    editPerson(id, name, couple = null, children = []){
        if (id){
            const person =  this.people[id]
            if (name) person.name = name
            if (couple) person.modifyCouple(couple)
            if (children.length()>0) person.children = children
        }else{
            console.log('No existe')
        }
    }

    displayTree(person = null, level = 0) {
        if (person === null) {
            person = this.root;
        }

        const indent = " ".repeat(level * 4);
        const coupleName = person.couple ? ` & ${person.couple.name}` : "";
        console.log(`${indent}${person.name}${coupleName}`);

        for (const child of person.children) {
            this.displayTree(child, level + 1);
        }
    }
}


function main() {
    const jaehaerys = new Person(1, "Jaehaerys I Targaryen");
    const alysanne = new Person(2, "Alysanne Targaryen");

    const baelon = new Person(3, "Baelon Targaryen");
    const alyssa = new Person(4, "Alyssa Targaryen");

    const viserys = new Person(5, "Viserys I Targaryen");
    const aemma = new Person(6, "Aemma Arryn");

    const daemon = new Person(7, "Daemon Targaryen");
    const rhea = new Person(8, "Rhea Royce");
    const laena = new Person(9, "Laena Velaryon");
    const rhaenyra = new Person(10, "Rhaenyra Targaryen");

    const alicent = new Person(11, "Alicent Hightower");
    const aegonII = new Person(12, "Aegon II Targaryen");
    const helaena = new Person(13, "Helaena Targaryen");
    const aemond = new Person(14, "Aemond Targaryen");
    const daeron = new Person(15, "Daeron Targaryen");

    jaehaerys.modifyCouple(alysanne);
    baelon.modifyCouple(alyssa);
    baelon.children = [viserys, daemon];
    viserys.modifyCouple(aemma);
    viserys.children = [rhaenyra];
    daemon.modifyCouple(rhea);
    daemon.children = [];

    daemon.modifyCouple(laena);
    const baela = new Person(16, "Baela Targaryen");
    const rhaena = new Person(17, "Rhaena Targaryen");
    daemon.children = [baela, rhaena];

    rhaenyra.modifyCouple(daemon);

    viserys.modifyCouple(alicent);
    viserys.children.push(aegonII, helaena, aemond, daeron);

    const familyTree = new FamilyTree(viserys);
    familyTree.addPerson(jaehaerys);
    familyTree.addPerson(alysanne);
    familyTree.addPerson(baelon);
    familyTree.addPerson(alyssa);
    familyTree.addPerson(daemon);
    familyTree.addPerson(rhea);
    familyTree.addPerson(laena);
    familyTree.addPerson(rhaenyra);
    familyTree.addPerson(alicent);
    familyTree.addPerson(aegonII);
    familyTree.addPerson(helaena);
    familyTree.addPerson(aemond);
    familyTree.addPerson(daeron);
    familyTree.addPerson(baela);
    familyTree.addPerson(rhaena);

    familyTree.displayTree();
}

main();