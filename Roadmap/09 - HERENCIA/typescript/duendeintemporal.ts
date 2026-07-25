/* #09 { retosparaprogramadores } HERENCIA Y POLIMORFISMO */
// bibliography
//Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
//GPT

/* In JavaScript, inheritance is a mechanism that allows one object to acquire the properties and methods of another object. This is typically achieved through prototypes, where an object can inherit from another object's prototype, enabling code reuse and the creation of hierarchical relationships between objects. JavaScript supports both classical inheritance (using constructor functions and the `prototype` property) and modern inheritance (using `class` syntax introduced in ES6).
All objects have an internal property called [[Prototype]], which is a reference to another object. This prototype chain allows for inheritance, where an object can access properties and methods from its prototype.
When you create an object using a constructor function, you can set its prototype using the prototype property. 
With the introduction of ES6, JavaScript introduced class syntax, which is essentially syntactic sugar over the existing prototype-based inheritance. When you define a class, JavaScript still uses prototypes behind the scenes*/

// short for console.log()
const log = console.log;

    log('Retosparaprogramadores #9'); // Retosparaprogramadores #9 

interface IAnimal {
    name: string;
    sound: string;
    type: string;
    speak(): void;
}

class Animal implements IAnimal {
    protected _name: string;
    protected _sound: string;
    protected _type: string;

    constructor(name: string, sound: string, type: string) {
        this._name = name || 'set no name';
        this._sound = sound || 'set no sound';
        this._type = type || 'set no type';
    }

    get name(): string {
        return this._name;
    }

    get sound(): string {
        return this._sound;
    }

    get type(): string {
        return this._type;
    }

    set name(name: string) {
        this._name = name;
    }

    speak(): void {
        log(`${this.name} the ${this._type} say: ${this._sound}!`);
    }
}

interface IPet extends IAnimal {
    eat(meal: string): void;
    move(): void;
}

class Dog extends Animal implements IPet {
    constructor(name: string, sound: string, type: string) {
        super(name, sound, type);
    }

    eat(meal: string): void {
        log(`${this._name} the ${this._type} eat some: ${meal}`);
    }

    move(): void {
        log(`the ${this._type} moves it's tail`);
    }
}

const capDog = new Dog('Capitan', 'I guau some pizza', 'Dog');
capDog.speak(); // Capitan the Dog say: I guau some pizza!
capDog.eat('pizza'); // Capitan the Dog eat some: pizza
capDog.move(); // the Dog moves it's tail

class Cat extends Animal implements IPet {
    constructor(name: string, sound: string, type: string) {
        super(name, sound, type);
    }

    eat(meal: string): void {
        log(`${this._name} the ${this._type} eat some: ${meal}`);
    }

    move(): void {
        log(`the ${this._type} hunt the rat`);
    }
}

const blackJack = new Cat('BlackJack', 'Miuauuuu', 'Cat');
blackJack.speak(); // BlackJack the Cat say: Miuauuuu!
blackJack.eat('rat snack'); // BlackJack the Cat eat some: rat snack
blackJack.move(); // the Cat hunt the rat

//Note: is interesting know that we can use variables like key-value assign to object properties, this also work with functions, see:

interface IPerson {
    name: string;
    age: number;
    email: string;
    personJob?: string;
}

const makePerson = (name: string, age: number, email: string): IPerson => {
    return { name, age, email };
};
const person = makePerson('Angy', 28, 'badgirl@greenhouse.net');
log(person); // { name: "Angy", age: 28, email: "badgirl@greenhouse.net" }

//using destructuring
let {name: personName, age: personAge, email: personEmail, personJob = 'Web Developer'} = person;
log(personAge); // 28
log(personJob)// Web Developer


interface IUser {
    id: string;
    name: string;
    email: string;
    country: string;
    userData(): IUserData;
}

interface IUserData {
    id: string;
    name: string;
    email: string;
    country: string;
}

class User implements IUser {
    protected _id: string;
    protected _name: string;
    protected _email: string;
    protected _country: string;

    constructor(id: string, name: string, email: string, country: string) {
        try {
            this._id = this.setId(id);
            this._name = this.setName(name);
            this._email = this.setEmail(email);
            this._country = this.setCountry(country);
            this.validateProperties();
        } catch (error) {
            console.error('Error creating User:', (error as Error).message);
            throw error;
        }
    }

    get id() {
        return this._id;
    }

    get name() {
        return this._name;
    }

    get email() {
        return this._email;
    }

    get country() {
        return this._country;
    }

    set id(id: string) {
        this._id = this.setId(id);
    }

    set name(name: string) {
        this._name = this.setName(name);
    }

    set email(email: string) {
        this._email = this.setEmail(email);
    }

    set country(country: string) {
        this._country = this.setCountry(country);
    }

    protected setId(id: string): string {
        const idString = String(id);
        const maxLength = 15;

        if (idString.length > maxLength) {
            throw new Error(`ID must be at most ${maxLength} characters long.`);
        }

        return idString;
    }

    protected setName(name: string): string {
        const nameString = String(name);
        const maxLength = 35;

        if (nameString.length > maxLength) {
            throw new Error(`Name must be at most ${maxLength} characters long.`);
        }

        return nameString;
    }

    protected setEmail(email: string): string {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$/;

        if (!emailRegex.test(email)) {
            throw new Error('Invalid email address format.');
        }

        return email;
    }

    protected setCountry(country: string): string {
        const countryString = String(country);
        const maxLength = 35;

        if (countryString.length > maxLength) {
            throw new Error(`Country must be at most ${maxLength} characters long.`);
        }

        return countryString;
    }

    validateProperties() {
        if (!this._id || !this._name || !this._email || !this._country) {
            throw new Error('All properties must be set before freezing the object.');
        }
    }

    userData(): IUserData {
        return {
            id: this._id,
            name: this._name,
            email: this._email,
            country: this._country
        };
    }
}


try {
    let sussy = new User('0067', 'Sussan', 'sussy45@something.dt', 'Canada');
    console.log(sussy.userData()); // { id: "0067", name: "Sussan", email: "sussy45@something.dt", country: "Canada" }
} catch (error: unknown) {
    if (error instanceof Error) {
        console.error('Failed to create user:', error.message);
    }
}

//Note: if we use a number to set the value for id 0067 becomes 55 cause is turned to a decimal value 

interface ISuperUser extends IUser {
    hasPermission(): boolean;
    displayUserInfo(): string;
}

class SuperUser extends User implements ISuperUser {
    private _permission: boolean;

    constructor(id: string, name: string, email: string, country: string) {
        super(id, name, email, country);
        this._permission = true;
    }

    hasPermission(): boolean {
        return this._permission;
    }

    displayUserInfo(): string {
        const userInfo = this.userData();
        return `${userInfo.name} has permission: ${this.hasPermission()}`;
    }
}

const niko = new SuperUser('001', 'Niko', 'duendeintemporal@hotmail.com', 'Venezuela');
niko.country = 'undefined'; 
log(niko.id); // 001
log(niko.country); // undefined
log(niko.hasPermission()); // true
log(niko.userData()); // { id: "001", name: "Niko", email: "duendeintemporal@hotmail.com", country: "undefined" }

// Extra Exercises


interface IEmployed {
    id: string;
    name: string;
    occupation: string;
    employedData(): IEmployedData;
}

interface IEmployedData {
    id: string;
    name: string;
    occupation: string;
}

class Employed implements IEmployed {
    protected _id: string;
    protected _name: string;
    protected _occupation: string;

    constructor(id: string, name: string, occupation: string) {
        try {
            this._id = this.setId(id);
            this._name = this.setName(name);
            this._occupation = this.setOccupation(occupation);
            this.validateProperties();
        } catch (error) {
            console.error('Error creating Employed:', (error as Error).message);
            throw error;
        }
    }

    get id() {
        return this._id;
    }

    get name() {
        return this._name;
    }

    get occupation() {
        return this._occupation;
    }

    set id(id: string) {
        this._id = this.setId(id);
    }

    set name(name: string) {
        this._name = this.setName(name);
    }

    set occupation(occupation: string) {
        this._occupation = this.setOccupation(occupation);
    }

    protected setId(id: string): string {
        const idString = String(id);
        const maxLength = 15;

        if (idString.length > maxLength) {
            throw new Error(`ID must be at most ${maxLength} characters long.`);
        }

        return idString;
    }

    protected setName(name: string): string {
        const nameString = String(name);
        const maxLength = 35;

        if (nameString.length > maxLength) {
            throw new Error(`Name must be at most ${maxLength} characters long.`);
        }

        return nameString;
    }

    protected setOccupation(occupation: string): string {
        const occupationStr = String(occupation);
        const maxLength = 50;

        if (occupationStr.length > maxLength) {
            throw new Error(`Occupation must be at most ${maxLength} characters long.`);
        }

        return occupationStr;
    }

    validateProperties() {
        if (!this._id || !this._name || !this._occupation) {
            throw new Error('All properties must be set before freezing the object.');
        }
    }

    employedData(): IEmployedData {
        return {
            id: this._id,
            name: this._name,
            occupation: this._occupation
        };
    }
}

interface IDeveloper extends IEmployed {
    functions(): void;
}

class Developer extends Employed implements IDeveloper {
    private _languages: string[];
    private _area: string;

    constructor(id: string, name: string, occupation: string, languages: string[], area: string) {
        super(id, name, occupation);
        this._languages = languages;
        this._area = area;
    }

    functions(): void {
        log(`Developer ID: ${this._id} | Name: ${this._name} | Occupation: ${this._occupation} | Area: ${this._area} | Languages: ${this._languages.join(', ')}`);
    }
}

class Secretary extends Employed {
    constructor(id: string, name: string, occupation: string) {
        super(id, name, occupation);
    }

    functions(): void {
        log(`Secretary ID: ${this._id} | Name: ${this._name} | Occupation: ${this._occupation} | Responsibilities: Administrative operations and user attention.`);
    }
}

class Manager extends Employed {
    protected _employeds: string[];

    constructor(id: string, name: string, occupation: string, employeds: string[]) {
        super(id, name, occupation);
        this._employeds = employeds;
    }

    functions(): void {
        log(`Manager ID: ${this._id} | Name: ${this._name} | Occupation: ${this._occupation} | Supervising Employees: ${this._employeds.join(', ')}`);
    }
}

class GeneralManager extends Manager {
    constructor(id: string, name: string, occupation: string, employeds: string[]) {
        super(id, name, occupation, employeds);
    }

    functions(): void {
        log(`General Manager ID: ${this._id} | Name: ${this._name} | Occupation: ${this._occupation} | Supervising Employees: ${this._employeds.join(', ')}`);
    }
}

const s1 = new Secretary('0023', 'Gabriela Mistral', 'Secretary');
const d12 = new Developer('0041', 'Niko Zen', 'Web Developer', ['Python', 'JavaScript', 'Rust', 'Ruby', 'Bash'], 'Frontend');
const m3 = new Manager('0098', 'Patty Smith', 'Manager', [s1.name, d12.name]);
const mg2 = new GeneralManager('003', 'Lenny Kravitz', 'General Manager', [m3.name]);

log(s1.employedData()); // id: "0023", name: "Gabriela Mistral", occupation: "Secretary"
log(d12.functions()); // Developer ID: 0041 | Name: Niko Zen | Occupation: Web Developer | Area: Frontend | Languages: Python, JavaScript, Rust, Ruby, Bash
log(m3.functions()); // Manager ID: 0098 | Name: Patty Smith | Occupation: Manager | Supervising Employees: Gabriela Mistral, Niko Zen
log(mg2.functions()); // General Manager ID: 003 | Name: Lenny Kravitz | Occupation: General Manager | Supervising Employees: Patty Smith

