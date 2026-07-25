import readline from 'node:readline/promises'

/* -------------------------------------------------------------------------- */
/*                                    TYPES                                   */
/* -------------------------------------------------------------------------- */

interface CalendarCell {
    discovered: boolean
    id: number
}

/* -------------------------------------------------------------------------- */
/*                                   ERRORS                                   */
/* -------------------------------------------------------------------------- */

class CalendarCellDiscoveredError extends Error {
    public constructor(cell: CalendarCell) {
        super(`${cell.id} calendar cell is already discovered`)
        this.name = 'CalendarCellDiscoveredError'
    }
}

class CalendarDayNotFoundError extends Error {
    public constructor(day: number) {
        super(`${day} calendar day not found`)
        this.name = 'CalendarDayNotFoundError'
    }
}

interface CalendarDayOuOfRangeErrorConstructor {
    day: number
    from: number
    to: number
}

class CalendarDayOuOfRangeError extends Error {
    public constructor({day, from, to}: CalendarDayOuOfRangeErrorConstructor) {
        super(
            `${day} calendar day is out of range, it must be between ${from} and ${to} (both included)`
        )
        this.name = 'CalendarDayOuOfRangeError'
    }
}

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* -------------------------------- Calendar -------------------------------- */

interface ICalendar {
    getArray2D: () => CalendarCell[][]
    getFrom: () => number
    getTo: () => number

    discoverDay: (day: number) => void
    toPrint: () => string
}

interface CalendarConstructor {
    from: number
    to: number
}

class Calendar implements ICalendar {
    static rows: number = 4
    static cols: number = 6

    private array2D: CalendarCell[][]
    private readonly from: number
    private readonly to: number

    public constructor({from, to}: CalendarConstructor) {
        let i: number
        let j: number
        let counter: number = from

        this.from = from
        this.to = to

        this.array2D = Array(Calendar.rows)
        for (i = 0; i < Calendar.rows; i++) {
            this.array2D[i] = Array(Calendar.cols)

            for (j = 0; j < Calendar.cols; j++) {
                this.array2D[i][j] = {discovered: false, id: counter}
                counter++
            }
        }
    }

    public getArray2D(): CalendarCell[][] {
        return this.array2D
    }

    public getFrom(): number {
        return this.from
    }

    public getTo(): number {
        return this.to
    }

    public discoverDay(day: number): void {
        let i: number
        let j: number
        let flag: boolean = false
        let counter: number = this.from

        if (day < this.from || day > this.to)
            throw new CalendarDayOuOfRangeError({
                day,
                from: this.from,
                to: this.to,
            })

        for (i = 0; counter <= this.to && i < this.array2D.length; i++) {
            for (j = 0; counter <= this.to && j < this.array2D[i].length; j++) {
                if (this.array2D[i][j].id === day) {
                    if (this.array2D[i][j].discovered)
                        throw new CalendarCellDiscoveredError(
                            this.array2D[i][j]
                        )

                    this.array2D[i][j].discovered = true
                    flag = true
                    break
                }

                counter++
            }

            if (flag) break
        }

        if (!flag) throw new CalendarDayNotFoundError(day)
    }

    public toPrint(): string {
        let calendarPrintable: string[] = []

        let i: number
        let j: number
        let counter: number = this.from

        let row: CalendarCell[]
        let col: CalendarCell
        let rowPrintable: string

        for (i = 0; counter <= this.to && i < this.array2D.length; i++) {
            row = this.array2D[i]

            rowPrintable = i === 0 ? '' : '\n'
            rowPrintable +=
                `${'*'.repeat(4)} `.repeat(row.length).trimEnd() + '\n'

            for (j = 0; counter <= this.to && j < row.length; j++) {
                col = row[j]

                rowPrintable += `*${
                    col.discovered
                        ? ''.padStart(2, '*')
                        : col.id.toString().padStart(2, '0')
                }* `

                counter++
            }

            rowPrintable = rowPrintable.trimEnd() + '\n'
            rowPrintable += `${'*'.repeat(4)} `.repeat(row.length).trimEnd()

            calendarPrintable.push(rowPrintable)
        }

        return calendarPrintable.join('\n')
    }
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

;(async () => {
    const calendar: ICalendar = new Calendar({
        from: 1,
        to: 24,
    })

    const rl: readline.Interface = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    })

    let input01: string
    let input02: string

    console.log(calendar.toPrint())

    console.log(
        '\n> Available operations...\n\n' +
            '  1 - Discover day.\n' +
            '  0 - Exit.'
    )

    input01 = (await rl.question('\n> Enter an operation: ')).trim()

    while (input01 != '0') {
        switch (input01) {
            case '1':
                input02 = (
                    await rl.question('\n> Enter the day to discover: ')
                ).trim()

                try {
                    calendar.discoverDay(parseInt(input02))
                    console.clear()
                    console.log(`> Day ${input02} discovered!`)
                } catch (error) {
                    if (error instanceof CalendarDayOuOfRangeError) {
                        console.clear()
                        console.error(
                            `\n> The day ${input02} must be between ${calendar.getFrom()} and ${calendar.getTo()} (both included)!`
                        )
                    } else if (error instanceof CalendarCellDiscoveredError) {
                        console.clear()
                        console.error(
                            `\n> The day ${input02} is already discovered!`
                        )
                    } else if (error instanceof CalendarDayNotFoundError) {
                        console.clear()
                        console.error(
                            `\n> ${input02} day not found in the calendar!`
                        )
                    } else {
                        console.clear()
                        console.error(
                            '\n> An error occurred on discover the day!'
                        )
                    }
                }
                break

            default:
                console.clear()
                console.log('\n> Invalid operation! Try again...')
        }

        console.log(`\n${calendar.toPrint()}`)

        console.log(
            '\n> Available operations...\n\n' +
                '  1 - Discover day.\n' +
                '  0 - Exit.'
        )

        input01 = (await rl.question('\n> Enter an operation: ')).trim()
    }

    rl.close()
})()
