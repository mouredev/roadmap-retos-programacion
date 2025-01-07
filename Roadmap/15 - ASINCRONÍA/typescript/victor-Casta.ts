async function myAsyncFunction():Promise<void> {
  console.log('myAsyncFunction')
  console.log('la ejecución de la función tardará 5 segundos')
  const data = await new Promise((resolve) => {
    setTimeout(() => {console.log('Función finalizada')}, 5000)
  })
  console.log(data)
}

myAsyncFunction()

// extra

async function D(): Promise<void> {
  const data = await new Promise((resolve) => setTimeout(() => resolve("D"), 1000))
  console.log(data)
}

async function fetchMultiple(): Promise<void> {
  const [data1, data2, data3] = await Promise.all([
    new Promise((resolve) => setTimeout(() => resolve("A"), 1000)),
    new Promise((resolve) => setTimeout(() => resolve("B"), 2000)),
    new Promise((resolve) => setTimeout(() => resolve("C"), 3000)),
  ])

  console.log(data1)
  console.log(data2)
  console.log(data3)

  await D()
}

fetchMultiple()