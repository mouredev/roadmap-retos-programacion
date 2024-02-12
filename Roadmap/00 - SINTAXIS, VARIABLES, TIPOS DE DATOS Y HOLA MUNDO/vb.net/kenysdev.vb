' ╔══════════════════════════════════════╗
' ║ Autor: Kenys Alvarado                ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 - VB.NET                        ║
' ╚══════════════════════════════════════╝
' 1. Sitio web oficial:
' *********************
' https://learn.microsoft.com/es-es/dotnet/visual-basic/

Imports System
Module Program
    Sub Main(args As String())

        ' 2. Sintaxis para comentarios:
        ' *****************************
        Dim edad As Integer = 21 'comentario inline

        ' Comentarios Block
        ' '''
        '   comentario para
        '   múltiples líneas.
        ' '''

        ' TODO: Futuras modificaciones o escritura.
        ' HACK: Solución temporal, revisar y mejorar.
        ' BUG: Corregir

#Disable Warning IDE0018 ' Desactivar temporalmente una advertencia.
        ' código ...
#Enable Warning IDE0018 ' Restaurarla después

        ''' <summary>
        ''' Comentarios XML, para generadores de documentación
        ''' </summary>
        ''' <param name="parametro">Descripción del parámetro.</param>
        ''' <returns>Descripción del valor de retorno.</returns>

#If DEBUG Then
        ' Comentarios condicionales
        ' Este código se compila solo en configuraciones de depuración
#End If

        ' 3. Variable y constante.
        ' ************************
        Dim variable_edad As Integer = 21
        Const Constante As Double = 3.14

        ' 4. Variables para datos primitivos.
        ' ***********************************
        ' Enteros:
        Dim entero As Integer = 42         ' Entero de 32 bits
        Dim byteEntero As Byte = 255       ' Entero sin signo de 8 bits
        Dim corto As Short = 10000         ' Entero de 16 bits
        Dim largo As Long = 123456789L     ' Entero de 64 bits
        ' uint, ushort, ulong -> No soportan números negativos

        ' Decimales:
        Dim flotante As Single = 3.14F          ' Número de punto flotante de 32 bits
        Dim doble As Double = 3.14159           ' Número de punto flotante de 64 bits
        Dim decimalValor As Decimal = 123.456D ' Número decimal de 128 bits

        ' Caracteres y Cadenas:
        Dim caracter As Char = "A"c           ' Carácter Unicode
        Dim cadena As String = "Hola"         ' Cadena de caracteres

        ' Booleanos:
        Dim esVerdadero As Boolean = True     ' Valor booleano verdadero
        Dim esFalso As Boolean = False        ' Valor booleano falso

        ' 5. Imprime: hola, lenguaje:
        ' **************************
        Console.WriteLine("¡Hola, VB.NET!")
    End Sub
End Module