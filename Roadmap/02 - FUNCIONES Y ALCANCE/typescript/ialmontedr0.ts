/**
 * Funciones basicas Typescript
 */

// Funcion sin parametros ni retorno
function primerFucion(): void {
    console.log("Funcion sin parametros ni retorno");
  }
  
  // Funcion con un parametro sin retorno
  function funcionConParametro(param1: string): void {
    console.log(`Funcion con un parametro: ${param1}`);
  }
  
  // Funcion con varios parametros sin retorno
  function funcionConParametros(param1: string, param2: number): void {
    console.log(`Funcion con varios parametros: ${param1}, ${param2}`);
  }
  
  // Funcion con un parametro y retorno
  
  function funcionConParametroYRetorno(param: string): string {
    return `Funcion con un parametro y retorno: ${param}`;
  }
  
  // Funcion dentro de otra funcion
  function funcionConFuncionInterna(): void {
    function funcionInterna(): void {
      console.log("Funcion dentro de otra funcion");
    }
  }
  
  /**
   * Ejemplo de funciones ya creadas en Typescript
   */
  
  // Funcion Math.random()
  
  function ejemploFuncionMathRandom(): void {
    const numeroRandom = Math.random();
    console.log(`Ejemplo Math.random(): ${numeroRandom}`);
  }
  
  /**
   * Variables locales y globales
   */
  
  // Variable global
  let variableGlobal: string = "Variable global";
  
  // Funcion con variable global
  
  function ejemploFuncionConVariableGlobal(): void {
    console.log(`Ejemplo con variable global: ${variableGlobal}`);
  }
  
  // Funcion con variable local
  function ejemploFuncionConVariableLocal(variableLocal: string): void {
    console.log(`Ejemplo con variable local: ${variableLocal}`);
  }
  
  /**
   * Ejercicio extra Funcion que imprime numeros y concatena cadenas
   */
  function ejercicioExtra(primerTexto: string, segundoTexto: string): void {
    let numeroImpresiones: number = 0;
    for (let i = 1; i <= 100; i++) {
      if (i % 3 === 0 && i % 5 === 0) {
        console.log(`${primerTexto} ${segundoTexto}`);
        numeroImpresiones++;
      } else if (i % 3 === 0) {
        console.log(primerTexto);
        numeroImpresiones++;
      } else if (i % 5 === 0) {
        console.log(segundoTexto);
        numeroImpresiones++;
      } else {
        console.log(i);
        numeroImpresiones++;
      }
    }
  }
  
  /**
   * Llamadas a las funciones
   */
  
  primerFucion();
  funcionConParametro("Parametro 1");
  funcionConParametros("Parametro 1", 2);
  console.log(funcionConParametroYRetorno("Parametro 1"));
  funcionConFuncionInterna();
  ejemploFuncionMathRandom();
  ejemploFuncionConVariableGlobal();
  ejemploFuncionConVariableLocal("Variable local");
  ejercicioExtra("Texto 1", "Texto 2");