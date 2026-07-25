/* #09 HERENCIA Y POLIMORFISMO */
// bibliography
//Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
//GTT

/* In JavaScript, inheritance is a mechanism that allows one object to acquire the properties and methods of another object. This is typically achieved through prototypes, where an object can inherit from another object's prototype, enabling code reuse and the creation of hierarchical relationships between objects. JavaScript supports both classical inheritance (using constructor functions and the `prototype` property) and modern inheritance (using `class` syntax introduced in ES6).
All objects have an internal property called [[Prototype]], which is a reference to another object. This prototype chain allows for inheritance, where an object can access properties and methods from its prototype.
When you create an object using a constructor function, you can set its prototype using the prototype property. 
With the introduction of ES6, JavaScript introduced class syntax, which is essentially syntactic sugar over the existing prototype-based inheritance. When you define a class, JavaScript still uses prototypes behind the scenes*/

// short for console.log()
let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #9.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #9. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #9'); 
});


class Animal{
    constructor(name, sound, type){
        this._name = name || 'set no name';
        this._sound = sound || 'set no sound';
        this._type = type || 'set no type';
    }

    get name(){
        return this._name; 
    }

    set name(name){
        this._name = name;
    }

    speak(){
        log(`${this.name} the ${this._type} say: ${this._sound}!`)
    }
}

class Dog extends Animal{
    constructor(name, sound, type){
      super(name, sound, type);
    }

    eat(meal){
        log(`${this._name} the ${this._type} eat some: ${meal}`)
    }

    move(){
        log(`the ${this._type} moves it's tail`)
    }
}

const capDog = new Dog('Capitan', 'I guau some pizza', 'Dog');
capDog.speak(); // Capitan the Dog say: I guau some pizza!
capDog.eat('pizza'); // Capitan the Dog eat some: pizza
capDog.move(); // the Dog moves it's tail

class Cat extends Animal{
    constructor(name, sound, type){
        super(name, sound, type);
    }

    eat(meal){
        log(`${this._name} the ${this._type} eat some: ${meal}`)
    }

    move(){
        log(`the ${this._type} hunt the rat`)
    }

}

const blackJack = new Cat('BlackJack', 'Miuauuuu', 'Cat');
blackJack.speak(); // BlackJack the Cat say: Miuauuuu!
blackJack.eat('rat snack'); // BlackJack the Cat eat some: rat snack
blackJack.move(); // the Cat hunt the rat

//Note: is interesting know that we can use variables like key-value assign to object properties, this also work with functions, see:

const makePerson = (name, age, email)=> {
    return { name, age, email };
}
const person = makePerson('Angy', 28, 'badgirl@greenhouse.net');
log(person); // { name: "Angy", age: 28, email: "badgirl@greenhouse.net" }

//using destructuring
let {name: personName, age: personAge, email: personEmail, personJob = 'Web Developer'} = person;
log(personAge); // 28
log(personJob)// Web Developer


class User {
    constructor(id, name, email, country) {
        try {
            this._id = this.setId(id);
            this._name = this.setName(name);
            this._email = this.setEmail(email);
            this._country = this.setCountry(country);
            this.validateProperties(); // Validate properties before freezing or sealing
            //Object.seal(this); // Seal the object to prevent further properties deletions
        } catch (error) {
            console.error('Error creating User:', error.message);
            // Handle the error as needed (e.g., set default values, rethrow, etc.)
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

    set id(id) {
        this._id = this.setId(id);
    }

    set name(name) {
        this._name = this.setName(name);
    }

    set email(email) {
        this._email = this.setEmail(email);
    }

    set country(country) {
        this._country = this.setCountry(country);
    }

    setId(id) {
        const idString = String(id);
        const maxLength = 15;

        if (idString.length > maxLength) {
            throw new Error(`ID must be at most ${maxLength} characters long.`);
        }

        return idString;
    }

    setName(name) {
        const nameString = String(name);
        const maxLength = 35;

        if (nameString.length > maxLength) {
            throw new Error(`Name must be at most ${maxLength} characters long.`);
        }

        return nameString;
    }

    setEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$/;

        if (!emailRegex.test(email)) {
            throw new Error('Invalid email address format.');
        }

        return email;
    }

    setCountry(country) {
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

    userData() {
        return { id: this._id, name: this._name, email: this._email, country: this._country };
    }
}


try {
    let sussy = new User('0067', 'Sussan', 'sussy45@something.dt', 'Canada');
    console.log(sussy.userData());
} catch (error) {
    console.error('Failed to create user:', error.message);
}

//Note: if we use a number to set the value for id 0067 becomes 55 cause is turned to a decimal value 

class SuperUser extends User{
    constructor(id, name, email, country){
        super(id, name, email, country);
        this.permission = true;
    }

        hasPermission() {
            return this.permission;
        }
    
        displayUserInfo() {
            const userInfo = this.userData();
            return `${userInfo.name} has permission: ${this.hasPermission()}`;
        }
}

const niko = new SuperUser('001', 'Niko', 'duendeintemporal@hotmail.com', 'Venezuela');
niko.country = 'undefined'; 
log(niko._id); // 001
log(niko.country) // undefined
log(niko.permission); // true
log(niko.userData()); // { id: "001", name: "Niko", email: "duendeintemporal@hotmail.com", country: "undefined" }

// Extra Exercises


class Employed {
    constructor(id, name, occupation) {
        try {
            this._id = this.setId(id);
            this._name = this.setName(name);
            this._occupation = this.setOccupation(occupation);
            this.validateProperties();
        } catch (error) {
            console.error('Error creating Employed:', error.message);
            // Handle the error as needed (e.g., set default values, rethrow, etc.)
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

    set id(id) {
        this._id = this.setId(id);
    }

    set name(name) {
        this._name = this.setName(name);
    }

    set occupation(occupation) {
        this._occupation = this.setOccupation(occupation);
    }

    setId(id) {
        const idString = String(id);
        const maxLength = 15;

        if (idString.length > maxLength) {
            throw new Error(`ID must be at most ${maxLength} characters long.`);
        }

        return idString;
    }

    setName(name) {
        const nameString = String(name);
        const maxLength = 35;

        if (nameString.length > maxLength) {
            throw new Error(`Name must be at most ${maxLength} characters long.`);
        }

        return nameString;
    }

    setOccupation(occupation) {
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

    employedData() {
        return { id: this._id, name: this._name, occupation: this._occupation };
    }
}

class Developer extends Employed {
    constructor(id, name, occupation, languages, area) {
        super(id, name, occupation);
        this._languages = languages;
        this._area = area;
    }

    functions() {
        log(`Developer ID: ${this._id} | Name: ${this._name} | Occupation: ${this._occupation} | Area: ${this._area} | Languages: ${this._languages.join(', ')}`);
    }
}

class Secretary extends Employed {
    constructor(id, name, occupation) {
        super(id, name, occupation);
    }

    functions() {
        log(`Secretary ID: ${this._id} | Name: ${this._name} | Occupation: ${this._occupation} | Responsibilities: Administrative operations and user attention.`);
    }
}

class Manager extends Employed {
    constructor(id, name, occupation, employeds) {
        super(id, name, occupation);
        this._employeds = employeds; // Expecting an array of employees
    }

    functions() {
        log(`Manager ID: ${this._id} | Name: ${this._name} | Occupation: ${this._occupation} | Supervising Employees: ${this._employeds.join(', ')}`);
    }
}

class GeneralManager extends Manager{
    constructor(id, name, ocupation, employeds){
        super(id, name, ocupation, employeds);
    }

    functions() {
        log(`General Manager ID: ${this._id} | Name: ${this._name} | Occupation: ${this._occupation} | Supervising Employees: ${this._employeds.join(', ')}`);
    }
}

const s1 = new Secretary('0023', 'Gabriela Mistral', 'Secretary');
const d12 = new Developer('0041', 'Niko Zen', 'Web Developer', ['Python, ','JavaScript', 'Rust', 'Ruby', 'Bash']);
const m3 = new Manager('0098', 'Patty Smith', 'Manager', [s1.name, d12.name]);
const mg2 = new GeneralManager('003', 'Lenny Kravitz', 'General Manager', [m3.name]);

log(s1.employedData()); // id: "0023", name: "Gabriela Mistral", occupation: "Secretary"
log(d12.functions()); // Developer ID: 0041 | Name: Niko Zen | Occupation: Web Developer | Area: undefined | Languages: Python, , JavaScript, Rust, Ruby, Bash
log(m3.functions()); // Manager ID: 0098 | Name: Patty Smith | Occupation: Manager | Supervising Employees: Gabriela Mistral, Niko Ze
log(mg2.functions()); // General Manager ID: 003 | Name: Lenny Kravitz | Occupation: General Manager | Supervising Employees: Patty Smith
