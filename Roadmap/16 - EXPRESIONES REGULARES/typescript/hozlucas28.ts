/*
    Regular expressions...
*/

console.log('Regular expressions...')

const customText: string =
	'¡Hola Mundo! Hoy es 15/04/2024. Quedan 263 días para terminar el año 2024.'

const numbersInsideCustomText: `${number}` = customText
	.match(/[0-9]/g)
	?.join('') as `${number}`

console.log(`\n\`customText\` = '${customText}'`)

console.log(`\nNumbers inside \`customText\` --> ${numbersInsideCustomText}`)

console.log(
	'\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

const regularExpressions = {
	email: new RegExp(/^[a-zA-Z0-9]*@(gmail|outlook|hotmail|yahoo)\.com$/),
	phoneNumber: new RegExp(/^\+\d{1,4} \d{10}$/),
	url: new RegExp(
		/^https?:\/\/([a-zA-Z0-9]*\.)?[a-zA-Z0-9]*\.([a-zA-Z]{3})(\.[a-zA-Z]{2,3})?\/?$/
	),
}

const emails: string[] = [
	'hozlucas28@gmail.com',
	'hozlucas28@dev.com',
	'hozlucas-28@hotmail.com',
	'hozlucas28@meli.com',
	'hozlucas28@edu.com',
]

const phoneNumbers: string[] = [
	'+1234567890',
	'+1 1234567890',
	'+1234 1234567890',
	'+123456789',
	'+123456789 1234567890',
]

const urls: string[] = [
	'https://www.example.cóm',
	'http://example.com',
	'https://subdomain.example.com',
	'http://www.example.c2.uk',
	'https://www.example.org',
]

console.log('\n\nEmails...')

for (const email of emails) {
	const isValid: boolean = regularExpressions.email.test(email)
	console.log(`\n'${email}' is valid? --> ${isValid}`)
}

console.log('\n\nPhone numbers...')

for (const phoneNumber of phoneNumbers) {
	const isValid: boolean = regularExpressions.phoneNumber.test(phoneNumber)
	console.log(`\n'${phoneNumber}' is valid? --> ${isValid}`)
}

console.log('\n\nUrls...')

for (const url of urls) {
	const isValid: boolean = regularExpressions.url.test(url)
	console.log(`\n'${url}' is valid? --> ${isValid}`)
}
