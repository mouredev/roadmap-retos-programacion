/**
 * Demostración de diferentes mecanismos de iteración en TypeScript
 * 
 * TypeScript extiende JavaScript añadiendo tipos estáticos y algunas
 * características adicionales, lo que nos permite escribir código
 * más robusto y mantenible.
 */

// Configuración inicial para algunos ejemplos
const numbers: number[] = Array.from({length: 10}, (_, i) => i + 1);

class IterationDemo {
    private static printNumbers(numbers: number[]): void {
        console.log(numbers.join(' '));
    }

    // 1. Bucle for tradicional
    static forLoop(): void {
        console.log("1. Usando bucle for tradicional:");
        const result: number[] = [];
        for (let i: number = 1; i <= 10; i++) {
            result.push(i);
        }
        this.printNumbers(result);
    }

    // 2. Bucle while
    static whileLoop(): void {
        console.log("\n2. Usando bucle while:");
        const result: number[] = [];
        let count: number = 1;
        while (count <= 10) {
            result.push(count);
            count++;
        }
        this.printNumbers(result);
    }

    // 3. Bucle do...while
    static doWhileLoop(): void {
        console.log("\n3. Usando bucle do...while:");
        const result: number[] = [];
        let num: number = 1;
        do {
            result.push(num);
            num++;
        } while (num <= 10);
        this.printNumbers(result);
    }

    // 4. forEach con array
    static forEachLoop(): void {
        console.log("\n4. Usando forEach con array:");
        const result: number[] = [];
        numbers.forEach((num: number): void => {
            result.push(num);
        });
        this.printNumbers(result);
    }

    // 5. for...of loop
    static forOfLoop(): void {
        console.log("\n5. Usando for...of:");
        const result: number[] = [];
        for (const num of numbers) {
            result.push(num);
        }
        this.printNumbers(result);
    }

    // 6. Array.map
    static arrayMap(): void {
        console.log("\n6. Usando Array.map:");
        const result: number[] = Array.from({length: 10}).map((_, i: number): number => i + 1);
        this.printNumbers(result);
    }

    // 7. Recursión con tipo de retorno explícito
    static recursion(n: number = 1, result: number[] = []): number[] {
        if (n <= 10) {
            result.push(n);
            return this.recursion(n + 1, result);
        }
        return result;
    }

    static showRecursion(): void {
        console.log("\n7. Usando recursión:");
        const result: number[] = this.recursion();
        this.printNumbers(result);
    }

    // 8. Generator function con tipo Generator
    static *numberGenerator(): Generator<number, void, unknown> {
        for (let i: number = 1; i <= 10; i++) {
            yield i;
        }
    }

    static showGenerator(): void {
        console.log("\n8. Usando Generator function:");
        const result: number[] = [...this.numberGenerator()];
        this.printNumbers(result);
    }

    // 9. Implementación de Iterable
    static iterableExample(): void {
        console.log("\n9. Usando implementación de Iterable:");
        
        class NumberRange implements Iterable<number> {
            constructor(private start: number, private end: number) {}

            *[Symbol.iterator](): Iterator<number> {
                for (let i: number = this.start; i <= this.end; i++) {
                    yield i;
                }
            }
        }

        const numberRange = new NumberRange(1, 10);
        const result: number[] = [...numberRange];
        this.printNumbers(result);
    }

    // 10. Reduce con tipos explícitos
    static reduceExample(): void {
        console.log("\n10. Usando Reduce:");
        const result: number[] = numbers.reduce((acc: number[], curr: number): number[] => {
            acc.push(curr);
            return acc;
        }, []);
        this.printNumbers(result);
    }
}

// Ejecutar todas las demostraciones
console.log("=== Demostración de Mecanismos de Iteración en TypeScript ===\n");

IterationDemo.forLoop();
IterationDemo.whileLoop();
IterationDemo.doWhileLoop();
IterationDemo.forEachLoop();
IterationDemo.forOfLoop();
IterationDemo.arrayMap();
IterationDemo.showRecursion();
IterationDemo.showGenerator();
IterationDemo.iterableExample();
IterationDemo.reduceExample();

console.log("\n=== Fin de la demostración ===");

// Ejemplo de uso con tipos genéricos
interface IterableCollection<T> {
    forEach(callback: (item: T) => void): void;
}

class NumberCollection implements IterableCollection<number> {
    constructor(private numbers: number[]) {}

    forEach(callback: (item: number) => void): void {
        for (const num of this.numbers) {
            callback(num);
        }
    }
}

// Bonus: Demostración de uso de la interfaz genérica
console.log("\nBonus: Usando interfaz genérica IterableCollection:");
const collection = new NumberCollection(numbers);
const result: number[] = [];
collection.forEach((num: number): void => {
    result.push(num);
});
console.log(result.join(' '));