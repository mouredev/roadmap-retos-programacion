const asyncFunction = async (name, seconds) => {
  console.log(`Inicia la ejecucion de ${name}`)
  console.log(`Duracion de ${name}: ${seconds} segundos`)
  
  await new Promise(res => {
    setTimeout(res, seconds * 1000)
  })

  console.log(`Finaliza la ejecuncion de ${name}`)
}

const main = async () => {
  const promise1 = asyncFunction('Funcion 1', 5)
  const promise2 = asyncFunction('Funcion 2', 3)

  await Promise.all([promise1, promise2])
}

main()


// DIFICULTAD EXTRA

const funcionC = async () => {
  console.log(`Inicia la ejecucion de la funcion C`)
  
  await new Promise(res => {
    setTimeout(res, 3000)
  })

  console.log(`Finaliza la ejecucion de la funcion C luego de 3 segundos`)
}

const funcionB = async () => {
  console.log(`Inicia la ejecucion de la funcion B`)
  
  await new Promise(res => {
    setTimeout(res, 2000)
  })

  console.log(`Finaliza la ejecucion de la funcion B luego de 2 segundos`)
}

const funcionA = async () => {
  console.log(`Inicia la ejecucion de la funcion A`)
  
  await new Promise(res => {
    setTimeout(res, 1000)
  })

  console.log(`Finaliza la ejecucion de la funcion A luego de 1 segundo`)
}

const funcionD = async () => {
  console.log(`Inicia la ejecucion de la funcion D`)
  
  await new Promise(res => {
    setTimeout(res, 1000)
  })

  console.log(`Finaliza la ejecucion de la funcion D luego de 1 segundo`)
}

const mainFunction = async () => {
  const respuestaC = funcionC()
  const respuestaB = funcionB()
  const respuestaA = funcionA()

  await Promise.all([respuestaC, respuestaB, respuestaA])

  const respuestaD = await funcionD()
}

mainFunction()