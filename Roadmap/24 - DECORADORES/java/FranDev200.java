public class FranDev200 {


    interface Cafe{

        public String descripcion();

        public double precio();

    }

    // Objeto a decorar
    public static class CafeSolo implements  Cafe{


        @Override
        public String descripcion() {
            return "Cafe solo";
        }

        @Override
        public double precio() {
            return 1.50;
        }
    }

    // Decorador
    public static abstract class CafeDecorador implements  Cafe{

        protected Cafe cafe;

        public CafeDecorador(Cafe cafe) {
            this.cafe = cafe;
        }

        @Override
        public String descripcion() {
            return cafe.descripcion();
        }

        @Override
        public double precio() {
            return cafe.precio();
        }
    }

    // Decoraciones
    public static class Leche extends CafeDecorador {

        public Leche(Cafe cafe) {
            super(cafe);
        }

        @Override
        public String descripcion() {
            return cafe.descripcion() + ", leche";
        }

        @Override
        public double precio() {
            return cafe.precio() + 0.15;
        }

    }

    public static class Chocolate extends CafeDecorador {

        public Chocolate(Cafe cafe) {
            super(cafe);
        }

        @Override
        public String descripcion() {
            return cafe.descripcion() + ", chocolate";
        }

        @Override
        public double precio() {
            return cafe.precio() + 0.50;
        }

    }

    public static class Nata extends CafeDecorador {

        public Nata(Cafe cafe) {
            super(cafe);
        }

        @Override
        public String descripcion() {
            return cafe.descripcion() + ", nata";
        }

        @Override
        public double precio() {
            return cafe.precio() + 0.25;
        }

    }

    public static class Azucar extends CafeDecorador {

        public Azucar(Cafe cafe) {
            super(cafe);
        }

        @Override
        public String descripcion() {
            return cafe.descripcion() + ", azucar";
        }

        @Override
        public double precio() {
            return cafe.precio() + 0.10;
        }

    }

    static void main() {


        /*

        EJERCICIO:
         * Explora el concepto de "decorador" y muestra cómo crearlo
         * con un ejemplo genérico.

         */
        Cafe cafe = new CafeSolo();

        System.out.println("Tabla de precios de Cafés");
        System.out.println("=========================");
        System.out.println(cafe.descripcion() + " --> " + cafe.precio());
        cafe = new Leche(cafe);
        System.out.println(cafe.descripcion() + " --> " + cafe.precio());
        cafe = new Chocolate(cafe);
        System.out.println(cafe.descripcion() + " --> " + cafe.precio());
        cafe = new Nata(cafe);
        System.out.println(cafe.descripcion() + " --> " + cafe.precio());
        cafe = new Azucar(cafe);
        System.out.println(cafe.descripcion() + " --> " + cafe.precio());


        /*

         * DIFICULTAD EXTRA (opcional):
         * Crea un decorador que sea capaz de contabilizar cuántas veces
         * se ha llamado a una función y aplícalo a una función de tu elección.

         */

        System.out.println("\nEJERCICIO EXTRA");
        System.out.println("===============\n");

        Saludo saludo = new Mensaje();
        System.out.println(saludo.saludar()); // Saludo normal sin numero


        saludo = new SaludoContabilizado(saludo);

        for(int i = 0; i < 20; i++){
            System.out.println(saludo.saludar());
        }


    }

    interface Saludo{
        String saludar();
    }

    static class Mensaje implements Saludo{

        @Override
        public String saludar() {
            return "Saludo";
        }

    }

    static abstract class Implementacion implements Saludo{

        Saludo saludo;

        public Implementacion(Saludo saludo) {
            this.saludo = saludo;
        }

        @Override
        public String saludar() {

            return saludo.saludar();
        }
    }

    static class SaludoContabilizado extends Implementacion{


        private int nroSaludo = 0;
        public SaludoContabilizado(Saludo saludo) {
            super(saludo);
        }

        @Override
        public String saludar() {

            nroSaludo++;
            return saludo.saludar() + " " +  nroSaludo;
        }
    }


}
