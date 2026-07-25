(() => {
  /*
    * EJERCICIO:
    * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
    *   su tipo de dato.
    * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
    *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
    * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
  */

  let numberA: number = 7
  let numberByA: number = numberA
  console.log(`Valor de numberByA (por valor): ${numberByA}`)

  const userslist: Array<string> = ["Victor", "victorCasta"]
  const userslistB: Array<string> = userslist
  console.log(`Valor de userslistB (por referencia): ${userslistB}`)

  const assignedValue = (a: number): void => {
    let b: number = a
    console.log(`Valor inicial de variable a: ${a}`)
    console.log(`Valor inicial de variable b (copia de a): ${b}`)
    b = 7
    console.log(`Valor de a después de cambiar el valor de b: ${a}`)
    console.log(`Valor de b después de cambiar el valor de b: ${b}`)
  }

  assignedValue(9)

  const assignedReference = (a: Array<number>): void => {
    let b: Array<number> = a
    console.log(`Valor inicial de variable a: ${a}`)
    console.log(`Valor inicial de variable b (referencia de a): ${b}`)
    b.push(3)
    console.log(`Valor de a después de modificar b: ${a}`)
    console.log(`Valor de b después de modificar b: ${b}`)
  }

  assignedReference([1, 2])

  /*
  * DIFICULTAD EXTRA (opcional):
  * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
  * - Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
  *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
  *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
  *   Comprueba también que se ha conservado el valor original en las primeras.
  */

  let variable1: number = 1
  let variable2: number = 2
  let variable3: Array<number> = [1, 2]
  let variable4: Array<number> = [3, 4]


  const program1 = (param1: number, param2: number): Array<number> => {
    const temp = param1
    param1 = param2
    param2 = temp
    return [param1, param2]
  }

  const program2 = (param1: Array<number>, param2: Array<number>): Array<Array<number>> => {
    const temp = [...param1]
    param1.length = 0
    param1.push(...param2)
    param2.length = 0
    param2.push(...temp)
    return [param1, param2]
  }

  const results1: Array<number> = program1(variable1, variable2)
  const results2: Array<Array<number>> = program2([...variable3], [...variable4])

  const resultVariable1: number = results1[0]
  const resultVariable2: number = results1[1]
  const resultVariable3: Array<number> = results2[0]
  const resultVariable4: Array<number> = results2[1]


  console.log("Variables por valor originales")
  console.log(variable1)
  console.log(variable2)

  console.log("Variables por valor nuevas")
  console.log(resultVariable1)
  console.log(resultVariable2)

  console.log("Variables por referencia originales")
  console.log(variable3)
  console.log(variable4)

  console.log("Variables por referencia nuevas")
  console.log(resultVariable3)
  console.log(resultVariable4)

})()
