// ----FUNCIONES BASICAS----
// Sin parametros ni retorno

pubic static void saludar() {
System.out.println("¡Hola! Que tengas un buen dia".);
}

//Con parametros sin retornos

public static void saludarPersona(String nombre) {
System.out.println("¡Hola!, " + nombre + "¡Bienvenido!"):
}

//Sin parametros, con retorno
public static double obtenerNumeroPi() {
retrun 3.1416;
}

//Con parametros y con retorno
public static int sumarNumeros(int numeroA, int numeroB) {
int resultado = numaroA + numeroB;
return resultado;
}

//Funciones dentro de funciones

import java.util.function.Function;

public static void ejemploFuncionInterna() {
//Esto es lo mas cercano a una funcion
Function<Integer, Integer> duplicar = (numero) -> numero * 2;

int resultado = duplicar.apply(5);
System.out.println("Resultado de funcion interna (lambda): " + resultado);
}

// Funciones nativas
public static void ejemploFuncionesNativas() {
//calcular raiz cuadrada
double raiz = Math.sqrt(25);
System.out.println("La raiz cuadrada de 25 es : " + raiz);

//Convertir un texto completo a mayusculas
String texto = "hola mundo";
String textoMayuscula = texto.toUpperCase();
System.out.println("Texto convertido: " + textoMayuscula);
}


// Variable global
public static String variableGlobal = " Pueden verme de donde sea. ";

//Variable local
public static void pruebaVariable () {
String variableLocal = "Soy local y existo en este metodo. ";

System.out.println(variableGlobal);
System.out.println(variableLocal);
}

public static void otroMetodo() {
System.out.println(variableGlobal); // Imprime sin problemas
System.out.println(variableLocal); // Aqui da un ERROR aquí no existe
}


// ---Dificultad extra---

public static int retoFizzBuzz(String textoUno,  String textoDos) {
int contadorNumeros = 0;

for (int i = 1; i <= 100; i++) {
  if (i % 3 == 0 && i % 5 == 0) {
System.out.println(textoUno + textoDos);
} else if (i % 3 == 0) {
System.out.println(textoUno);
} else if ( i % 5 == 0) {
System.out.println(textoDos);
} else {
System.out.println(i);
contadorNumeros++;
}
}

return contadorNumeros;
}



