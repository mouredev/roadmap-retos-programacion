class BasicMath {
  sumar(a, b){
    return a + b
  }

  restar(a, b){
    return a - b
  }

  multiplicar(a, b){
    return a * b
  }

  dividir(a, b){
    if (b === 0) {
      throw new Error('Division by zero is not allowed')
    }
    return a / b
  }
}

const mathDecorator = (fun) => {
  return function(...args){
    console.log(`Llamando a la funcion ${fun.name} con argumentos`, args)
    return fun.apply(this, args)
  }
}

BasicMath.prototype.sumar = mathDecorator(BasicMath.prototype.sumar)
BasicMath.prototype.restar = mathDecorator(BasicMath.prototype.restar)
BasicMath.prototype.multiplicar = mathDecorator(BasicMath.prototype.multiplicar)
BasicMath.prototype.dividir = mathDecorator(BasicMath.prototype.dividir)

const test = new BasicMath()

console.log(test.sumar(2, 3))
console.log(test.restar(5, 3))
console.log(test.multiplicar(4, 3)) 
console.log(test.dividir(10, 2)) 