int cola[5]; // Declara una cola de enteros
int pila[5]; // Declara una pila de tamaño 5
int frente = -1; // Inicializa el índice del frente de la cola
int final = -1; // Inicializa el índice del final de la cola
int top = -1; // Inicializa el índice superior de la pila

void setup() {
  Serial.begin(9600);

  // Simula la adición de datos a la pila
  for (int i = 1; i <= 5; i++) {
    if (!pilaLlena()) {
      push(i * 10); // Agrega valores multiplicados por 10 a la pila
      Serial.println("Añadido a la pila: " + String(i * 10));
    } else {
      Serial.println("La pila está llena. No se puede añadir más.");
    }
  }

  Serial.println("------------------");

  // Simula la adición de datos a la cola
  for (int i = 1; i <= 5; i++) {
    if (!colaLlena()) {
      encolar(i * 5); // Agrega valores multiplicados por 5 a la cola
      Serial.println("Añadido a la cola: " + String(i * 5));
    } else {
      Serial.println("La cola está llena. No se puede añadir más.");
    }
  }

  Serial.println("------------------");

  // Simula la eliminación de elementos de la pila
  while (!pilaVacia()) {
    int valor = pop();
    Serial.println("Eliminado de la pila: " + String(valor));
  }

  Serial.println("------------------");

  // Simula la eliminación de elementos de la cola
  while (!colaVacia()) {
    int valor = desencolar();
    Serial.println("Eliminado de la cola: " + String(valor));
  }
}

void loop() {
  // El loop está vacío ya que la lógica principal se ejecutó en el setup
}

void push(int dato) {
  if (!pilaLlena()) {
    top++;
    pila[top] = dato;
  }
}

int pop() {
  if (!pilaVacia()) {
    int valor = pila[top];
    top--;
    return valor;
  }
  return -1; // Valor de error (pila vacía)
}

bool pilaLlena() {
  return top == 4; // Tamaño de la pila - 1
}

bool pilaVacia() {
  return top == -1;
}

void encolar(int dato) {
  if (!colaLlena()) {
    if (frente == -1) {
      frente = 0;
    }
    final = (final + 1) % 5;
    cola[final] = dato;
  }
}

int desencolar() {
  if (!colaVacia()) {
    int valor = cola[frente];
    if (frente == final) {
      frente = -1;
      final = -1;
    } else {
      frente = (frente + 1) % 5;
    }
    return valor;
  }
  return -1; // Valor de error (cola vacía)
}

bool colaLlena() {
  return (frente == 0 && final == 4) || (frente == final + 1);
}

bool colaVacia() {
  return frente == -1;
}
