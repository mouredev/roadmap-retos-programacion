/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
------------------------------------------
* FUNCIONES DE ORDEN SUPERIOR
------------------------------------------
*/

#pragma warning disable CA1050
class Program {
    /*
    * EJERCICIO #1:
    * Explora el concepto de funciones de orden superior en tu lenguaje 
    * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
    */
    delegate int ArithmeticOperation(int x, int y);

    static Func<int, int, int> ArithmeticOp(ArithmeticOperation operation) {
        return (x, y) => operation(x, y);
    }

    static int Add(int x, int y) {
        return x + y;
    }

    static int Subtract(int x, int y) {
        return x - y;
    }

    static int Multiply(int x, int y) {
        return x * y;
    }

    /*
    * EJERCICIO #2:
    * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
    * lista de calificaciones), utiliza funciones de orden superior para 
    * realizar las siguientes operaciones de procesamiento y análisis:
    * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
    *   y promedio de sus calificaciones.
    * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
    *   que tienen calificaciones con un 9 o más de promedio.
    * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
    * - Mayor calificación: Obtiene la calificación más alta de entre todas las
    *   de los alumnos.
    * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
    */

    static readonly List<Dictionary<string, object>> studentsList = [
        new() { {"name", "Ken"}, {"dob", "2012-04-21"}, {"grades", new List<double> {9.5, 9.4, 9.3, 9.2} } },
        new() { {"name", "Ben"}, {"dob", "2012-03-20"}, {"grades", new List<double> {8.5, 8.4, 8.3, 8.2} } },
        new() { {"name", "Ada"}, {"dob", "2012-02-19"}, {"grades", new List<double> {7.5, 7.4, 7.3, 7.2} } },
        new() { {"name", "Zoe"}, {"dob", "2012-01-18"}, {"grades", new List<double> {9.0, 9.1, 9.0, 9.1} } }
    ];

    delegate void PrintFunction(Dictionary<string, object> student);

    static Action<List<Dictionary<string, object>>> HigherOrderFun(string msg, PrintFunction printFn) {
        void wrapper(List<Dictionary<string, object>> students) {
            Console.WriteLine($"\n----\n{msg}");
            foreach (var student in students) {
                printFn(student);
            }
        }

        return wrapper;
    }


    static void PrintGradePointAverage(Dictionary<string, object> student) {
        var grades = (List<double>)student["grades"];
        double averageGrade = grades.Sum() / grades.Count;
        Console.WriteLine($"{student["name"]} {averageGrade}");
    }

    static void PrintTopStudents(Dictionary<string, object> student) {
        var grades = (List<double>)student["grades"];
        double average = grades.Sum() / grades.Count;
        if (average >= 9) {
            Console.WriteLine(student["name"]);
        }
    }

    static void PrintBirthOrder(Dictionary<string, object> student) {
        Console.WriteLine($"{student["name"]} {student["dob"]}");
    }

    static void PrintHighestGrade(Dictionary<string, object> student) {
        double  maxGrade = ((List<double>)student["grades"]).Max();
        Console.WriteLine($"{student["name"]} {maxGrade}");
    }

    static void Main() {
        Console.WriteLine("EJERCICIO #1");
        var addFunc = ArithmeticOp(Add);
        var subtractFunc = ArithmeticOp(Subtract); 
        var multiplyFunc = ArithmeticOp(Multiply);

        Console.WriteLine(addFunc(3, 5));
        Console.WriteLine(subtractFunc(10, 3));
        Console.WriteLine(multiplyFunc(2, 4));

        Console.WriteLine("EJERCICIO #2");
        var gradePointAverage = HigherOrderFun("Promedio calificaciones", PrintGradePointAverage);
        var topStudents = HigherOrderFun("Mejores estudiantes:", PrintTopStudents);
        var birthOrder = HigherOrderFun("Por nacimiento:", PrintBirthOrder);
        var highestGrade = HigherOrderFun("Mayor calificación:", PrintHighestGrade);

        gradePointAverage(studentsList);
        topStudents(studentsList);
        birthOrder([.. studentsList.OrderBy(student => (string)student["dob"])]);
        highestGrade(studentsList);

    }
}
