
public class JuanGuzmanG {

    static int staticNumero = 1;

    public static void numeros() {
        int intNumero = 2;
    }
    
    public static void main(String args[]) {
        //funcion sin parametro ni retorno
        saludar();

        //con uno o varios parametros;
        saludoPersonalizado("juan", 18);

        //con retorno
        String mensaje = saludoGuardado();
        System.out.println("mensaje obtenido:" + mensaje);

        //funcion dentro de funcion
        System.out.println("mayor que 5? " + raiz(8));

        // funciones de Math, ya creadas por java
        System.out.println("raiz: " + Math.sqrt(16));
        System.out.println("Exponente: " + Math.pow(2, 3));
        System.out.println("Numero aleatorio: " + Math.random());

        //funciones de cadena
        System.out.println("hola tiene: " + "hola".length() + " letras");
        System.out.println("hola y " + "hola".toUpperCase());
        System.out.println("hola: " + "hola".charAt(1));

        //funcion para numeros
        System.out.println("4" + "en tipo numero: " + Integer.valueOf("4"));

        //variables locales y globales
        System.out.println("global: " + staticNumero);
        //System.out.println("local: "+intNumero);
        
        //Dificultad extra
        System.out.println("contador: "+multiplos("hola", "mundo"));
    }
    
    static int multiplos(String cadena1, String cadena2){
        int contador = 0;
        for(int i=1; i<=100;i++ ){
            if(i%3==0 && i%5==0){
                System.out.println(i+": "+cadena1+" "+cadena2);
            }else if(i%5==0){
                System.out.println(i+": "+cadena2);
            }else if(i%3==0){
                System.out.println(i+": "+cadena1);
            }else{
                System.out.println(i);
                contador++;
            }
        }
        return contador;
        
        /*
        tambien:
        String salida = "";
        if(i%3==0){
            salida += cadena1;
        }
        if(i%5==0){
            salida += cadena2;
        }
        if(salida.isEmpty()){
            System.out.println(i);
            contador++;
        } else {
            System.out.println(salida);
        }
        */
    }

    static void saludar() {
        System.out.println("hola");
    }

    static void saludoPersonalizado(String nombre, Integer edad) {
        System.out.println("mi nombre es: " + nombre + " tengo: " + edad);
    }

    static String saludoGuardado() {
        return "viene de una funcion";
    }

    static boolean raiz(Integer numero) {
        return resultado((int) Math.sqrt(numero));
    }

    static boolean resultado(Integer valorRaiz) {
        return (valorRaiz >= 5);
    }

}
