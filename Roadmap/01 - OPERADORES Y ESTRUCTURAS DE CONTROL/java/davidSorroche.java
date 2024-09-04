import java.util.Optional;

public class OperadoresEstructurasDeControl {
    public final int CINCO = 5;
    public final String JAVA = "Java";
    
    /*  Métodos para cálculos de operadores aritméticos:
            - Suma (+).
            - Resta (-).
            - Multiplicación (*).
            - División (/).
            - Módulo (%).
    */
    
    public int suma(int num1, int num2) {
        return num1 + num2;
    }
    
    public int resta(int num1, int num2) {
        return num1 - num2;
    }
    
    public int multiplicacion(int num1, int num2) {
        return num1 * num2;
    }
    
    public Optional<Double> division(int num1, int num2) { 
        if(num2 == 0) {
            return Optional.empty();
        }
        return Optional.of((double) num1 / num2);
    }
    
    public Optional<Integer> divisionEntera(int num1, int num2) {
        if(num2 == 0) {
            return Optional.empty();
        }
        return Optional.of(num1 / num2);
    }
    
    public Optional<Integer> modulo(int num1, int num2) {
        if(num2 == 0) {
            return Optional.empty();
        }
        return Optional.of(num1 % num2);
    }
    
    /*  Métodos para cálculos usando operadores unarios.
            - Más Unario (+).
            - Menos Unario (-).
            - Incremento (++). * Corrección posterior y corrección anterior.
            - Decremento (--). * Corrección posterior y corrección anterior.
            - Complemento Lógico (!).
    */
    
    public int masUnario(int num) {
        return + num;
    }
    
    public int menosUnario(int num) {
        return - num;
    }
    
    public int incrementoPosterior(int num) {
        return num++;
    }
    
    public int incrementoAnterior(int num) {
        return ++num;
    }

    public int decrementoPosterior(int num) {
        return num--;
    }
    
    public int decrementoAnterior(int num) {
        return --num;
    }
    
    public boolean complementoLogico(boolean booleano) {
        return !booleano;
    }
    
    /*  Métodos para usos de las unidades de asignación.
            - Asignación (=)
            - Suma y Asignación (+=)
            - Resta y Asignación (-=)
            - Multiplicación y Asignación (*=)
            - División y Asignación (/=)
            - Módulo y Asignación (%=)
    */
    
    public Object asignacion(Object valor) {     
        Optional<Object> nuevoValor = Optional.ofNullable(valor);        
        return nuevoValor.isPresent() ? nuevoValor : "Lo siento, no has introducido ningún valor para asignárselo a la variable \"nuevoValor\"";
    }
    
    public int sumaAsignacion(int num1, int num2) {
        return num1 += num2;    
    }
    
    public String anadidoAsignacion(String cad1, String cad2) {
        return cad1 += cad2;
    }
    
    public int restaAsignacion(int num1, int num2) {
        return num1 -= num2;
    }
    
    public int multiplicacionAsignacion(int num1, int num2) {
        return num1 *= num2;
    }
    
    public double divisionAsignacion(int num1, int num2) {
        return num1 /= (double)num2;
    }
    
    public int divisionAsignacionEntera(int num1, int num2) {
        return num1 /= num2;
    }
    
    public int moduloAsignacion(int num1, int num2) {
        return num1 %= num2;
    }
    
    /*  Métodos para usos de operadores relacionales.
            - Igual a (==).
            - Distinto a(!=).
            - Mayor que (>).
            - Mayor o igual que (>=).
            - Menor que (<).
            - Menor o igual que (<=).
    */
    
    public boolean igualdad (Object valor1, Object valor2) {
        return valor1 == valor2;
    }
    
    public boolean desigualdad(Object valor1, Object valor2) {
        return valor1 != valor2;
    }
    
    public boolean mayor(int num1, int num2) {
        return num1 > num2;
    }
    
    public boolean mayorIgual(int num1, int num2) {
        return num1 >= num2;
    }
    
    public boolean menor(int num1, int num2) {
        return num1 < num2;
    }
    
    public boolean menorIgual(int num1, int num2) {
        return num1 <= num2;
    }
    
    /*  Métodos para usos de operadores condicionales.
            - condicional AND (&&).
            - condicional OR (||).
            - ternario(?:).
    */
    
    public boolean and (int num1, int num2) {
        return num1 == this.CINCO && num2 == this.CINCO;
    }
    
    public boolean or (String cad1, String cad2) {
        return cad1.equalsIgnoreCase(this.JAVA) || cad2.equalsIgnoreCase(this.JAVA);
    }
    
    public String ternario(String lenguaje) {
        return lenguaje.equalsIgnoreCase(this.JAVA) ? "Estás estudiando lenguaje ".concat(JAVA) : "No estás estudiando el lenguaje".concat(lenguaje);
    }
    
    /*  Métodos para usos de operadores de bits en números enteros.
            - desplazamiento izquierda (<<).
            - desplazamiento derecha (>>).
            - invertir (~).
            - operacion AND (&).
            - operación OR exclusivo (^).
            - operación OR inclusivo (|).
    */
    
    public int desplazamientoIzquierda (int num, int pos) {
        return num << pos;
    }
    
    public int desplazamientoDerecha (int num, int pos) {
        return num >> pos;
    }
    
    public int inversion (int num) {
        return ~ num;
    }
    
    public int operadorAND (int num1, int num2) {
        return num1 & num2;
    }
    
    public int operadorORExclusivo (int num1, int num2) {
        return num1 ^ num2;
    }
    
    public int operadorORInclusivo (int num1, int num2) {
        return num1 | num2;
    }
}
