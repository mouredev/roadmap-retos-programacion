const recursiveFunction = (value: number): void => {
  console.log(value)
  if(value === 0){
    return
  }
  else{
    recursiveFunction(value - 1)
  }
}

recursiveFunction(100)

const obtenerFactorial = (factorial: number): number => {
  if(factorial < 0){
    return -1
  }else if (factorial === 0){
    return 1
  }else {
    return (factorial * obtenerFactorial(factorial - 1))
  }
}

console.log('factorial: ', obtenerFactorial(10))

const fibonacci = (position: number): number => {
  if(position <= 1) return 1
  const result = fibonacci(position - 1) + fibonacci(position - 2)
  return result
}

console.log('fibonacci: ', fibonacci(5))
