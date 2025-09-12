import {setTimeout} from 'timers/promises'

/* -------------------------------------------------------------------------- */
/*                     SUPERHEROREGENERATINGERROR (ERROR)                     */
/* -------------------------------------------------------------------------- */

class SuperheroRegeneratingError extends Error {
    public constructor(superhero: ISuperhero) {
        super(`${superhero.getName()} is regenerating`)
        this.name = 'SuperheroRegeneratingError'
    }
}

/* -------------------------------------------------------------------------- */
/*                              SUPERHERO (CLASS)                             */
/* -------------------------------------------------------------------------- */

interface ISuperhero {
    getAttackDamage: () => Readonly<[number, number]>
    getLifePoints: () => number
    getName: () => Capitalize<string>
    isRegenerating: () => boolean
    setRegenerating: (regenerating: boolean) => this
    evadeAttack: () => boolean
    produceDamage: () => number | never
    receiveDamage: (damage: number) => this
}

interface SuperheroConstructor {
    lifePoints: number
    attackDamage: [number, number]
    evadePercentage: number
    name: Capitalize<string>
}

class Superhero implements ISuperhero {
    private lifePoints: number
    private regenerating: boolean
    private readonly attackDamage: Readonly<[number, number]>
    private readonly evadePercentage: number
    private readonly name: Capitalize<string>

    protected constructor({
        attackDamage,
        evadePercentage,
        lifePoints,
        name,
    }: SuperheroConstructor) {
        this.lifePoints = lifePoints
        this.regenerating = false
        this.attackDamage = attackDamage
        this.evadePercentage = evadePercentage
        this.name = name
    }

    public getAttackDamage(): Readonly<[number, number]> {
        return this.attackDamage
    }

    public getLifePoints(): number {
        return this.lifePoints
    }

    public getName(): Capitalize<string> {
        return this.name
    }

    public isRegenerating(): boolean {
        return this.regenerating
    }

    public setRegenerating(regenerating: boolean): this {
        this.regenerating = regenerating
        return this
    }

    public evadeAttack(): boolean {
        const rndNumber: number = Math.random()
        return rndNumber <= this.evadePercentage
    }

    public produceDamage(): number | never {
        if (this.isRegenerating()) throw new SuperheroRegeneratingError(this)

        const [minAttackDamage, maxAttackDamage]: readonly [number, number] =
            this.getAttackDamage()

        const rndDamage: number = Math.max(
            minAttackDamage,
            Math.round(Math.random() * maxAttackDamage)
        )

        return rndDamage
    }

    public receiveDamage(damage: number): this {
        this.lifePoints -= damage
        return this
    }
}

/* -------------------------------------------------------------------------- */
/*                              WOLVERINE (CLASS)                             */
/* -------------------------------------------------------------------------- */

interface IWolverine {}

interface WolverineConstructor
    extends Omit<
        SuperheroConstructor,
        'attackDamage' | 'evadePercentage' | 'name'
    > {}

class Wolverine extends Superhero implements IWolverine {
    public constructor({lifePoints}: WolverineConstructor) {
        super({
            attackDamage: [10, 120],
            evadePercentage: 0.2,
            lifePoints,
            name: 'Wolverine',
        })
    }
}

/* -------------------------------------------------------------------------- */
/*                              DEADPOOL (CLASS)                              */
/* -------------------------------------------------------------------------- */

interface IDeadpool {}

interface DeadpoolConstructor
    extends Omit<
        SuperheroConstructor,
        'attackDamage' | 'evadePercentage' | 'name'
    > {}

class Deadpool extends Superhero implements IDeadpool {
    public constructor({lifePoints}: DeadpoolConstructor) {
        super({
            attackDamage: [10, 100],
            evadePercentage: 0.25,
            lifePoints,
            name: 'Deadpool',
        })
    }
}

/* -------------------------------------------------------------------------- */
/*                          SUPERHEROESFIGHT (CLASS)                          */
/* -------------------------------------------------------------------------- */

interface Turn {
    attacker: ISuperhero
    number: number
    victim: ISuperhero
}

interface ExecutedTurn extends Turn {
    damageProducedByAttacker: number
    damageReceivedByVictim: number
    victimAvoidAttack: boolean
}

interface ISuperheroFight {
    getTurn: () => Readonly<Turn>
    getWinner: () => ISuperhero | undefined
    executeTurn: () => Readonly<ExecutedTurn> | never
}

interface SuperheroFightConstructor {
    superHeroOne: ISuperhero
    superHeroTwo: ISuperhero
}

class SuperheroFight implements ISuperheroFight {
    private turn: Readonly<Turn>
    private winner: undefined | ISuperhero

    public constructor({
        superHeroOne,
        superHeroTwo,
    }: SuperheroFightConstructor) {
        this.turn = {
            attacker: superHeroOne,
            number: 1,
            victim: superHeroTwo,
        }

        this.winner = undefined
    }

    public getTurn(): Readonly<Turn> {
        return this.turn
    }

    public getWinner(): undefined | ISuperhero {
        return this.winner
    }

    public executeTurn(): Readonly<ExecutedTurn> | never {
        const {attacker, number, victim} = this.getTurn()
        victim.setRegenerating(false)

        this.turn = {
            attacker: victim,
            number: number + 1,
            victim: attacker,
        }

        try {
            const damageProducedByAttacker = attacker.produceDamage()
            const attackerAttackDamage: Readonly<[number, number]> =
                attacker.getAttackDamage()

            const victimAvoidAttack = victim.evadeAttack()

            if (!victimAvoidAttack) {
                victim.receiveDamage(damageProducedByAttacker)
                victim.setRegenerating(
                    damageProducedByAttacker === attackerAttackDamage[1]
                )

                if (victim.getLifePoints() <= 0) this.winner = attacker
            }

            return {
                attacker,
                victim,
                number,
                damageProducedByAttacker,
                victimAvoidAttack,
                damageReceivedByVictim: victimAvoidAttack
                    ? 0
                    : damageProducedByAttacker,
            }
        } catch (error) {
            throw error
        }
    }
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

;(async () => {
    const deadpool: Deadpool = new Deadpool({lifePoints: 500})
    const wolverine: Wolverine = new Wolverine({lifePoints: 500})

    const superheroFight: SuperheroFight = new SuperheroFight({
        superHeroOne: deadpool,
        superHeroTwo: wolverine,
    })

    while (!superheroFight.getWinner()) {
        await setTimeout(1000)
        const currentTurn: Readonly<Turn> = superheroFight.getTurn()

        try {
            const executedTurn: Readonly<ExecutedTurn> =
                superheroFight.executeTurn()

            if (executedTurn.victimAvoidAttack) {
                console.log(
                    `\n> Turn N°${
                        currentTurn.number
                    }: ${currentTurn.victim.getName()} avoided ${currentTurn.attacker.getName()} attack.`
                )

                continue
            }

            console.log(
                `\n> Turn N°${
                    currentTurn.number
                }: ${currentTurn.attacker.getName()} attacked ${currentTurn.victim.getName()} with ${
                    executedTurn.damageProducedByAttacker
                } points of damage.`
            )

            console.log(
                `[ Life points of Deadpool: ${deadpool.getLifePoints()} ]\n` +
                    `[ Life points of Wolverine: ${wolverine.getLifePoints()} ]`
            )
        } catch (error) {
            if (error instanceof SuperheroRegeneratingError) {
                console.log(
                    `\n> Turn N°${currentTurn.number}: ${error.message}.`
                )
            }
        }
    }

    console.log(`\n¡The winner is ${superheroFight.getWinner()?.getName()}!`)
})()
