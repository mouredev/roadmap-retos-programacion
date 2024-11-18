function recursiva(num) {    
  if (num >= 0) {
      console.log(num)      
      recursiva(--num)
  } else {      
      return 0
  }
}

recursiva(10)

function factorial(num) {    
    return (num === 1) ? 1 : num * factorial(num - 1)    
}

console.log(factorial(6))

function fibonacci(posicion) {
    if (posicion === 0) return 0
    else if (posicion === 1) return 1
    else return fibonacci(posicion - 1) + fibonacci(posicion - 2)   
}

console.log(fibonacci(8))

