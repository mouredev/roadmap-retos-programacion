const arrTest = [123, 0, -42]
const arrTestError = [123, 0, -42, 'string'] // hace falta comentar el if que corrobora que son números

const sumar = (a,b) => {
  return a + b
}

function testSumar(arr) { // test sin librerias externas
  let i = 0
  try {
    do {
      for (let index = i; index < arr.length; index++) {
        if (typeof arr[i] === 'number' && typeof arr[index] === 'number') { // iría donde ingresan los datos pero en este ejercicio no existe eso
          if (typeof sumar(arr[i], arr[index]) !== 'number') throw new Error("La función NO funciona correctamente");
        }
      }
      i++
    } while (i < arr.length)
  } catch (e) {
    console.log(e.message)
  }
}

testSumar(arrTest)

// ------------------------------------------ DIFICULTAD EXTRA ------------------------------------------
const arrLenguajes = ["C", "Java", "Python", "C++", "C#", "JavaScript", "PHP", "R", "Swift", "Rust", "Go (Golang)", "Kotlin", "Ruby", "Julia", "Nim", "Perl", "Vala", "SAS", "Scratch", "D", "Dart", "PL/SQL", "Logo", "COBOL", "Tcl", "Smalltalk", "ABC", "Algol", "APL", "Bash", "Carbon", "CFML", "CHILL", "CLIPS", "Forth", "TypeScript", "HTML/CSS", "Razor", "Elixir", "Erlang", "ASP.NET", "Zig", "M4"]
const requiredKeys = new Set(["name", "age", "birth_date", "programming_languages"])

const diccionario = {
  name: 'Pedro',
  age: 23,
  // birth_date: '-03-04-22',
  birth_date: '03/04/22',
  programming_languages: ['JavaScript', 'C#', 'M4'],
  // asd: 'asd'
}

function testCampos(dic) {
  let keys = Object.keys(dic)
  if (keys.length === requiredKeys.size && keys.every(k => requiredKeys.has(k))) {
    testDatos(dic)
  } else console.log('Los campos del diccionario son incorrectos')
}

function testDatos(dic) {
  const date = new Date
  let values = Object.values(dic)
  let correctName = values[0].length <= 0 || (/\d|\W/g).test(values[0])
  let correctAge = values[1].length <= 0 || values[1].length >= 125
  const correctLanguages = () => {
    for (let i = 0; i < values[3].length; i++) {
      if (!(arrLenguajes.includes(values[3][i]))) { // revisa que el lenguaje ingresado este en el listado de arriba, ya que hacer un regex me parecio muy dificil
        return true
      }
    } return false
  }
  let correctBirthDate
  if (!(/[^\d]-|-\d+[^\d-]|[a-zA-Z]|(-\d+){3}/g).test(values[2])) { // detecta si hay un número negativo o una letra
    let [day, month, year] = values[2].split(/\W/g).map(Number)
    correctBirthDate = 
    day <= 0 || day > 31 ||
    month <= 0 || month > 12 ||
    (year <= 100
      ? false // ya se verifica en el regex
      : year < (date.getFullYear() -125)  ||  year > date.getFullYear())
  } else correctBirthDate = true
  if (correctName || correctAge || correctLanguages() || correctBirthDate) { // si algún dato es incorrecto la variable o función devuelve/es  true
    console.log('Los datos introducidos son INCORRECTOS')
  } else console.log('Los campos y los datos son CORRECTOS')
}

testCampos(diccionario)