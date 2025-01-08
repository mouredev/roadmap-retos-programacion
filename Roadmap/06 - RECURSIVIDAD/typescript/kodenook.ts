
/**
 * The function "recursion" in TypeScript prints numbers from the input number down to 0 using
 * recursion.
 * @param {number} number - The `number` parameter in the `recursion` function is a numeric value that
 * determines how many times the function will recursively call itself. The function will log the value
 * of `number` to the console and then recursively call itself with `number - 1` until `number` is
 * greater than
 */
function recursion(number: number): void {
    console.log(number)
    if (number > 0) {
        recursion(--number)
    }
}

recursion(100)

/*
    Exercise
*/

/**
 * The function calculates the factorial of a given number recursively in TypeScript.
 * @param {number} number - The `number` parameter in the `factorial` function represents the number
 * for which you want to calculate the factorial. It is the input value for which the factorial will be
 * calculated recursively.
 * @param {number} [result=1] - The `result` parameter in the `factorial` function is used to keep
 * track of the intermediate result as the factorial calculation progresses through recursive calls. It
 * is initialized with a default value of 1 when the function is first called. As the function
 * recursively calculates the factorial of a number, the `
 */
function factorial(number: number, result: number = 1): void {

    if (number > 1) {
        factorial(number - 1, number * result)
    } else {
        console.log(result)
    }
}

factorial(5)

/**
 * The function calculates the Fibonacci number at a given position using recursion.
 * @param {number} position - The `position` parameter in the `fibonacci` function represents the
 * position of the Fibonacci number in the sequence that you want to calculate. For example, if
 * `position` is 5, it means you want to find the 5th Fibonacci number in the sequence.
 * @returns the value of the Fibonacci sequence at the specified position.
 */
function fibonacci(position: number): number {
    if (position > 2) {
        return fibonacci(position - 1) + fibonacci(position - 2)
    } else {
        return 1
    }
}

console.log(fibonacci(7))
