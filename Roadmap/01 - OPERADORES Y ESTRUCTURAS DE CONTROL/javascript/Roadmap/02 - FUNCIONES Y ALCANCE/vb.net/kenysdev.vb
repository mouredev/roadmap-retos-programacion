' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
Module Program
    ' ----------
    ' Funciones:
    ' ----------
    ' Función estática sin retorno
    Sub print(ByVal msg As Object)
        Console.WriteLine(msg)
    End Sub

    ' Funcion estática con retorno:
    Function Suma(ByVal a As Integer, ByVal b As Integer) As Integer
        Return a + b
    End Function

    ' Con Parámetro Opcional
    Sub Divide(ByVal a As Integer, Optional ByVal b As Integer = 2)
        print(a / b)
    End Sub

    ' Con Parámetros de Salida
    Sub Dividir(ByVal dividendo As Integer, ByVal divisor As Integer, ByRef cociente As Integer, ByRef residuo As Integer)
        cociente = dividendo / divisor
        residuo = dividendo Mod divisor
    End Sub

    ' Funciones Recursivas
    Function Factorial(ByVal n As Integer) As Integer
        Return If(n = 0, 1, n * Factorial(n - 1))
    End Function

    'NOTE: las funciones anidadas (funciones dentro de funciones) no son permitidas.
    
    ' ----------
    ' Ejercicio:
    ' ----------
    ' * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    ' * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    ' * - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    ' * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    ' * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    ' * - La función retorna el número de veces que se ha impreso el número en lugar de los textos.""")

    Function Ejercicio(ByVal str1 As String, ByVal str2 As String) As Integer
        Dim nVeces As Integer = 0
        For num As Integer = 1 To 100
            If num Mod 3 = 0 AndAlso num Mod 5 = 0 Then
                print(str1 & str2)
            ElseIf num Mod 3 = 0 Then
                print(str1)
            ElseIf num Mod 5 = 0 Then
                print(str2)
            Else
                nVeces += 1
                print(num)
            End If
        Next
        Return nVeces
    End Function

    Sub Main(args As String())
        ' Función estática sin retorno
        print("Estática")

        ' Función estática con retorno
        print(Suma(2, 2))

        ' Con Parámetro Opcional
        Divide(10)

        ' Con Parámetros de Salida
        Dim rCociente As Integer
        Dim rResiduo As Integer
        Dividir(10, 5, rCociente, rResiduo)
        print($"Cociente: {rCociente}, Residuo: {rResiduo}")

        ' Funciones Recursivas
        print(Factorial(4))

        ' Ejemplo de funciones incorporadas
        Dim un_bool As Boolean = True
        Dim a_str As String = Convert.ToString(un_bool)
        print(a_str)

        print(DateTime.Now)

        print("abc".Length)

        ' Ejercicio
        print(Ejercicio("múltiplo de 3", "múltiplo de 5"))
    End Sub
End Module