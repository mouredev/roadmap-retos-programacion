' _____________________________________
' https://github.com/kenysdev
' 2024 - vb.net
' _____________________________________
' 36 EL SOMBRERO SELECCIONADOR
' ------------------------------------
' * Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
' * de programación de Hogwarts para magos y brujas del código.
' * En ella, su famoso sombrero seleccionador ayuda a los programadores
' * a encontrar su camino...
' * Desarrolla un programa que simule el comportamiento del sombrero.
' * Requisitos:
' * 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
' * 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
' *    (Puedes elegir las que quieras)
' * Acciones:
' * 1. Crea un programa que solicite el nombre del alumno y realice 10
' *    preguntas, con cuatro posibles respuestas cada una.
' * 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
' * 3. Una vez finalizado, el sombrero indica el nombre del alumno
' *    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
' *    pero indicándole al alumno que la decisión ha sido complicada).


Module Program
    Private ReadOnly HOUSES As String() = {"Frontend", "Backend", "Mobile", "Data"}

    ' NOTA: Preguntas y respuestas generadas por IA
    Private ReadOnly QUESTIONS As String() = {
        "¿Qué te atrae más?",
        "¿Qué superhéroe de la programación te gustaría ser?",
        "En un proyecto de software, ¿qué rol te emociona más?",
        "Si tu código fuera una obra de arte, ¿qué estilo tendría?",
        "¿Qué animal de programación serías?",
        "En una hackathon, ¿qué tipo de proyecto propondrías?",
        "Si tu carrera en tech fuera una película, ¿de qué género sería?",
        "¿Qué herramienta de programación no puede faltar en tu caja de herramientas digital?",
        "Si pudieras resolver un gran problema en tech, ¿cuál elegirías?",
        "¿Qué tipo de equipo prefieres?"
    }

    Private ReadOnly ANSWERS As String()() = {
        New String() {"Crear experiencias visuales.", "Solucionar problemas de funcionamiento.", "Innovar en dispositivos portátiles.", "Descubrir tendencias ocultas."},
        New String() {"Diseñador de Interfaces, creando experiencias asombrosas", "Arquitecto de Sistemas, construyendo estructuras robustas", "Mago de Apps, conjurando soluciones móviles", "Explorador de Datos, descubriendo tesoros ocultos"},
        New String() {"Director de UX, orquestando la sinfonía visual", "Ingeniero de Backend, dominando la lógica del servidor", "Desarrollador de Apps, llevando la potencia al bolsillo", "Científico de Datos, descifrando los secretos de la información"},
        New String() {"Minimalismo elegante, como una landing page perfecta", "Arquitectura compleja, como un sistema distribuido", "Diseño adaptativo, fluyendo en diferentes dispositivos", "Visualización de datos, pintando historias con números"},
        New String() {"Un camaleón, adaptándome a diferentes frameworks", "Un pulpo, manejando múltiples servicios a la vez", "Un colibrí, ágil y siempre en movimiento", "Una lechuza, analizando datos con sabiduría"},
        New String() {"Una web app que revolucione la experiencia del usuario", "Un sistema de IA que optimice procesos backend", "Una app móvil que cambie la forma de interactuar con el mundo", "Un proyecto de big data que prediga tendencias futuras"},
        New String() {"Comedia romántica con JavaScript y CSS", "Thriller de ciencia ficción con microservicios", "Aventura de acción en el mundo de las apps", "Documental profundo sobre el universo de los datos"},
        New String() {"Un editor de código con plugins para diseño visual", "Una robusta suite de testing y depuración", "Un emulador multi-dispositivo de última generación", "Una plataforma de análisis de datos en tiempo real"},
        New String() {"Hacer que la accesibilidad web sea universal", "Crear una arquitectura de software autorreparable", "Desarrollar una plataforma de AR/VR para educación móvil", "Construir un modelo de IA ético y transparente"},
        New String() {"Creativos enfocados en diseño.", "Técnicos que construyen sistemas.", "Especialistas en aplicaciones móviles.", "Expertos en datos y análisis."}
    }

    Private Class SortingHat
        Private ReadOnly scores As Dictionary(Of String, Integer)

        Public Sub New()
            scores = HOUSES.ToDictionary(Function(house) house, Function(house) 0)
        End Sub

        Public Sub AskQuestion(qNum As Integer, question As String, answers As String())
            Console.WriteLine($"{vbCrLf}#{qNum}: {question}")
            For i As Integer = 0 To answers.Length - 1
                Console.WriteLine($"{i + 1}) {answers(i)}")
            Next

            While True
                Console.Write("Elige tu respuesta (1-4): ")
                Dim choice As Integer
                If Integer.TryParse(Console.ReadLine(), choice) AndAlso choice >= 1 AndAlso choice <= 4 Then
                    scores(HOUSES(choice - 1)) += 1
                    Exit While
                Else
                    Console.WriteLine("Por favor, elige un número entre 1 y 4.")
                End If
            End While
        End Sub

        Public Function SelectHouse() As String
            Dim maxScore = scores.Values.Max()
            Dim topHouses = scores.Where(Function(kv) kv.Value = maxScore).Select(Function(kv) kv.Key).ToList()

            If topHouses.Count > 1 Then
                Console.WriteLine(vbCrLf & "La decisión ha sido complicada.")
                Return topHouses(New Random().Next(topHouses.Count))
            End If
            Return topHouses(0)
        End Function
    End Class

    Sub Main()
        Console.WriteLine("EL SOMBRERO SELECCIONADOR")
        Console.Write("¿Cuál es tu nombre? : ")
        Dim name As String = If(Console.ReadLine(), String.Empty)
        Dim hat As New SortingHat()

        For i As Integer = 0 To QUESTIONS.Length - 1
            hat.AskQuestion(i + 1, QUESTIONS(i), ANSWERS(i))
        Next

        Dim selectedHouse As String = hat.SelectHouse()
        Console.WriteLine($"{vbCrLf}'{name}' pertenecerá a la casa '{selectedHouse}'{vbCrLf}")
    End Sub
End Module
