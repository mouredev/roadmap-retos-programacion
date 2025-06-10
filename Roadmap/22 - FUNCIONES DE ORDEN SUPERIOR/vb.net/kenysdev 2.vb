' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
'-----------------------------------------------
'* FUNCIONES DE ORDEN SUPERIOR
'-----------------------------------------------

Module Program
    '* EJERCICIO #1:
    '* Explora el concepto de funciones de orden superior en tu lenguaje 
    '* creando ejemplos simples (a tu elección) que muestren su funcionamiento.

    Delegate Function ArithmeticOperation(x As Integer, y As Integer) As Integer

    Function ArithmeticOp(operation As ArithmeticOperation) As Func(Of Integer, Integer, Integer)
        Return Function(x, y) operation(x, y)
    End Function

    Function Add(x As Integer, y As Integer) As Integer
        Return x + y
    End Function

    Function Subtract(x As Integer, y As Integer) As Integer
        Return x - y
    End Function

    Function Multiply(x As Integer, y As Integer) As Integer
        Return x * y
    End Function

    '* EJERCICIO #2
    '* Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
    '* lista de calificaciones), utiliza funciones de orden superior para 
    '* realizar las siguientes operaciones de procesamiento y análisis:
    '* - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
    '*   y promedio de sus calificaciones.
    '* - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
    '*   que tienen calificaciones con un 9 o más de promedio.
    '* - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
    '* - Mayor calificación: Obtiene la calificación más alta de entre todas las
    '*   de los alumnos.
    '* - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).

    ReadOnly studentsList As New List(Of Dictionary(Of String, Object)) From {
        New Dictionary(Of String, Object) From {{"name", "Ken"}, {"dob", "2012-04-21"}, {"grades", {9.5, 9.4, 9.3, 9.2}.ToList()}},
        New Dictionary(Of String, Object) From {{"name", "Ben"}, {"dob", "2012-03-20"}, {"grades", {8.5, 8.4, 8.3, 8.2}.ToList()}},
        New Dictionary(Of String, Object) From {{"name", "Ada"}, {"dob", "2012-02-19"}, {"grades", {7.5, 7.4, 7.3, 7.2}.ToList()}},
        New Dictionary(Of String, Object) From {{"name", "Zoe"}, {"dob", "2012-01-18"}, {"grades", {9.0, 9.1, 9.0, 9.1}.ToList()}}
    }

    Delegate Sub PrintFunction(student As Dictionary(Of String, Object))

    Function HigherOrderFun(msg As String, printFn As PrintFunction) As Action(Of List(Of Dictionary(Of String, Object)))
        Dim wrapper As Action(Of List(Of Dictionary(Of String, Object))) =
            Sub(students)
                Console.WriteLine($"{vbCrLf}----{vbCrLf}{msg}")
                For Each student In students
                    printFn(student)
                Next
            End Sub

        Return wrapper
    End Function

    Sub PrintGradePointAverage(student As Dictionary(Of String, Object))
        Dim grades = DirectCast(student("grades"), List(Of Double))
        Dim averageGrade = grades.Sum() / grades.Count
        Console.WriteLine($"{student("name")} {averageGrade}")
    End Sub

    Sub PrintTopStudents(student As Dictionary(Of String, Object))
        Dim grades = DirectCast(student("grades"), List(Of Double))
        Dim average = grades.Sum() / grades.Count
        If average >= 9 Then
            Console.WriteLine(student("name"))
        End If
    End Sub

    Sub PrintBirthOrder(student As Dictionary(Of String, Object))
        Console.WriteLine($"{student("name")} {student("dob")}")
    End Sub

    Sub PrintHighestGrade(student As Dictionary(Of String, Object))
        Dim maxGrade = DirectCast(student("grades"), List(Of Double)).Max()
        Console.WriteLine($"{student("name")} {maxGrade}")
    End Sub

    Sub Main()
        Console.WriteLine("EJERCICIO #1")
        Dim addFunc = ArithmeticOp(AddressOf Add)
        Dim subtractFunc = ArithmeticOp(AddressOf Subtract)
        Dim multiplyFunc = ArithmeticOp(AddressOf Multiply)

        Console.WriteLine(addFunc(3, 5))
        Console.WriteLine(subtractFunc(10, 3))
        Console.WriteLine(multiplyFunc(2, 4))

        Console.WriteLine("EJERCICIO #2")
        Dim gradePointAverage = HigherOrderFun("Promedio calificaciones", AddressOf PrintGradePointAverage)
        Dim topStudents = HigherOrderFun("Mejores estudiantes:", AddressOf PrintTopStudents)
        Dim birthOrder = HigherOrderFun("Por nacimiento:", AddressOf PrintBirthOrder)
        Dim highestGrade = HigherOrderFun("Mayor calificación:", AddressOf PrintHighestGrade)

        gradePointAverage(studentsList)
        topStudents(studentsList)
        birthOrder(studentsList.OrderBy(Function(student) CStr(student("dob"))).ToList())
        highestGrade(studentsList)
    End Sub

End Module
