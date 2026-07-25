using System;
using System.Collections.Generic;
using System.Linq;

/*
 * PRINCIPIO ABIERTO-CERRADO (OCP)
 * 
 * El principio establece que las entidades de software (clases, módulos, funciones, etc.) 
 * deberían estar:
 * - ABIERTAS para la extensión: Podemos agregar nuevo comportamiento
 * - CERRADAS para la modificación: No debemos modificar el código existente
 * 
 * Beneficios:
 * 1. Código más mantenible y escalable
 * 2. Reduce el riesgo de bugs en código existente
 * 3. Facilita la adición de nuevas funcionalidades
 */

namespace OCP.Calculator
{
    // EJEMPLO INCORRECTO (Violando OCP)
    // ❌ Cada vez que queremos agregar una nueva operación, debemos modificar la clase existente
    public class BadCalculator
    {
        public decimal Calculate(decimal a, decimal b, string operation)
        {
            switch (operation)
            {
                case "sum":
                    return a + b;
                case "subtract":
                    return a - b;
                case "multiply":
                    return a * b;
                case "divide":
                    return a / b;
                // Si queremos agregar una nueva operación, debemos modificar esta clase
                // violando el principio OCP
                default:
                    throw new ArgumentException("Operación no soportada");
            }
        }
    }

    // EJEMPLO CORRECTO (Siguiendo OCP)
    // Definimos una interfaz para las operaciones
    public interface IOperation
    {
        decimal Execute(decimal a, decimal b);
        string Symbol { get; }
        string Name { get; }
    }

    // Implementamos cada operación como una clase separada
    public class Addition : IOperation
    {
        public decimal Execute(decimal a, decimal b) => a + b;
        public string Symbol => "+";
        public string Name => "Suma";
    }

    public class Subtraction : IOperation
    {
        public decimal Execute(decimal a, decimal b) => a - b;
        public string Symbol => "-";
        public string Name => "Resta";
    }

    public class Multiplication : IOperation
    {
        public decimal Execute(decimal a, decimal b) => a * b;
        public string Symbol => "*";
        public string Name => "Multiplicación";
    }

    public class Division : IOperation
    {
        public decimal Execute(decimal a, decimal b)
        {
            if (b == 0)
                throw new DivideByZeroException("No se puede dividir por cero");
            return a / b;
        }
        public string Symbol => "/";
        public string Name => "División";
    }

    // Podemos agregar nuevas operaciones sin modificar el código existente
    public class Power : IOperation
    {
        public decimal Execute(decimal a, decimal b)
        {
            return (decimal)Math.Pow((double)a, (double)b);
        }
        public string Symbol => "^";
        public string Name => "Potencia";
    }

    // Clase para resultados de operaciones
    public class OperationResult
    {
        public decimal Value { get; set; }
        public string Operation { get; set; }
        public decimal FirstOperand { get; set; }
        public decimal SecondOperand { get; set; }
        public bool IsSuccess { get; set; }
        public string ErrorMessage { get; set; }

        public override string ToString() =>
            IsSuccess
                ? $"{FirstOperand} {Operation} {SecondOperand} = {Value}"
                : $"Error: {ErrorMessage}";
    }

    // La calculadora que cumple con OCP
    public class Calculator
    {
        private readonly Dictionary<string, IOperation> _operations;

        public Calculator()
        {
            _operations = new Dictionary<string, IOperation>();
        }

        // Método para registrar nuevas operaciones
        public void RegisterOperation(IOperation operation)
        {
            _operations[operation.Symbol] = operation;
        }

        // Método para realizar cálculos con manejo de errores
        public OperationResult Calculate(decimal a, decimal b, string symbol)
        {
            try
            {
                if (!_operations.TryGetValue(symbol, out var operation))
                {
                    return new OperationResult
                    {
                        IsSuccess = false,
                        ErrorMessage = $"Operación {symbol} no soportada"
                    };
                }

                return new OperationResult
                {
                    IsSuccess = true,
                    Value = operation.Execute(a, b),
                    Operation = symbol,
                    FirstOperand = a,
                    SecondOperand = b
                };
            }
            catch (Exception ex)
            {
                return new OperationResult
                {
                    IsSuccess = false,
                    ErrorMessage = ex.Message,
                    Operation = symbol,
                    FirstOperand = a,
                    SecondOperand = b
                };
            }
        }

        // Método para obtener operaciones disponibles
        public IEnumerable<(string Symbol, string Name)> GetAvailableOperations()
        {
            return _operations.Values.Select(op => (op.Symbol, op.Name));
        }
    }

    // Clase principal para demostración
    public class Program
    {
        public static void Main()
        {
            // Creamos una instancia de la calculadora
            var calculator = new Calculator();

            // Registramos las operaciones básicas
            calculator.RegisterOperation(new Addition());
            calculator.RegisterOperation(new Subtraction());
            calculator.RegisterOperation(new Multiplication());
            calculator.RegisterOperation(new Division());

            // Mostramos las operaciones disponibles
            Console.WriteLine("Operaciones disponibles:");
            foreach (var (symbol, name) in calculator.GetAvailableOperations())
            {
                Console.WriteLine($"- {name} ({symbol})");
            }

            // Probamos las operaciones básicas
            var testCases = new[]
            {
                (a: 10m, b: 5m, symbol: "+"),
                (a: 10m, b: 5m, symbol: "-"),
                (a: 10m, b: 5m, symbol: "*"),
                (a: 10m, b: 5m, symbol: "/")
            };

            Console.WriteLine("\nProbando operaciones básicas:");
            foreach (var (a, b, symbol) in testCases)
            {
                var result = calculator.Calculate(a, b, symbol);
                Console.WriteLine(result);
            }

            // Agregamos una nueva operación (potencia) sin modificar el código existente
            calculator.RegisterOperation(new Power());
            
            Console.WriteLine("\nProbando nueva operación (potencia):");
            var powerResult = calculator.Calculate(2, 3, "^");
            Console.WriteLine(powerResult);

            // Probamos el manejo de errores
            Console.WriteLine("\nProbando manejo de errores:");
            
            // División por cero
            var divByZeroResult = calculator.Calculate(5, 0, "/");
            Console.WriteLine(divByZeroResult);

            // Operación no existente
            var invalidOpResult = calculator.Calculate(5, 2, "%");
            Console.WriteLine(invalidOpResult);
        }
    }
}

/*
 * EXPLICACIÓN DE POR QUÉ ESTE DISEÑO CUMPLE CON OCP:
 * 
 * 1. ABIERTO PARA EXTENSIÓN:
 *    - Podemos agregar nuevas operaciones implementando la interfaz IOperation
 *    - No necesitamos modificar ninguna clase existente
 *    - Cada operación está encapsulada en su propia clase
 * 
 * 2. CERRADO PARA MODIFICACIÓN:
 *    - La clase Calculator no necesita ser modificada para agregar nuevas operaciones
 *    - El código existente permanece intacto cuando agregamos nuevas funcionalidades
 *    - La interfaz IOperation define un contrato claro que no cambia
 * 
 * 3. VENTAJAS DE ESTE DISEÑO:
 *    - Fácil de mantener y extender
 *    - Cada operación está aislada y puede ser probada independientemente
 *    - Reduce el acoplamiento entre componentes
 *    - Facilita la adición de nuevas operaciones sin riesgo de afectar las existentes
 * 
 * 4. CARACTERÍSTICAS ESPECÍFICAS DE LA IMPLEMENTACIÓN EN C#:
 *    - Uso de interfaces y genéricos
 *    - Manejo de errores con try-catch y tipos específicos de excepciones
 *    - Uso de tipos decimales para precisión en cálculos
 *    - Clase específica para resultados con estado de éxito/error
 *    - Uso de características modernas de C# como tuplas y expression-bodied members
 *    - Organización en namespace
 *    - Uso de LINQ para consultas
 */