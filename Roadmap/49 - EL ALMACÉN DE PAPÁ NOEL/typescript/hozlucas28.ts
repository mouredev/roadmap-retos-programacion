import readline from 'node:readline/promises'

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

interface IPasswordGenerator {
    getAdvice: (password: string) => string
    getFailAttempts: () => number
    getMaximumLength: () => number
    isThePassword: (password: string) => boolean
}

interface PasswordGeneratorConstructor {
    hash: string
    maximumLength: number
}

class PasswordGenerator implements IPasswordGenerator {
    private failAttempts: number
    private readonly hash: string
    private readonly maximumLength: number
    private readonly password: string

    public constructor({hash, maximumLength}: PasswordGeneratorConstructor) {
        this.failAttempts = 0
        this.hash = hash
        this.maximumLength = maximumLength

        let password: string = ''
        while (password.length < maximumLength) {
            const rndChar = hash[Math.floor(Math.random() * hash.length)]
            if (!password.includes(rndChar)) password += rndChar
        }

        this.password = password
    }

    public getAdvice(password: string): string {
        let advice: string[] = []

        console.log(this.password)

        for (let i = 0; i < password.length; i++) {
            const char = password[i]
            const rPasswordChar = this.password[i]

            if (char === rPasswordChar) {
                advice.push(`  - "${char}" is in the correct position.`)
                continue
            }

            if (this.password.includes(char)) {
                advice.push(`  - "${char}" exist but it's not in the ${i + 1}th position.`)
                continue
            }

            advice.push(`  - "${char}" not exist in the password.`)
        }

        return advice.join('\n')
    }

    public getFailAttempts(): number {
        return this.failAttempts
    }

    public getMaximumLength(): number {
        return this.maximumLength
    }

    public isThePassword(password: string): boolean {
        if (this.password === password) return true

        this.failAttempts++
        return false
    }
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

;(async () => {
    const hash: string = 'ABC123'
    const maximumLength: number = 4

    const passwordGenerator: IPasswordGenerator = new PasswordGenerator({
        hash,
        maximumLength,
    })

    const rl: readline.Interface = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    })

    const regex: RegExp = new RegExp(`^[${hash}]{${maximumLength}}$`)
    const formatter: Intl.ListFormat = new Intl.ListFormat('en', {style: 'long', type: 'disjunction'})

    let userInput: string = (await rl.question('> Enter the password (maximum of 4 chars): ')).trim()

    while (!regex.test(userInput)) {
        console.log(
            `\n> Error! The password length must be less than 4 characters, and it should contain ${formatter.format(
                hash
            )}. Try again...`
        )
        userInput = (await rl.question('\n> Enter the password (maximum of 4 chars): ')).trim()
    }

    while (passwordGenerator.getFailAttempts() < 10) {
        console.log(`\n${passwordGenerator.getAdvice(userInput)}`)

        console.log('\n> Invalid password! Try again...')

        userInput = (await rl.question('\n> Enter the password (maximum of 4 chars): ')).trim()

        while (!regex.test(userInput)) {
            console.log(
                `\n> Error! The password length must be less than 4 characters, and it should contain ${formatter.format(
                    hash
                )}. Try again...`
            )
            userInput = (await rl.question('\n> Enter the password (maximum of 4 chars): ')).trim()
        }

        if (passwordGenerator.isThePassword(userInput)) break
    }

    passwordGenerator.getFailAttempts() < 10
        ? console.log(`\n> Santa won! The password is "${userInput}".`)
        : console.log('\n> Santa lost! Storage will be closed forever.')

    rl.close()
})()
