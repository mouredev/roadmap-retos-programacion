/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ContratoReto01 {
    event LogResultado(string mensaje, uint256 resultado);
    event LogResultadoBit(string mensaje, uint16 resultado);
    event LogResultado(string mensaje, bool resultado);
    event LogError(string mensaje);
    event LogErrorData(bytes data);

    // Aritméticos, lógicos, de comparación, asignación
    // https://www.geeksforgeeks.org/solidity-operators/
    function operacionesBasicas() public {
        uint256 a = 10;
        uint256 b = 5;

        // 1. Operadores Arimeticos
        uint256 suma = a + b;
        uint256 resta = a - b;
        uint256 multiplicacion = a * b;
        uint256 division = a / b;
        uint256 modulo = a % b;
        uint256 decremento = --b;
        uint256 incremento = ++a;

        emit LogResultado("Suma: (a + b): ", suma);
        emit LogResultado("Resta: (a - b): ", resta);
        emit LogResultado("Multiplicacion: (a * b): ", multiplicacion);
        emit LogResultado("Division: (a / b): ", division);
        emit LogResultado("Modulo: (a % b): ", modulo);
        emit LogResultado("Decremento: ( -- b ): ", decremento);
        emit LogResultado("Decremento: ( ++a ): ", incremento);

        // 2. Operadores Relacionales
        bool esIgual = a == b;
        bool noEsIgual = a != b;
        bool esMayor = a > b;
        bool esMenor = a < b;
        bool esMayorOIgual = a >= b;
        bool esMenorOIgual = a <= b;

        emit LogResultado("Igual a: (a == b): ", esIgual ? 1 : 0);
        emit LogResultado("No es igual a: (a != b): ", noEsIgual ? 1 : 0);
        emit LogResultado("Mayor que: (a > b): ", esMayor ? 1 : 0);
        emit LogResultado("Menor que: (a < b): ", esMenor ? 1 : 0);
        emit LogResultado(
            "Mayor que o igual: (a >= b): ",
            esMayorOIgual ? 1 : 0
        );
        emit LogResultado(
            "Menor que o igual: (a <= b): ",
            esMenorOIgual ? 1 : 0
        );

        // 3. Operadores Logicos
        emit LogResultado("AND: a == b && a > 0 : ", (a == b && a > 0));
        emit LogResultado("OR: a == b || a > 0 : ", (a == b || a > 0));
        emit LogResultado("NOT: !( a == b )  : ", !(a == b));

        // 4. Bitwise Operators
        // Declaring variables
        uint16 aa = 20;
        uint16 bb = 10;

        emit LogResultadoBit("Bitwise AND: (aa & bb)", aa & bb);
        emit LogResultadoBit("BitWise OR: (aa | bb)", aa | bb);
        emit LogResultadoBit("Bitwise XOR: (aa ^ bb)", aa ^ bb);
        emit LogResultadoBit("Bitwise Not: ( ~aa)", ~aa);
        emit LogResultadoBit("Left Shift: (aa << bb)", aa << bb);
        emit LogResultadoBit("Right Shift: (aa >> bb)", aa >> bb);

        //5. Operadores de Asignacion
        uint16 assignment = 20;
        uint assignment_add = 50;
        uint assign_sub = 50;
        uint assign_mul = 10;
        uint assign_div = 50;
        uint assign_mod = 32;

        assignment_add += 10;
        assign_sub -= 20;
        assign_mul *= 10;
        assign_div /= 10;
        assign_mod %= 20;

        emit LogResultado("assignment_add += 10: ", assignment_add);
        emit LogResultado("assign_sub -= 20: ", assign_sub);
        emit LogResultado("assign_mul *= 10:  ", assign_mul);
        emit LogResultado("assign_div /= 10: ", assign_div);
        emit LogResultado("assign_mod %= 20: ", assign_mod);
        
        // 6. Operador Condicional
        uint result = (a > b? a-b : b-a);
        emit LogResultado("(a > b? a-b : b-a): ", result);

    }

    // Condicionales
    function condicionales(uint256 numero) public {
        if (numero > 20) {
            emit LogResultado("Numero mayor a 20", numero);
        } else if (numero == 20) {
            emit LogResultado("Numero igual a 20", numero);
        } else {
            emit LogResultado("Numero menor a 20", numero);
        }
    }

    // Iterativas
    // EXTRA
    function iterativas() public {
        for (uint256 i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                emit LogResultado("Numero par y no es 16 ni multiplo de 3", i);
            }
        }
    }

    /*
        Excepciones: En Solidity, puedes controlar las excepciones utilizando estructuras como require, 
        revert, assert y manejo de excepciones con try/catch.
        https://solidity-by-example.org/try-catch/ 
    */

    // Ejemplo de revert con require
    function dividir(uint256 a, uint256 b) public pure returns (uint256) {
        require(b != 0, "No se puede dividir por cero");
        return a / b;
    }

    // Manejo de Excepciones con Try/Catch (Solidity 0.8.0 y versiones posteriores):
    // Ejemplo de manejo de excepciones con try/catch
    function transferir(address destinatario, uint256 cantidad) public {
        try msg.sender.transfer(cantidad) {
            // Éxito: hacer algo si la transferencia es exitosa
        } catch Error(string memory errorMessage) {
            // Manejar la excepción: errorMessage contiene información sobre el error
            emit LogError(errorMessage);
        } catch (bytes memory errorData) {
            // Manejar otras excepciones
            emit LogErrorData(errorData);
        }
    }

    // Ejemplo de assert
    /*
        assert se utiliza para verificar condiciones que deben ser siempre ciertas. 
        Si la condición no se cumple, se produce una excepción que no puede ser manejada 
        y terminará la ejecución del contrato. 
    */
    function realizarOperacion(
        uint256 a,
        uint256 b
    ) public pure returns (uint256) {
        uint256 resultado = a * b;
        assert(resultado > 0);
        return resultado;
    }
}
