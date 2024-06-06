const radios: Array<number> = [1, 2, 3]

const calcularArea = (radio: number) => {
  return Math.PI * (radio ** 2)
}

const calcularDiametro = (radio: number) => {
  return 2 * radio
}

const calcular = (radios: Array<number>, funcion) => {
  const resultados: Array<number> = []
  for (let i: number = 0; i < radios.length; i++){
    resultados.push(funcion(radios[i]))
  }
  return resultados
}

console.log('Areas: ', calcular(radios, calcularArea))
console.log('Diametros: ', calcular(radios, calcularDiametro))