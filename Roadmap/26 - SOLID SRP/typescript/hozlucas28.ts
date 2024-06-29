/*
    Single Responsibility Principle (SRP)...
*/

console.log('Single Responsibility Principle (SRP)...')

console.log('\nBad implementation of Single Responsibility Principle (SRP)...')

interface User {
    email: string
    firstName: string
    lastName: string
}

interface IBadUser extends User {
    saveUser(): this
}

class BadUser implements IBadUser {
    email: string
    firstName: string
    lastName: string

    constructor({email, firstName, lastName}: User) {
        this.email = email
        this.firstName = firstName
        this.lastName = lastName
    }

    saveUser(): this {
        console.log('User saved!')
        return this
    }
}

console.log(`\n\`\`\`\ninterface User {
    email: string
    firstName: string
    lastName: string
}

interface IBadUser extends User {
    saveUser(): this
}

class BadUser implements IBadUser {
    email: string
    firstName: string
    lastName: string

    constructor({email, firstName, lastName}: User) {
        this.email = email
        this.firstName = firstName
        this.lastName = lastName
    }

    saveUser(): this {
        console.log('User saved!')
        return this
    }
}\n\`\`\``)

console.log(
    '\nThis is a bad implementation of Single Responsibility Principle (SRP), \n' +
        'because the class "BadUser" has two responsibilities:\n\n' +
        '1°) User creation.\n' +
        '2°) Data persistence of the user.'
)

console.log('\nGood implementation of Single Responsibility Principle (SRP)...')

interface IGoodUser extends User {}

class GoodUser implements IGoodUser {
    email: string
    firstName: string
    lastName: string

    constructor({email, firstName, lastName}: User) {
        this.email = email
        this.firstName = firstName
        this.lastName = lastName
    }
}

interface IGoodUserDatabase {
    user: GoodUser
    saveUser(): this
}

class GoodUserDatabase implements IGoodUserDatabase {
    user: GoodUser

    constructor(user: GoodUser) {
        this.user = user
    }

    saveUser(): this {
        console.log('User saved!')
        return this
    }
}

console.log(`\n\`\`\`\ninterface IGoodUser extends User {}

class GoodUser implements IGoodUser {
    email: string
    firstName: string
    lastName: string

    constructor({email, firstName, lastName}: User) {
        this.email = email
        this.firstName = firstName
        this.lastName = lastName
    }
}

interface IGoodUserDatabase {
    user: GoodUser
    saveUser(): this
}

class GoodUserDatabase implements IGoodUserDatabase {
    user: GoodUser

    constructor(user: GoodUser) {
        this.user = user
    }

    saveUser(): this {
        console.log('User saved!')
        return this
    }
}\n\`\`\``)

console.log(
    '\nThis is a good implementation of Single Responsibility Principle (SRP), \n' +
        'because the class "GoodUser" has only one responsability and \n' +
        'the class "GoodUserDatabase" too.'
)
