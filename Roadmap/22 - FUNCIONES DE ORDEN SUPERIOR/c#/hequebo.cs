class Program
{
    static void Main(string[] args)
    {
        /*
         * Una función de orden superior o HOF por sus siglas
         * en inglés es una función la cual recibe en sus
         * argumentos una o más funciones o regresa una función
         * o ambos
         */
        Console.WriteLine($"{Operation(3, 6, Addition)}");
        Console.WriteLine($"{Operation(3, 6, Substraction)}");
        Console.WriteLine($"{Operation(3, 6, Multiplication)}");

        // Ejercicio Extra
        Console.ReadLine();
        Console.Clear();
        var students = new List<Student>
        {
           new Student
           {
               Name ="Emilio Quezada", 
               Birthdate = new DateTime(1997, 07, 28),
               Grades= new List<decimal>{8.5m, 9.8m, 8.3m, 8.5m }
           },
           new Student
           {
               Name ="Aldo Díaz",
               Birthdate = new DateTime(1998, 10, 5),
               Grades= new List<decimal>{9.5m, 9.9m, 8.3m, 8.9m }
           },
           new Student
           {
               Name ="Samantha Ortega",
               Birthdate = new DateTime(1997, 03, 30),
               Grades= new List<decimal>{8.6m, 9, 9.5m, 8.5m }
           },
        };
        /*
         * En .Net LINQ utiiliza funciones de orden superarior en las cuales reciben dentro
         * de sus parámetros una expresión lambda
         */
        var averageList = students.Select(s => new { Name = s.Name, Average = Average(s.Grades) });
        Console.WriteLine("---Promedios estudiantes---");
        foreach (var student in averageList )
            Console.WriteLine($"Nombre: {student.Name}, Promerdio: {student.Average}");
        
        Console.WriteLine("---Cuadro de honor---");
        var bestStudents = students.Where(s => Average(s.Grades) >= 9).Select(s => new { Name = s.Name, Average = Average(s.Grades)});
        foreach (var student in bestStudents)
            Console.WriteLine($"Nombre: {student.Name}, Promedio: {student.Average}");
        
        Console.WriteLine("---Estudiante ordenados por edad---");
        var orderedStudents = students.OrderBy(s => s.Birthdate);
        foreach (var student in orderedStudents)
            Console.WriteLine($"Nombre: {student.Name}, Fecha de Nacimiento: {student.Birthdate.ToShortDateString()}");

        Console.WriteLine("---Estudiate con calificación más alta---");
        var highestGrade = students.OrderByDescending(s => Max(s.Grades)).Select(s => new { Name = s.Name, Grade = Max(s.Grades) }).First();
        Console.WriteLine($"Nombre: {highestGrade.Name}, Calificación: {highestGrade.Grade}");

    }
    static int Addition(int x,  int y) => x + y;
    static int Substraction(int x, int y) => x - y;
    static int Multiplication(int x, int y) => x * y;
    /*
     * La función Operation recibe en sus argumentos
     * dos datos de tipo entero y una funcion(Func)
     * la cual recibe dos datos de tipo entero y 
     * devuelve un tipo entero. 
     * Así mismo la función Operation devuelve una 
     * función.
     */
    static int Operation(int x, int y, Func<int, int, int> fn) => fn(x, y);
    static decimal Average(List<decimal> grades) => grades.Sum() / grades.Count;
    static decimal Max(List<decimal> grades) => grades.Max(g => g);
    

}
class Student
{
    public string Name { get; set; }
    public DateTime Birthdate { get; set; }
    public List<decimal> Grades { get; set; }
}
