' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝

' # Recursividad
' --------------
' - La recursividad es la capacidad de una función para llamarse a sí misma,ya sea 
'   de forma directa o indirecta, con el propósito de resolver un problema. 
Module Program
    Sub Main(args As String())
        '- imprimiendo números del 100 al 0.
        '  Ejemplo con recursividad directa
        '  ocurre cuando una función se llama a sí misma. */

        Recursive(100)

        '- Ejemplo con recursividad indirecta
        '  implica que varias funciones se llamen entre sí.

        Recursive2(100)

        ' ___________________________________________________________________
        ' Ejercicios:
        ' -----------
        ' 1. Calcular el factorial de un número concreto (la función recibe ese número).
        ' 4! = 4 * 3 * 2 * 1 = 24 */

        Console.WriteLine($"Factorial de 4: {Factorial(4)}")

        '2. Calcular el valor de un elemento concreto (según su posición) en la 
        '   sucesión de Fibonacci (la función recibe la posición).
        '   n : |0|1|2|3|4|5|6|..
        '   fb: |0|1|1|2|3|5|8|..
        '        |+|=^   |+|=^ ..  */

        Console.WriteLine($"Posición 4 en Fibonacci: {Fibonacci(4)}")

    End Sub

    Sub Recursive(ByVal n As Integer)
        Console.WriteLine(n)
        If n > 0 Then
            Recursive(n - 1)
        End If
    End Sub

    Sub Subs(ByVal n As Integer)
        Recursive2(n - 1)
    End Sub

    Sub Recursive2(ByVal n As Integer)
        Console.WriteLine(n)
        If n > 0 Then
            Subs(n)
        End If
    End Sub

    Function Factorial(ByVal n As Integer) As Integer
        If n <> 0 Then
            Return n * Factorial(n - 1)
        Else
            Return 1
        End If

        ''* Explicación
        '    fac(4)
        '        | = 24 
        '     return 4 * fac(3) ->(4 * 6)
        '                  | = 6 
        '         return 3 * fac(2) ->(3 * 2)
        '                      | = 2 
        '             return 2 * fac(1) ->(2 * 1)
        '                          | = 1 
        '                 return 1 * fac(0) ->(1 * 1)
        '                              | = return 1 -> caso base */

    End Function

    Function Fibonacci(ByVal n As Integer) As Integer
        If n <= 1 Then
            Return n
        Else
            Return Fibonacci(n - 1) + Fibonacci(n - 2)
        End If

        ''* Explicación fib(4) 
        '                         return 3
        '               fib(3)      / \    fib(2)
        '                / \ =2      +      / \ =1
        '          fib(2) + fib(1)    fib(1) + fib(0) -> caso base
        '          / \ =1
        '    fib(1) + fib(0) -> caso base  */

    End Function
End Module