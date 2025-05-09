import fs from 'node:fs/promises'

/* -------------------------------------------------------------------------- */
/*                                    TYPES                                   */
/* -------------------------------------------------------------------------- */

type Status = 'active' | 'inactive'

interface User {
    id: number
    email: `${string}@${string}.com`
    status: Status
}

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

interface CreateCSVParams<T extends object> {
    data: T[]
    path: `${string}.csv`
}

async function createCSV<T extends object>({path, data}: CreateCSVParams<T>) {
    const columns: string[] = Object.keys(data[0])
    const rows: string[] = [columns.join(',')]

    for (const element of data) {
        const row: string = Object.values(element).join(',')
        rows.push(row)
    }

    await fs.writeFile(path, rows.join('\n'), {encoding: 'utf-8'})
}

interface GetChoicesParams<T> {
    amount: number
    choices: T[]
    uniqueKey?: keyof T
}

function getChoices<T>({amount, choices, uniqueKey}: GetChoicesParams<T>): T[] {
    const selectedChoices: T[] = []

    while (selectedChoices.length < amount) {
        const randomIndex: number = Math.floor(Math.random() * choices.length)
        const choiceSelected: T = choices[randomIndex]

        const cmpFn = (value: T) => {
            return uniqueKey
                ? value[uniqueKey] === choiceSelected[uniqueKey]
                : value === choiceSelected
        }

        if (selectedChoices.findIndex(cmpFn) != -1) continue
        selectedChoices.push(choiceSelected)
    }

    return selectedChoices
}

interface GetCSVParams {
    path: `${string}.csv`
}

async function getCSV<T extends object>({path}: GetCSVParams): Promise<T[]> {
    const data: T[] = []

    const csvContent = await fs.readFile(path, {encoding: 'utf-8'})

    const csvContentArr: string[] = csvContent.split('\n')
    const csvColumnsArr: string[] = csvContentArr[0].split(',')
    const csvRowsArr: string[] = csvContentArr.slice(1)

    for (const row of csvRowsArr) {
        const rowArr = row.split(',')

        const newData: any = {}
        for (let j = 0; j < csvColumnsArr.length; j++) {
            const column: string = csvColumnsArr[j]
            newData[column] = rowArr[j]
        }

        data.push(newData)
    }

    return data
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

;(async () => {
    const users: User[] = [
        {
            email: 'test01@gmail.com',
            id: 1,
            status: 'active',
        },
        {
            email: 'test02@gmail.com',
            id: 2,
            status: 'inactive',
        },
        {
            email: 'test03@gmail.com',
            id: 3,
            status: 'inactive',
        },
        {
            email: 'test04@gmail.com',
            id: 4,
            status: 'active',
        },
        {
            email: 'test05@gmail.com',
            id: 5,
            status: 'inactive',
        },
        {
            email: 'test06@gmail.com',
            id: 6,
            status: 'active',
        },
        {
            email: 'test07@gmail.com',
            id: 7,
            status: 'active',
        },
        {
            email: 'test08@gmail.com',
            id: 8,
            status: 'active',
        },
    ]

    await createCSV({data: users, path: './users.csv'})
    const csvUsers: User[] = await getCSV<User>({path: './users.csv'})

    const activeUsers = csvUsers.filter((user) => user.status === 'active')

    const winners: User[] = getChoices<User>({
        amount: 3,
        choices: activeUsers,
        uniqueKey: 'id',
    })

    console.log('> The first winner is...')
    console.log(
        `> Congratulations ${winners[0].email} with id ${winners[0].id}, you won a subscription!`
    )

    console.log('\n> The second winner is...')
    console.log(
        `> Congratulations ${winners[1].email} with id ${winners[1].id}, you won a discount!`
    )

    console.log('\n> The third winner is...')
    console.log(
        `> Congratulations ${winners[2].email} with id ${winners[2].id}, you won a book!`
    )
})()
