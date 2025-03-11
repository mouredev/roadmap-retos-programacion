import readline from 'node:readline/promises'

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

interface IChristmasTree {
    getHeight: () => number
    getTree: () => string

    addBalls: (ball: string) => this
    addLights: (light: string) => this
    addStar: (star: string) => this
    removeBalls: (ball: string) => this
    removeLights: (light: string) => this
    removeStar: (star: string) => this
    turnOffLights: (lightOff: string) => this
    turnOnLights: (lightOn: string) => this
}

interface ChristmasTreeConstructor {
    height: number
}

class ChristmasTree implements IChristmasTree {
    private lightsIndexes: [number, number][]
    private readonly height: number
    private tree: string[]

    public constructor({height}: ChristmasTreeConstructor) {
        let tree: string[] = []

        for (let i = 0; i < height; i++) {
            const branchBlankSpaces = height >= 2 ? ' '.repeat(height - i - 1) : ' '
            tree.push(`${branchBlankSpaces}${'*'.repeat(i * 2 + 1)}`)
        }

        const trunkBlankSpaces: string = height >= 2 ? ' '.repeat(height - 2) : ''
        tree.push(`${trunkBlankSpaces}|||`, `${trunkBlankSpaces}|||`)

        this.height = height
        this.lightsIndexes = []
        this.tree = tree
    }

    public getHeight(): number {
        return this.height
    }

    public getTree(): string {
        return this.tree.join('\n')
    }

    public addBalls(ball: string): this {
        for (let i = 1; i < this.tree.length - 2; i++) {
            const branch: string = this.tree[i]
            let counter: number = 0

            let newBranch: string = ''

            for (let j = 0; j < branch.length; j++) {
                const char = branch[j]
                newBranch += !(counter % 2) && char === '*' ? ball : char
                counter++
            }

            this.tree[i] = newBranch
        }

        return this
    }

    public addLights(ball: string): this {
        for (let i = 1; i < this.tree.length - 2; i++) {
            const branch: string = this.tree[i]
            let counter: number = 0

            let newBranch: string = ''

            for (let j = 0; j < branch.length; j++) {
                const char = branch[j]

                if (counter % 2 && char === '*') {
                    newBranch += ball
                    this.lightsIndexes.push([i, j])
                } else newBranch += char

                counter++
            }

            this.tree[i] = newBranch
        }

        return this
    }

    public addStar(star: string): this {
        this.tree[0] = this.tree[0].replace('*', star)
        return this
    }

    public removeBalls(ball: string): this {
        for (let i = 1; i < this.tree.length - 2; i++) {
            this.tree[i] = this.tree[i].replaceAll(ball, '*')
        }

        return this
    }

    public removeLights(light: string): this {
        while (this.lightsIndexes.length != 0) {
            const [branch, index]: [number, number] = this.lightsIndexes[0]

            let newBranch: string = ''

            for (let j = 0; j < this.tree[branch].length; j++) {
                if (j === index) {
                    newBranch += '*'
                    this.lightsIndexes.splice(0, 1)
                    continue
                }

                newBranch += this.tree[branch][j]
            }

            this.tree[branch] = newBranch
        }

        return this
    }

    public removeStar(star: string): this {
        this.tree[0] = this.tree[0].replace(star, '*')
        return this
    }

    public turnOffLights(lightOff: string): this {
        for (let i = 0; i < this.lightsIndexes.length; i++) {
            const [branch, index]: [number, number] = this.lightsIndexes[i]

            let newBranch: string = ''

            for (let j = 0; j < this.tree[branch].length; j++) {
                newBranch += j === index ? lightOff : this.tree[branch][j]
            }

            this.tree[branch] = newBranch
        }

        return this
    }

    public turnOnLights(lightOn: string): this {
        for (let i = 0; i < this.lightsIndexes.length; i++) {
            const [branch, index]: [number, number] = this.lightsIndexes[i]

            let newBranch: string = ''

            for (let j = 0; j < this.tree[branch].length; j++) {
                newBranch += j === index ? lightOn : this.tree[branch][j]
            }

            this.tree[branch] = newBranch
        }

        return this
    }
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

;(async () => {
    const rl: readline.Interface = readline.createInterface({output: process.stdout, input: process.stdin})

    let input: string = (await rl.question('> Enter the height of the christmas tree: ')).trim()

    const christmasTree: IChristmasTree = new ChristmasTree({height: parseInt(input)})

    console.clear()
    console.log(christmasTree.getTree())

    console.log(
        '\n> Available operations...\n\n' +
            '  1 - Add star.\n' +
            '  2 - Remove star.\n' +
            '  3 - Add balls.\n' +
            '  4 - Remove balls.\n' +
            '  5 - Add lights.\n' +
            '  6 - Remove lights.\n' +
            '  7 - Turn on lights.\n' +
            '  8 - Turn off lights.\n' +
            '  0 - Exit.'
    )

    input = (await rl.question('\n> Enter an operation: ')).trim()

    while (input !== '0') {
        switch (input) {
            case '1':
                christmasTree.addStar('@')

                console.clear()
                console.log(christmasTree.getTree())
                break

            case '2':
                christmasTree.removeStar('@')

                console.clear()
                console.log(christmasTree.getTree())
                break

            case '3':
                christmasTree.addBalls('o')

                console.clear()
                console.log(christmasTree.getTree())
                break

            case '4':
                christmasTree.removeBalls('o')

                console.clear()
                console.log(christmasTree.getTree())
                break

            case '5':
                christmasTree.addLights('+')

                console.clear()
                console.log(christmasTree.getTree())
                break

            case '6':
                christmasTree.removeLights('*')

                console.clear()
                console.log(christmasTree.getTree())
                break

            case '7':
                christmasTree.turnOnLights('+')

                console.clear()
                console.log(christmasTree.getTree())
                break

            case '8':
                christmasTree.turnOffLights('*')

                console.clear()
                console.log(christmasTree.getTree())
                break

            default:
                console.log('\n> Invalid operation! Try again...')
        }

        console.log(
            '\n> Available operations...\n\n' +
                '  1 - Add star.\n' +
                '  2 - Remove star.\n' +
                '  3 - Add balls.\n' +
                '  4 - Remove balls.\n' +
                '  5 - Add lights.\n' +
                '  6 - Remove lights.\n' +
                '  7 - Turn on lights.\n' +
                '  8 - Turn off lights.\n' +
                '  0 - Exit.'
        )

        input = (await rl.question('\n> Enter an operation: ')).trim()
    }

    rl.close()
})()
