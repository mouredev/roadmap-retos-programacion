//EJERCICIO
interface Person {
	name: string
	age: number
}

interface Programer {
	languages: string[]
}

class Programer implements Person, Programer {
	name: string
	age: number

	constructor(name: string, age: number, languages: string[]) {
		this.name = name
		this.age = age
		this.languages = languages
	}

	sayHi(): void {
		console.log(`Hi, my name is ${this.name}`)
	}
}

let Sebas = new Programer('Sebastian', 23, ['Java', 'Python', 'C++'])

Sebas.sayHi()
