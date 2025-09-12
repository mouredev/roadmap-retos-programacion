/* -------------------------------------------------------------------------- */
/*                                  ERRORS.TS                                 */
/* -------------------------------------------------------------------------- */

interface SportEventErrorsRtn {
    notEnoughCompetitors: string
}

function sportEventErrors<T>(sportEvent: ISportEvent): SportEventErrorsRtn {
    const name: Lowercase<string> = sportEvent.getName()
    const competitors: ICompetitor[] = sportEvent.getCompetitors()

    return {
        notEnoughCompetitors: `Sport event '${name}' needs more competitors. It currently has ${competitors.length} competitor(s), but requires a minimum of ${SportEvent.minimumNumberOfCompetitors}.`,
    }
}

/* -------------------------------------------------------------------------- */
/*                                  UTILS.TS                                  */
/* -------------------------------------------------------------------------- */

interface CountriesRankingByNumberOfMedalsRtn {
    name: Country
    numberOfMedals: number
}

function countriesRankingByNumberOfMedals(
    ...sportEvents: ISportEvent[]
): CountriesRankingByNumberOfMedalsRtn[] {
    const medalRankingPerCountry: CountriesRankingByNumberOfMedalsRtn[] = []

    const winners: ICompetitor[] = []
    for (let i = 0; i < sportEvents.length; i++) {
        const sportEventWinners = sportEvents[i].getWinners()
        winners.push(...sportEventWinners)
    }

    const indexesToIgnore: number[] = []

    for (let i = 0; i < winners.length; i++) {
        if (indexesToIgnore.includes(i)) continue

        const anchorWinner = winners[i]
        const anchorWinnerCountry: Country = anchorWinner.getCountry()
        const anchorWinnerMedals: IMedal[] = anchorWinner.getMedals()

        const countryStats: CountriesRankingByNumberOfMedalsRtn = {
            name: anchorWinnerCountry,
            numberOfMedals: anchorWinnerMedals.length,
        }

        for (let j = i + 1; j < winners.length; j++) {
            if (indexesToIgnore.includes(j)) continue

            const nextWinner = winners[j]
            const nextWinnerCountry: Country = nextWinner.getCountry()
            const nextWinnerMedals: IMedal[] = nextWinner.getMedals()

            const areSameCountry: boolean =
                anchorWinnerCountry.toUpperCase() ===
                nextWinnerCountry.toUpperCase()

            if (areSameCountry) {
                countryStats.numberOfMedals += nextWinnerMedals.length
                indexesToIgnore.push(j)
            }
        }

        medalRankingPerCountry.push(countryStats)
    }

    medalRankingPerCountry.sort((a, b) => {
        const comparison: number = b.numberOfMedals - a.numberOfMedals
        return comparison === 0 ? a.name.localeCompare(b.name) : comparison
    })

    return medalRankingPerCountry
}

function thereAreDuplicatedElements<T extends object>(array: T[]): boolean {
    if (array.length < 2) return false

    const arrayStr: string[] = array.map((element) => JSON.stringify(element))
    const uniqueElements: Set<string> = new Set(arrayStr)
    return array.length !== uniqueElements.size
}

/* -------------------------------------------------------------------------- */
/*                                  MEDAL.TS                                  */
/* -------------------------------------------------------------------------- */

type MedalCategory = Lowercase<'gold' | 'silver' | 'bronze'>

interface IMedal {
    getDate: () => Date
    getEvent: () => ISportEvent
    getMedalCategory: () => MedalCategory
}

interface MedalConstructor {
    date: Date
    event: ISportEvent
    medalCategory: 'gold' | 'silver' | 'bronze'
}

class Medal implements IMedal {
    private readonly date: Date
    private readonly event: ISportEvent
    private readonly medalCategory: MedalCategory

    public constructor({date, event, medalCategory}: MedalConstructor) {
        this.date = date
        this.event = event
        this.medalCategory = medalCategory
    }

    public getDate(): Date {
        return this.date
    }

    public getEvent(): ISportEvent {
        return this.event
    }

    public getMedalCategory(): MedalCategory {
        return this.medalCategory
    }
}

/* -------------------------------------------------------------------------- */
/*                                COMPETITOR.TS                               */
/* -------------------------------------------------------------------------- */

type Country =
    | Lowercase<
          | 'argentina'
          | 'españa'
          | 'estados unidos'
          | 'méxico'
          | 'canada'
          | 'chile'
          | 'brazil'
          | 'germany'
          | 'france'
          | 'italy'
          | 'australia'
          | 'japan'
      >
    | (string & {})

interface ICompetitor {
    getName: () => Lowercase<string>
    getMedals: () => IMedal[]
    getCountry: () => Country
    addMedals: (...newMedals: IMedal[]) => this
}

interface CompetitorConstructor {
    country: Country
    name: Lowercase<string>
    medals?: IMedal[]
}

class Competitor implements ICompetitor {
    private country: Country
    private medals: IMedal[]
    private name: Lowercase<string>

    public constructor({country, medals, name}: CompetitorConstructor) {
        if (medals && thereAreDuplicatedElements(medals)) {
            throw new Error(
                'Duplicate medals detected. Each medal must be unique.'
            )
        }

        this.country = country
        this.medals = medals ?? []
        this.name = name
    }

    public getCountry(): Country {
        return this.country
    }

    public getMedals(): IMedal[] {
        return this.medals
    }

    public getName(): Lowercase<string> {
        return this.name
    }

    public addMedals(...newMedals: IMedal[]): this {
        const existingMedals: IMedal[] = this.medals
        const joinedMedals: IMedal[] = [...existingMedals, ...newMedals]

        if (thereAreDuplicatedElements(joinedMedals)) {
            throw new Error(
                'Duplicate medals detected. Each medal must be unique.'
            )
        }

        this.medals = joinedMedals
        return this
    }
}

/* -------------------------------------------------------------------------- */
/*                                SPORTEVENT.TS                               */
/* -------------------------------------------------------------------------- */

interface ISportEvent {
    getCompetitors: () => ICompetitor[]
    getName: () => Lowercase<string>
    getWinners: () => [ICompetitor, ICompetitor, ICompetitor]
    addCompetitors: (...newCompetitors: ICompetitor[]) => this
    start: () => this
}

class SportEvent implements ISportEvent {
    public static readonly minimumNumberOfCompetitors = 3

    private competitors: ICompetitor[]
    private name: Lowercase<string>
    private winners: [ICompetitor, ICompetitor, ICompetitor]

    public constructor(
        name: Lowercase<string>,
        competitors: ICompetitor[] = []
    ) {
        if (competitors && thereAreDuplicatedElements(competitors)) {
            throw new Error(
                'Duplicate competitors detected. Each competitor must be unique.'
            )
        }

        this.name = name
        this.competitors = competitors
    }

    public getCompetitors(): ICompetitor[] {
        return this.competitors
    }

    public getName(): Lowercase<string> {
        return this.name
    }

    public getWinners(): [ICompetitor, ICompetitor, ICompetitor] {
        return this.winners
    }

    private hasEnoughCompetitors(): boolean {
        return this.competitors.length >= SportEvent.minimumNumberOfCompetitors
    }

    public addCompetitors(...newCompetitors: ICompetitor[]): this {
        const existingCompetitors: ICompetitor[] = this.competitors
        const joinedCompetitors: ICompetitor[] = [
            ...existingCompetitors,
            ...newCompetitors,
        ]

        if (thereAreDuplicatedElements(joinedCompetitors)) {
            throw new Error(
                'Duplicate competitors detected. Each competitor must be unique.'
            )
        }

        this.competitors = joinedCompetitors
        return this
    }

    public start(): this {
        if (!this.hasEnoughCompetitors()) {
            const errorMessage: string =
                sportEventErrors(this).notEnoughCompetitors
            throw new Error(errorMessage)
        }

        const indexOfRndCompetitor = (
            indexesToIgnore: number[] = []
        ): number => {
            const competitorI: number = Math.min(
                Math.floor(
                    Math.random() * Math.max(10, this.competitors.length)
                ),
                this.competitors.length - 1
            )

            if (indexesToIgnore.includes(competitorI))
                return indexOfRndCompetitor(indexesToIgnore)
            return competitorI
        }

        const firstPlaceI: number = indexOfRndCompetitor()
        const secondPlaceI: number = indexOfRndCompetitor([firstPlaceI])
        const thirdPlaceI: number = indexOfRndCompetitor([
            firstPlaceI,
            secondPlaceI,
        ])

        const goldMedal: IMedal = new Medal({
            date: new Date(),
            event: this,
            medalCategory: 'gold',
        })

        const silverMedal: IMedal = new Medal({
            date: new Date(),
            event: this,
            medalCategory: 'silver',
        })

        const bronzeMedal: IMedal = new Medal({
            date: new Date(),
            event: this,
            medalCategory: 'bronze',
        })

        this.competitors[firstPlaceI].addMedals(goldMedal)
        this.competitors[secondPlaceI].addMedals(silverMedal)
        this.competitors[thirdPlaceI].addMedals(bronzeMedal)

        this.winners = [
            this.competitors[firstPlaceI],
            this.competitors[secondPlaceI],
            this.competitors[thirdPlaceI],
        ]

        return this
    }
}

/* -------------------------------------------------------------------------- */
/*                                  EXERCISE                                  */
/* -------------------------------------------------------------------------- */

console.log('> Paris 2024 olympic games...')

const firstSportEvent: ISportEvent = new SportEvent('football')
const secondSportEvent: ISportEvent = new SportEvent('handball')
const thirdSportEvent: ISportEvent = new SportEvent('table tennis')
const fourthSportEvent: ISportEvent = new SportEvent('swimming')

console.log('\n> First sport event...\n')
console.dir(firstSportEvent)

console.log('\n> Second sport event...\n')
console.dir(secondSportEvent)

console.log('\n> Third sport event...\n')
console.dir(thirdSportEvent)

console.log('\n> Fourth sport event...\n')
console.dir(fourthSportEvent)

const competitorsOfFirstSportEvent: ICompetitor[] = [
    new Competitor({country: 'argentina', name: 'lionel messi'}),
    new Competitor({country: 'españa', name: 'sergio ramos'}),
    new Competitor({country: 'estados unidos', name: 'megan rapinoe'}),
    new Competitor({country: 'méxico', name: 'hirving lozano'}),
    new Competitor({country: 'canada', name: 'christine sinclair'}),
]

const competitorsOfSecondSportEvent: ICompetitor[] = [
    new Competitor({country: 'brazil', name: 'neymar'}),
    new Competitor({country: 'germany', name: 'manuel neuer'}),
    new Competitor({country: 'france', name: 'antoine griezmann'}),
    new Competitor({country: 'italy', name: 'giorgio chiellini'}),
    new Competitor({country: 'australia', name: 'sam kerr'}),
]

const competitorsOfThirdSportEvent: ICompetitor[] = [
    new Competitor({country: 'japan', name: 'naomi osaka'}),
    new Competitor({country: 'china', name: 'liu shiwen'}),
    new Competitor({country: 'south korea', name: 'choi hyojoo'}),
    new Competitor({country: 'singapore', name: 'feng tianwei'}),
    new Competitor({country: 'germany', name: 'han ying'}),
]

const competitorsOfFourthSportEvent: ICompetitor[] = [
    new Competitor({country: 'sweden', name: 'sarah sjöström'}),
    new Competitor({country: 'united states', name: 'caleb dressel'}),
    new Competitor({country: 'australia', name: 'emma mckeon'}),
    new Competitor({country: 'canada', name: 'penny oleksiak'}),
    new Competitor({country: 'netherlands', name: 'ranomi kromowidjojo'}),
]

console.log('\n> Competitors of first sport event...\n')
console.dir(competitorsOfFirstSportEvent)

console.log('\n> Competitors of second sport event...\n')
console.dir(competitorsOfSecondSportEvent)

console.log('\n> Competitors of third sport event...\n')
console.dir(competitorsOfThirdSportEvent)

console.log('\n> Competitors of fourth sport event...\n')
console.dir(competitorsOfFourthSportEvent)

firstSportEvent.addCompetitors(...competitorsOfFirstSportEvent).start()
secondSportEvent.addCompetitors(...competitorsOfSecondSportEvent).start()
thirdSportEvent.addCompetitors(...competitorsOfThirdSportEvent).start()
fourthSportEvent.addCompetitors(...competitorsOfFourthSportEvent).start()

const winnersOfFirstSportEvent = firstSportEvent.getWinners()
const winnersOfSecondSportEvent = secondSportEvent.getWinners()
const winnersOfThirdSportEvent = thirdSportEvent.getWinners()
const winnersOfFourthSportEvent = fourthSportEvent.getWinners()

console.log('\n> Winners of first sport event...\n')
console.dir(winnersOfFirstSportEvent)

console.log('\n> Winners of second sport event...\n')
console.dir(winnersOfSecondSportEvent)

console.log('\n> Winners of third sport event...\n')
console.dir(winnersOfThirdSportEvent)

console.log('\n> Winners of fourth sport event...\n')
console.dir(winnersOfFourthSportEvent)

const medalRankingPerCountry = countriesRankingByNumberOfMedals(
    firstSportEvent,
    secondSportEvent,
    thirdSportEvent,
    fourthSportEvent
)

console.log('\n> Medal ranking per country...\n')
console.dir(medalRankingPerCountry)
