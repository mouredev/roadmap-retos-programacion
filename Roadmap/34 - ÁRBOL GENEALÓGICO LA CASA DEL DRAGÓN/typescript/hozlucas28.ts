import type {UUID} from 'crypto'
import {randomUUID} from 'crypto'

/* -------------------------------------------------------------------------- */
/*                                    TYPES                                   */
/* -------------------------------------------------------------------------- */

type Name = `${Capitalize<string>} ${Capitalize<string>}`

type FamilyStatus = Lowercase<'father' | 'mother'>

interface PrettifiedPerson {
    name: string
    children?: string
    familyStatus?: FamilyStatus
    father?: Name
    mother?: Name
    partner?: Name
}

/* -------------------------------------------------------------------------- */
/*                                   ERRORS                                   */
/* -------------------------------------------------------------------------- */

class PersonNotFound extends Error {
    public constructor(UUID: UUID) {
        super(`Person with ${UUID} UUID not found`)
        this.name = 'PersonNotFound'
    }
}

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* --------------------------------- Person --------------------------------- */

interface IPerson {
    getName: () => Name
    getUUID: () => UUID
    getChildren: () => IPerson[] | undefined
    getPartner: () => IPerson | undefined
    getFamilyStatus: () => FamilyStatus | undefined
    getFather: () => IPerson | undefined
    getMother: () => IPerson | undefined
    setPartner: (partner: IPerson) => void
    addChildren: (...children: IPerson[]) => void
    removeChildren: (...children: UUID[]) => void
}

interface PersonConstructor {
    readonly name: Name
    readonly uuid: UUID
    children?: IPerson[]
    partner?: IPerson
    readonly familyStatus?: FamilyStatus
    readonly father?: IPerson
    readonly mother?: IPerson
}

class Person implements IPerson {
    private readonly name: Name
    private readonly uuid: UUID
    private children?: IPerson[]
    private partner?: IPerson
    private readonly familyStatus?: FamilyStatus
    private readonly father?: IPerson
    private readonly mother?: IPerson

    public constructor({
        name,
        uuid,
        children,
        partner,
        familyStatus,
        father,
        mother,
    }: PersonConstructor) {
        partner && partner.setPartner(this)
        father && father.addChildren(this)
        mother && mother.addChildren(this)

        this.name = name
        this.uuid = uuid
        this.children = children
        this.partner = partner
        this.familyStatus = familyStatus
        this.father = father
        this.mother = mother
    }

    public getName(): Name {
        return this.name
    }

    public getUUID(): UUID {
        return this.uuid
    }

    public getChildren(): IPerson[] | undefined {
        return this.children
    }

    public getPartner(): IPerson | undefined {
        return this.partner
    }

    public getFamilyStatus(): FamilyStatus | undefined {
        return this.familyStatus
    }

    public getFather(): IPerson | undefined {
        return this.father
    }

    public getMother(): IPerson | undefined {
        return this.mother
    }

    public setPartner(partner: IPerson): void {
        this.partner = partner
    }

    public addChildren(...children: IPerson[]): void {
        this.children?.push(...children) ?? (this.children = [...children])
    }

    public removeChildren(...children: UUID[]): void {
        if (!this.children) return

        for (let i = 0; i < children.length; i++) {
            const uuid: UUID = children[i]
            const sonIndex: number = this.children.findIndex(
                (son) => uuid === son.getUUID()
            )

            if (sonIndex < 0) throw new PersonNotFound(uuid)
            this.children.splice(sonIndex, 1)
        }
    }
}

/* ------------------------------- FamilyTree ------------------------------- */

interface IFamilyTree {
    getPerson: (uuid: UUID) => IPerson
    getPeople: () => IPerson[] | undefined
    addPeople: (...people: IPerson[]) => void
    removePeople: (...people: UUID[]) => void
    toPrettifiedPeople: () => PrettifiedPerson[]
}

interface FamilyTreeConstructor {
    readonly people?: IPerson[]
}

class FamilyTree implements IFamilyTree {
    private people?: IPerson[]

    public constructor({people}: FamilyTreeConstructor = {}) {
        this.people = people
    }

    public getPerson(uuid: UUID): IPerson {
        const people: IPerson[] | undefined = this.people
        const person: IPerson | undefined = people?.find(
            (person) => person.getUUID() === uuid
        )

        if (!person) throw new PersonNotFound(uuid)

        return person
    }

    public getPeople(): IPerson[] | undefined {
        return this.people
    }

    public addPeople(...people: IPerson[]): void {
        this.people?.push(...people) ?? (this.people = [...people])
    }

    public removePeople(...people: UUID[]): void {
        if (!this.people) return

        for (let i = 0; i < people.length; i++) {
            const uuid: UUID = people[i]
            const personIndex: number = this.people.findIndex(
                (person) => uuid === person.getUUID()
            )

            if (personIndex < 0) throw new PersonNotFound(uuid)
            this.people.splice(personIndex, 1)
        }
    }

    public toPrettifiedPeople(): PrettifiedPerson[] {
        const people: IPerson[] | undefined = this.people

        let prettifiedPeople: PrettifiedPerson[] = []
        if (!people) return prettifiedPeople

        for (const person of people) {
            const name: Name = person.getName()
            const familyStatus: FamilyStatus | undefined =
                person.getFamilyStatus()
            const father: IPerson | undefined = person.getFather()
            const mother: IPerson | undefined = person.getMother()
            const partner: IPerson | undefined = person.getPartner()

            const prettifiedPerson: PrettifiedPerson = {
                name,
                children: undefined,
                familyStatus,
                father: father ? father.getName() : undefined,
                mother: mother ? mother.getName() : undefined,
                partner: partner ? partner.getName() : undefined,
            } satisfies PrettifiedPerson

            const children: IPerson[] | undefined = person.getChildren()
            if (children) {
                const sons: string[] = []
                for (const son of children) {
                    sons.push(son.getName())
                }

                const formatter: Intl.ListFormat = new Intl.ListFormat('en', {
                    style: 'long',
                    type: 'conjunction',
                })

                prettifiedPerson.children = formatter.format(sons)
            }

            prettifiedPeople.push(prettifiedPerson)
        }

        return prettifiedPeople
    }
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

/**
 * House of Dragon family tree from the first row to the third one.
 *
 * > House of Dragon official family tree: https://www.hbo.com/house-of-the-dragon/character-guide
 */

console.log(
    'House of Dragon family tree from the first row to the third one...\n'
)

const jaehaerysTargaryen: Person = new Person({
    name: 'Jaehaerys Targaryen',
    uuid: randomUUID(),
    familyStatus: 'father',
})

const alysanneTargaryen: Person = new Person({
    name: 'Alysanne Targaryen',
    uuid: randomUUID(),
    partner: jaehaerysTargaryen,
    familyStatus: 'mother',
})

const jocelynBaratheon: Person = new Person({
    name: 'Jocelyn Baratheon',
    uuid: randomUUID(),
    familyStatus: 'mother',
})

const aemonTargaryen: Person = new Person({
    name: 'Aemon Targaryen',
    uuid: randomUUID(),
    partner: jocelynBaratheon,
    familyStatus: 'father',
    father: jaehaerysTargaryen,
    mother: alysanneTargaryen,
})

const baelonTargaryen: Person = new Person({
    name: 'Baelon Targaryen',
    uuid: randomUUID(),
    familyStatus: 'mother',
    father: jaehaerysTargaryen,
    mother: alysanneTargaryen,
})

const alyssaTargaryen: Person = new Person({
    name: 'Alyssa Targaryen',
    uuid: randomUUID(),
    partner: baelonTargaryen,
    familyStatus: 'mother',
    father: jaehaerysTargaryen,
    mother: alysanneTargaryen,
})

const lyonelStrong: Person = new Person({
    name: 'Lyonel Strong',
    uuid: randomUUID(),
    familyStatus: 'father',
})

const vaemondValaryon: Person = new Person({
    name: 'Vaemond Valaryon',
    uuid: randomUUID(),
})

const corlysVelaryon: Person = new Person({
    name: 'Corlys Velaryon',
    uuid: randomUUID(),
    familyStatus: 'father',
})

const rhaenysTargaryen: Person = new Person({
    name: 'Rhaenys Targaryen',
    uuid: randomUUID(),
    familyStatus: 'mother',
    partner: corlysVelaryon,
    father: aemonTargaryen,
    mother: jocelynBaratheon,
})

const rheaRoyce: Person = new Person({
    name: 'Rhea Royce',
    uuid: randomUUID(),
    familyStatus: 'mother',
})

const daemonTargaryen: Person = new Person({
    name: 'Daemon Targaryen',
    uuid: randomUUID(),
    familyStatus: 'father',
    partner: rheaRoyce,
    father: baelonTargaryen,
    mother: alyssaTargaryen,
})

const aemmaArryn: Person = new Person({
    name: 'Aemma Arryn',
    uuid: randomUUID(),
    familyStatus: 'mother',
})

const viserysTargaryen: Person = new Person({
    name: 'Viserys Targaryen',
    uuid: randomUUID(),
    familyStatus: 'father',
    partner: aemmaArryn,
    father: baelonTargaryen,
    mother: alyssaTargaryen,
})

const ottoHightower: Person = new Person({
    name: 'Otto Hightower',
    uuid: randomUUID(),
    familyStatus: 'father',
})

const hobertHightower: Person = new Person({
    name: 'Hobert Hightower',
    uuid: randomUUID(),
})

const familyTree: FamilyTree = new FamilyTree()

familyTree.addPeople(
    jaehaerysTargaryen,
    alysanneTargaryen,
    jocelynBaratheon,
    aemonTargaryen,
    baelonTargaryen,
    alyssaTargaryen,
    lyonelStrong,
    vaemondValaryon,
    corlysVelaryon,
    rhaenysTargaryen,
    rheaRoyce,
    daemonTargaryen,
    aemmaArryn,
    viserysTargaryen,
    ottoHightower,
    hobertHightower
)

console.table(familyTree.toPrettifiedPeople())

console.log(
    '\n> House of Dragon official family tree: https://www.hbo.com/house-of-the-dragon/character-guide'
)
