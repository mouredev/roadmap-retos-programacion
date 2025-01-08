' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝
Module Program
    '------------------------------------------
    '# Herencia
    '------------------------------------------
    '- Permite definir una clase que hereda atributos y métodos de una 
    '  clase existente, para reutilización y organización.
    '- La clase que hereda se conoce como “subclase” o “clase hija”.
    '- La clase de la que hereda se conoce como “superclase” o “clase padre”.

    ' Polimorfismo:
    ' ----------------------------------------
    ' - Los objetos de diferentes clases pueden ser accedidos utilizando el 
    '   mismo interfaz, mostrando un comportamiento distinto 
    '   (tomando diferentes formas) según cómo sean accedidos. */

    ' SuperClase
    Public Class Animal
        Public Property Name As String
        Public Property Sound As String

        Public Sub New(ByVal name As String, ByVal sound As String)
            Me.Name = name
            Me.Sound = sound
        End Sub

        Public Sub MakeSound()
            Console.WriteLine($"{Name} hace: {Sound}")
        End Sub
    End Class

    ' Subclases
    Public Class Dog
        Inherits Animal
        Public Sub New(ByVal name As String)
            MyBase.New(name, "Woof")
        End Sub
    End Class

    Public Class Cat
        Inherits Animal
        Public Sub New(ByVal name As String)
            MyBase.New(name, "Meow")
        End Sub
    End Class

    ''____________________________________________________
    '* Ejercicio usando herencia y Polimorfismo.
    '- Implementa la jerarquía de una empresa de desarrollo formada por 
    '  empleados que pueden ser Gerentes, Gerentes de Proyectos o Programadores.
    '- Cada empleado tiene un identificador y un nombre.
    '- Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
    '  actividad, y almacenan los empleados a su cargo. */

    ' Clase Employees
    Public Class Employees
        Public Shared employees As New List(Of String())
        Public identifier As String = ""
        Public tasks As New HashSet(Of String)()
        Public staff As New HashSet(Of String)()

        Public Sub Add(ParamArray names As String())
            For Each name In names
                employees.Add({identifier, name})
            Next
        End Sub

        Public Sub Print()
            For Each employee In employees
                If employee(0) = identifier Then
                    Console.WriteLine($"{employee(1)} -> {identifier}")
                End If
            Next
        End Sub

        Public Sub Functions()
            Console.WriteLine(vbCrLf + $"Funciones de {identifier}")
            For Each task In tasks
                Console.WriteLine(task)
            Next
            Console.WriteLine("--------------------")
        End Sub

        Public Sub Subordinates()
            Console.WriteLine(vbCrLf + $"Subordinados de un {identifier}")
            For Each employee In employees
                If staff.Contains(employee(0)) Then
                    Console.WriteLine($"{employee(1)} -> {employee(0)}")
                End If
            Next
            Console.WriteLine("--------------------")
        End Sub
    End Class

    ' Subclases de Employees
    Public Class Manager
        Inherits Employees
        Public Sub New()
            identifier = "Gerente"
            tasks = New HashSet(Of String)({"- Supervisión", "- Toma de decisiones"})
            staff = New HashSet(Of String)({"Gerente de Proyecto", "Programador"})
        End Sub
    End Class

    Public Class ProjectManager
        Inherits Employees
        Public Sub New()
            identifier = "Gerente de Proyecto"
            tasks = New HashSet(Of String)({"- Planificación", "- Coordinación de proyectos"})
            staff = New HashSet(Of String)({"Programador"})
        End Sub
    End Class

    Public Class Programmer
        Inherits Employees
        Public Sub New()
            identifier = "Programador"
            tasks = New HashSet(Of String)({"- Desarrollo", "- Mantenimiento de código"})
            staff = New HashSet(Of String)({"No tiene subordinados"})
        End Sub
    End Class

    ''____________________________________________________
    Sub Main()
        Dim dog As New Dog("Max")
        Dim cat As New Cat("Milo")
        dog.MakeSound()
        cat.MakeSound()

        Dim manager As New Manager()
        Dim projectManager As New ProjectManager()
        Dim programmer As New Programmer()

        manager.Add("Ben", "Dan")
        projectManager.Add("Ray", "Joe")
        programmer.Add("Leo", "Sam", "Zoe", "Ana")

        manager.Functions()
        projectManager.Functions()
        programmer.Functions()

        manager.Subordinates()
        projectManager.Subordinates()

        Console.WriteLine("Total:")
        manager.Print()
        projectManager.Print()
        programmer.Print()
    End Sub
End Module
