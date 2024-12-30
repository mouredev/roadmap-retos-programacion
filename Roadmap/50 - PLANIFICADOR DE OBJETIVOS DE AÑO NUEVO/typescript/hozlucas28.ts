import type {UUID} from 'node:crypto'
import {randomUUID} from 'node:crypto'
import fs from 'node:fs/promises'
import readline from 'node:readline/promises'

/* -------------------------------------------------------------------------- */
/*                                    TYPES                                   */
/* -------------------------------------------------------------------------- */

interface YearPlan {
    january: [Goal, number][]
    february: [Goal, number][]
    march: [Goal, number][]
    april: [Goal, number][]
    may: [Goal, number][]
    june: [Goal, number][]
    july: [Goal, number][]
    august: [Goal, number][]
    september: [Goal, number][]
    october: [Goal, number][]
    november: [Goal, number][]
    december: [Goal, number][]
}

/* -------------------------------------------------------------------------- */
/*                                   ERRORS                                   */
/* -------------------------------------------------------------------------- */

class MonthsOutOfRange extends Error {
    public constructor() {
        super('Months out of range')
        this.name = 'MonthsOutOfRange'
    }
}

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* ---------------------------------- Goal ---------------------------------- */

interface GoalConstructor {
    amount: number
    description: string
    monthsLimit: number
    units: string
}

class Goal {
    static maxMonthsLimit: number = 12

    private readonly amount: number
    private readonly description: string
    private readonly id: UUID
    private readonly monthsLimit: number
    private readonly units: string

    public constructor({amount, description, monthsLimit, units}: GoalConstructor) {
        this.amount = amount
        this.description = description
        this.id = randomUUID()
        this.units = units

        if (monthsLimit < 1 || monthsLimit > Goal.maxMonthsLimit) throw new MonthsOutOfRange()

        this.monthsLimit = monthsLimit
    }

    public getAmount(): number {
        return this.amount
    }

    public getDescription(): string {
        return this.description
    }

    public getId(): UUID {
        return this.id
    }

    public getMonthsLimit(): number {
        return this.monthsLimit
    }

    public getUnits(): string {
        return this.units
    }

    public toYearPlan(): YearPlan {
        const yearPlan: YearPlan = {
            january: [],
            february: [],
            march: [],
            april: [],
            may: [],
            june: [],
            july: [],
            august: [],
            september: [],
            october: [],
            november: [],
            december: [],
        }

        let counter: number = this.amount
        while (counter) {
            let monthCounter: number = this.monthsLimit
            for (const key in yearPlan) {
                if (!counter || !monthCounter) break

                if ((yearPlan[key] as [Goal, number][])[0]) {
                    ;(yearPlan[key] as [Goal, number][])[0][1]++
                } else {
                    ;(yearPlan[key] as [Goal, number][])[0] = [this, 1]
                }

                monthCounter--
                counter--
            }
        }

        return yearPlan
    }
}

/* -------------------------------- YearGoals ------------------------------- */

class YearGoals {
    static maxGoals: number = 10

    private goals: Goal[]
    private plan: YearPlan

    public constructor() {
        this.goals = []

        this.plan = {
            january: [],
            february: [],
            march: [],
            april: [],
            may: [],
            june: [],
            july: [],
            august: [],
            september: [],
            october: [],
            november: [],
            december: [],
        }
    }

    public getGoals(): Goal[] {
        return this.goals
    }

    public getPlan(): YearPlan {
        return this.plan
    }

    private appendGoalToPlan(goal: Goal): void {
        const goalYearPlan: YearPlan = goal.toYearPlan()

        for (const key in goalYearPlan) {
            ;(this.plan[key] as [Goal, number][]).push(...(goalYearPlan[key] as [Goal, number][]))
        }
    }

    private removeGoalFromPlan(id: UUID): void {
        for (const key in this.plan) {
            const goalI: number = this.plan[key].findIndex(([goal]: [Goal, number]) => goal.getId() === id)
            if (goalI === -1) break

            this.plan[key].splice(goalI, 1)
        }
    }

    public addGoal(newGoal: Goal): boolean {
        if (this.goals.length === YearGoals.maxGoals) return false
        const newGoalID: UUID = newGoal.getId()

        const goalI: number = this.goals.findIndex((goal) => goal.getId() === newGoalID)
        if (goalI !== -1) return false

        this.goals.push(newGoal)
        this.appendGoalToPlan(newGoal)

        return true
    }

    public removeGoal(id: UUID): boolean {
        const goalI: number = this.goals.findIndex((goal) => goal.getId() === id)
        if (goalI === -1) return false

        this.goals.splice(goalI, 1)
        this.removeGoalFromPlan(id)

        return true
    }

    public async savePlan(
        path: `${string}.txt`,
        goalToRow: (goal: Goal, amount: number, index: number) => string,
        monthTitle: (key: string) => string = (month) => `${month[0].toUpperCase()}${month.slice(1)}:`
    ): Promise<void> {
        const data: string[] = []

        for (const key in this.plan) {
            const goalsMonth: [Goal, number][] = this.plan[key]

            const rows: string[] = [monthTitle(key)]
            for (let i = 0; i < goalsMonth.length; i++) {
                const [goal, amount] = goalsMonth[i]
                rows.push(goalToRow(goal, amount, i))
            }

            data.push(rows.join('\n'), '\n\n')
        }

        await fs.writeFile(path, data, {encoding: 'utf-8'})
    }
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

;(async () => {
    const yearGoals: YearGoals = new YearGoals()

    const rl: readline.Interface = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    })

    console.log(
        '> Available operations:\n\n' +
            ' 1 - Add goal.\n' +
            ' 2 - Remove goal.\n' +
            ' 3 - Show goals.\n' +
            ' 4 - Show plan.\n' +
            ' 5 - Save plan.\n' +
            ' 0 - Exit.'
    )

    let input: string = (await rl.question('\n> Select an operation: ')).trim()

    while (input !== '0') {
        switch (input) {
            case '1':
                console.log('\n> Complete the following goal data...')
                const units: string = (await rl.question('\n> Units: ')).trim()
                const amount: number = parseInt((await rl.question('\n> Amount (as a number): ')).trim())
                const description: string = (await rl.question('\n> Description: ')).trim()

                let monthsLimit: number = parseInt((await rl.question('\n> Months limit (as a number): ')).trim())
                while (monthsLimit < 1 || monthsLimit > Goal.maxMonthsLimit) {
                    console.log('\n> Error! Months limit must be between 1 and 12 (both included). Try again...')
                    monthsLimit = parseInt((await rl.question('\n> Months limit (as a number): ')).trim())
                }

                const goal: Goal = new Goal({amount, description, monthsLimit, units})

                yearGoals.addGoal(goal)
                    ? console.log('\n> Goal added!')
                    : console.log('\n> An error occurred! The goal was not added.')
                break

            case '2':
                const goalId: UUID = (await rl.question('\n> Goal id to remove: ')).trim() as UUID

                yearGoals.removeGoal(goalId)
                    ? console.log(`\n> Goal "${goalId}" removed!`)
                    : console.log('\n> An error occurred! The goal was not removed.')
                break

            case '3':
                const goals: Goal[] = yearGoals.getGoals()

                const goalsRows: string[] = []
                for (const goal of goals) {
                    goalsRows.push(
                        `\n• Goal "${goal.getId()}"...` +
                            `\n\n  - ID: "${goal.getId()}".` +
                            `\n  - Description: \"${goal.getDescription()}\".` +
                            `\n  - Months limit: ${goal.getMonthsLimit()}.` +
                            `\n  - Amount: ${goal.getAmount()}.` +
                            `\n  - Units: "${goal.getUnits()}".`
                    )
                }

                goalsRows.length && console.log(goalsRows.join('\n'))
                break

            case '4':
                const plan: YearPlan = yearGoals.getPlan()

                const planRows: string[] = []
                for (const key in plan) {
                    const goals: [Goal, number][] = plan[key]

                    let planRow: string = `\n${key[0].toUpperCase()}${key.slice(1)}:`
                    for (let i = 0; i < goals.length; i++) {
                        const [goal, amount] = goals[i]
                        const desc: string = goal.getDescription()
                        const units: string = goal.getUnits()
                        const totalAmount: number = goal.getAmount()
                        planRow += `\n[ ] ${i + 1}. ${desc} (${amount} ${units}/mes). Total: ${totalAmount}.`
                    }

                    planRows.push(planRow)
                }

                planRows.length && console.log(planRows.join('\n'))
                break

            case '5':
                const currentDate: Date = new Date()
                const savePlanPath = `${process.cwd()}\\plan-${currentDate.getFullYear()}.txt` as const
                await yearGoals.savePlan(savePlanPath, (goal, amount, index) => {
                    const desc: string = goal.getDescription()
                    const units: string = goal.getUnits()
                    const totalAmount: number = goal.getAmount()
                    return `[ ] ${index + 1}. ${desc} (${amount} ${units}/mes). Total: ${totalAmount}.`
                })

                console.log(`\n> Plan saved in "${savePlanPath}" path.`)
                break

            default:
                console.log('\n> Invalid operation! Try again...')
                break
        }

        console.log(
            '\n> Available operations:\n\n' +
                ' 1 - Add goal.\n' +
                ' 2 - Remove goal.\n' +
                ' 3 - Show goals.\n' +
                ' 4 - Show plan.\n' +
                ' 5 - Save plan.\n' +
                ' 0 - Exit.'
        )

        input = (await rl.question('\n> Select an operation: ')).trim()
    }

    rl.close()
})()
