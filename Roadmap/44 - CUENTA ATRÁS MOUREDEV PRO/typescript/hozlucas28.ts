import {setTimeout} from 'node:timers/promises'
import {isMainThread, parentPort, Worker} from 'node:worker_threads'

interface TimeRemaining {
    days: number
    hours: number
    minutes: number
    seconds: number
}

function getTimeRemaining(from: Date, to: Date): TimeRemaining {
    const epochFrom: number = from.valueOf()
    const epochTo: number = to.valueOf()

    let conversion: number
    let epochRemainingTime: number = epochTo - epochFrom

    if (epochRemainingTime <= 0)
        return {
            days: 0,
            hours: 0,
            minutes: 0,
            seconds: 0,
        }

    conversion = 24 * 60 * 60 * 1000
    const days: number = Math.floor(epochRemainingTime / conversion)
    epochRemainingTime -= days * conversion

    conversion = 60 * 60 * 1000
    const hours: number = Math.floor(epochRemainingTime / conversion)
    epochRemainingTime -= hours * conversion

    conversion = 60 * 1000
    const minutes: number = Math.floor(epochRemainingTime / conversion)
    epochRemainingTime -= minutes * conversion

    conversion = 1000
    const seconds: number = Math.floor(epochRemainingTime / conversion)
    epochRemainingTime -= seconds * conversion

    return {
        days: Math.max(0, days),
        hours: Math.max(0, hours),
        minutes: Math.max(0, minutes),
        seconds: Math.max(0, seconds),
    }
}

async function main() {
    let startDate: Date = new Date() // Current date
    const endDate: Date = new Date(2024, 10, 27, 23, 59, 0, 0)
    let remainingTime: TimeRemaining = getTimeRemaining(startDate, endDate)

    if (!isMainThread) parentPort?.postMessage('clearConsole')

    console.log(
        `> Time remaining for ${endDate.toUTCString()}: ` +
            `[ ${remainingTime.days.toString().padStart(6, '0')} days | ` +
            `${remainingTime.hours.toString().padStart(2, '0')} hours | ` +
            `${remainingTime.minutes.toString().padStart(2, '0')} minutes | ` +
            `${remainingTime.seconds.toString().padStart(2, '0')} seconds ].`
    )

    while (
        remainingTime.days ||
        remainingTime.hours ||
        remainingTime.minutes ||
        remainingTime.seconds
    ) {
        startDate = new Date() // Current date
        remainingTime = await setTimeout(
            1 * 1000,
            getTimeRemaining(startDate, endDate)
        )

        if (!isMainThread) parentPort?.postMessage('clearConsole')

        console.log(
            `> Time remaining for ${endDate.toUTCString()}: ` +
                `[ ${remainingTime.days.toString().padStart(6, '0')} days | ` +
                `${remainingTime.hours.toString().padStart(2, '0')} hours | ` +
                `${remainingTime.minutes
                    .toString()
                    .padStart(2, '0')} minutes | ` +
                `${remainingTime.seconds
                    .toString()
                    .padStart(2, '0')} seconds ].`
        )
    }

    console.log('\n> The day has come!')
}

if (isMainThread) {
    const worker: Worker = new Worker(__filename)

    worker.on('message', (message) => {
        if (message === 'clearConsole') console.clear()
    })
} else {
    main()
}
