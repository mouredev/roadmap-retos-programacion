/**
 * 02 FUNCIONES Y ALCANCE
 *
 * @author martinbohorquez
 */
class martinbohorquez {

    /**
     * Ejemplo de Método estático, sin retorno y sin parámetros.
     */
    static saludar(): void {
        console.log("Hola, TypeScript!");
    }

    /**
     * Ejemplo de Método estático, sin retorno, con parámetros.
     *
     * @param name tipo string.
     */
    static saludarWithName(name: string): void {
        console.log(`Hola, ${name}!`);
    }

    /**
     * Ejemplo de Método estático, con retorno y sin parámetros.
     *
     * @return tipo string.
     */
    static saludarKotlin(): string {
        return "Hola, Kotlin!";
    }

    /**
     * Ejemplo de Método estático, con retorno y parámetros.
     *
     * @param salario tipo number.
     * @param percentAhorro tipo number.
     * @return ahorro mensual, tipo number.
     */
    static calcularAhorroMensual(salario: number, percentAhorro: number): number {
        return salario * percentAhorro;
    }

    /**
     * Método con retorno y parámetros.
     *
     * @param ahorroMensual tipo number.
     * @param tasaAnual tipo number.
     * @param periodos tipo number.
     * @return ahorro total, tipo number.
     */

    /**
     * Método con retorno y parámetros.
     *
     * @param salario tipo number.
     * @param percentAhorro tipo number.
     * @param tasaAnual tipo number.
     * @param periodos tipo number.
     * @return ahorro total, tipo number.
     */

    calcularAhorro(param1: number, param2: number, param3: number, param4?: number): number {
        if (param4 !== undefined) {
            // Lógica para el cálculo basado en salario, percentAhorro, tasaAnual, periodos
            const pago = martinbohorquez.calcularAhorroMensual(param1, param2);
            return this.calcularAhorro(pago, param3, param4);
        } else {
            // Lógica para el cálculo basado en ahorroMensual, tasaAnual, periodos
            const periodosPorAnio = 12; // Capitalización mensual
            const tasaMensual = Math.pow(1 + param2, 1 / periodosPorAnio) - 1; // Tasa mensual
            return param1 * ((Math.pow(1 + tasaMensual, param3) - 1) / tasaMensual);
        }
    }

    /**
     * DIFICULTAD EXTRA (Ejercicio fizz buzz)
     *
     * @param texto1 el texto para los divisores de 3.
     * @param texto2 el texto para los divisores de 5.
     * @return el número de veces que mostró números y no texto.
     */
    fizzBuzz(texto1: string, texto2: string): number {
        let counter = 0;
        let result: string;

        for (let i = 1; i <= 100; i++) {
            result = "";

            if (i % 3 === 0) {
                result += texto1;
            }

            if (i % 5 === 0) {
                result += texto2;
            }

            if (result === "") {
                result = i.toString();
                counter++;
            }

            console.log(result);
        }
        return counter;
    }
}


/**
 * Método principal
 */
function main(): void {
    console.log("---- SALUDAR ----");
    martinbohorquez.saludar();
    martinbohorquez.saludarWithName("Python");
    martinbohorquez.saludarWithName("Typescript");
    console.log(martinbohorquez.saludarKotlin());

    console.log("---- CALCULAR AHORRO ----");
    let salario = 4000;
    let percentAhorro = 62.5 / 100;
    let tasaAnual = 8.00 / 100;
    let periodos = 3 * 12;

    const df = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });
    const dfp = new Intl.NumberFormat('en-US', { style: 'percent', minimumFractionDigits: 2 });

    console.log("Salario: " + df.format(salario));
    console.log("Porcentaje de ahorro (%): " + dfp.format(percentAhorro));
    console.log("Periodos de ahorro (meses): " + periodos);
    console.log("Tasa de interés anual (%): " + dfp.format(tasaAnual));

    const ahorroMensual = martinbohorquez.calcularAhorroMensual(salario, percentAhorro);
    console.log("El ahorro mensual: " + df.format(ahorroMensual));

    // Crear instancia
    const mbohorquez = new martinbohorquez();
    const ahorroTotal = mbohorquez.calcularAhorro(ahorroMensual, tasaAnual, periodos);
    console.log("El ahorro total generado es: " + df.format(ahorroTotal));
    console.log();

    salario = 1500;
    percentAhorro = 67.5 / 100;
    tasaAnual = 7.50 / 100;
    periodos = 2 * 12;

    console.log("Salario: " + df.format(salario));
    console.log("Porcentaje de ahorro (%): " + dfp.format(percentAhorro));
    console.log("Periodos de ahorro (meses): " + periodos);
    console.log("Tasa de interés anual (%): " + dfp.format(tasaAnual));

    const ahorroTotal2 = mbohorquez.calcularAhorro(salario, percentAhorro, tasaAnual, periodos);
    console.log("El ahorro total generado es: " + df.format(ahorroTotal2));
    console.log();

    console.log("DIFICULTAD EXTRA");
    const numeros = mbohorquez.fizzBuzz("fizz", "buzz");
    console.log("números de: " + numeros);
}
    
// Llamada al método principal
main();
