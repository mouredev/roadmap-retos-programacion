public class LucasAG01 {


        //Funcion bloque de codigo para reutilizarlo de otras formas.

        //FUNCIONES DEFINIDAS POR EL USUARIO. las crea el usuario como le da la gana

        //Simple

        /*
        modificadorAcceso tipoRetorno nombreFuncion (tipoParametro1 nombreParametro1, tipoParametro2 nombreParametro2, ...) {
            Cuerpo de la función
            Procesamiento y cálculos
        return valorRetorno;
           }
         */

        //Funcion sin retorno ni parametros

        public void SaludosDefault(){
            System.out.println("Saludos!!");
        }

        //Funcion con parametro sin retorno

        public void Presentacion (String parametro){
            System.out.println("Hola buenos días "+parametro);
        }

        //Funcion con retorno, es decir, ejecuta una lógica y devuelve algo, en la decalarciond e la función, en vez de void (sin retorno) colocaresmos el tipo de dato a devolver
        public String suma (int a, int b) {
            return "El resultado es "+a+b; //devulve un String
        }
        public int suma2 (int a ,int b){
            return a+b; //Devulve un int directamente
        }

        //Funciones dentro de funciones
        public void funcionesDentro(){
            System.out.println("Aquí debajo te dejaré el resultado de la funcion saludos.");
            SaludosDefault();
        }
        public void funcionesDentro2(String parametro){
            System.out.println("Aquí debajo te dejaré el resultado de la funcion Presentacion: ");
            Presentacion(parametro);
        }

        //Las funciones tienen unos modificadores de acceso, que sirven para mantener una limpieza y fundamentalmente seguridad en el codigo.
        // El acceso es lo primeor que ponemos
         /*
            public: La función es accesible desde cualquier clase.
            private: La función solo es accesible dentro de la misma clase en la que se define.
            protected: La función es accesible dentro de la misma clase y sus subclases.
            Sin modificador (por defecto): La función es accesible dentro del mismo paquete.
          */


    public  void funcionPublica() {
        // Accesible desde cualquier clase
    }

    private void funcionPrivada() {
        // Accesible solo dentro de la clase LucasAG01
    }

    protected  void funcionProtegida() {
        // Accesible dentro de la clase LucasAG01 y sus subclases
    }

    void funcionPorDefecto() {
        // Accesible dentro del mismo paquete
    }

    // Para poder usar estos métodos en diferentes clases, sin necesidad de instanciar un objeto: LucasAG01 metodo = new LucasAG01, en el metodo main x ej
    // tenemos que declarar el método como 'static'.
    // Al hacer esto, indicamos que es un método de clase, lo que significa que puede ser llamado
    // directamente a través del nombre de la clase.
    // Esto es útil cuando queremos que el método se pueda utilizar de manera global,
    // independientemente de las instancias de la clase.
    //ejemplo: public static void llamar(){sout("Hola que tal");}


    //funcion n numeros nos sabes cuantos los separas por ,
    public static int sumarN (int... numeros){
        int suma = 0;
        for (int num : numeros) {
            suma += num;
        }
        return suma;
    }

    //Tambien hay funciones creadas por el lenguage en si, como Math, toUpperCase

    //Aquí cremos una funcion y dentro de esta una funcion del lenguaje, generamos un nuemro entre 1 y 50
    public static void NUmeroAleatorio (){

         int numero= (int) (Math.random()*50)+1;

        System.out.println(numero);
    }






    public static void main(String[] args) {

            LucasAG01 lucasAG01 = new LucasAG01();
            lucasAG01.SaludosDefault();
            lucasAG01.Presentacion("Lucas");
            lucasAG01.funcionesDentro();
            lucasAG01.funcionesDentro2("Lucas");
            NUmeroAleatorio(); //Como use static, no tengo que usar objeto LucasAG01


    }

    //Ejericicio Extra

    public static int Extra (String para1, String para2){
        int contador =0;
        for (int i = 1; i <= 100; i++){

            if (i%3==0 && i%5==0){
                System.out.println(para1+para2);
            }
            else if (i%3==0){
                System.out.println(para1);
            } else if (i%5==0){
                System.out.println(para2);
            } else {
                System.out.println(i);
            }
            contador++;
        }
        return contador;
    }


     /*
     •	int contador = 0 : Se inicializa el contador en 0, el cual se incrementará en cada iteración del bucle.
     •	else: Si el número i no es divisible ni por 3 ni por 5, simplemente se imprime el número i.
     •	contador++: En cada iteración del bucle, el contador se incrementa en 1
     •	return contador;: Al final del método, se devuelve el valor del contador, que debería ser 100, ya que el bucle corre exactamente 100 veces.

       TEMA CONTADOR:

       Es una variable que lleva el registro del numero de veces que ocurre un evento específico, como el n de ietraciones en un bucle
       creamos u contador a 0
       luego dentro del for, cada vez que el bucle realiza una iteracion, cuando llega al final, hacemos que dicho contador aumnete en 1 contador++;

       return contador, Cuando el bucle termina, 100 veces , la funcion devuelve el valor del contador, en este caso 100.

       se incrementa en cada iteración del bucle, lo que permite llevar un registro de cuántas veces se ha ejecutado el bucle. Al final del método,
       el contador devuelve el número total de iteraciones, que en este caso es 100.
       Aunque en este escenario el uso del contador puede parecer redundante (ya que sabemos de antemano que habrá 100 iteraciones),
       sigue siendo una práctica común y útil, especialmente en casos donde el número de iteraciones podría variar.

      */





















}
