import * as fs from 'node:fs'
import * as readline from 'readline-sync'

/*
    JSON and XML files...
*/

console.log('JSON and XML files...')

console.log(`type FileBasename = \`\${string}.\${string}\`

type Content<AsXML extends boolean = false> = AsXML extends true
    ? {
            age: number
            name: string
            'born-date': Date
            'programming-languages': Record<string, string>
      }
    : {
            age: number
            bornDate: Date
            name: string
            programmingLanguages: string[]
      }

function stringifyXml<T extends Record<string, unknown>>(
    content: T,
    forceLineBreak: boolean = false
) {
    let stringifiedContent: string = ''

    for (const key of Object.keys(content)) {
        const line =
            typeof content[key] === 'object' && !(content[key] instanceof Date)
                ? stringifyXml(content[key] as Record<string, unknown>, true)
                : content[key]
        const lineBreak =
            forceLineBreak || stringifiedContent.length > 0 ? '\\n' : ''
        stringifiedContent += \`\${lineBreak}<\${key}>\${line}</\${key}>\`
    }

    return stringifiedContent
}

const jsonFilePath: FileBasename = 'author.json'
const xmlFilePath: FileBasename = 'author.xml'

// Delete files if exist
if (fs.existsSync(jsonFilePath)) fs.rmSync(jsonFilePath)
if (fs.existsSync(xmlFilePath)) fs.rmSync(xmlFilePath)

// Format contents
const jsonNewContent: Content = {
    age: 22,
    bornDate: new Date(2002, 1, 20),
    name: 'Lucas',
    programmingLanguages: ['TypeScript', 'Python', 'Go (Golang)'],
}

const xmlNewContent: Content<true> = {
    age: 22,
    name: 'Lucas',
    'born-date': new Date(2002, 1, 20),
    'programming-languages': {
        typescript: 'TypeScript',
        python: 'Python',
        go: 'Go (Golang)',
    },
}

// Write files
const stringifiedJsonContent: string = JSON.stringify(jsonNewContent)
const stringifiedXmlContent: string = stringifyXml(xmlNewContent)

fs.writeFileSync(jsonFilePath, stringifiedJsonContent, { encoding: 'utf-8' })
fs.writeFileSync(xmlFilePath, stringifiedXmlContent, { encoding: 'utf-8' })

// Print files content
const jsonContent = fs.readFileSync(jsonFilePath, { encoding: 'utf-8' })
const xmlContent = fs.readFileSync(xmlFilePath, { encoding: 'utf-8' })

console.log(\`\\n\${jsonContent}\`)
console.log(\`\\n\${xmlContent}\`)

// Delete files
fs.rmSync(xmlFilePath)
fs.rmSync(jsonFilePath)`)

type FileBasename = `${string}.${string}`

type Content<AsXML extends boolean = false> = AsXML extends true
	? {
			age: number
			name: string
			'born-date': Date
			'programming-languages': Record<string, string>
	  }
	: {
			age: number
			bornDate: Date
			name: string
			programmingLanguages: string[]
	  }

function stringifyXml<T extends Record<string, unknown>>(
	content: T,
	forceLineBreak: boolean = false
) {
	let stringifiedContent: string = ''

	for (const key of Object.keys(content)) {
		const line =
			typeof content[key] === 'object' && !(content[key] instanceof Date)
				? stringifyXml(content[key] as Record<string, unknown>, true)
				: content[key]
		const lineBreak =
			forceLineBreak || stringifiedContent.length > 0 ? '\n' : ''
		stringifiedContent += `${lineBreak}<${key}>${line}</${key}>`
	}

	return stringifiedContent
}

const jsonFilePath: FileBasename = 'author.json'
const xmlFilePath: FileBasename = 'author.xml'

// Delete files if exist
if (fs.existsSync(jsonFilePath)) fs.rmSync(jsonFilePath)
if (fs.existsSync(xmlFilePath)) fs.rmSync(xmlFilePath)

// Format contents
const jsonNewContent: Content = {
	age: 22,
	bornDate: new Date(2002, 1, 20),
	name: 'Lucas',
	programmingLanguages: ['TypeScript', 'Python', 'Go (Golang)'],
}

const xmlNewContent: Content<true> = {
	age: 22,
	name: 'Lucas',
	'born-date': new Date(2002, 1, 20),
	'programming-languages': {
		typescript: 'TypeScript',
		python: 'Python',
		go: 'Go (Golang)',
	},
}

// Write files
const stringifiedJsonContent: string = JSON.stringify(jsonNewContent)
const stringifiedXmlContent: string = stringifyXml(xmlNewContent)

fs.writeFileSync(jsonFilePath, stringifiedJsonContent, { encoding: 'utf-8' })
fs.writeFileSync(xmlFilePath, stringifiedXmlContent, { encoding: 'utf-8' })

// Print files content
const jsonContent = fs.readFileSync(jsonFilePath, { encoding: 'utf-8' })
const xmlContent = fs.readFileSync(xmlFilePath, { encoding: 'utf-8' })

console.log(`\n${jsonContent}`)
console.log(`\n${xmlContent}`)

// Delete files
fs.rmSync(xmlFilePath)
fs.rmSync(jsonFilePath)

console.log(
	'\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

class JsonFile {
	private path: string
	private isDeleted: boolean

	constructor(path: string, initialContent: Content) {
		this.path = `${path}.json`
		this.isDeleted = false
		this.rewriteContent(initialContent)
	}

	public getContent(): Content {
		this.validate()
		const content: string = fs.readFileSync(this.path, { encoding: 'utf-8' })
		const parsedContent: Content = JSON.parse(content)
		return parsedContent
	}

	private rewriteContent(content: Content): this {
		const stringifiedContent = JSON.stringify(content)
		fs.writeFileSync(this.path, stringifiedContent, {
			encoding: 'utf-8',
		})

		return this
	}

	private validate(): never | void {
		if (this.isDeleted) throw new Error('The file was deleted!')
	}

	public appendProgrammingLanguage(programmingLanguage: string): this {
		this.validate()

		const content: Content = this.getContent()
		if (
			!content.programmingLanguages.some(
				(language) =>
					language.toUpperCase() === programmingLanguage.toUpperCase()
			)
		) {
			content.programmingLanguages.push(programmingLanguage)
			this.rewriteContent(content)
		}

		return this
	}

	public deleteFile(): void {
		this.validate()

		this.isDeleted = true
		fs.rmSync(this.path)
	}

	public removeProgrammingLanguage(programmingLanguage: string): this {
		this.validate()

		const content: Content = this.getContent()
		content.programmingLanguages = content.programmingLanguages.filter(
			(language) => language.toUpperCase() !== programmingLanguage.toUpperCase()
		)
		this.rewriteContent(content)
		return this
	}

	public updateAge(newAge: number): this {
		this.validate()

		const content: Content = this.getContent()
		content.age = newAge
		this.rewriteContent(content)
		return this
	}

	public updateName(newName: string): this {
		this.validate()

		const content: Content = this.getContent()
		content.name = newName
		this.rewriteContent(content)
		return this
	}

	public updateBornDate(newDate: Date): this {
		this.validate()

		const content: Content = this.getContent()
		content.bornDate = newDate
		this.rewriteContent(content)
		return this
	}
}

class XmlFile {
	private path: string
	private isDeleted: boolean

	constructor(path: string, initialContent: Content<true>) {
		this.path = `${path}.xml`
		this.isDeleted = false
		this.rewriteContent(initialContent)
	}

	public getContent(): Content<true> {
		this.validate()

		const content: string = fs.readFileSync(this.path, { encoding: 'utf-8' })
		const parsedContent: Content<true> = this.parseContent(content)
		return parsedContent
	}

	private parseContent(content: string): Content<true> {
		const parsedContent: Content<true> = {
			age: 0,
			name: '',
			'programming-languages': {},
			'born-date': new Date(),
		}

		for (const line of content.split('\n')) {
			const match = line.match(/<([\w|-]*)>(.*)</)
			if (!match) continue

			const [, tag, content] = match as [string, keyof Content<true>, string]

			if (tag === 'age') {
				parsedContent.age = parseInt(content)
			} else if (tag === 'name') {
				parsedContent.name = content
			} else if (tag === 'born-date') {
				// @ts-expect-error
				parsedContent['born-date'] = content
			} else {
				parsedContent['programming-languages'] = {
					...parsedContent['programming-languages'],
					[tag]: content,
				}
			}
		}

		return parsedContent
	}

	private rewriteContent(content: Content<true>): this {
		const stringifiedContent: string = this.stringifiedContent(content)
		fs.writeFileSync(this.path, stringifiedContent, { encoding: 'utf-8' })
		return this
	}

	private stringifiedContent(
		content: Content<true> | Content<true>['programming-languages'],
		startLineBreak: boolean = false,
		endLineBreak: boolean = false
	): string {
		let stringifiedContent: string = ''

		for (const key of Object.keys(content) as (keyof typeof content)[]) {
			const lineBreak = startLineBreak || stringifiedContent ? '\n' : ''
			const lineBreakEnd = endLineBreak ? '\n' : ''

			const line =
				typeof content[key] === 'object' && !(content[key] instanceof Date)
					? this.stringifiedContent(
							content[key] as Content<true>['programming-languages'],
							true,
							true
					  )
					: content[key]
			stringifiedContent += `${lineBreak}<${key}>${line}</${key}>${lineBreakEnd}`
		}

		return stringifiedContent
	}

	private validate(): never | void {
		if (this.isDeleted) {
			throw new Error('The file was deleted!')
		}
	}

	public appendProgrammingLanguage(programmingLanguage: string): this {
		const content: Content<true> = this.getContent()

		Object.assign<Content<true>, Partial<Content<true>>>(content, {
			'programming-languages': {
				...content['programming-languages'],
				[programmingLanguage.toLowerCase()]: programmingLanguage,
			},
		})
		this.rewriteContent(content)

		return this
	}

	public deleteFile(): void {
		this.validate()

		this.isDeleted = true
		fs.rmSync(this.path)
	}

	public removeProgrammingLanguage(programmingLanguage: string): this {
		const content: Content<true> = this.getContent()
		let sanitizedProgrammingLanguages: Content<true>['programming-languages'] =
			{}

		for (const key of Object.keys(content['programming-languages'])) {
			if (key.toLowerCase() !== programmingLanguage.toLowerCase()) {
				sanitizedProgrammingLanguages = {
					...sanitizedProgrammingLanguages,
					[key]: content['programming-languages'][key],
				}
			}
		}
		content['programming-languages'] = sanitizedProgrammingLanguages
		this.rewriteContent(content)

		return this
	}

	public updateAge(newAge: number): this {
		const content: Content<true> = this.getContent()
		content.age = newAge
		this.rewriteContent(content)
		return this
	}

	public updateName(newName: string): this {
		const content: Content<true> = this.getContent()
		content.name = newName
		this.rewriteContent(content)
		return this
	}

	public updateBornDate(newBornDate: Date): this {
		const content: Content<true> = this.getContent()
		content['born-date'] = newBornDate
		this.rewriteContent(content)
		return this
	}
}

type Operation = Uppercase<
	| 'append language'
	| 'print'
	| 'remove language'
	| 'update age'
	| 'update born date'
	| 'update name'
	| 'exit'
>

const jsonFile: JsonFile = new JsonFile('additional-challenge', {
	age: 22,
	bornDate: new Date(2002, 1, 20),
	name: 'Lucas',
	programmingLanguages: ['TypeScript'],
})

let exit: boolean = false
do {
	const input = readline
		.question(
			"\nWrite an operation ('append language', 'print', 'remove language', 'update age', 'update born date', 'update name', or 'exit'): "
		)
		.trim()
		.toUpperCase() as Operation

	switch (input) {
		case 'APPEND LANGUAGE':
			const newProgrammingLanguage: string = readline.question(
				'\nNew programming language: '
			)
			jsonFile.appendProgrammingLanguage(newProgrammingLanguage)
			break

		case 'PRINT':
			const content: Content = jsonFile.getContent()
			console.log()
			console.table(content)
			break

		case 'REMOVE LANGUAGE':
			const programmingLanguageToDelete: string = readline.question(
				'\nProgramming language to delete: '
			)
			jsonFile.removeProgrammingLanguage(programmingLanguageToDelete)
			break

		case 'UPDATE AGE':
			const newAge: number = parseInt(readline.question('\nNew age: '))
			jsonFile.updateAge(newAge)
			break

		case 'UPDATE BORN DATE':
			const newBornDate: string = readline.question(
				'\nNew born date (year-month-day): '
			)
			jsonFile.updateBornDate(new Date(newBornDate))
			break

		case 'UPDATE NAME':
			const newName: string = readline.question('\nNew name: ')
			jsonFile.updateName(newName)
			break

		case 'EXIT':
			exit = true
			jsonFile.deleteFile()
			break

		default:
			console.log('\nInvalid operation! Try again...')
	}
} while (!exit)

const xmlFile: XmlFile = new XmlFile('additional-challenge', {
	age: 22,
	name: 'Lucas',
	'born-date': new Date(2002, 1, 20),
	'programming-languages': {
		typescript: 'TypeScript',
	},
})

exit = false
do {
	const input = readline
		.question(
			"\nWrite an operation ('append language', 'print', 'remove language', 'update age', 'update born date', 'update name', or 'exit'): "
		)
		.trim()
		.toUpperCase() as Operation

	switch (input) {
		case 'APPEND LANGUAGE':
			const newProgrammingLanguage: string = readline.question(
				'\nNew programming language: '
			)
			xmlFile.appendProgrammingLanguage(newProgrammingLanguage)
			break

		case 'PRINT':
			const content: Content<true> = xmlFile.getContent()
			console.log()
			console.table(content)
			break

		case 'REMOVE LANGUAGE':
			const programmingLanguageToDelete: string = readline.question(
				'\nProgramming language to delete: '
			)
			xmlFile.removeProgrammingLanguage(programmingLanguageToDelete)
			break

		case 'UPDATE AGE':
			const newAge: number = parseInt(readline.question('\nNew age: '))
			xmlFile.updateAge(newAge)
			break

		case 'UPDATE BORN DATE':
			const newBornDate: string = readline.question(
				'\nNew born date (year-month-day): '
			)
			xmlFile.updateBornDate(new Date(newBornDate))
			break

		case 'UPDATE NAME':
			const newName: string = readline.question('\nNew name: ')
			xmlFile.updateName(newName)
			break

		case 'EXIT':
			exit = true
			xmlFile.deleteFile()
			break

		default:
			console.log('\nInvalid operation! Try again...')
	}
} while (!exit)
