function esperar2segundos(resolve) {
  console.log('esperar2segundos, la funcón tardara en ejecutarse 2 segundos')
  return new Promise(() => {
    setTimeout(() => {
      console.log('esperar2segundos: He finalizado mi ejecución')
      resolve()
    }, 2000)
  })
}

async function asincrona() {
  await esperar2segundos()
}

asincrona()

// ------------------------------------ DIFICULTAD EXTRA ------------------------------------
function C() {
  console.log('La función "C" ha empezado su ejecución')
  return new Promise(resolve => {
    setTimeout(() => {
      resolve()
      console.log('La función "C" ha finalizado su ejecución')
    }, 3000)
  })
}

function B() {
  console.log('La función "B" ha empezado su ejecución')
  return new Promise(resolve => {
    setTimeout(() => {
      resolve()
      console.log('La función "B" ha finalizado su ejecución')
    }, 2000)
  })
}

function A() {
  console.log('La función "A" ha empezado su ejecución')
  return new Promise(resolve => {
    setTimeout(() => {
      resolve()
      console.log('La función "A" ha finalizado su ejecución')
    }, 1000)
  })
}

function D() {
  console.log('La función "D" ha empezado su ejecución')
  return new Promise(resolve => {
    setTimeout(() => {
      resolve()
      console.log('La función "D" ha finalizado su ejecución')
    }, 1000)
  })
}

async function program() {
  await Promise.all([C(),B(),A()])
  await D()
}

program()