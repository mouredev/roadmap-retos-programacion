// Enlance oficial para aprender sobre Arduino: https://www.arduino.cc/en/Guide
// Este es un comentario en una sola linea
/*
	Este es un comentario en varias lineas
	Este es otro comentario en varias lineas
*/

// Esta es una variable global
int globalVariable = 0;

void setup() {
  // Esta es una variable local
	int localVariable = 2;
	// Esta es una constante
	const int constantVariable = 3;  // Su valor no puede cambiar

	// Tipos de datos primitivos
	bool booleanVariable = true;  // true o false
	char charVariable = 'a';  // Un solo caracter
	int intVariable = 1;  // Entero
	float floatVariable = 1.0;  // Decimal
	double doubleVariable = 1.0;  // Decimal con mayor precision

	// Tipos de datos compuestos
	const char *stringVariable = "Hola mundo";  // Cadena de caracteres
	String stringVariable2 = "Hola mundo";  // Cadena de caracteres
	const char arrayVariable[] = "Hola mundo";  // Arreglo de caracteres
	int arrayVariable2[] = {1, 2, 3};  // Arreglo de enteros

	Serial.begin(9600);  // Inicializa el puerto serial
}

void loop() {
	Serial.println("Hola Arduino!");	// Imprime en el puerto serial
	delay(1000);  // Espera 1 segundo
}
