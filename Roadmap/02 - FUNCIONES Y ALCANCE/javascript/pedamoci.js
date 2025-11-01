//  ----------------------- FUNCIONES BASICAS -----------------------
  // Sin parámetros ni retorno
    function saludar() {  // función normal
      console.log('Hola, mundo')
    }
    const preguntar = ()=> { // función flecha
      console.log('Todo bien?')
    }
    saludar()
    preguntar()

  // Con parámetros sin retorno
    function saludoPersonalizado(nombre) {
      console.log(`Hola, ${nombre}`)
    }
    const nacimiento = (edad) => {
      const actualYear = new Date().getFullYear()
      console.log('Año de nacimiento: ', actualYear - edad)
    }
    saludoPersonalizado('Jaime')
    nacimiento(98)

  // Con parámetros y retorno
    function sumar(num1, num2) {
      return num1 + num2
    }
    const multiplicar = (num1, num2) => {
      return num1 * num2
    }
    console.log('Suma: ', sumar(5, 3))
    console.log('Multiplicación: ', multiplicar(7, 8))

//  ----------------------- FUNCIONES DENTRO DE FUNCIONES -----------------------
  // Función normal dentro de función normal
    function areaTrianguloRectangulo(altura, base) {
      const areaCuadrado = altura * base
      function area(areaCuadrado) {
        return areaCuadrado / 2
      }
      return area(areaCuadrado)
    }
    console.log('Area del triángulo rectángulo: ', areaTrianguloRectangulo(10, 5))

  // Función flecha dentro de función flecha
    const volumenCilindro = (radio, altura) => {
      const areaCirculo = (r) => Math.PI * (r ** 2)
      return areaCirculo(radio) * altura
    }
    console.log('Volumen de la cilindro: ', volumenCilindro(3, 10))

  // Función flecha dentro de función normal
    function areaHexagono(lado, base, hipotenusa) {
      const perimetro = lado * 6
      const apotema = (b, h) => {
        return Math.sqrt((-(b **2)) + (h ** 2))
      }
      return (perimetro * apotema(base, hipotenusa)) / 2
    }
    console.log('Area del hexágono: ', areaHexagono(6, 10, 12))

  // Función normla dentro de función flecha
    const areaCirculo = (radio) => {
      function area(r) {
        return Math.PI * (r ** 2)
      }
      return area(radio)
    }
    console.log('Area del círculo: ', areaCirculo(7))

//  ----------------------- FUNCIONES DENTRO DEL LENGUAJE -----------------------
  console.log('Según la función isFinite 10/3 es finito? ', isFinite(10/3))

//  ----------------------- VARIABLES LOCALES Y GLOBALES -----------------------
  let global = 'Soy global' // Variable global
  function bloqueUno () {
    let localFunction = 'Soy local de función' // Variable local de la función
    const bloqueDos = () => {
      let localFunctionFlecha = 'Soy local de función flecha' // Variable local de la función flecha
      console.log(`La variable global es: ${global}, la variable local de la función es: ${localFunction} y la variable local de la función flecha es: ${localFunctionFlecha}`)
    }
    console.log(`La variable global es: ${global}, la variable local de la función es: ${localFunction} y la variable local de la función flecha es: UNDIFINED`)
    bloqueDos()
  }
  console.log(`La variable global es: ${global}, la variable local de la función es: UNDIFINED y la variable local de la función flecha es: UNDIFINED`)
  bloqueUno()

//  ----------------------- DIFICULTAD EXTRA -----------------------
function impresora(s1, s2) {
  let cantNumImpresos = 0
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(s1 + s2)
    } else if (i % 3 === 0) {
      console.log(s1)
    } else if (i % 5 === 0 ) {
      console.log(s2)
    } else {
      cantNumImpresos++
      console.log(i)
    }
  }
  return cantNumImpresos
}
let str1 = prompt('ingresa la primera cadena de texto: ')
let str2 = prompt('ingresa la segunda cadena de texto: ')
console.log(`Se ha impreso el un número en lugar del texto: ${impresora(str1, str2)} veces`)