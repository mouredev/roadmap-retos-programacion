/*
    Estructuras...
*/

// Array
const arr: string[] = ['Hello', 'World']
console.log('Array structure: const <ARRAY NAME>: <DATA TYPE>[] = [<ELEMENTS...>]')
console.log(`const arr: string[] = ['Hello', 'World'] --> arr = [${arr}]`)

// Tuple
const tuple: [string, number] = ['Lucas', 21]
console.log("\nTuple structure: const <TUPLE NAME>: [<DATA TYPE OF 'N' ELEMENT...>] = [<ELEMENTS...>]")
console.log(`const tuple: [string, number] = ['Lucas', 21] --> tuple = [${tuple}]`)

// Object
const obj: Record<string, string> = {
	apple: 'Manzana',
	banana: 'Banana',
	orange: 'Naranja',
}

console.log(
	'\nObject structure: const <OBJECT NAME>: Record<<DATA TYPE OF KEYS>, <DATA TYPE OF VALUES>> = {<PROPERTIES...>}'
)
console.table(obj)

// Enum
enum MyCustomEnum {
	firstName = 'Lucas',
	lastName = 'Hoz',
}
console.log('\nEnum structure: enum <ENUM NAME> {<ELEMENTS...>}')
console.table({
	firstName: MyCustomEnum.firstName,
	lastName: MyCustomEnum.lastName,
})

console.log('\n# ---------------------------------------------------------------------------------- #')

/*
    Insert, delete, update, and sort operations
*/

let array: number[] = []
let object: Record<string, string> = {}

// Insert element/s at the end of an array structure
array.push(1, 2, 3, 4, 5, 6, 7, 8)
console.log('\nInsert element/s at the end of an array structure: <ARRAY NAME>.push(<ELEMENTS...>)')
console.log(`[].push(1, 2, 3, 4, 5, 6, 7, 8) --> array = [${array}]`)

// Insert element/s at the beginning of an array structure
array.unshift(-2, -1, 0)
console.log('\nInsert element/s at the beginning of an array structure: <ARRAY NAME>.unshift(<ELEMENTS...>)')
console.log(`[1, 2, 3, 4, 5, 6, 7, 8].unshift(-2, -1 , 0) --> array = [${array}]`)

// Delete an element of an array structure
array = array.filter((_, index) => index !== 4)
console.log(
	'\nDelete an element of an array structure: <ARRAY NAME> = <ARRAY NAME>.filter((_, index) => index !== <INDEX OF THE ELEMENT TO DELETE>)'
)
console.log(
	`[-2, -1 , 0, 1, 2, 3, 4, 5, 6, 7, 8] = [-2, -1 , 0, 1, 2, 3, 4, 5, 6, 7, 8].filter((_, index) => index !== 4) --> array = [${array}]`
)

// Delete the first element of an array structure
array.shift()
console.log('\nDelete the first element of an array structure: <ARRAY NAME>.shift()')
console.log(`[-2, -1 , 0, 1, 3, 4, 5, 6, 7, 8].shift() --> array = [${array}]`)

// Delete the last element of an array structure
array.pop()
console.log('\nDelete the last element of an array structure: <ARRAY NAME>.pop()')
console.log(`[-1, 0, 1, 3, 4, 5, 6, 7, 8].pop() --> array = [${array}]`)

// Update an element of an array structure
array[6] = 6 * 2
console.log('\nUpdate an element of an array structure: <ARRAY NAME>[<INDEX OF THE ELEMENT TO UPDATE>] = <NEW VALUE>')
console.log(`[-1, 0, 1, 3, 4, 5, 6, 7][6] = 6 * 2 --> array = [${array}]`)

// Sort an array structure
array.sort((a, b) => a - b)
console.log('\nSort an array structure: <ARRAY NAME>.sort(<SORT FUNCTION>)')
console.log(`[-1, 0, 1, 3, 4, 5, 12, 7].sort((a, b) => a - b) --> array = [${array}]`)

// Insert property/ies into an object structure
object = {
	...object,
	first: '1°',
	second: '2°',
	third: '3°',
}
console.log('\nInsert property/ies into an object structure: <OBJECT NAME> = {...<OBJECT NAME>, <PROPERTIES...>}')
console.log(`{} = {
	...{},
	first: '1°',
	second: '2°',
	third: '3°',
} --> object = {${Object.entries(object)}}`)

// Delete a property of an object structure
delete object['second']
console.log("\nDelete a property of an object structure: delete <OBJECT NAME>['<KEY OF THE PROPERTY TO DELETE>'])")
console.log(`delete {first: '1°', second: '2°', third: '3°'}['second'] --> object = {${Object.entries(object)}}}`)

// Update a property of an object structure
object['first'] = 'First place'
console.log("\nUpdate a property of an object structure: <OBJECT NAME>['KEY OF THE PROPERTY TO UPDATE'] = <NEW VALUE>")
console.log(`{first: '1°', third: '3°'}['first'] = 'First place' --> object = {${Object.entries(object)}}}`)

console.log('\n# ---------------------------------------------------------------------------------- #')

/*
    Additional challenge...
*/

type Contact = {
	name: string
	phoneNumber: string
}

type Operation = 'FIND' | 'INSERT' | 'UPDATE' | 'DELETE' | 'EXIT'

const contacts: Contact[] = []

const getContactInfo = (name: string): Contact | undefined =>
	contacts.find((value) => value.name.toUpperCase() === name.toUpperCase())

const getContactName = (msg: string, msgOnInvalid: string, shouldExist: boolean): string | null => {
	let name = prompt(msg)
	if (!name) return null

	const contactInfo = getContactInfo(name)
	const condition = shouldExist ? contactInfo === undefined : contactInfo !== undefined
	while (condition) {
		name = prompt(msgOnInvalid)
		if (!name) break
	}

	return name
}

const getContactPhoneNumber = (msg: string, msgOnInvalid: string): string | null => {
	let phoneNumber = prompt(msg)
	if (!phoneNumber) return null

	while (!isValidPhoneNumber(phoneNumber)) {
		phoneNumber = prompt(msgOnInvalid)
		if (!phoneNumber) break
	}

	return phoneNumber
}

const isValidPhoneNumber = (phoneNumber: string): boolean =>
	phoneNumber.length <= 11 && (phoneNumber.match(/[^0-9]/g) ?? []).length === 0

let exit = false
while (!exit) {
	const operation = (
		prompt("Select an operation ('Find', 'Insert', 'Update', 'Delete' or 'Exit'):") ?? ''
	).toUpperCase() as Operation

	switch (operation) {
		case 'FIND':
			const contactName = getContactName(
				'Enter the name of the contact:',
				"The contact doesn't exists! Enter another name:",
				true
			)
			if (!contactName) continue

			const contactInfo = getContactInfo(contactName)
			console.log(`Contact info: ${contactInfo?.name} / ${contactInfo?.phoneNumber}`)
			break

		case 'INSERT':
			const newContactName = getContactName(
				'Enter the name of the new contact:',
				'The contact already exists! Try with another name:',
				false
			)
			if (!newContactName) continue

			let newContactPhoneNumber = getContactPhoneNumber(
				'Enter the phone number of new contact:',
				'Invalid phone number! Enter a valid one:'
			)
			if (!newContactPhoneNumber) continue

			contacts.push({
				name: newContactName,
				phoneNumber: newContactPhoneNumber,
			})

			console.log('Contact inserted!')
			break

		case 'UPDATE':
			const contactNameToUpdate = getContactName(
				'Enter the name of the contact to update:',
				"The contact doesn't exists! Enter another name:",
				true
			)
			if (!contactNameToUpdate) continue

			const newName = getContactName('Enter the new name:', 'There is a contact with this name! Try another one:', false)
			if (!newName) continue

			const newPhoneNumber = getContactPhoneNumber('Enter the new phone number:', 'Invalid phone number! Enter a valid one:')
			if (!newPhoneNumber) continue

			const contactToUpdate = contacts.findIndex((value) => value.name.toUpperCase() === contactNameToUpdate.toUpperCase())
			contacts[contactToUpdate] = {
				name: newName,
				phoneNumber: newPhoneNumber,
			}

			console.log('Contact updated!')

			break

		case 'DELETE':
			const contactNameToDelete = getContactName(
				'Enter the name of the contact to delete:',
				"The contact doesn't exists! Enter another name:",
				true
			)
			if (!contactNameToDelete) continue

			const contactToDelete = contacts.findIndex((value) => value.name.toUpperCase() === contactNameToDelete.toUpperCase())
			contacts.splice(contactToDelete, 1)

			console.log('Contact deleted!')
			break

		case 'EXIT':
			console.log('Program finished!')
			exit = true
			break

		default:
			break
	}
}
