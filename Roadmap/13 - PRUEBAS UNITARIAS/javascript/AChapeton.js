// ! NOTA: El archivo utiliza la libreria Jest. Para utilizarlo, seguir los siguientes pasos:
// 1. Se debe de ejecutar el comando "npm i --save-dev jest"
// 2. En la lista de scripts dentro de package.json, incluir "test": "jest"
// 3. Cambiar el nombre del archivo a "AChapeton.test.js"

const sum = (a, b) => {
  return a + b
}

describe('Funcion Sum', () => {
  test('Debe de sumar dos numeros', () => {
    expect(sum(1, 2)).toBe(3)
  })
})

// DIFICULTAD EXTRA

const diccionario = {
  name: "Andres", 
  age: 26,
  birth_date: '02/06/1997',
  programming_languages: [
    "TypeScript", "JavaScript", "Python"
  ]
}

describe('Diccionario', () => {
  test('Deben de existir los 4 campos', () => {
    const keys = Object.keys(diccionario)
    expect(keys).toContain('name')
    expect(keys).toContain('age')
    expect(keys).toContain('birth_date')
    expect(keys).toContain('programming_languages')
  })

  test('Los datos deben de ser correctos', () => {
    const values = Object.values(diccionario)
    expect(values).toContain('Andres')
    expect(values).toContain(26)
    expect(values).toContain('02/06/1997')
    expect(values[3]).toEqual([
      "TypeScript", "JavaScript", "Python"
    ])
  })
})