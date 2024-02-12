// no arguments, no return
function sayHello() {
  console.log("Hello. This function doesn't has parameter and return")
}

// argument and return
function square(number: number) {
  return number * number;
}

// Nested functions
function getScore(name: String, num1: number, num2: number) {
  function add(name: String, num1: number, num2: number) {
    return name + " scored  " + (num1 + num2);
  }
  console.log(add(name, num1, num2))
}

// Function printing
sayHello()
console.log("This function has a parameter and return: " + square(2))
getScore("Sniker", 20, 20)
console.log("Console.log() is an example of a function")

let varGlobal = 0
// Challenge
function printTheChallenge(text1: String, text2: String) {
  for (let i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      console.log(text1.concat(text2.toString()))
    } else if (i % 3 == 0) {
      console.log(text1)
    } else if (i % 5 == 0) {
      console.log(text2)
    } else {
      console.log(i)
      varGlobal += 1
    }
  }
  return varGlobal
}

console.log("Number of times the number has been printed:", printTheChallenge("Star", "Wars"))