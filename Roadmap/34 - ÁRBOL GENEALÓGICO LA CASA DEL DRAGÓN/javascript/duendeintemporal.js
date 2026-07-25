//#34 - ARBOL GENEALÓGICO DE LA CASA DEL DRAGÓN:
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
 *    - Modificar pareja e hijo
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 * 
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
 */

/*          Arbol Genealógico

Rey Viserys I Targaryen:
    Título: Rey de los Siete Reinos.
    Esposas:
        Aemma Arryn (madre de Rhaenyra y Aegon II).
        Alicent Hightower (madre de Aegon III, Aemond y otros).
    Hijos:
        Con Aemma Arryn:
            Rhaenyra Targaryen (heredera al trono).
            Aegon II Targaryen (rival de Rhaenyra).
        Con Alicent Hightower:
            Aegon III Targaryen.
            Aemond Targaryen.
        Otros hijos (como Daeron Targaryen).
Rhaenyra Targaryen:
    Título: Princesa de Dragonstone, heredera al trono.
    Esposo: Laenor Velaryon (hijo de Corlys Velaryon y Rhaenys Targaryen).
    Hijos: Joffrey Velaryon. Lucerys Velaryon. Jorah Velaryon.
Aegon II Targaryen:
    Título: Rey de los Siete Reinos (rival de Rhaenyra).
    Hijos: No se menciona que Aegon II tenga hijos legítimos en la serie.
Alicent Hightower:
    Título: Reina consorte.
    Hijos: Aegon III Targaryen. Aemond Targaryen. Daeron Targaryen (en algunas versiones de la historia).
    Familia: Proviene de la influyente Casa Hightower, que juega un papel importante en la política de Westeros.
Aemond Targaryen:
    Título: Príncipe de la Casa Targaryen.
    Hermanos: Aegon III y Daeron Targaryen.
Laenor Velaryon:
    Título: Príncipe de la Casa Velaryon.
    Esposa: Rhaenyra Targaryen.
    Hijos: Joffrey, Lucerys y Jorah Velaryon (aunque su paternidad es cuestionada). */

    let log = console.log;

    window.addEventListener('load', ()=>{
        const body = document.querySelector('body');
        const title = document.createElement('h1');
        
        body.style.setProperty('background', '#000');
        body.style.setProperty('text-align', 'center');
        
        title.textContent = 'Retosparaprogramadores #34.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '100vh');
        
        body.appendChild(title);
        
        setTimeout(()=>{
        alert('Retosparaprogramadores #34. Please open the Browser Developer Tools.');
        }, 2000);
        log( 'Retosparaprogramadores #34'); 
    });
    

    class Person {
        constructor(id, name, mother = '', father = '', partners = [], childrens = []) {
            this.id = id;
            this.name = name;
            this.mother = mother;
            this.father = father;
            this.partners = this.setPartners(partners);
            this.childrens = this.setChildrens(childrens);
        }
    
        setPartners(partners) {
            if (!partners) {
                log('You have to give a valid name string or array');
                return [];
            }
            if (Array.isArray(partners)) {
                return [...partners];
            } else {
                return [partners];
            }
        }
    
        setChildrens(childrens) {
            if (!childrens) {
                log('You have to give a valid name string or array');
                return [];
            }
            if (Array.isArray(childrens)) {
                return [...childrens];
            } else {
                return [childrens];
            }
        }
    
        getPartners() {
            return this.partners.length > 0 ? this.partners : `there's no partners for ${this.name}`;
        }
    
        getChildrens() {
            return this.childrens.length > 0 ? this.childrens : `there's no childrens for ${this.name}`;
        }
    }
    
    class GenealogyTree {
        constructor(persons = []) {
            this.persons = persons;
        }
    
        addPerson(person) {
            if (this.persons.some(p => p.id === person.id)) {
                log(`The ${person.name} is already added`);
                return;
            }
            this.persons.push(person);
        }
    
        deletePerson(personId) {
            const index = this.persons.findIndex(p => p.id === personId);
            if (index === -1) {
                log(`The person with id ${personId} isn't already added`);
                return;
            }
            this.persons.splice(index, 1);
        }
    
        showTree() {
            this.persons.forEach(p => {
                log(`ID: ${p.id}, Name: ${p.name}, Mother: ${p.mother}, Father: ${p.father}, Partners: ${p.getPartners()}, Childrens: ${p.getChildrens()}`);
            });
        }
    }
    
    const king = new Person(1, 'Rey Viserys I Targaryen', '', '', ['Aemma Arryn', 'Alicent Hightower'], ['Rhaenyra Targaryen', 'Aegon II Targaryen', 'Aegon III Targaryen', 'Aemond Targaryen', 'Daeron Targaryen']);
    const princess = new Person(2, 'Rhaenyra Targaryen', 'Aemma Arryn', 'Rey Viserys I Targaryen', ['Laenor Velaryon'], ['Joffrey Velaryon', 'Lucerys Velaryon', 'Jorah Velaryon']);
    const kingAegonII = new Person(3, 'Aegon II Targaryen', 'Aemma Arryn', 'Rey Viserys I Targaryen');
    const queen = new Person(4, 'Alicent Hightower', '', '', ['Rey Viserys I Targaryen'], ['Aegon III Targaryen', 'Aemond Targaryen', 'Daeron Targaryen']);
    const princeAemond = new Person(5, 'Aemond Targaryen', '', '', [], []);
    const princeLaenor = new Person(6, 'Laenor Velaryon', '', '', ['Rhaenyra Targaryen'], ['Joffrey Velaryon', 'Lucerys Velaryon', 'Jorah Velaryon']);
    
    const dragonHouseTree = new GenealogyTree([king, princess, kingAegonII, queen, princeAemond, princeLaenor]);
    
    dragonHouseTree.showTree();
    