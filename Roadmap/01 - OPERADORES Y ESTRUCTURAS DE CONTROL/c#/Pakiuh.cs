// Operadores de asignación
int x1 = 10; // asignación
x1 += 5; // suma y asignación
x1 -= 2; // resta y asignación
x1 *= 3; // multiplicación y asignación
x1 /= 2; // división y asignación
x1 %= 3; // módulo y asignación

// Operadores aritméticos
int y1 = x1 + 5; // suma
int z = x1 - y1; // resta
int a = x1 * y1; // multiplicación
int b = x1 / y1; // división
int c = x1 % y1; // módulo
int d = x1++; // incremento
int e = y1--; // decremento

// Operadores de comparación
bool isEqual = x1 == y1; // igual a
bool isNotEqual = x1 != y1; // no igual a
bool isGreaterThan = x1 > y1; // mayor que
bool isLessThan = x1 < y1; // menor que
bool isGreaterThanOrEqual = x1 >= y1; // mayor o igual que
bool isLessThanOrEqual = x1 <= y1; // menor o igual que

// Operadores lógicos
bool and = x1 > 5 && y1 < 10; // y lógico
bool or = x1 > 5 || y1 < 10; // o lógico
bool not = !(x1 == y1); // no lógico

// Operador ternario
string result = x1 > y1 ? "x es mayor que y" : "x no es mayor que y";

// Operadores de bits
int shiftLeft = x1 << 2; // desplazamiento a la izquierda
int shiftRight = x1 >> 2; // desplazamiento a la derecha
int bitwiseAnd = x1 & y1; // y a nivel de bits
int bitwiseOr = x1 | y1; // o a nivel de bits
int bitwiseXor = x1 ^ y1; // xor a nivel de bits
int bitwiseNot = ~x1; // no a nivel de bits

// Declaraciones condicionales
int x2 = 10;
if (x2 > 5) {
    Console.WriteLine("x es mayor que 5");
} else if (x2 < 5) {
    Console.WriteLine("x es menor que 5");
} else {
    Console.WriteLine("x es igual a 5");
}

// Declaración switch
switch (x2) {
    case 5:
        Console.WriteLine("x es 5");
        break;
    case 10:
        Console.WriteLine("x es 10");
        break;
    default:
        Console.WriteLine("x no es ni 5 ni 10");
        break;
}

// Bucle for
for (int i = 0; i < 5; i++) {
    Console.WriteLine("El valor de i es: " + i);
}

// Bucle while
int j = 0;
while (j < 5) {
    Console.WriteLine("El valor de j es: " + j);
    j++;
}

// Bucle do while
int k = 0;
do {
    Console.WriteLine("El valor de k es: " + k);
    k++;
} while (k < 5);

// Manejo de excepciones
try {
    int y2 = x2 / 0; // Dividir por cero lanzará una excepción
} catch (DivideByZeroException error) {
    Console.WriteLine("Ha ocurrido un error: " + error.Message);
} finally {
    Console.WriteLine("Este bloque se ejecuta independientemente de si se produjo una excepción o no");
}

// Dificulata Extra
for (int i = 10; i <= 55; i++) {
    if (i % 2 == 0 && i != 16 && i % 3 != 0) {
        Console.WriteLine(i);
    }
}