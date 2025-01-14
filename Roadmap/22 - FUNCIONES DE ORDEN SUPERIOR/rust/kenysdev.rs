/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* FUNCIONES DE ORDEN SUPERIOR
-----------------------------------------

* EJERCICIO #1:
* Explora el concepto de funciones de orden superior en tu lenguaje 
* creando ejemplos simples (a tu elección) que muestren su funcionamiento.
*/

type ArithmeticOperation = fn(i32, i32) -> i32;

fn arithmetic_op(operation: ArithmeticOperation) -> impl Fn(i32, i32) -> i32 {
    move |x, y| operation(x, y)
}

fn add(x: i32, y: i32) -> i32 {
    x + y
}

fn subtract(x: i32, y: i32) -> i32 {
    x - y
}

fn multiply(x: i32, y: i32) -> i32 {
    x * y
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

type Student = (String, String, Vec<f64>);

type PrintFunction<'a> = fn(&'a Student);

fn higher_order_fun<'a>(msg: &'static str, print_fn: PrintFunction<'a>) -> impl Fn(&'a Vec<Student>) + 'a {
    move |students: &'a Vec<Student>| {
        println!("\n----\n{}", msg);
        for student in students {
            print_fn(student);
        }
    }
}
fn print_grade_point_average(student: &Student) {
    let (name, _, grades) = student;
    let average_grade: f64 = grades.iter().sum::<f64>() / grades.len() as f64;
    println!("{} {}", name, average_grade);
}

fn print_top_students(student: &Student) {
    let (name, _, grades) = student;
    let average: f64 = grades.iter().sum::<f64>() / grades.len() as f64;
    if average >= 9.0 {
        println!("{}", name);
    }
}

fn print_birth_order(student: &Student) {
    let (name, dob, _) = student;
    println!("{} {}", name, dob);
}

fn print_highest_grade(student: &Student) {
    let (name, _, grades) = student;
    let max_grade = grades.iter().fold(f64::MIN, |max, &grade| max.max(grade));
    println!("{} {}", name, max_grade);
}


fn main() {

    println!("EJERCICIO #1");

    let add_func = arithmetic_op(add);
    let subtract_func = arithmetic_op(subtract);
    let multiply_func = arithmetic_op(multiply);

    println!("{}", add_func(3, 5));
    println!("{}", subtract_func(10, 3));
    println!("{}", multiply_func(2, 4));
    

    //_______________________________________________________________________________
    println!("EJERCICIO #2");

    let students_list = vec![
        ("Ken".to_string(), "2012-04-21".to_string(), vec![9.5, 9.4, 9.3, 9.2]),
        ("Ben".to_string(), "2012-03-20".to_string(), vec![8.5, 8.4, 8.3, 8.2]),
        ("Ada".to_string(), "2012-02-19".to_string(), vec![7.5, 7.4, 7.3, 7.2]),
        ("Zoe".to_string(), "2012-01-18".to_string(), vec![9.0, 9.1, 9.0, 9.1]),
    ];

    let grade_point_average = higher_order_fun("Promedio calificaciones:", print_grade_point_average);
    let top_students = higher_order_fun("Mejores estudiantes:", print_top_students);
    let highest_grade = higher_order_fun("Mayor calificación:", print_highest_grade);

    grade_point_average(&students_list);
    top_students(&students_list);

    let sorted_students: Vec<(String, String, Vec<f64>)> = {
        let mut sorted_students = students_list.clone();
        sorted_students.sort_by(|a, b| a.1.cmp(&b.1));
        sorted_students
    };

    let birth_order = higher_order_fun("Por nacimiento:", print_birth_order);
    birth_order(&sorted_students);

    highest_grade(&students_list);
 
}
