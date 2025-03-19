public class david-quinones {
    public static void main(String[] args) {
        
        /*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)*/
 
        //Ejemplo de función sin parámetros ni retorno
        funcionSinParametrosNiRetorno();
        //Ejemplo de función con un parámetro y sin retorno
        funcionConUnParametroSinRetorno(5);

        //Ejemplo de función sin parametro y con retorno
        System.out.println(funcionConUnParametroConRetorno());
        //Ejemplo de función con varios parámetros y con retorno
        System.out.println(funcionConVariosParametrosConRetorno(5, 10));

        //Ejemplo de función con una función dentro
        funcionConFuncionDentro();
        
        //funcion del sistema
        System.out.println("El valor de PI es: " + Math.PI);
        //otra funcion del sistema
        System.out.println("El valor de la raiz cuadrada de 25 es: " + Math.sqrt(25));
        //otra funcion del sistema
        System.out.println("El valor de 5 elevado a 3 es: " + Math.pow(5, 3));
        //otra funcion del sistema que no sea Math
        System.out.println("El valor de la longitud de la cadena 'Hola' es: " + "Hola".length());
        // otra de sistema que no sea de las anteriores
        System.out.println("El valor de la cadena 'Hola' en mayusculas es: " + "Hola".toUpperCase()); 


        //Ejemplo de variable global
        int variableGlobal = 10;
        System.out.println("El valor de la variable global es: " + variableGlobal);
        //ejemplo de variable local
        funcionConVariableLocal();      

        //extra
        functionExtra1("david", "quinones");


    }

    private static void funcionSinParametrosNiRetorno(){
        System.out.println("Ejemplo de función sin parámetros ni retorno");
    }

    private static void funcionConUnParametroSinRetorno(int parametro){
        System.out.println("Ejemplo de función con un parámetro y sin retorno: " + parametro);
    }

    private static int funcionConUnParametroConRetorno(){
        return 5;
    }

    private static int funcionConVariosParametrosConRetorno(int parametro1, int parametro2){
        return parametro1 + parametro2;
    }

    private static void funcionConFuncionDentro(){
        System.out.println("Ejemplo de función con una función dentro");
        funcionSinParametrosNiRetorno();
    }

    private static void funcionConVariableLocal(){
        int variableLocal = 5;
        System.out.println("El valor de la variable local es: " + variableLocal);
    }

    private static int functionExtra1(String cadena1, String cadena2){
        int contador = 0;
        for(int i = 1; i <= 100; i++){
            if(i % 3 == 0 && i % 5 == 0){
                System.out.println(cadena1 + cadena2);
            }else if(i % 3 == 0){
                System.out.println(cadena1);
            }else if(i % 5 == 0){
                System.out.println(cadena2);
            }else{
                System.out.println(i);
                contador += i;
            }
        }

        return contador;
    }

    
}
