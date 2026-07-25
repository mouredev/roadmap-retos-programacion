package retosProgramacion;

public class RetoDos {

    public static void main(String[] args) {
        
        //Ejercicio de dificultad extra
        for (int num = 10; num <= 55; num++) {
            if (num != 16 && num%2 == 0 && num%3 != 0){        
            System.out.println(num);
            }
        }

        //operadores aritméticos
        int a = 15;
        int b = 3;
        System.out.println("Suma de a + b = " + (a + b));
        System.out.println("Resta de a - b = " + (a - b));
        System.out.println("Multiplicación de a * b = " + (a * b));
        System.out.println("División de a/b = " + (a / b));
        System.out.println("Módulo de a % b = " + (a % b));

        //Operadores de asignación
        int miNumero = 10; //Asignación simple
        System.out.println(miNumero);
        miNumero += 2; //Suma y asignación
        System.out.println(miNumero);
        miNumero -= 3; //Resta y asignación
        System.out.println(miNumero);
        miNumero *= 4; //Multiplicación y asignación
        System.out.println(miNumero);
        miNumero /= 5; //División y asignación
        System.out.println(miNumero);
        miNumero %= 6; //Módulo y asignación
        System.out.println(miNumero);

        //Operadores unarios
        System.out.println("Mantiene el signo: " + (+a));
        System.out.println("Cambia el signo: " + (-a));
        System.out.println("Autoincremento e impresión: " + (++a));
        System.out.println("Impresión y autoincremento: " + (a++));
        System.out.println("Autodecremento e impresión: " + (--a));
        System.out.println("Impresión y autodecremento: " + (a--));

        //Operadores Relacionales
        System.out.println("Los dos números son iguales: " + (a == b)); //igualdad
        System.out.println("Los dos números son iguales: " + (a != b)); //desigualdad
        System.out.println("A es mayor que B: " + (a > b)); //mayor que
        System.out.println("A es menor que B: " + (a < b)); //menor que
        System.out.println("A es mayor o igual a B: " + (a >= b)); //mayor o igual que
        System.out.println("A es menor o igual a B: " + (a <= b)); //menor o igual que

        //Operadores Lógicos
        System.out.println("A es mayor y menor que B: " + (a > b && a < b)); //AND lógico
        System.out.println("A es mayor o menor que B: " + (a > b || a < b)); //OR lógico
        System.out.println("A es mayor que B: " + !(a > b));//NOT lógico, Invierte el true o false
        System.out.println("A es mayor o igual que B: " + (a > b ^ a < b));//XOR lógico, devuelve true si sólo una lo es

        //Operadores Bit a Bit
        System.out.println("AND bit a bit: " + (a & b));
        System.out.println("OR bit a bit: " + (a | b));
        System.out.println("XOR bit a bit: " + (a ^ b));
        System.out.println("NOT bit a bit: " + (~a));
        System.out.println("Desplazamiento a la izquierda: " + (a << 1));
        System.out.println("Desplazamiento a la derecha: " + (a >> 1));
        System.out.println("Desplazamiento a la derecha sin signo: " + (a >>> 1));

        //Operador ternario (Condicional)
        int c = (a > 10) ? 2 : 5;
        System.out.println("El valor de c será: " + c);

        //Operador de instancia (Instanceof)
        String s = "Hola";
        boolean objetoTipo = s instanceof String;
        System.out.println("El objeto c es de tipo String: " + objetoTipo);

        //Operadores de tipo (Cast)
        double d = 10.5;
        int i = (int) d;
        System.out.println("El número double 10.5 es el número entero: " + i);

        //Estructuras de control de decisión (Condicionales) 
        if (a >= 15) { //If
            System.out.println("A es igual o mayor a 15");
        }

        if (a >= 15) { //Else
            System.out.println("A es igual o mayor a 15");
        } else {
            System.out.println("A es menor que 15");
        }

        if (a > 15) { //else if
            System.out.println("A es  mayor a 15");
        } else if (a < 15) {
            System.out.println("A es menor a 15");
        } else {
            System.out.println("A es igual a 15");
        }

        switch (b) { //Switch
            case 1:
                System.out.println("B es igual a 1");
                break;
            case 2:
                System.out.println("B es igual a 2");
                break;
            case 3:
                System.out.println("B es igual a 3");
                break;
            default:
                System.out.println("B no tiene valor");
        }

        //Estructuras de control de repeticion (Bucles)
        for (int ini = 1; ini <= 5; ini++) { //For
            System.out.println("Iteración: " + ini);
        }

        int contador = 0;
        while (contador < 5) { //While
            System.out.println("Contador: " + contador);
            contador++;
        }

        int contador2 = 0;
        do {
            System.out.println("Contador: " + contador2); //do-while
            contador2++;
        } while (contador2 < 3);

        String[] lista = {"Rodri", "Vinicius", "Bellingham", "Kroos", "Lamine", "Carvajal"}; //for-each(Mejorado para Arrays y Colecciones)
        for (String list : lista) {
            System.out.println("El nombre del juagador es: " + list);
        }

        //Estructuras de control de salto
        for (int k = 0; k < 5; k++) {
            if (k == 2) {
                break; //BREAK
            }
            System.out.println(k);
        }

        for (int k = 0; k < 5; k++) {
            if (k == 2) {
                continue; //CONTINUE
            }
            System.out.println(k);
        }

        for (int k = 0; k < 5; k++) {
            if (k == 2) {
                return; //RETURN
            }
            System.out.println(k);
        }

        //Control de manejo de excepciones
        try {
            System.out.println(10 / 0);
        } catch (Exception e) {
            System.out.println("Se ha producido un error");
        } finally {
            System.out.println("Ha finalizado correctamente");
        }
       
    }
}



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
