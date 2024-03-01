
/**
 * The function "recursion" recursively logs numbers starting from the input number until reaching 0.
 * @param number - The `recursion` function takes a parameter `number`, which is used to control the
 * recursion. The function will log the value of `number` and then recursively call itself with
 * `number` decremented by 1, until `number` is no longer greater than 0.
 */
function recursion(number) {
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
 * The factorial function calculates the factorial of a given number recursively.
 * @param number - The `number` parameter in the `factorial` function represents the integer for which
 * you want to calculate the factorial. It is the input value for which the factorial will be computed.
 * @param [result=1] - The `result` parameter in the `factorial` function is used to keep track of the
 * intermediate result as the factorial calculation progresses through recursive calls. It starts with
 * a default value of 1 and gets updated with the multiplication of `number` and the current `result`
 * in each recursive call.
 */
function factorial(number, result = 1) {

    if (number > 1) {
        factorial(number - 1, number * result)
    } else {
        console.log(result)
    }
}

factorial(5)

/**
 * The function calculates the Fibonacci number at a given position using recursion.
 * @param position - The `position` parameter in the `fibonacci` function represents the position of
 * the Fibonacci number in the sequence that you want to calculate. For example, if `position` is 5,
 * the function will return the 5th Fibonacci number in the sequence.
 * @returns the value of the Fibonacci sequence at the specified position.
 */
function fibonacci(position) {
    if (position > 2) {
        return fibonacci(position - 1) + fibonacci(position - 2)
    } else {
        return 1
    }
}

console.log(fibonacci(7))
