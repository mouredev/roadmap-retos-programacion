let myArray = ['a', 'b', 'c', 'd']

//TRY - Bloque del codigo que se va a evaluar
//CATCH - Bloque del codigo que se ejecuta si se encuentra un error en el bloque TRY
//FINALLY - Bloque de codigo (opcional) que se va a ejecutar una vez haya terminado el bloque TRY, independientemente de su resultado

try{
    myArray[8].length
}catch(error){
  throw 'No se puede acceder a una posicion que no existe en el array.' + error
}finally{
  console.log(myArray.length)
}



// DIFICULTAD EXTRA

class customException extends Error{
  constructor(message){
    super(message)
    this.name = 'Custom Exception'
  }
}

const myFunction = (num1, num2) => {
  try{
    if(num1 < 0){
      throw new Error('El primer valor no puede ser menor a cero.')
    }

    if((num2 % 2) !== 0){
      throw new Error('El segundo valor debe ser un numero par.')
    }

    if((num1 + num2) > 99){
      throw new customException('La suma de los valores no puede sobrepasar de 100.')
    }
  }catch(error){
    console.log('Tipo de error: ', error instanceof customException ? 'Custom error' : 'Normal error')
    console.log('Mensaje de error: ', error.message)
  }finally{
    console.log('Fin del ejercicio')
  }
}

myFunction(444, 50)