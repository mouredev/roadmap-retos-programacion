/*
    Higher order functions (HOF)...
*/

console.log('Higher order functions (HOF)...')

function toFilter<T>(array: T[], callback: (element: T) => boolean): T[] {
    const filteredArray: T[] = []

    for (const element of array) {
        callback(element) && filteredArray.push(element)
    }

    return filteredArray
}

const numbers: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(`\nnumbers = [${numbers}]`)

const oddNumbers: number[] = toFilter(numbers, (element) => element % 2 !== 0)
console.log(`\noddNumbers = [${oddNumbers}]`)

const evenNumbers: number[] = toFilter(numbers, (element) => element % 2 === 0)
console.log(`\nevenNumbers = [${evenNumbers}]`)

console.log(
    '\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...\n')

interface Student {
    bornDate: Date
    name: string
    qualifications: number[]
}

function getAverageQualification(student: Student): number {
    const total: number = student.qualifications.reduce(
        (prevValue, currentValue) => prevValue + currentValue,
        0
    )

    const averageQualification: number = total / student.qualifications.length

    return parseFloat(averageQualification.toFixed(2))
}

const students: Student[] = [
    {
        bornDate: new Date(2002, 20, 2),
        name: 'Lucas Hoz',
        qualifications: [7.5, 6.8, 8.2],
    },
    {
        bornDate: new Date(2003, 10, 15),
        name: 'John Doe',
        qualifications: [9.1, 8.5, 7.9],
    },
    {
        bornDate: new Date(2001, 5, 30),
        name: 'Jane Smith',
        qualifications: [8.7, 9.3, 10.0],
    },
    {
        bornDate: new Date(2004, 2, 12),
        name: 'Alex Johnson',
        qualifications: [6.4, 7.2, 8.9],
    },
    {
        bornDate: new Date(2000, 8, 5),
        name: 'Sarah Brown',
        qualifications: [9.5, 9.8, 9.2],
    },
    {
        bornDate: new Date(2005, 11, 25),
        name: 'Michael Davis',
        qualifications: [7.1, 8.3, 7.7],
    },
    {
        bornDate: new Date(2002, 1, 18),
        name: 'Emily Wilson',
        qualifications: [8.9, 9.6, 9.4],
    },
    {
        bornDate: new Date(2003, 6, 9),
        name: 'Daniel Thompson',
        qualifications: [7.8, 8.1, 7.5],
    },
]

console.log('Students...')
console.table(students)

const studentsWithNameAndAverageQualification = students.map((student) => ({
    name: student.name,
    averageQualification: getAverageQualification(student),
}))

console.log('\nStudents with name and average qualification...')
console.table(studentsWithNameAndAverageQualification)

const studentsWithAverageQualificationMoreThanNine: Student[] = toFilter(
    students,
    (student) => {
        const qualificationAverage: number = getAverageQualification(student)
        return qualificationAverage >= 9
    }
)

console.log('\nStudents with an average qualification more than nine...')
console.table(studentsWithAverageQualificationMoreThanNine)

const sortedStudentsByBornDate: Student[] = students.toSorted((a, b) => {
    return b.bornDate.getTime() - a.bornDate.getTime()
})

console.log('\nSorted students by born date (youngest to oldest)...')
console.table(sortedStudentsByBornDate)

const studentsWithNameAndBestQualification = students.map((student) => ({
    name: student.name,
    bestQualification: Math.max(...student.qualifications),
}))

console.log('\nStudents with name and best qualification...')
console.table(studentsWithNameAndBestQualification)
