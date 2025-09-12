/*
    Inheritance...
*/

type Feeding = 'carnivorous' | 'herbivorous' | 'omnivores'

type AnimalAttributes = {
	averageSpeed: number
	averageWeight: number
	feeding: Feeding
	name: string
	sound: string
}

class Animal {
	protected _averageSpeed: number
	protected _averageWeight: number
	protected _feeding: Feeding
	protected _name: string
	protected _sound: string

	constructor({ averageSpeed, averageWeight, feeding, name, sound }: AnimalAttributes) {
		this._averageSpeed = averageSpeed
		this._averageWeight = averageWeight
		this._feeding = feeding
		this._name = name
		this._sound = sound
	}

	public set averageSpeed(averageSpeed) {
		this._averageSpeed = averageSpeed
	}

	public set averageWeight(averageWeight) {
		this._averageWeight = averageWeight
	}

	public set feeding(feeding) {
		this._feeding = feeding
	}

	public set name(name) {
		this.name = name
	}

	public set sound(sound) {
		this.sound = sound
	}

	public get averageSpeed() {
		return this._averageSpeed
	}

	public get averageWeight() {
		return this._averageWeight
	}

	public get feeding() {
		return this._feeding
	}

	public get name() {
		return this.name
	}

	public get sound() {
		return this.sound
	}

	public getAttributes(): AnimalAttributes {
		return {
			averageSpeed: this._averageSpeed,
			averageWeight: this._averageWeight,
			feeding: this._feeding,
			name: this._name,
			sound: this._sound,
		}
	}

	public printAttributes() {
		console.table(this.getAttributes())
		return this
	}

	public printSound() {
		console.log(`\n${this._sound}`)
		return this
	}
}

interface DogAttributes extends AnimalAttributes {
	ownerName: string
	ownerPhone: string
}

class Dog extends Animal {
	private _ownerName: string
	private _ownerPhone: string

	constructor({ ownerName, ownerPhone, ...fatherProps }: DogAttributes) {
		super(fatherProps)
		this._ownerName = ownerName
		this._ownerPhone = ownerPhone
	}

	public set ownerName(ownerName) {
		this._ownerName = ownerName
	}

	public set ownerPhone(ownerPhone) {
		this._ownerPhone = ownerPhone
	}

	public get ownerName() {
		return this._ownerName
	}

	public get ownerPhone() {
		return this._ownerPhone
	}

	public getAttributes(): DogAttributes {
		return {
			...super.getAttributes(),
			ownerName: this._ownerName,
			ownerPhone: this._ownerPhone,
		}
	}
}

interface CatAttributes extends DogAttributes {}

class Cat extends Dog {
	constructor({ ...fatherProps }: CatAttributes) {
		super(fatherProps)
	}
}

console.log('Inheritance in TypeScript...')

console.log(`\ntype Feeding = 'carnivorous' | 'herbivorous' | 'omnivores'

type AnimalAttributes = {
    averageSpeed: number
    averageWeight: number
    feeding: Feeding
    name: string
    sound: string
}

class Animal {
    protected _averageSpeed: number
    protected _averageWeight: number
    protected _feeding: Feeding
    protected _name: string
    protected _sound: string

    constructor({ averageSpeed, averageWeight, feeding, name, sound }: AnimalAttributes) {
        this._averageSpeed = averageSpeed
        this._averageWeight = averageWeight
        this._feeding = feeding
        this._name = name
        this._sound = sound
    }

    public set averageSpeed(averageSpeed) {
        this._averageSpeed = averageSpeed
    }

    public set averageWeight(averageWeight) {
        this._averageWeight = averageWeight
    }

    public set feeding(feeding) {
        this._feeding = feeding
    }

    public set name(name) {
        this.name = name
    }

    public set sound(sound) {
        this.sound = sound
    }

    public get averageSpeed() {
        return this._averageSpeed
    }

    public get averageWeight() {
        return this._averageWeight
    }

    public get feeding() {
        return this._feeding
    }

    public get name() {
        return this.name
    }

    public get sound() {
        return this.sound
    }

    public getAttributes(): AnimalAttributes {
        return {
            averageSpeed: this._averageSpeed,
            averageWeight: this._averageWeight,
            feeding: this._feeding,
            name: this._name,
            sound: this._sound,
        }
    }

    public printAttributes() {
        console.table(this.getAttributes())
        return this
    }

    public printSound() {
        console.log(\`\\n\${this._sound}\`)
        return this
    }
}

interface DogAttributes extends AnimalAttributes {
    ownerName: string
    ownerPhone: string
}

class Dog extends Animal {
    private _ownerName: string
    private _ownerPhone: string

    constructor({ ownerName, ownerPhone, ...fatherProps }: DogAttributes) {
        super(fatherProps)
        this._ownerName = ownerName
        this._ownerPhone = ownerPhone
    }

    public set ownerName(ownerName) {
        this._ownerName = ownerName
    }

    public set ownerPhone(ownerPhone) {
        this._ownerPhone = ownerPhone
    }

    public get ownerName() {
        return this._ownerName
    }

    public get ownerPhone() {
        return this._ownerPhone
    }

    public getAttributes(): DogAttributes {
        return {
            ...super.getAttributes(),
            ownerName: this._ownerName,
            ownerPhone: this._ownerPhone,
        }
    }
}

interface CatAttributes extends DogAttributes {}

class Cat extends Dog {
    constructor({ ...fatherProps }: CatAttributes) {
        super(fatherProps)
    }
}`)

console.log(`\nconst dog = new Dog({
    averageSpeed: 48,
    averageWeight: 80,
    feeding: 'carnivorous',
    name: 'Chop',
    ownerName: 'Lucas Hoz',
    ownerPhone: '1158946872',
    sound: 'Woof',
})

console.log('\\nDog attributes...')
dog.printAttributes()`)

const dog = new Dog({
	averageSpeed: 48,
	averageWeight: 80,
	feeding: 'carnivorous',
	name: 'Chop',
	ownerName: 'Lucas Hoz',
	ownerPhone: '1158946872',
	sound: 'Woof',
})

console.log('\nDog attributes...')
dog.printAttributes()

console.log(`\nconst cat = new Cat({
    averageSpeed: 38,
    averageWeight: 5,
    feeding: 'carnivorous',
    name: 'Fifi',
    ownerName: 'Nahuel Gonzales',
    ownerPhone: '1145982657',
    sound: 'Meow',
})

console.log('\\nCat attributes...')
cat.printAttributes()`)

const cat = new Cat({
	averageSpeed: 38,
	averageWeight: 5,
	feeding: 'carnivorous',
	name: 'Fifi',
	ownerName: 'Nahuel Gonzales',
	ownerPhone: '1145982657',
	sound: 'Meow',
})

console.log('\nCat attributes...')
cat.printAttributes()

console.log('\n# ---------------------------------------------------------------------------------- #\n')

/*
    Additional challenge...
*/

console.log('Additional challenge...')

type Gender = 'F' | 'M' | 'N/A'

interface PersonAttributes {
	firstName: string
	lastName: string
	phoneNumber: string
	age: number
	gender: Gender
}

class Person {
	private _age: number
	private _firstName: string
	private _gender: Gender
	private _lastName: string
	private _phoneNumber: string

	constructor({ age, firstName, gender, lastName, phoneNumber }: PersonAttributes) {
		this._age = age
		this._firstName = firstName
		this._gender = gender
		this._lastName = lastName
		this._phoneNumber = phoneNumber
	}

	public set age(age) {
		this._age = age
	}

	public set firstName(firstName) {
		this._firstName = firstName
	}

	public set gender(gender) {
		this._gender = gender
	}

	public set lastName(lastName) {
		this._lastName = lastName
	}

	public set phoneNumber(phoneNumber) {
		this._phoneNumber = phoneNumber
	}

	public get age() {
		return this._age
	}

	public get firstName() {
		return this._firstName
	}

	public get gender() {
		return this._gender
	}

	public get lastName() {
		return this._lastName
	}

	public get phoneNumber() {
		return this._phoneNumber
	}

	public getAttributes(): PersonAttributes {
		return {
			age: this._age,
			firstName: this._firstName,
			gender: this._gender,
			lastName: this._lastName,
			phoneNumber: this._phoneNumber,
		}
	}
}

type Role = 'Manager' | 'Project manager' | 'Programmer'

interface EmployeeAttributes extends PersonAttributes {
	id: number
	role: Role
	salary: number
}

class Employee extends Person {
	private _id: number
	private _role: Role
	private _salary: number

	constructor({ id, role, salary, ...fatherProps }: EmployeeAttributes) {
		super(fatherProps)
		this._id = id
		this._role = role
		this._salary = salary
	}

	public set id(id) {
		this._id = id
	}

	public set role(role) {
		this._role = role
	}

	public set salary(salary) {
		this._salary = salary
	}

	public get id() {
		return this._id
	}

	public get role() {
		return this._role
	}

	public get salary() {
		return this._salary
	}

	public getAttributes(): EmployeeAttributes {
		return {
			...super.getAttributes(),
			id: this._id,
			role: this._role,
			salary: this._salary,
		}
	}
}

interface ManagerAttributes extends EmployeeAttributes {
	functions: string[]
	projectManagers: ProjectManager[]
}

class Manager extends Employee {
	private _functions: string[]
	private _projectManagers: ProjectManager[]

	constructor({ functions, projectManagers, ...fatherProps }: ManagerAttributes) {
		super(fatherProps)
		this._functions = functions
		this._projectManagers = projectManagers
	}

	public set functions(functions) {
		this._functions = functions
	}

	public set projectManagers(projectManagers) {
		this._projectManagers = projectManagers
	}

	public get functions() {
		return this._functions
	}

	public get projectManagers() {
		return this._projectManagers
	}

	public getAttributes(): ManagerAttributes {
		return {
			...super.getAttributes(),
			functions: this._functions,
			projectManagers: this._projectManagers,
		}
	}

	public makeManagement(): string {
		return 'Just a manager doing management things.'
	}
}

interface ProjectManagerAttributes extends EmployeeAttributes {
	completedProjects: number
	functions: string[]
	programmers: Programmer<string[]>[]
	projects: string[]
}

class ProjectManager extends Employee {
	private _completedProjects: number
	private _functions: string[]
	private _programmers: Programmer<string[]>[]
	private _projects: string[]

	constructor({ completedProjects, functions, programmers, projects, ...fatherProps }: ProjectManagerAttributes) {
		super(fatherProps)
		this._completedProjects = completedProjects
		this._functions = functions
		this._programmers = programmers
		this._projects = projects
	}

	public set completedProjects(completedProjects) {
		this._completedProjects = completedProjects
	}

	public set functions(functions) {
		this._functions = functions
	}

	public set programmers(programmers) {
		this._programmers = programmers
	}

	public set projects(projects) {
		this._projects = projects
	}

	public get completedProjects() {
		return this._completedProjects
	}

	public get functions() {
		return this._functions
	}

	public get programmers() {
		return this._programmers
	}

	public get projects() {
		return this._projects
	}

	public getAttributes(): ProjectManagerAttributes {
		return {
			...super.getAttributes(),
			completedProjects: this._completedProjects,
			functions: this._functions,
			programmers: this._programmers,
			projects: this._projects,
		}
	}

	public makeManagement(): string {
		return 'Just a project manager doing everything expect programming.'
	}
}

type Side = 'Backend' | 'Frontend' | 'Full Stack'

interface ProgrammerAttributes<T extends string[]> extends EmployeeAttributes {
	languages: T
	side: Side
}

class Programmer<T extends string[]> extends Employee {
	private _languages: T
	private _side: Side
	private _yearsOfExperience: number

	constructor({ languages, side, ...fatherProps }: ProgrammerAttributes<T>) {
		super(fatherProps)
		this._languages = languages
		this._side = side
	}

	public set languages(languages) {
		this._languages = languages
	}

	public set side(side) {
		this._side = side
	}

	public get languages() {
		return this._languages
	}

	public get side() {
		return this._side
	}

	public getAttributes(): ProgrammerAttributes<T> {
		return {
			...super.getAttributes(),
			languages: this._languages,
			side: this._side,
		}
	}

	public writeCode(language: T[number]): string {
		return `Writing code in ${language}`
	}
}

const programmer = new Programmer({
	age: 22,
	firstName: 'Lucas',
	gender: 'M',
	id: 0,
	languages: ['JavaScript', 'TypeScript', 'Golang', 'Python'] as const,
	lastName: 'Hoz',
	phoneNumber: '1158746859',
	role: 'Programmer',
	salary: 2100,
	side: 'Frontend',
})

console.log('\nProgrammer attributes...')
console.table(programmer.getAttributes())

console.log('\nProgrammer methods...')
console.log(`programmer.writeCode('TypeScript') --> ${programmer.writeCode('TypeScript')}`)

const projectManager = new ProjectManager({
	age: 32,
	completedProjects: 17,
	firstName: 'Juan',
	functions: ['Time management'],
	gender: 'M',
	id: 1,
	lastName: 'Gonzales',
	phoneNumber: '1157486558',
	programmers: [programmer],
	projects: ['Mercado Stories', 'Carrefour Delivery'],
	role: 'Project manager',
	salary: 3000,
})

console.log('\nProject manager attributes...')
console.table(projectManager.getAttributes())

console.log('\nProject manager methods...')
console.log(`projectManager.makeManagement() --> ${projectManager.makeManagement()}`)
console.log(`projectManager.programmers[0].writeCode() --> ${projectManager.programmers[0].writeCode('TypeScript')}`)

const manager = new Manager({
	age: 45,
	firstName: 'Maria',
	functions: ['Financial management', 'Time management', 'General administration'],
	gender: 'F',
	id: 3,
	lastName: 'Nuñez',
	phoneNumber: '1124585669',
	projectManagers: [projectManager],
	role: 'Manager',
	salary: 4500,
})

console.log('\nManager attributes...')
console.table(manager.getAttributes())

console.log('\nManager methods...')
console.log(`manager.makeManagement() --> ${manager.makeManagement()}`)
console.log(`manager.projectManagers[0].makeManagement() --> ${manager.projectManagers[0].makeManagement()}`)
