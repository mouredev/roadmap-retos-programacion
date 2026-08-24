// https://www.typescriptlang.org/

// Error forzado: división por cero
try {
  const result = 10 / 0;
  if (!isFinite(result)) throw new Error("División por cero");
  console.log(result);
} catch (e) {
  console.log(e);
} finally {
  console.log("Bloque finally ejecutado");
}

// Error forzado: acceso a índice inválido
try {
  const arr: number[] = [1, 2, 3];
  const val = arr[10];
  if (val === undefined) throw new RangeError("Índice fuera de rango");
  console.log(val);
} catch (e) {
  console.log(e);
}

// Dificultad extra: función con tres tipos de excepción

class ValidationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "ValidationError";
  }
}

function riskyOperation(a: number, b: number, index: number): void {
  const arr: number[] = [10, 20, 30];

  if (b === 0) {
    throw new RangeError("No se puede dividir por cero");
  }

  if (arr[index] === undefined) {
    throw new TypeError("Índice inválido en el array");
  }

  if (a < 0) {
    throw new ValidationError("El valor de 'a' no puede ser negativo");
  }

  console.log(`Resultado: ${arr[index] / b + a}`);
}

function runOperation(a: number, b: number, index: number): void {
  try {
    riskyOperation(a, b, index);
    console.log("Operación completada sin errores");
  } catch (e) {
    if (e instanceof ValidationError) {
      console.log(`ValidationError: ${e.message}`);
    } else if (e instanceof TypeError) {
      console.log(`TypeError: ${e.message}`);
    } else if (e instanceof RangeError) {
      console.log(`RangeError: ${e.message}`);
    }
  } finally {
    console.log("---");
  }
}

runOperation(5, 2, 1);
runOperation(5, 0, 1);
runOperation(5, 2, 9);
runOperation(-1, 2, 1);
