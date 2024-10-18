/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* --------------------------------- Fighter -------------------------------- */

interface IFighter {
    getLife: () => number
    getAttack: () => number
    getDefense: () => number
    getName: () => string
    getSpeed: () => number
    setLife: (newLife: number) => this
    clone: () => IFighter
}

interface FighterConstructor {
    attack: number
    defense: number
    name: string
    speed: number
    life?: number
}

class Fighter implements IFighter {
    private life: number
    private readonly attack: number
    private readonly defense: number
    private readonly name: string
    private readonly speed: number

    public constructor({
        attack,
        defense,
        name,
        speed,
        life = 100,
    }: FighterConstructor) {
        this.life = life
        this.attack = attack
        this.defense = defense
        this.name = name
        this.speed = speed
    }

    public getLife(): number {
        return this.life
    }

    public getAttack(): number {
        return this.attack
    }

    public getDefense(): number {
        return this.defense
    }

    public getName(): string {
        return this.name
    }

    public getSpeed(): number {
        return this.speed
    }

    public setLife(newLife: number): this {
        this.life = Math.max(newLife, 0)
        return this
    }

    public clone(): IFighter {
        return new Fighter({
            attack: this.attack,
            defense: this.defense,
            name: this.name,
            speed: this.speed,
            life: this.life,
        })
    }
}

/* ------------------------------- Tournament ------------------------------- */

interface ShiftInformation {
    attackDamage: number
    attacker: IFighter
    shift: number
    victim: IFighter
}

interface Round {
    infoPerShift?: ShiftInformation[]
    looser: IFighter
    shifts: number
    winner: IFighter
}

interface ITournament {
    getPhase: () => number
    getTeamA: () => IFighter[]
    getTeamB: () => IFighter[]
    getWinner: () => IFighter | undefined
    executeNextRound: () => Round
}

interface TournamentConstructor {
    teamA: IFighter[]
    teamB: IFighter[]
}

class Tournament implements ITournament {
    private pairOfFighters: IFighter[]
    private phase: number
    private readonly teamA: IFighter[]
    private readonly teamB: IFighter[]
    private round: number
    private winner?: IFighter

    public constructor({teamA, teamB}: TournamentConstructor) {
        if (teamA.length != teamB.length)
            throw new Error(
                'The number of fighters in both teams must be equal'
            )

        if (teamA.length % 2 || teamB.length % 2)
            throw new Error('The number of fighters in both teams must be even')

        this.pairOfFighters = []
        this.phase = 1
        this.teamA = teamA
        this.teamB = teamB
        this.round = 0
        this.winner = undefined

        this.setRndPairOfFighters()
    }

    public getPhase(): number {
        return this.phase
    }

    public getTeamA(): IFighter[] {
        return this.teamA
    }

    public getTeamB(): IFighter[] {
        return this.teamB
    }

    public getWinner(): IFighter | undefined {
        return this.winner
    }

    private setRndPairOfFighters(): void {
        const indexesToIgnoreA: number[] = []
        const indexesToIgnoreB: number[] = []

        let rndIndex: number
        let rndFighter: IFighter

        for (let i = 0; i < this.teamA.length; i++) {
            do {
                rndIndex = Math.floor(Math.random() * this.teamA.length)
            } while (indexesToIgnoreA.includes(rndIndex))

            rndFighter = this.teamA[rndIndex]

            this.pairOfFighters.push(rndFighter)
            indexesToIgnoreA.push(rndIndex)

            do {
                rndIndex = Math.floor(Math.random() * this.teamB.length)
            } while (indexesToIgnoreB.includes(rndIndex))

            rndFighter = this.teamB[rndIndex]

            this.pairOfFighters.push(rndFighter)
            indexesToIgnoreB.push(rndIndex)
        }
    }

    public executeNextRound(): Round {
        if (this.winner) throw new Error('The tournament already has a winner')
        if (this.pairOfFighters.length < 2)
            throw new Error('Not enough fighters to execute the next round')

        this.round += 1
        const offset: number = this.round - 1

        let fighter01: IFighter = this.pairOfFighters[offset]
        let fighter02: IFighter = this.pairOfFighters[offset + 1]
        let fighterAux: IFighter

        if (fighter01.getSpeed() < fighter02.getSpeed()) {
            fighterAux = fighter01
            fighter01 = fighter02
            fighter02 = fighterAux
        }

        let shifts: number = 0
        const infoPerShift: ShiftInformation[] = []

        while (fighter01.getLife() && fighter02.getLife()) {
            let attackDamage: number = 0

            if (Math.random() > 0.2) {
                const attack: number = fighter01.getAttack()
                const defense: number = fighter02.getDefense()

                attackDamage = Math.abs(attack - defense)
                if (defense > attack) attackDamage = attackDamage * 0.1

                fighter02.setLife(fighter02.getLife() - attackDamage)
            }

            infoPerShift.push({
                attackDamage,
                attacker: fighter01.clone(),
                victim: fighter02.clone(),
                shift: ++shifts,
            })

            fighterAux = fighter01
            fighter01 = fighter02
            fighter02 = fighterAux
        }

        fighter01 = this.pairOfFighters[offset]
        fighter02 = this.pairOfFighters[offset + 1]

        const looserIndex: number = fighter01.getLife() ? offset + 1 : offset
        const looser: IFighter = this.pairOfFighters.splice(looserIndex, 1)[0]

        if (this.pairOfFighters.length < 2) this.winner = this.pairOfFighters[0]

        if (this.round == this.pairOfFighters.length) {
            this.round = 0
            this.phase += 1
        }

        return {
            winner: fighter01.getLife() ? fighter01.clone() : fighter02.clone(),
            looser,
            shifts,
            infoPerShift,
        }
    }
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

const teamA: IFighter[] = [
    new Fighter({attack: 90, defense: 80, name: 'Goku', speed: 95}),
    new Fighter({attack: 85, defense: 75, name: 'Vegeta', speed: 90}),
    new Fighter({attack: 70, defense: 65, name: 'Piccolo', speed: 80}),
    new Fighter({attack: 60, defense: 55, name: 'Krillin', speed: 70}),
]

const teamB: IFighter[] = [
    new Fighter({attack: 88, defense: 78, name: 'Frieza', speed: 92}),
    new Fighter({attack: 82, defense: 72, name: 'Cell', speed: 88}),
    new Fighter({attack: 75, defense: 65, name: 'Majin Buu', speed: 85}),
    new Fighter({attack: 65, defense: 60, name: 'Broly', speed: 75}),
]

const tournament: ITournament = new Tournament({teamA, teamB})

let rounds: number = 0

while (!tournament.getWinner()) {
    const round: Round = tournament.executeNextRound()

    if (round.infoPerShift) {
        console.log(
            `> Round ${++rounds} ` +
                `(${round.winner.getName()} vs ` +
                `${round.looser.getName()})...\n`
        )

        for (const shift of round.infoPerShift) {
            if (shift.attackDamage > 0) {
                console.log(
                    `> Shift ${shift.shift}: ` +
                        `${shift.attacker.getName()} attacks ` +
                        `${shift.victim.getName()} with an attack damage of ` +
                        `${shift.attackDamage}.`
                )
            } else {
                console.log(
                    `> Shift ${shift.shift}: ` +
                        `${shift.attacker.getName()} attacks ` +
                        `${shift.victim.getName()}, but ${shift.victim.getName()} ` +
                        `evades the attack.`
                )
            }
        }
    }

    console.log(
        `\n> ${round.winner.getName()} wins the fight against ` +
            `${round.looser.getName()} in ${round.shifts} shifts!\n`
    )
}

console.log(
    `> The winner of the tournament is ${tournament.getWinner()?.getName()}!`
)
