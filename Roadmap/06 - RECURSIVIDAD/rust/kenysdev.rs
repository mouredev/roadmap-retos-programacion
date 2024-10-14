/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* RECURSIVIDAD
-----------------------------------------
- La recursividad es la capacidad de una función para llamarse a sí misma,ya sea 
  de forma directa o indirecta, con el propósito de resolver un problema.
*/
fn main() {
    // __________________________________
    // Recursividad directa(es una función se llama a sí misma.)
    // imprimiendo números del 100 al 0.
    fn num(n: i16) {
        println!("{n}");
        // Caso base(evitar repetición indefinida)
        if n > 0 {
            num(n - 1);
        }
    }

    num(100);

    // __________________________________
    // Recursividad indirecta(Cuando varias funciones se llamen entre sí.)
    // imprimiendo números de 100 al 0 e indicar si es par.
    fn is_even(n: i16) {
        if n %2 == 0 {
            write(n, true);
        } else {
            write(n, false)
        }              
    }

    fn write(n: i16, even: bool) {
        println!("- {n} -> es par?: {even}");
        if n > 0 {
            is_even(n - 1)
        }
    }

    is_even(100);

    // __________________________________
    // EJERCICIO
    // Calcular el factorial de un número concreto (la función recibe ese número).
    // 4! = 4 * 3 * 2 * 1 = 24
    fn factorial(n: i32) -> i32{
        if n != 0 {
            n * factorial(n - 1)
        } else {
            1
        }
    }
    /* explicación
    fac(4)
        | = 24 
     return 4 * fac(3) ->(4 * 6)
                  | = 6 
         return 3 * fac(2) ->(3 * 2)
                      | = 2 
             return 2 * fac(1) ->(2 * 1)
                          | = 1 
                 return 1 * fac(0) ->(1 * 1)
                              | = return 1 -> caso base
    */

    println!("Factorial de 4: {}", factorial(4));

    /* __________________________________
    * - Calcular el valor de un elemento concreto (según su posición) en la 
        sucesión de Fibonacci (la función recibe la posición).
    * n : |0|1|2|3|4|5|6|...
    * fb: |0|1|1|2|3|5|8|...
    *      |+|=^   |+|=^ ...
    */

    fn fibonacci(n: i16) -> i16{
        if n <= 1 {
            return  n;
        } else {
            fibonacci(n - 1) + fibonacci(n - 2)
        }
    }

    /* explicación fb(4)
                            return 3
                  fib(3)      / \    fib(2)
                   / \ =2      +      / \ =1
             fib(2) + fib(1)    fib(1) + fib(0) -> caso base
              / \ =1
        fib(1) + fib(0) -> caso base

    NOTE: Esto es ineficiente para valores grandes de "n".
    */

    println!("fibonacci(4): {}", fibonacci(4));
}

