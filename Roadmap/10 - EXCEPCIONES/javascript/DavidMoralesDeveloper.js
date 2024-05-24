//TryChach

try {
    noexitefuncion()
} catch (error) {
    console.log(`${error} estamos en chatch`)
}finally{
    console.log('Declare primero la funcion')
  }

//   console.log('ola k ace , si me ejecuto despues de el error')

//   extra 
// creando error
class customError extends Error {
constructor(message){
    super(message)
    this.name = 'Custom Exception'
}
}

function funcionCreada (parametro1){

try {

    if (parametro1.length < 3){
        throw new Error('El primer valor no puede ser menor a 3.')
    }else if (parametro1[1] === 0) {
        console.log('el parametro 1 no puede ser 0')
    }else if (typeof parametro1 === 'string') {
       throw new customError('el parametro debe ser un Array')
    }
    
} catch (error) {
    console.log('Tipo de error: ', error instanceof customError ? 'Custom error' : 'Normal error')
    console.log('Mensaje de error: ', error.message)
    
} finally{
    console.log('Fin del ejercicio')
}

}
funcionCreada([0, 1])
// funcionCreada([0, 0, 1, 2, 3])
// funcionCreada('HOLA')


