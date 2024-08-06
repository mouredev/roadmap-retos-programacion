/*
    Singleton pattern...
*/

console.log('Singleton pattern...')

interface ICounter {
    getCount(): Counter['count']
    decrement(): this
    increment(): this
}

class Counter implements ICounter {
    private static instance: Counter

    private count: number

    private constructor() {
        this.count = 0
    }

    public static getInstance(): Counter {
        if (!Counter.instance) {
            Counter.instance = new Counter()
        }

        return Counter.instance
    }

    public getCount(): number {
        return this.count
    }

    public decrement(): this {
        this.count--
        return this
    }

    public increment(): this {
        this.count++
        return this
    }
}

const counter01: Counter = Counter.getInstance()
const counter02: Counter = Counter.getInstance()

console.log(
    '\nAre `counter01` and `counter02` the same instance of `Counter` class?',
    counter01 === counter02
)

console.log('\nMethod call of `counter01` instance...')

counter01.increment().increment().increment()
console.log('\ncounter01.increment().increment().increment()')

console.log(
    '\nCount attribute of `counter01` instance -->',
    counter01.getCount()
)

console.log('\nMethod call of `counter02` instance...')

counter02.decrement()
console.log('\ncounter02.decrement()')

console.log(
    '\nCount attribute of `counter02` instance -->',
    counter02.getCount()
)

console.log(
    '\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

interface IUserSession {
    getEmail(): UserSession['email']
    getId(): UserSession['id']
    getName(): UserSession['name']
    getUserName(): UserSession['userName']

    setEmail(newEmail: UserSession['email']): this
    setId(newId: UserSession['id']): this
    setName(newName: UserSession['name']): this
    setUserName(newUserName: UserSession['userName']): this

    deleteData(): this
}

interface AUserSession {
    email: string
    id: string
    name: string
    userName: string
}

class UserSession implements IUserSession {
    private static instance: UserSession

    private email: AUserSession['email']
    private id: AUserSession['email']
    private name: AUserSession['email']
    private userName: AUserSession['email']

    private constructor({email, id, name, userName}: AUserSession) {
        this.email = email
        this.id = id
        this.name = name
        this.userName = userName
    }

    public static getInstance(
        {
            email = '',
            id = '',
            name = '',
            userName = '',
        }: Partial<AUserSession> = {
            email: '',
            id: '',
            name: '',
            userName: '',
        }
    ): UserSession {
        if (!UserSession.instance) {
            UserSession.instance = new UserSession({
                email,
                id,
                name,
                userName,
            })
        }

        return UserSession.instance
    }

    public getEmail(): AUserSession['email'] {
        return this.email
    }

    public getId(): AUserSession['id'] {
        return this.id
    }

    public getName(): AUserSession['name'] {
        return this.name
    }

    public getUserName(): AUserSession['userName'] {
        return this.userName
    }

    public setEmail(newEmail: AUserSession['email']): this {
        this.email = newEmail
        return this
    }

    public setId(newId: AUserSession['id']): this {
        this.id = newId
        return this
    }

    public setName(newName: AUserSession['name']): this {
        this.name = newName
        return this
    }

    public setUserName(newUserName: AUserSession['userName']): this {
        this.userName = newUserName
        return this
    }

    public deleteData(): this {
        this.email = ''
        this.id = ''
        this.name = ''
        this.userName = ''

        return this
    }
}

const userSession: UserSession = UserSession.getInstance({
    email: 'gomezjuan69@gmail.com',
    id: '155-AV25-12Z',
    name: 'Juan',
    userName: 'Juanceto01',
})

console.log(
    '\nUser:',
    userSession.getId(),
    userSession.getName(),
    userSession.getUserName(),
    userSession.getEmail()
)

userSession.deleteData()
console.log('\nUser data deleted!')

console.log(
    '\nUser:',
    userSession.getId(),
    userSession.getName(),
    userSession.getUserName(),
    userSession.getEmail()
)
