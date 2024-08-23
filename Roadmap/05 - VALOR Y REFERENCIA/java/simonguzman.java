public class simonguzman {
    public static void main(String[] args) {

        int a = 5;
        int b = a;
        int[] array1 = {1, 2, 3};
        int[] array2 = array1;
        Coche c = new Coche(5, "Opel", "Astra", 85, 1200, 14000 );
        String miCadena = "Hola: Ejercicio #05";

        //Asignacion por valor
        b=10;
        System.out.println(a);
        System.out.println(b);
        modificarNumero(a);
        System.out.println(a);

        //Asignacion por referencia
        array2[0] = 10;
        for (int i = 0; i < array1.length; i++) {
            System.out.println(array1[i]);
        }
        for (int i = 0; i < array2.length; i++) {
            System.out.println(array2[i]);
        }

        System.out.println(array1[0]);
        System.out.println(array2[0]);

        modificarArray(array1);
        for (int i = 0; i < array1.length; i++) {
            System.out.println(array1[i]);
        }
        for (int i = 0; i < array2.length; i++) {
            System.out.println(array2[i]);
        }

        //Objeto por referencia

        System.out.println(c.getNumPuertas());
        System.out.println(c.getMarca());
        System.out.println(c.getModelo());
        System.out.println(c.getNumCaballos());
        System.out.println(c.getCilindrada());
        System.out.println(c.getPrecio());

        modificarCoche(c);

        System.out.println(c.getNumPuertas());
        System.out.println(c.getMarca());
        System.out.println(c.getModelo());
        System.out.println(c.getNumCaballos());
        System.out.println(c.getCilindrada());
        System.out.println(c.getPrecio());


        //Objeto inmutable
        System.out.println(miCadena);
        modificarCadena(miCadena);
        System.out.println(miCadena);

        //Ejercicio adicional
        //Intercambio por valor
        int num1 = 0;
        int num2 = 1;
        int []arreglo1 = {1,2,3};
        int []arreglo2 = {4,5,6};

        System.out.println(num1);
        System.out.println(num2);
        int[] intercambio = intercambioXValor(num1, num2);
        for(int i = 0; i < intercambio.length; i++){
            System.out.println(intercambio[i]);
        }

        //Intercambio por referencia
        for (int i = 0; i < arreglo1.length; i++){
            System.out.print(arreglo1[i]);
        }
        for (int i = 0; i < arreglo2.length; i++){
            System.out.print(arreglo2[i]);
        }
        System.out.println();
        intercambioXReferencia(arreglo1, arreglo2);
        for (int i = 0; i < arreglo1.length; i++){
            System.out.print(arreglo1[i]);
        }
        for (int i = 0; i < arreglo2.length; i++){
            System.out.print(arreglo2[i]);
        }
    }

        public static int[] intercambioXValor(int num1, int num2){
            int aux = 0;
            aux = num1;
            num1 = num2;
            num2 = aux;
            return new int[] {num1,num2};
        }

    public static void intercambioXReferencia(int[] arreglo1, int[] arreglo2){
        for (int i = 0; i < arreglo1.length; i++) {
            int temp = arreglo1[i];
            arreglo1[i] = arreglo2[i];
            arreglo2[i] = temp;
        }
    }
    private static void modificarCadena(String miCadena){
        miCadena = "Modificacion de un string";
    }

    public static void modificarNumero(int num){
        num = 4;
    }

    public static void modificarArray(int[] array){
        array[0] = 0;
        array[1] = 1;
        array[2] = 2;
    }

    public static void modificarCoche(Coche c){
        c.setNumPuertas(3);
        c.setMarca("Citroen");
        c.setModelo("C3");
        c.setNumCaballos(92);
        c.setCilindrada(1400);
        c.setPrecio(17000);
    }

}


class Coche{
    private int numPuertas;
    private String marca;
    private String modelo;
    private int numCaballos;
    private int cilindrada;
    private double precio;

    public Coche(){

    }

    public Coche(int numPuertas, String marca, String modelo, int numCaballos, int cilindrada, double precio){
        this.numPuertas = numPuertas;
        this.marca = marca;
        this.modelo = modelo;
        this.numCaballos = numCaballos;
        this.cilindrada = cilindrada;
        this.precio = precio;
    }

    public int getNumPuertas() {
        return numPuertas;
    }

    public void setNumPuertas(int numPuertas) {
        this.numPuertas = numPuertas;
    }       

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public int getNumCaballos() {
        return numCaballos;
    }
    
    public void setNumCaballos(int numCaballos) {
        this.numCaballos = numCaballos;
    }

    public int getCilindrada() {
        return cilindrada;
    }

    public void setCilindrada(int cilindrada) {
        this.cilindrada = cilindrada;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }
}