import { describe, expect, it } from 'vitest'

const sumaDosNumeros = (num1, num2) => {
  if (typeof num1 !== 'number' || typeof num2 !== 'number') throw new Error('Los parámetros ingresados deben ser números')
  if (Number.isNaN(num1) || Number.isNaN(num2)) throw new Error('Los parámetros ingresados deben ser números')
  const suma = num1 + num2
  return suma
}

describe('sumaDosNumeros', () => {
  it('Deberia ser una funcion', () => {
    expect(typeof sumaDosNumeros).toBe('function')
  })
  it('Deberia throw si los parámetros ingresados no son números', () => {
    expect(() => sumaDosNumeros()).toThrow()
  })
  it('Deberia throw un error específico si los parámetros ingresados no son números', () => {
    expect(() => sumaDosNumeros()).toThrow('Los parámetros ingresados deben ser números')
  })
  it('Deberia throw un error específico si un NaN es ingresado como parámetro', () => {
    expect(() => sumaDosNumeros(NaN, NaN)).toThrow('Los parámetros ingresados deben ser números')
  })
  it('Deberia return una suma', () => {
    expect(sumaDosNumeros(1, 1)).toBe(2)
  })
})

//Extra

const diccionario = {
  name: 'Ángel',
  age: 44,
  birth_date: '16/09/1979',
  programming_languages: ['html', 'css', 'javascript']
}

describe('diccionario', () => {
  it('Sí el diccionario existe', () => {
    expect(diccionario).toBeTruthy()
  })
  it('Sí diccionario es un objeto', () => {
    expect(typeof diccionario).toBe('object')
  })
  it('El diccionario debería tener las claves name, age, birth_date y programming_languages', () => {
    const keysFromDiccionario = Object.keys(diccionario)
    const keysBuscadas = ['name', 'age', 'birth_date', 'programming_languages']
    expect(keysFromDiccionario.some(e => keysBuscadas.includes(e))).toBe(true)
  })
  it('Shuld have no other property', () => {
    const result = Object.prototype.hasOwnProperty.call(diccionario, 'casado')
    expect(result).toBeFalsy()
  })
  it('La propiedad name deberia ser Ángel', () => {
    const result = diccionario.name
    expect(result).toBe('Ángel')
  })
  it('La propiedad age deberia ser 44', () => {
    const result = diccionario.age
    expect(result).toBe(44)
  })
  it('La propiedad birth_date deberia ser 16/09/1979', () => {
    const result = diccionario.birth_date
    expect(result).toBe('16/09/1979')
  })
  it('La propiedad programming_languages deberia contener los lenguajes html, css y javascript', () => {
    const lenguajes = diccionario.programming_languages
    const lenguajesBuscados = ['html', 'css', 'javascript']
    expect(lenguajes.some(e => lenguajesBuscados.includes(e))).toBe(true)
  })
})