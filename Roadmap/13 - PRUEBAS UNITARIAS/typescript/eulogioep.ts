// Definimos un tipo para las funciones matemáticas
type MathFunction = (a: number, b: number) => number;

/**
 * Función que suma dos números y retorna el resultado.
 * @param a Primer número a sumar.
 * @param b Segundo número a sumar.
 * @returns La suma de a y b.
 */
const suma: MathFunction = (a, b) => {
    return a + b;
};

/**
 * Enum para los lenguajes de programación
 */
enum ProgrammingLanguage {
    TypeScript = "TypeScript",
    JavaScript = "JavaScript",
    Python = "Python"
}

/**
 * Interfaz que define la estructura del objeto de datos personales.
 */
interface DatosPersonales {
    readonly name: string;
    age: number;
    birth_date: string;
    programming_languages: ProgrammingLanguage[];
}

/**
 * Crea y retorna un objeto con datos personales.
 * @returns Objeto con datos personales.
 */
function crearObjeto(): DatosPersonales {
    return {
        name: "Tu nombre",
        age: 30,
        birth_date: "1993-01-01",
        programming_languages: [ProgrammingLanguage.TypeScript, ProgrammingLanguage.JavaScript, ProgrammingLanguage.Python]
    };
}

// Pruebas unitarias (usando una sintaxis similar a Jest, pero sin importar la librería)
describe('Pruebas de la función suma', () => {
    test('Suma de 2 y 3 debería ser 5', () => {
        expect(suma(2, 3)).toBe(5);
    });

    test('Suma de -1 y 1 debería ser 0', () => {
        expect(suma(-1, 1)).toBe(0);
    });

    test('Suma de -2 y -3 debería ser -5', () => {
        expect(suma(-2, -3)).toBe(-5);
    });
});

describe('Pruebas del objeto de datos personales', () => {
    const objeto: DatosPersonales = crearObjeto();

    test('El objeto debe contener todas las propiedades requeridas', () => {
        expect(objeto).toHaveProperty('name');
        expect(objeto).toHaveProperty('age');
        expect(objeto).toHaveProperty('birth_date');
        expect(objeto).toHaveProperty('programming_languages');
    });

    test('Los datos en el objeto deben ser correctos', () => {
        expect(objeto.name).toBe("Tu nombre");
        expect(typeof objeto.age).toBe('number');
        expect(objeto.birth_date).toMatch(/^\d{4}-\d{2}-\d{2}$/);
        expect(Array.isArray(objeto.programming_languages)).toBe(true);
        expect(objeto.programming_languages.length).toBeGreaterThan(0);
        expect(objeto.programming_languages).toContain(ProgrammingLanguage.TypeScript);
    });
});

// Nota: Las funciones 'describe', 'test', 'expect', etc. no están definidas aquí.
// En un entorno real, necesitarías importar estas funciones de una biblioteca de pruebas.