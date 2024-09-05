import readline from 'node:readline/promises'

/* -------------------------------------------------------------------------- */
/*                                    TYPES                                   */
/* -------------------------------------------------------------------------- */

interface Question<T extends string[]> {
    correctAnswer: T[number]
    options: [...T]
    points: number
    question: `${string}?`
}

interface QuestionsPerHouse {
    backend: [
        Question<['Java', 'JavaScript', 'Python', 'Ruby']>,
        Question<['MySQL', 'MongoDB', 'PostgreSQL', 'SQLite']>
    ]
    data: [
        Question<
            [
                'Data analysis',
                'Data visualization',
                'Data mining',
                'Data modeling'
            ]
        >,
        Question<['Python', 'R', 'SQL', 'Julia']>
    ]
    frontend: [
        Question<['HTML', 'CSS', 'JavaScript', 'Python']>,
        Question<['React', 'Angular', 'Vue', 'Ember']>
    ]
    mobile: [
        Question<['iOS', 'Android', 'React Native', 'Flutter']>,
        Question<['Swift', 'Kotlin', 'Java', 'Objective-C']>
    ]
}

/* -------------------------------------------------------------------------- */
/*                                    UTILS                                   */
/* -------------------------------------------------------------------------- */

function randomChoice<T>(...choices: T[]): T {
    const rndChoice: T = choices[Math.floor(Math.random() * choices.length)]
    return rndChoice
}

async function makeQuestion<T extends string[]>(
    question: Question<T>
): Promise<number> {
    const rl: readline.Interface = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    })

    const formatter: Intl.ListFormat = new Intl.ListFormat('en', {
        style: 'long',
        type: 'disjunction',
    })

    const optionsFormatted: string = formatter.format(question.options)

    const optionsNormalized: string[] = question.options.map((opt) =>
        opt.toUpperCase()
    )

    let userAnswer: string = (
        await rl.question(`> ${question.question} (${optionsFormatted}): `)
    )
        .trim()
        .toUpperCase()

    while (!optionsNormalized.includes(userAnswer)) {
        console.log('\n> Invalid option! Try again...')

        userAnswer = (
            await rl.question(
                `\n> ${question.question} (${optionsFormatted}): `
            )
        )
            .trim()
            .toUpperCase()
    }
    rl.close()

    return userAnswer === question.correctAnswer ? question.points : 0
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

const questionsPerHouse: QuestionsPerHouse = {
    backend: [
        {
            correctAnswer: 'JavaScript',
            options: ['Java', 'JavaScript', 'Python', 'Ruby'],
            question:
                'What is the primary language used in backend development?',
            points: 5,
        },
        {
            correctAnswer: 'PostgreSQL',
            options: ['MySQL', 'MongoDB', 'PostgreSQL', 'SQLite'],
            points: 5,
            question:
                'Which database is commonly used for storing data in backend applications?',
        },
    ],
    data: [
        {
            correctAnswer: 'Data analysis',
            options: [
                'Data analysis',
                'Data visualization',
                'Data mining',
                'Data modeling',
            ],
            points: 5,
            question:
                'What is the process of analyzing and interpreting data called?',
        },
        {
            correctAnswer: 'Julia',
            options: ['Python', 'R', 'SQL', 'Julia'],
            points: 5,
            question:
                'Which programming language is commonly used for data analysis?',
        },
    ],
    frontend: [
        {
            correctAnswer: 'JavaScript',
            options: ['HTML', 'CSS', 'JavaScript', 'Python'],
            points: 5,
            question:
                'What is the primary language used in frontend development?',
        },
        {
            correctAnswer: 'Angular',
            options: ['React', 'Angular', 'Vue', 'Ember'],
            points: 5,
            question:
                'Which framework is commonly used for building user interfaces?',
        },
    ],
    mobile: [
        {
            correctAnswer: 'Flutter',
            options: ['iOS', 'Android', 'React Native', 'Flutter'],
            points: 5,
            question:
                'Which platform is commonly used for developing mobile applications?',
        },
        {
            correctAnswer: 'Objective-C',
            options: ['Swift', 'Kotlin', 'Java', 'Objective-C'],
            points: 5,
            question:
                'What is the primary language used in mobile app development?',
        },
    ],
}

;(async () => {
    const rl: readline.Interface = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    })

    const userName: string = (await rl.question('> Enter your name: ')).trim()
    rl.close()

    const points: [keyof QuestionsPerHouse, number][] = [
        ['backend', 0],
        ['data', 0],
        ['frontend', 0],
        ['mobile', 0],
    ]

    console.log()
    points[0][1] += await makeQuestion(questionsPerHouse.backend[0])

    console.log()
    points[0][1] += await makeQuestion(questionsPerHouse.backend[1])

    console.log()
    points[1][1] += await makeQuestion(questionsPerHouse.data[0])

    console.log()
    points[1][1] += await makeQuestion(questionsPerHouse.data[1])

    console.log()
    points[2][1] += await makeQuestion(questionsPerHouse.frontend[0])

    console.log()
    points[2][1] += await makeQuestion(questionsPerHouse.frontend[1])

    console.log()
    points[3][1] += await makeQuestion(questionsPerHouse.mobile[0])

    console.log()
    points[3][1] += await makeQuestion(questionsPerHouse.mobile[1])

    const maxPoints: [keyof QuestionsPerHouse, number][] = []

    for (const [house, housePoints] of points) {
        if (maxPoints.length === 0) {
            maxPoints.push([house, housePoints])
            continue
        }

        if (maxPoints[0][1] > housePoints) continue

        if (maxPoints[0][1] === housePoints)
            maxPoints.push([house, housePoints])
        else maxPoints[0] = [house, housePoints]
    }

    if (maxPoints.length === 1) {
        console.log(
            `\n> ${userName} will be part of the ${maxPoints[0][0]} house!`
        )
        return
    }

    const rndChoice: [keyof QuestionsPerHouse, number] = randomChoice(
        ...maxPoints
    )

    console.log(
        `\n> The decision has been complicated,` +
            ` but ${userName} will be part of the ${rndChoice[0]} house!`
    )
})()
