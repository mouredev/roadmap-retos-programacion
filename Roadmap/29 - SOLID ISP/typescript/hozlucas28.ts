/*
    Interface Segregation Principle (ISP)...
*/

console.log('Interface Segregation Principle (ISP)...')

interface IBadAnimal {
    fly: () => void
    run: () => void
    swim: () => void
}

class BadDog implements IBadAnimal {
    fly(): void {
        throw new Error('A dog can not fly')
    }

    run(): void {
        console.log('The dog is running!')
    }

    swim(): void {
        console.log('The dog is swimming!')
    }
}

class BadDuck implements IBadAnimal {
    fly(): void {
        console.log('The duck is flying!')
    }

    run(): void {
        console.log('The duck is running!')
    }

    swim(): void {
        console.log('The duck is swimming!')
    }
}

console.log('\nBad implementation of Interface Segregation Principle (ISP)...')

console.log(`\n\`\`\`\ninterface IBadAnimal {
    fly: () => void
    run: () => void
    swim: () => void
}

class BadDog implements IBadAnimal {
    fly(): void {
        throw new Error('A dog can not fly')
    }

    run(): void {
        console.log('The dog is running!')
    }

    swim(): void {
        console.log('The dog is swimming!')
    }
}

class BadDuck implements IBadAnimal {
    fly(): void {
        console.log('The duck is flying!')
    }

    run(): void {
        console.log('The duck is running!')
    }

    swim(): void {
        console.log('The duck is swimming!')
    }
}\n\`\`\``)

console.log(
    '\nThis is a bad implementation of Interface Segregation Principle (ISP),\n' +
        'because the "BadDog" class should not implement an interface with methods\n' +
        'that it is going to never use. So, the implemented interface ("IBadAnimal")\n' +
        'is to general for the "BadDog" class, but perfect for the "BadDuck" class.'
)

console.log('\nGood implementation of Interface Segregation Principle (ISP)...')

interface IAerialAnimal {
    fly: () => void
}

interface IAquaticAnimal {
    swim: () => void
}

interface ITerrestrialAnimal {
    run: () => void
}

class GoodDog implements ITerrestrialAnimal, IAquaticAnimal {
    run(): void {
        console.log('The dog is running!')
    }

    swim(): void {
        console.log('The dog is swimming!')
    }
}

class GoodDuck implements IAerialAnimal, IAquaticAnimal, ITerrestrialAnimal {
    fly(): void {
        console.log('The duck is flying!')
    }

    run(): void {
        console.log('The duck is running!')
    }

    swim(): void {
        console.log('The duck is swimming!')
    }
}

console.log(`\n\`\`\`\ninterface IAerialAnimal {
    fly: () => void
}

interface IAquaticAnimal {
    swim: () => void
}

interface ITerrestrialAnimal {
    run: () => void
}

class GoodDog implements ITerrestrialAnimal, IAquaticAnimal {
    run(): void {
        console.log('The dog is running!')
    }

    swim(): void {
        console.log('The dog is swimming!')
    }
}

class GoodDuck implements IAerialAnimal, IAquaticAnimal, ITerrestrialAnimal {
    fly(): void {
        console.log('The duck is flying!')
    }

    run(): void {
        console.log('The duck is running!')
    }

    swim(): void {
        console.log('The duck is swimming!')
    }
}\n\`\`\``)

console.log(
    '\nThis is a good implementation of Interface Segregation Principle (ISP),\n' +
        'because the "GoodDog" class only implements the necessary methods, without\n' +
        'any extras. Also, the "GoodDuck" class utilizes an interface perfectly suited\n' +
        'to its needs, with no extra methods.'
)

console.log(
    '\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

interface IBlackAndWhitePrinter {
    print: () => void
}

class BlackAndWhitePrinter implements IBlackAndWhitePrinter {
    constructor() {}

    print(): void {
        console.log('Paper printed in black and white!')
    }
}

interface IColorPrinter {
    print: () => void
}

class ColorPrinter implements IColorPrinter {
    constructor() {}

    print(): void {
        console.log('Paper printed in color!')
    }
}

interface IMultifunctionalPrinter extends IBlackAndWhitePrinter, IColorPrinter {
    scan: () => void
    sendFax: () => void
}

class MultifunctionalPrinter implements IMultifunctionalPrinter {
    constructor() {}

    print(): void {
        console.log('Paper printed!')
    }

    scan(): void {
        console.log('Scan completed!')
    }

    sendFax(): void {
        console.log('Fax sent!')
    }
}

const blackAndWhitePrinter: BlackAndWhitePrinter = new BlackAndWhitePrinter()
const colorPrinter: ColorPrinter = new ColorPrinter()
const multifunctionalPrinter: MultifunctionalPrinter =
    new MultifunctionalPrinter()

console.log()
blackAndWhitePrinter.print()

console.log()
colorPrinter.print()

console.log()
multifunctionalPrinter.print()

console.log()
multifunctionalPrinter.scan()

console.log()
multifunctionalPrinter.sendFax()
