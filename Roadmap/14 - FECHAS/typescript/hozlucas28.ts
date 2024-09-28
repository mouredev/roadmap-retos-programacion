/*
    Dates...
*/

console.log('Dates...')

const actualDate: Date = new Date()
const bornDate: Date = new Date(2002, 1, 20)

console.log(`\nToday is: ${actualDate}`)
console.log(`\nLucas Hoz born date: ${bornDate}`)

const millisecondsPerDay: number = 86_400_000
const millisecondsBetweenDates = actualDate.getTime() - bornDate.getTime()
const daysBetweenDates = Math.round(
	millisecondsBetweenDates / millisecondsPerDay
)

console.log(
	`\nNumber of days between today and Lucas Hoz born date: ${daysBetweenDates} days`
)

console.log(
	'\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

function dayOfYear(date: Date): number {
	const millisecondsPerDay: number = 86_400_000

	const baseDate = new Date(date.getFullYear(), 0, 0)
	const dayOfTheYear = Math.floor(
		(date.getTime() - baseDate.getTime()) / millisecondsPerDay
	)

	return dayOfTheYear
}

const bornDateObj = {
	day: bornDate.getDate(),
	month: bornDate.getMonth() + 1,
	year: bornDate.getFullYear(),
	hours: bornDate.getHours(),
	minutes: bornDate.getMinutes(),
	seconds: bornDate.getSeconds(),
	dayOfTheYear: dayOfYear(bornDate),
	dayOfTheWeek: bornDate.getDay(),
	monthName: bornDate.toLocaleString('en', { month: 'long' }),
}

console.log(
	`\nDay, month, and year: ${bornDateObj.day}, ${bornDateObj.month}, and ${bornDateObj.year}`
)

console.log(
	`\nHours, minutes, and seconds: ${bornDateObj.hours} hours, ${bornDateObj.minutes} minutes, and ${bornDateObj.seconds} seconds`
)

console.log(`\nDay of the year: ${bornDateObj.dayOfTheYear}`)

console.log(`\nName of the month: ${bornDateObj.monthName}`)
