
' ╔══════════════════════════════════════════╗
' ║ Autor:  Juan Villegas Dev (Devian)       ║
' ║ Ejercicio:  00 - SINTAXIS, VARIABLES,... ║
' ║ GitHub: https://github.com/juandevian    ║
' ║ Fecha enunciado: 26/12/2023              ║
' ║ Fecha publicación solución: 26/09/2024   ║
' ║ Dificultad: BAJA                         ║
' ║ 2024 -  VB.NET  Visual Basic.NET         ║
' ╚══════════════════════════════════════════╝

Module ModProgram
    ' 00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
    ' Visual Basic.NET
    ' Sitio web oficial: https://learn.microsoft.com/es-es/dotnet/visual-basic/

    ' Los comentarios son notas cortas explicativas que se agregan al código
    ' para aportar mayor información a las personas que lo lean.
    ' Este es un comentario que comienza en el lado hizquierdo de la pantalla.

    ' TODO es una etiqueta de comentario. podemos crear las eqiqueas que necesitamos.
    ' desde el menú de Herramiesntas -> Configuración.

    Dim mStrLenguaje As String = "Visual Basic.NET"   ' Este es un comentario en líena de código.
    REM Esta es otra forma de escribir comentarios,
    REM es menos usada y requiere más espacio en memoria.
    REM Se recomienda usar ' para los comentarios.

    ' No Exist una forma para comentarios multilínea
    ' Al necesitar extender el comentario se requiere
    ' agregar el simbolo ' al inicio de cada línea. 

    ''' Esta es la estructura para realizar comentaris XML
    ''' Podemos agregar infomración importante a IntelliSense de esta forma
    ''' <summary>
    ''' Determina cualquier espesificación clave que exista
    ''' </summary>
    ''' <param name="regKey"> Definimos el string de saludo</param>
    ''' <return> Cuál es el valor de retorno y las condiciones para el mismo</return>
    ''' <author></author>
    Function RegKeyExists(ByVal regKey As String) As Boolean
        Dim exists As Boolean = False
        Try

        Catch ex As Exception

        End Try
    End Function
    ' Los comentarios XML se realizan antes de una declaración de procedimiento,
    ' variable o función.

    ' Así se declara una variables locales: Dim nombreVariable As TipoDato
    Dim i, j, k As Integer
    ' Las tres variables de la declaración son definidas como típo Integer.  

    Dim l, m As Long, x, y As Single
    ' En esta declaracíon, l y m son tipo Long, x y y son Single.

    ' A las variables se les asigna el valor por medio del operador =,
    ' Dim nameVar As TipoDato = Valor
    Dim num1 As Integer = 3 ' Uso de tipado explícito.

    ' También se puede usar la inferencia de tipado.
    Dim num2 = 5
    ' Si quiere usar la inferencia de tipo de variable local,
    ' Option Infer debe establecerse en On.
    '
    ' La declaración de una variable depende de la "vigencia" que necesitemos de la misma.
    ' Podemos usar el modificador de acceso Public, Shared, Private o Static, que nos permiten
    ' ampliar o reducur suvigencia.

    ' Declaración de constantes. Valore almacenado en memoria que son inmutables e invariables.
    Const VERSION As Byte = 1

    ' Declaración de variables

    Dim variableBoolean As Boolean = True
    Dim variableByte As Byte = 255
    Dim variableChar As Char = "a"
    Dim variableDataTime As DateTime = "13:22:48 26-09-2024"
    Dim variableDecimal As Decimal = 1.0123456789012346
    Dim variableDouble As Double = 2.0123456789012346
    Dim variableInteger As Integer = 1999
    Dim variableInt32 As Int32 = -1999
    Dim variableInt64 As Int64 = -900000000
    Dim variableLong As Long = -900000000
    Dim variableObject As Object = {"Raro es ", 1, "el objeto aquel."}
    Dim variableSByte As SByte = -128
    Dim variableShort As Short = -32767
    Dim variableSingle As Single = 3.1416
    Dim varString As String = "Acá se esecribe el menaje con la historia de IAN"
    Dim varUInteger As UInteger = 3276744567
    Dim varUULong As ULong = 3215647465468454901
    Dim varUShort As UShort = 65535

    '  ========================================================================
    ' | TIPO DE DATO      | ALMACENAMIENTO NOMINAL  | INTERVALO DE VALORES     |
    ' |===================|=========================|==========================|
    ' | Boolean           | Depende de la plataforma| True o False             |
    ' | Byte              | 1 byte                  | De 0 a 255 (sin signo)   |
    ' | Char              | 2 bytes                 | De 0 a 65535 (sin signo) |
    ' | DateTime          | 8 bytes                 | F 00:00:00 1-1-1900      |
    ' | Decimal           | 16 byte                 | 0 a 7.9E + 28 digitos    |
    ' | Double            | 8 bytes                 | - 1.7E 308 a 4.9E 324    |
    ' | Int32, Integer    | 4 bytes                 | -2147483648 a 2147483647 |
    ' | Int64, Long       | 8 bytes                 | +-9223372036854775808    |
    ' | Object            | 8 bytes                 | Cuañquier tipo de dato   |
    ' | SByte             | 1 byte                  | De -128 a 127 (con signo)|
    ' | Short             | 2 bytes                 | -32768 a 32767           |
    ' | Single            | 4 bytes                 | 3.40E 45                 |
    ' | String            | Variable                | De 0 a 2000 millones     |
    ' | UInteger, UInt32  | 4 bytes                 | De 0 a 4294967295        |
    ' | ULong, UInt64     | 8 bytes                 | De 0 a 1.8E 19           |
    ' | ValueType (Custom)| Variable                |                          |
    ' | UShort            | 2 bytes                 | De 0 a 65535 (sin signo) |
    ' --------------------------------------------------------------------------

    Sub Main()

        Console.WriteLine("Hola, {0}.", mStrLenguaje)

    End Sub

End Module

' Fuente. https://retosdeprogramacion.com/roadmap/
' ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
' - Recuerda que todas las instrucciones de participación están en el
'   repositorio de GitHub.
' 
' Lo primero... ¿Ya has elegido un lenguaje?
' - No todos son iguales, pero sus fundamentos suelen ser comunes.
' - Este primer reto te servirá para familiarizarte con la forma de participar
'   enviando tus propias soluciones.
' 
'-----------------------------------------------------
' ### EJERCICIO:
'-----------------------------------------------------
' - Crea un comentario en el código y coloca la URL del sitio web oficial del
'   lenguaje de programación que has seleccionado.
' - Representa las diferentes sintaxis que existen de crear comentarios
'   en el lenguaje (en una línea, varias...).
' - Crea una variable (y una constante si el lenguaje lo soporta).
' - Crea variables representando todos los tipos de datos primitivos
'   del lenguaje (cadenas de texto, enteros, booleanos...).
' - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
' 
'  ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
'  debemos comenzar por el principio.
'____________________________________________________
' # INFORMACIÓN ADICIONAL:
''
' ____________________________________________________
' # COMENTARIOS PERSONALES:
'
' Finalizado exitosamente
' Elaboración más extensa de lo calculado, especialmente realizando la busqueda de
' todos los tipos de datos nativos en la documentación del lenguaje.
' ____________________________________________________
