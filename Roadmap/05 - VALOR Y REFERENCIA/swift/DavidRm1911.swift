/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */



 //POR VALOR

 func ValorFunc(valor: Int){
    let num = valor + 2
    print("La variable por valor es: \(num)")
 }

 var valor = 10
  ValorFunc(valor: valor)
 print("Antes de entrar a la funcion: \(valor), y como es por valor no se modifica")


//Por referencia

var referencia = 20
func referenciaFun(valor: inout  Int ){
    valor += 13 
}

print("Antes de pasar por la funcion \(referencia)")
referenciaFun(valor: &referencia)
print("Despues de pasar por referencia: \(referencia), como se puede observar el valor ha sido modificado, aun habiendo sucedido dentro de la funcion") 

//Ejercicios dif extra:
func voltearValor(x: Int, y: Int ) -> (Int, Int){
    return (y,x)
}

var valor1 = 20
var valor2 = 40

var(xx,yy)=voltearValor(x: 20, y: 40)
print("Los valores originales son: valor1 = \(valor1) y valor2 = \(valor2)")
print("Los valores volteados son xx= \(xx) y yy= \(yy)")

//EJERCICIO EN REFERENCIA
var aux1: Int = 0
var aux2: Int = 0
func voltearRef(x: inout Int, y: inout Int){

    aux1 =  x
    aux2 = y
    x = aux2
    y = aux1

}

voltearRef(x: &valor1, y: &valor2)

print("Cuando se han volteado por referencia lo nuevos valores son para valor1(ref)= \(valor1), y de valor2(ref)= \(valor2)")
print("Hemos devuelto sus valores originales para q no se vean afectados de manera que valor 1 = \(aux1), \(aux2)")

