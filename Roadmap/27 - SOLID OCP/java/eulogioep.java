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

 import java.util.HashMap;
 import java.util.Map;
 import java.util.Set;
 import java.util.stream.Collectors;
 
 public class eulogioep {
     public static void main(String[] args) {
         // Creamos una instancia de la calculadora
         Calculator calculator = new Calculator();
 
         // Registramos las operaciones básicas
         calculator.registerOperation(new Addition());
         calculator.registerOperation(new Subtraction());
         calculator.registerOperation(new Multiplication());
         calculator.registerOperation(new Division());
 
         // Mostramos las operaciones disponibles
         System.out.println("Operaciones disponibles:");
         calculator.getAvailableOperations().forEach(op -> 
             System.out.println("- " + op.getName() + " (" + op.getSymbol() + ")")
         );
 
         // Probamos las operaciones básicas
         System.out.println("\nProbando operaciones básicas:");
         testOperation(calculator, 10.0, 5.0, "+");
         testOperation(calculator, 10.0, 5.0, "-");
         testOperation(calculator, 10.0, 5.0, "*");
         testOperation(calculator, 10.0, 5.0, "/");
 
         // Agregamos una nueva operación (potencia) sin modificar el código existente
         calculator.registerOperation(new Power());
         System.out.println("\nProbando nueva operación (potencia):");
         testOperation(calculator, 2.0, 3.0, "^");
 
         // Probamos el manejo de errores
         System.out.println("\nProbando manejo de errores:");
         testOperation(calculator, 5.0, 0.0, "/");  // División por cero
         testOperation(calculator, 5.0, 2.0, "%");  // Operación no existente
     }
 
     private static void testOperation(Calculator calculator, double a, double b, String symbol) {
         try {
             OperationResult result = calculator.calculate(a, b, symbol);
             System.out.println(result);
         } catch (Exception e) {
             System.out.println("Error: " + e.getMessage());
         }
     }
 }
 
 // EJEMPLO INCORRECTO (Violando OCP)
 class BadCalculator {
     public double calculate(double a, double b, String operation) {
         switch (operation) {
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
                 throw new IllegalArgumentException("Operación no soportada");
         }
     }
 }
 
 // EJEMPLO CORRECTO (Siguiendo OCP)
 // Definimos una interfaz para las operaciones
 interface Operation {
     double execute(double a, double b) throws ArithmeticException;
     String getSymbol();
     String getName();
 }
 
 // Implementamos cada operación como una clase separada
 class Addition implements Operation {
     @Override
     public double execute(double a, double b) {
         return a + b;
     }
 
     @Override
     public String getSymbol() {
         return "+";
     }
 
     @Override
     public String getName() {
         return "Suma";
     }
 }
 
 class Subtraction implements Operation {
     @Override
     public double execute(double a, double b) {
         return a - b;
     }
 
     @Override
     public String getSymbol() {
         return "-";
     }
 
     @Override
     public String getName() {
         return "Resta";
     }
 }
 
 class Multiplication implements Operation {
     @Override
     public double execute(double a, double b) {
         return a * b;
     }
 
     @Override
     public String getSymbol() {
         return "*";
     }
 
     @Override
     public String getName() {
         return "Multiplicación";
     }
 }
 
 class Division implements Operation {
     @Override
     public double execute(double a, double b) {
         if (b == 0) {
             throw new ArithmeticException("No se puede dividir por cero");
         }
         return a / b;
     }
 
     @Override
     public String getSymbol() {
         return "/";
     }
 
     @Override
     public String getName() {
         return "División";
     }
 }
 
 // Podemos agregar nuevas operaciones sin modificar el código existente
 class Power implements Operation {
     @Override
     public double execute(double a, double b) {
         return Math.pow(a, b);
     }
 
     @Override
     public String getSymbol() {
         return "^";
     }
 
     @Override
     public String getName() {
         return "Potencia";
     }
 }
 
 // Clase para almacenar resultados de operaciones
 class OperationResult {
     private final double value;
     private final String operation;
     private final double firstOperand;
     private final double secondOperand;
 
     public OperationResult(double value, String operation, double firstOperand, double secondOperand) {
         this.value = value;
         this.operation = operation;
         this.firstOperand = firstOperand;
         this.secondOperand = secondOperand;
     }
 
     @Override
     public String toString() {
         return String.format("%.2f %s %.2f = %.2f", 
             firstOperand, operation, secondOperand, value);
     }
 }
 
 // La calculadora que cumple con OCP
 class Calculator {
     private final Map<String, Operation> operations;
 
     public Calculator() {
         this.operations = new HashMap<>();
     }
 
     // Método para registrar nuevas operaciones
     public void registerOperation(Operation operation) {
         operations.put(operation.getSymbol(), operation);
     }
 
     // Método para realizar cálculos
     public OperationResult calculate(double a, double b, String symbol) {
         Operation operation = operations.get(symbol);
         if (operation == null) {
             throw new IllegalArgumentException("Operación " + symbol + " no soportada");
         }
         double result = operation.execute(a, b);
         return new OperationResult(result, symbol, a, b);
     }
 
     // Método para obtener operaciones disponibles
     public Set<Operation> getAvailableOperations() {
         return operations.values().stream().collect(Collectors.toSet());
     }
 }
 
 /*
  * EXPLICACIÓN DE POR QUÉ ESTE DISEÑO CUMPLE CON OCP:
  * 
  * 1. ABIERTO PARA EXTENSIÓN:
  *    - Podemos agregar nuevas operaciones implementando la interfaz Operation
  *    - No necesitamos modificar ninguna clase existente
  *    - Cada operación está encapsulada en su propia clase
  * 
  * 2. CERRADO PARA MODIFICACIÓN:
  *    - La clase Calculator no necesita ser modificada para agregar nuevas operaciones
  *    - El código existente permanece intacto cuando agregamos nuevas funcionalidades
  *    - La interfaz Operation define un contrato claro que no cambia
  * 
  * 3. VENTAJAS DE ESTE DISEÑO:
  *    - Fácil de mantener y extender
  *    - Cada operación está aislada y puede ser probada independientemente
  *    - Reduce el acoplamiento entre componentes
  *    - Facilita la adición de nuevas operaciones sin riesgo de afectar las existentes
  * 
  * 4. CARACTERÍSTICAS ESPECÍFICAS DE LA IMPLEMENTACIÓN EN JAVA:
  *    - Uso de interfaces
  *    - Manejo de errores con excepciones específicas
  *    - Uso de genéricos con Map y Set
  *    - Clase específica para resultados inmutable
  *    - Uso de Streams para operaciones con colecciones
  *    - Formato de números con precisión decimal
  */