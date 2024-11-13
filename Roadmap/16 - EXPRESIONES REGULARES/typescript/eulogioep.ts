/**
 * Ejercicio de Expresiones Regulares en TypeScript
 * 
 * Este script demuestra el uso de expresiones regulares para:
 * 1. Extraer números de un texto
 * 2. Validar direcciones de email
 * 3. Validar números de teléfono
 * 4. Validar URLs
 */

// Texto de ejemplo para probar las expresiones regulares
const textoEjemplo: string = `Hola, tengo 25 años y mi número es 123-456-789. 
También puedes contactarme al +34 611 222 333 o por email a usuario@dominio.com. 
Visita mi página web en https://www.ejemplo.com para más información. 
Hay 42 razones para usar expresiones regulares y 100 formas de aplicarlas.`;

/**
 * Interfaz para los resultados de validación
 */
interface ResultadoValidacion {
    valor: string;
    esValido: boolean;
}

/**
 * 1. Clase para manejar la extracción de números
 */
class ExtractorNumeros {
    private static readonly PATRON: RegExp = /\b\d+\b/g;

    /**
     * Extrae todos los números de un texto dado
     * @param texto - El texto del que extraer los números
     * @returns Un array con todos los números encontrados
     */
    public static extraer(texto: string): string[] {
        return texto.match(this.PATRON) || [];
    }
}

/**
 * 2. Clase para validación de email
 */
class ValidadorEmail {
    private static readonly PATRON: RegExp = /^[\w.-]+@[\w.-]+\.\w+$/;

    /**
     * Valida una dirección de email
     * @param email - El email a validar
     * @returns Un objeto ResultadoValidacion con el resultado
     */
    public static validar(email: string): ResultadoValidacion {
        return {
            valor: email,
            esValido: this.PATRON.test(email)
        };
    }
}

/**
 * 3. Clase para validación de números de teléfono
 */
class ValidadorTelefono {
    private static readonly PATRON: RegExp = /^(\+\d{1,3}\s?)?(\d{3}[-\s]?){2}\d{3}$/;

    /**
     * Valida un número de teléfono
     * @param telefono - El número de teléfono a validar
     * @returns Un objeto ResultadoValidacion con el resultado
     */
    public static validar(telefono: string): ResultadoValidacion {
        return {
            valor: telefono,
            esValido: this.PATRON.test(telefono)
        };
    }
}

/**
 * 4. Clase para validación de URLs
 */
class ValidadorURL {
    private static readonly PATRON: RegExp = /^https?:\/\/(www\.)?[\w.-]+\.\w{2,}$/;

    /**
     * Valida una URL
     * @param url - La URL a validar
     * @returns Un objeto ResultadoValidacion con el resultado
     */
    public static validar(url: string): ResultadoValidacion {
        return {
            valor: url,
            esValido: this.PATRON.test(url)
        };
    }
}

/**
 * Función para imprimir los resultados de validación
 */
function imprimirResultados(titulo: string, resultados: ResultadoValidacion[]): void {
    console.log(`\n${titulo}`);
    resultados.forEach(({ valor, esValido }) => {
        console.log(`${valor} es ${esValido ? 'válido' : 'inválido'}`);
    });
}

// Ejecución de pruebas
function ejecutarPruebas(): void {
    console.log('=== PRUEBAS DE EXPRESIONES REGULARES ===');

    // 1. Extraer números
    const numerosEncontrados: string[] = ExtractorNumeros.extraer(textoEjemplo);
    console.log('\n1. Números encontrados:');
    numerosEncontrados.forEach(numero => console.log(numero));

    // 2. Validar emails
    const emails: string[] = ['usuario@dominio.com', 'email_invalido.com', 'test@test.co.uk'];
    const resultadosEmail: ResultadoValidacion[] = emails.map(email => ValidadorEmail.validar(email));
    imprimirResultados('2. Validación de emails:', resultadosEmail);

    // 3. Validar números de teléfono
    const telefonos: string[] = ['123-456-789', '+34 611 222 333', '1234', '999-999-999'];
    const resultadosTelefono: ResultadoValidacion[] = telefonos.map(tel => ValidadorTelefono.validar(tel));
    imprimirResultados('3. Validación de números de teléfono:', resultadosTelefono);

    // 4. Validar URLs
    const urls: string[] = ['https://www.ejemplo.com', 'http://ejemplo', 'https://dominio.es'];
    const resultadosURL: ResultadoValidacion[] = urls.map(url => ValidadorURL.validar(url));
    imprimirResultados('4. Validación de URLs:', resultadosURL);
}

// Ejecutar todas las pruebas
ejecutarPruebas();