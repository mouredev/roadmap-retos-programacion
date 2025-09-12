const pages = ['youtube', 'facebook', 'github', 'instagram', 'google']

function web(navegation) {
  console.log(`Actualmente estas en - ${pages[0]} -`)
  if (navegation == 'atras') {
    pages.unshift(pages[pages.length - 1])
    pages.pop()
  } else if (navegation == 'adelante') {
    pages.push(pages[0])
    pages.shift()
  } else if (navegation != '') {
    pages.push(navegation)
  }
  console.log(`Actualmente estas en - ${pages[0]} -`)
}

const docs = []

function imprimir(action) {
  if (action == 'imprimir' && docs.length == 0)
    console.log('No hay documentos para imprimir')
  if (action == 'imprimir') {
    while (docs.length > 0) {
      console.log('imprimiendo...' + docs.shift())
    }
  } else {
    docs.unshift(action)
    console.log('Your Documents: ' + docs)
  }
}

imprimir('doc - 1')
imprimir('doc - 2')
imprimir('doc - 3')
imprimir('imprimir')
imprimir('doc - 4')
