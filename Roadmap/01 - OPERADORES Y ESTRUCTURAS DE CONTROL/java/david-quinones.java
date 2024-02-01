import java.sql.SQLException;

public class david-quinones {

    public static void main(String[] args) {
        david-quinones lopez = new david-quinones();
        lopez.operadores();
    }   

    public void operadores() {
        arithmetic();
        assignment();
        comparison();
        logical();
        terario();
        bits();
        condicionales();
        iterativas();
        excepciones();
        // excepcionesTrows();
        jumpStructure();
        additionalExercice();
    }

    public void arithmetic() {
        System.out.println("Suma 20 + 3: " + (20 + 3));
        System.out.println("Resta 20 - 3: " + (20 - 3));
        System.out.println("Multiplicacion 20 * 3: " + (20 * 3));
        System.out.println("Division 20 / 3: " + (20 / 3));
        System.out.println("Modulo 20 % 3: " + (20 % 3));
        System.out.println("Potencia 20 ^ 3: " + (20 ^ 3));
        int i = 1;
        System.out.println("Incrementar i assignar variable i --> 2: " + ++i);
        System.out.println("Decrementar i assignar variable i --> 1: " + --i);
        int i2 = 20;
        System.out.println("Assignar i incrementar variable i2 --> 20: " + i2++);
        System.out.println("Mostrar variable incrementada i2 --> 21: " + i2);
        System.out.println("Assignar i decremntar variable i2 --> 21: " + i2--);
        System.out.println("Mostrar variable decrementada i2 --> 20: " + i2);
    }

    public void assignment() {
        int i = 10; // asignacion
        System.out.println(i);
        i += 10; // suma y asignacion
        System.out.println(i);
        i -= 3; // resta y asignacion
        System.out.println(i);
        i *= 3; // multiplica y asignacion
        System.out.println(i);
        i /= 1; // divide y asigna
        System.out.println(i);
        i %= 5; // modulo y asignacion
        System.out.println(i);
        i ^= 2; // potencia y asignacion
        System.out.println(i);
    }

    public void comparison() {
        System.out.println("Igualdad 10 = 5? " + (10 == 5));
        System.out.println("Diferente 10 != 5? " + (10 != 5));
        System.out.println("Mas grande 10 > 5? " + (10 > 5));
        System.out.println("Mas pequeño 10 < 5? " + (10 < 5));
        System.out.println("Igual o mas grande 10 >= 5? " + (10 >= 5));
        System.out.println("Igual o mas pequeño 10 <= 5? " + (10 <= 5));
    }

    public void logical() {
        System.out.println("AND && 5==5 && 6<10:" + (5 == 5 && 6 < 10));
        System.out.println("OR || 5==1 && 6<10:" + (5 == 1 || 6 < 10));
        System.out.println("NOT ! !false" + (!false));
    }

    public void terario() {
        System.out.println("Operador ternario--> 1 = 1" + (1 == 1 ? "si es igual" : "no es diferente"));
    }

    public void bits() {
        int a = 5;
        int b = 10;
        System.out.println("Operador AND &: " + (a & b));
        System.out.println("Operador OR |: " + (a | b));
        System.out.println("Operador XOR ^: " + (a ^ b));
        System.out.println("Desplazamiento izquierda <<: " + (a << b));
        System.out.println("Desplazamiento derecha >>: " + (a >> b));
    }

    /*
     * 
     * Estructuras de control
     * 
     * 
     */

    public void condicionales() {
        int david = 9;

        if (david == 11) {
            System.out.println("Entro el el If" + david);
        } else if (david == 12) {
            System.out.println("Entro en el Else If" + david);
        } else {
            System.out.println("Entro en el Else" + david);
        }

        // swith de toda la vida
        switch (david) {
            case 5:
                break;
            case 17:
                break;
            case 10: // no puede tener multiples casos
                System.out.println("Entro en el caso" + david);
                break; // para que pare y no siga
            default:
                System.out.println("Entro en el caso default, el valor es:" + david);
                break;
        }

        // switch Expressivo (Java 14) IDentico pero sin break -> se ejecuta el
        // siguiente
        switch (david) {
            case 5 -> System.out.println("Entro en el caso " + david);
            case 17, 9 -> System.out.println("Entro en el caso 17 o 9 " + david);
            case 10 -> System.out.println("Entro en el caso " + david);
            default -> System.out.println("Entro en el default " + david);
        }

        // switch expressions (Podemos assignar el resultado a una variable)
        String result = switch (david) {
            case 5 -> "Entro en el caso " + david;
            case 17, 9 -> "Entro en el caso 17, 9 " + david;
            case 10 -> "Entro en el caso " + david;
            default -> "Entro en el default " + david;
        };

        System.out.println("Result: " + result);

        // Podemos usar bloque de codigo
        switch (david) {
            case 1 -> {
                //
                // yield 1; --> esto es para devolver el resultado a case (si feura a una
                // variable)
            }
            default -> {
            }
        }

    }

    public void iterativas() {
        // for
        for (int i = 0; i < 10; i++) {
            System.out.println("For: " + i);
        }

        // for each
        for (String name : new String[] { "David", "Quinones" }) {
            System.out.println("palabras con forEach: " + name);
        }

        // while
        int i = 0;
        while (i < 10) { // comprueba la condicion y luego ejecuta el codigo
            System.out.println("While point: " + i);
            i++;
        }

        // do while
        int j = 0;
        do { // ejecutor el codigo en primer lugar y luego comprueba la condicion
            System.out.println("Do While point: " + j);
            j++;
        } while (j < 10); // si es true vuelve a ejecutar el codigo

    }

    public void excepciones() {
        // try catch
        try {
            // realiza codigo, si algo sale mal como por ejemplo dividir entre zero,
            // la aplicacion no finalizarà capturarà el error y lo mandara al catch,
            // siguiendo su ejecucion
        } catch (Exception e) {
            System.out.println(e.getCause());
        } finally {
            // siempre se ejecutarà tanto si captura un error como si funciona todo ok
        }

        // podemos hacer lanzar una excepcion si nos interesa
        try {
            throw new SQLException("Message de error en excepcion lanzada");
        } catch (Exception e) {
            System.out.println("Error capturado: " + e.getMessage());
        }
    }

    // declaramos un metodo e indicamos que puede lanzar una excepcion del tipos
    // mencionado
    public void excepcionesTrows() throws Exception {
        // quin llame este metodo tiene que manejar esta excepcion, ya sea con try_catch
        // o declarandose con throws (eccpecion)
    }

    // controles utilizados en todo lo anterior (continue, break, return)
    /* estructura de saltos */
    public void jumpStructure(){
        //break
        for(int i = 0; i < 5; i++){
            if(i == 3){
                break; // controlaremos si i = 3, si se cumple salimos del bucle for
            }
            System.out.println(i);
        }

        // continue
        for (int i = 0; i < 5 ; i++) {
            if(i == 3) {
                continue; // Si i = 3, saltmos a la sigiente iteracion sin seguir con nada que siga dentro del for
            }
            System.out.println(i);
        }

        // return 
        System.out.println(returnMetodo(0));
    }

    public int returnMetodo(int numero){
        if(numero == 3){
            return numero; //si es igual, retorno numero
        }
        return -1; // sino quadra, retorna valor 
    }

    public void additionalExercice(){
        /* ADDICIONAL */
        for(int i = 10; i < 56; i++){
            if(i == 16 || i % 2 != 0 || i % 3 == 0){ 

                continue;
            }
            System.out.println(i);
        }

    }







}
