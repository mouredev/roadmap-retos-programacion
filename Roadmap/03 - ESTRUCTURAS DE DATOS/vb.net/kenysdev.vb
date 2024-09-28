' ╔══════════════════════════════════════╗
' ║ Autor:  Kenys Alvarado               ║
' ║ GitHub: https://github.com/Kenysdev  ║
' ║ 2024 -  VB.NET                       ║
' ╚══════════════════════════════════════╝

' ESTRUCTURAS DE DATOS
' --------------------
Imports System.Formats

Module Program

    Sub Main(args As String())
        '_______________________________________________________
        ' Arrays(Arreglos):
        ' - Colección de elementos del mismo tipo almacenados en posiciones contiguas de memoria.
        ' - Acceso rápido a elementos por índice.
        Console.WriteLine("Arreglos")

        Dim numeros = New Integer(2) {}
        Dim palabras = New String() {"Hola", "Mundo"}

        ' Inserción:
        numeros(0) = 3
        numeros(1) = 2
        numeros(2) = 1

        ' Acceder:
        Console.WriteLine(numeros(0))

        ' Modificar:
        palabras(1) = "Ben"

        ' Ordenación:
        Array.Sort(numeros)

        ' Iteración:
        For i = 0 To numeros.Length - 1
            Console.WriteLine("Índice " & i & ": " & numeros(i))
        Next
        ' Nota: Los arreglos en VB.Net son de tamaño fijo después de la inicialización.

        '_______________________________________________________
        ' List(Listas):
        ' - Dinámicas y redimensionables, permiten almacenar elementos del mismo tipo.
        ' - Flexibilidad en la manipulación de datos.
        Console.WriteLine(vbCrLf & "Listas")

        Dim nombres As New List(Of String)
        Dim abc As New List(Of String) From {"a", "c", "d", "e"}

        ' Inserción:
        nombres.Add("Ben") ' Agrega elemento al final de la lista.
        abc.Insert(1, "b") ' Agrega un elemento en una posición específica.

        ' Acceder:
        Console.WriteLine(abc(1))

        ' Modificar:
        nombres(0) = "Zoe"

        ' Eliminacion:
        abc.Remove("a")
        abc.RemoveAt(1) ' por indice 
        abc.RemoveAll(Function(x) x = "c") ' todas las ocurrencias

        ' Ordenación:
        abc.Sort()

        ' Iteración:
        For Each i As String In abc
            Console.WriteLine(i)
        Next

        '_______________________________________________________
        ' Dictionary(Diccionarios):
        ' - Asocian claves únicas con valores, permitiendo búsquedas eficientes.
        ' - Almacenar y recuperar datos con base en claves.
        Console.WriteLine(vbCrLf & "Diccionarios")

        Dim nombre_edad As New Dictionary(Of String, Integer)
        Dim dic As New Dictionary(Of String, Integer) From {
            {"a", 1},
            {"b", 2}
        }

        ' Inserción:
        nombre_edad("Zoe") = 21
        dic.Add("c", 3)

        ' Acceder:
        Console.WriteLine(dic("b"))
        ' No mostrar excepción en caso de no existir.
        Dim valorx As String = Nothing
        If dic.TryGetValue("b", valorx) Then
            Console.WriteLine(valorx)
        End If

        ' Modificar:
        nombre_edad("Zoe") = 27

        ' Eliminacion:
        dic.Remove("c")

        ' Iteración:
        For Each valor As Integer In dic.Values ' o dic.Keys
            Console.WriteLine(valor)
        Next

        '_______________________________________________________
        ' HashSet(Conjuntos):
        ' - Colección sin duplicados, sin orden definido.
        ' - Verificación de pertenencia y eliminación de duplicados.
        Console.WriteLine(vbCrLf & "Conjuntos")

        Dim miConjunto As New HashSet(Of Integer)
        Dim otroConjunto = New HashSet(Of Integer) From {2, 3, 4}

        ' Inserción:
        miConjunto.Add(1)
        miConjunto.Add(2)

        ' Buscar:
        If otroConjunto.Contains(3) Then
            Console.WriteLine($"El conjunto contiene el elemento 3: {otroConjunto.Contains(3)}")
        End If

        ' Eliminacion:
        miConjunto.Remove(2)

        ' Verificación:
        Console.WriteLine(miConjunto.Contains(1))

        ' Operaciones:
        miConjunto.UnionWith(otroConjunto)     ' Unión de conjuntos
        miConjunto.IntersectWith(otroConjunto) ' Intersección de conjuntos
        miConjunto.ExceptWith(otroConjunto)    ' Diferencia de conjuntos

        ' Iteración:
        For Each elemento As Integer In otroConjunto
            Console.WriteLine(elemento)
        Next

        '_______________________________________________________
        ' Matrices:
        ' - Estructura bidimensional organizada en filas y columnas.
        ' - Representar datos tabulares.
        Console.WriteLine(vbCrLf & "Matrices")

        Dim mtx1(2, 2) As Integer
        Dim mtx2(,) As Integer = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}

        ' asignación:
        mtx1(0, 0) = 1
        mtx1(0, 1) = 2
        mtx1(0, 2) = 3

        ' Acceder:
        Console.WriteLine(mtx1(0, 1))

        ' Iteración:
        Dim filas = mtx2.GetLength(0)
        Dim columnas = mtx2.GetLength(1)
        For i = 0 To filas - 1
            For j = 0 To columnas - 1
                Console.Write(mtx2(i, j) & " ")
            Next
            Console.WriteLine()
        Next

        '_______________________________________________________
        ' Tuple(tuplas):
        ' - Agrupación de elementos heterogéneos como una entidad única.
        ' - Son inmutables.
        ' - Devolver múltiples valores desde un método.
        Console.WriteLine(vbCrLf & "tuplas")

        Dim miTupla = (1, "hola", 3.14, True)
        Dim tuplaConNombres = (numero:=1, saludo:="hola", pi:=3.14, esCierto:=True)
        Dim item1 As Object = 1
        Dim item2 As Object = "hola"
        Dim miTupla2 = New ValueTuple(Of Object, Object)(item1, item2)

        ' Acceder:
        Console.WriteLine(miTupla.Item1)
        Console.WriteLine(tuplaConNombres.saludo)

        '_______________________________________________________
        ' Ejercicio:
        ' * Crea una agenda de contactos por terminal.
        ' * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
        ' * - Cada contacto debe tener un nombre y un número de teléfono.
        ' * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
        ' *   los datos necesarios para llevarla a cabo.
        ' * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
        ' *   (o el número de dígitos que quieras)
        ' * - También se debe proponer una operación de finalización del programa.
        Console.WriteLine(vbCrLf & "Ejercicio")

        While True
            Agenda()
        End While
    End Sub

    Dim miAgenda As New Dictionary(Of String, String)
    Dim msg_home As String = ("
 Agenda de contactos
╔═══════════════════════════╗
║ 1. Nuevo      4. Editar   ║
║ 2. Buscar     5. Eliminar ║
║ 3. Lista      6. Salir    ║
╚═══════════════════════════╝
")
    Sub Agenda()
        Console.WriteLine(msg_home)
        Console.Write("Número de opción: ")
        Dim opcion As String = Console.ReadLine()

        Select Case opcion
            Case "1"
                Crear()
            Case "2"
                Buscar()
            Case "3"
                Lista()
            Case "4"
                Editar()
            Case "5"
                Eliminar()
            Case "6"
                Console.WriteLine("Adios")
                Environment.Exit(0)
            Case Else
                Console.WriteLine("Número 1 -> 6")
        End Select
    End Sub

    Sub Crear()
        Console.WriteLine("Crear contacto o 6 para Salir")
        Console.Write("Escriba el nombre: ")
        Dim nombre As String = Console.ReadLine()

        If nombre.Length < 1 Then
            Crear()
        ElseIf nombre = "6" Then
            Console.WriteLine("Cancelado")
        ElseIf miAgenda.ContainsKey(nombre) Then
            Console.WriteLine("El nombre ya existe.")
        Else
            Console.Write("Escriba el número: ")
            Dim numero As String = Console.ReadLine()

            If Integer.TryParse(numero, Nothing) AndAlso numero.Length > 0 AndAlso numero.Length <= 11 Then
                miAgenda(nombre) = numero
                Console.WriteLine("Guardado")
            Else
                Console.WriteLine("Número no válido.")
            End If
        End If
    End Sub

    Sub Buscar()
        Console.WriteLine("Buscar contacto o 6 para Salir")
        Console.Write("Escriba el nombre: " & vbCrLf)
        Dim nombre As String = Console.ReadLine()

        If nombre = "6" Then
            Console.WriteLine("Cancelado")
        ElseIf miAgenda.ContainsKey(nombre) Then
            Console.WriteLine(miAgenda(nombre))
        Else
            Console.WriteLine("Contacto no encontrado.")
        End If
    End Sub

    Sub Lista()
        Dim ordenarAgenda As New SortedDictionary(Of String, String)(miAgenda)

        For Each entry In ordenarAgenda
            Console.WriteLine($"{entry.Key}: {entry.Value}")
        Next
    End Sub

    Sub Editar()
        Console.WriteLine("Editar contacto o 6 para Salir")
        Console.Write("Escriba el nombre: ")
        Dim nombre As String = Console.ReadLine()

        If nombre = "6" Then
            Console.WriteLine("Cancelado")
        ElseIf miAgenda.ContainsKey(nombre) Then
            Console.Write("Escriba el nuevo número: ")
            Dim nuevoNumero As String = Console.ReadLine()

            If Integer.TryParse(nuevoNumero, Nothing) AndAlso nuevoNumero.Length > 0 AndAlso nuevoNumero.Length <= 11 Then
                miAgenda(nombre) = nuevoNumero
                Console.WriteLine("Contacto editado")
            Else
                Console.WriteLine("Número no válido.")
            End If
        Else
            Console.WriteLine("Contacto no encontrado.")
        End If
    End Sub

    Sub Eliminar()
        Console.WriteLine("Eliminar contacto o 6 para Salir")
        Console.Write("Escriba el nombre: ")
        Dim nombre As String = Console.ReadLine()

        If nombre = "6" Then
            Console.WriteLine("Cancelado")
        ElseIf miAgenda.ContainsKey(nombre) Then
            miAgenda.Remove(nombre)
            Console.WriteLine("Contacto eliminado")
        Else
            Console.WriteLine("Contacto no encontrado.")
        End If
    End Sub
End Module
