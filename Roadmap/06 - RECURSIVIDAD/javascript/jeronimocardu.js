/** RECURSIVIDAD */
function showNumber(number) {
  if (number >= 0) {
    console.log(number)
    showNumber(number - 1)
  }
}
showNumber(5)

/** FACTORIAL */
function getFactorial(number) {
  if (number < 0) {
    console.log('The negative numbers are invalid')
    return 0
  }
  if (number == 0) return 1
  return number * getFactorial(number - 1)
}
console.log(getFactorial(5))

/** FIBONACCI  */
function getFibonacci(number) {
  if (number == 0) return 0
  if (number == 1) return 1
  return getFibonacci(number - 1) + getFibonacci(number - 2)
}
console.log(getFibonacci(7))
