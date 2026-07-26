// Operadores aritmeticos 
int a = 10;
int b = 3;
int suma = a + b;
int resta = a - b;
int multiplicacion = a * b;
int division = a / b;
int residuo = a % b; 

//Operadores logicos && en boolean 
boolean tieneFondos = true;
boolean productoDisponible;

//Ambas de ven ser true para complir con la condición 
boolean puedeComprar = tieneFondos && productoDisponible; 
System.out.println(puedeComprar); // Imprime true 


//Operador con or || 
boolean tieneBeca = false; 
boolean tieneDescuento = true;

// Este operador devuelve verdadero cuando al menos una condicion es verdadera

if (tieneBeca || tieneDescuento) {
	System.out.println("Obtiene descuento");
}
//Operador NOT ! este operador invierte el valor 

boolean llueve = false;

if (!llueve) {
System.out.println("Podemos salir);
}

/*Operadores de comparación 
* 5 == 5 devuelve true 
* 5 != 3 devuelve true 
* 10 > 5 devuelve true 
*4 < 8  devuelve true 
* 5 >= 5 devuelve true 
3 <= 7 devuelve true */

int x = 10;
int y = 20;

boolean esMayo  = x > y;  //false
boolean esDiferente = x != y;   //true 

if (x <= y) {
System.oprintln ("x es menor o igual que y");
}

//Operadores de asignación 
int total = 0; // Asignación simple 

total += a; // 'total' ahora vale 10 (0 +10)
total -= b; // ´total' ahora vale 7 (10 - 3)
total *= 2; // 'total' ahora vale 14 (7 * 2)

System.out.println(total); //Imprime 14

//Tipos de incremento y decremento 
int contador = 10; 
contador++; // suma 1
contador--; // resta 1.


// Operador de identidad 
String texto1 = new String("hola");
String texto2 = new String("hola");
String texto3 = texto1;

boolean mismaIdentidad = (texto1 == texto3); // ture (apunta al mismo objeto 
boolean distintaIdentidad = (texto1 == texto2); //false (son objetos difeentes en memoria, aunqye tengan el mismo

/* Operadores de pertenencia se utilizan diferentes metodos y un operador específico instanceof este operador 
* pertenece a un tipo/clase */

String texto = "Hola";

// Verifia si el objeto pertenece a la clase String
boolean esCadena = texto instanceof String; //true 

//metodo contains pertenece a colecciones 
import java.util.ArraisList;
import java.util.List;

List<String> listaDeNombres = new ArraysList<>();
listaDeNombres.add("Ana");
listaDeNombres.add("Pedro");

//Verifica si "Ana " pertenece a la lista 
boolean perteneceALista = listaDeNombres.contains("Ana"); // true 

//Pertenencia en arreglo Arrays 
import java.util.Arrays;
int[] numeros ={1, 2, 3, 4, 5};

//Una forma rapida es convertirlo temporalmente a lista o usar streams 
boolean contieneNumero = Arrays.stream(numeros).anyMatch(n -> n == 3); //true

// Operadores a nivel de bits (Bitwise)
int bitA = 5;  // En binario: 0000 0101
int bitB = 3;  // En binario: 0000 0011

// AND (&) -> 0000 0001 (1 en decimal)
int resultadoAnd = bitA & bitB; 

// OR (|) -> 0000 0111 (7 en decimal)
int resultadoOr = bitA | bitB; 

// XOR (^) -> 0000 0110 (6 en decimal)
int resultadoXor = bitA ^ bitB; 

// NOT (~) -> Invierter todos los bits
int resultadoNot = ~bitA; 

// Desplazamiento a la izquierda (<<) -> 0000 1010 (10 en decimal)
int desplazarIzquierda = bitA << 1; 

// Desplazamiento a la derecha con signo (>>) -> 0000 0010 (2 en decimal)
int desplazarDerecha = bitA >> 1;

// Desplazamiento a la derecha sin signo (>>>)
int desplazarDerechaSinSigno = bitA >>> 1;

// === Estrucutras de control ===

// 1. CONDICIONALES 
int edad = 18;

if (edad >= 18) {
  System.out.println("Eres mayor de edad");
} else {
System.out.println("Eres menor de edad. ");
}

String dia = "Lunes";
switch (dia) {
case "Lunes":
  System.out.println("Inicio de semana. ");
  break;
case "Viernes":
  System.out.println("Casi fin de semana. ");
  break;
default:
  System.out.println("Otro dia de la semana. "); 
}

// 2. ITERATIVAS (Bucles)
// For 
System.out.println("Bucle FOR (DEL Q AL 3):");
for (int i = 1; i <= 3 ; i++) {
  System.out.println("Contador: " + i);
}
// WHILE
 System.out.println("Bucle WHILE: ");
int contadorWhile = 1;
while (contadorWhile <= 3) {
System.out.println("While: " + contadorWhile); 
contadorWhile ++;
}

// Bucle DO-WHILE 
int contadorDO = 1;
do {
System.out.println("Do-While:  " + contadorDo);
contadorDo++;
} while (contadorDo <= 3);

// 3. EXCEPCIONES 
try {
int numero = 10;
int resultado = numero / 0; // Esto va a generar un error ( no se puede dividir por cero)
} catch (ArithmeticException e) {
System.out.println("¡Error capturado! No se puede dividir por cero. "); 
}

// === DIFICULTAD ESTRA ===
for (int i = 10; i <=55; i++) {
//Si es par y además no es 16 y admea sno se puede dividir entre 3...
if (i % 2 == 0 && i != 16 && i % 3 !=0) {
System.out.println(i);
}
}


