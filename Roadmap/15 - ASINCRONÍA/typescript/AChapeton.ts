const asyncFunction: (name: string, seconds: number) => Promise<void> = async (name: string, seconds: number) => {
  console.log(`Inicia la ejecucion de ${name}`)
  console.log(`Duracion de ${name}: ${seconds} segundos`)
  
  await new Promise<void>(res => {
    setTimeout(res, seconds * 1000)
  })

  console.log(`Finaliza la ejecuncion de ${name}`)
}

const main: () => Promise<void> = async () => {
  const promise1: Promise<void> = asyncFunction('Funcion 1', 5)
  const promise2: Promise<void> = asyncFunction('Funcion 2', 3)

  await Promise.all([promise1, promise2])
}

main()


// DIFICULTAD EXTRA

const funcionC: () => Promise<void> = async () => {
  console.log(`Inicia la ejecucion de la funcion C`)
  
  await new Promise<void>(res => {
    setTimeout(res, 3000)
  })

  console.log(`Finaliza la ejecucion de la funcion C luego de 3 segundos`)
}

const funcionB: () => Promise<void> = async () => {
  console.log(`Inicia la ejecucion de la funcion B`)
  
  await new Promise<void>(res => {
    setTimeout(res, 2000)
  })

  console.log(`Finaliza la ejecucion de la funcion B luego de 2 segundos`)
}

const funcionA: () => Promise<void> = async () => {
  console.log(`Inicia la ejecucion de la funcion A`)
  
  await new Promise<void>(res => {
    setTimeout(res, 1000)
  })

  console.log(`Finaliza la ejecucion de la funcion A luego de 1 segundo`)
}

const funcionD: () => Promise<void> = async () => {
  console.log(`Inicia la ejecucion de la funcion D`)
  
  await new Promise<void>(res => {
    setTimeout(res, 1000)
  })

  console.log(`Finaliza la ejecucion de la funcion D luego de 1 segundo`)
}

const mainFunction: () => Promise<void>  = async () => {
  const respuestaC: Promise<void> = funcionC()
  const respuestaB: Promise<void> = funcionB()
  const respuestaA: Promise<void> = funcionA()

  await Promise.all([respuestaC, respuestaB, respuestaA])

  const respuestaD: void = await funcionD()
}

mainFunction()